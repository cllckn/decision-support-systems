# Module 6: Integrating Components into a Decision Support System

<!-- TOC -->
* [Module 6: Integrating Components into a Decision Support System](#module-6-integrating-components-into-a-decision-support-system)
  * [Case Study: End-to-End Development of a Decision Support System for a Real-World Problem](#case-study-end-to-end-development-of-a-decision-support-system-for-a-real-world-problem)
    * [Iris Dataset](#iris-dataset)
    * [DSS App (v1): Apache Kafka and  Web Socket Support (/kafka-socket-support)](#dss-app-v1-apache-kafka-and--web-socket-support-kafka-socket-support)
    * [DSS App (v2): All-in-One Decision Support System](#dss-app-v2-all-in-one-decision-support-system)
<!-- TOC -->

## Case Study: End-to-End Development of a Decision Support System for a Real-World Problem

This Decision Support System (DSS) application is a web-based platform designed to support data-driven decision-making
by integrating real-time data processing, machine learning, and secure user management.

![](../resources/figures/final-project-components.png)


**Purpose**

The goal of this application is to demonstrate how data collected from a web interface can be processed in 
real-time using a machine learning model, and how the results can be communicated back to the user with minimal delay.
It serves as a practical learning tool that brings together concepts from web development, data engineering, 
and machine learning.


### Iris Dataset

https://www.kaggle.com/datasets/uciml/iris

This application uses the **Iris dataset**, a classical dataset in the field of machine learning and pattern recognition. 
It consists of 150 samples of iris flowers from three different species: *Iris setosa*, *Iris versicolor*, 
and *Iris virginica*.

Each sample includes the following numerical features:

- Sepal Length (in cm)
- Sepal Width (in cm)
- Petal Length (in cm)
- Petal Width (in cm)

In this DSS application, only **Sepal Length** and **Sepal Width** are used as input features. These are submitted 
by the user through the interface and sent to a backend ML model that predicts the flower’s species.

The Iris dataset is included as part of many ML libraries such as `scikit-learn`, making it easy to load and use 
in Python-based machine learning models.


**Test Data for the Iris dataset**

| Sepal Length (cm) | Sepal Width (cm) | Expected Class  |
|-------------------|------------------|---|
| 5.1	              | 3.5              | setosa  |
| 6.0               | 2.2              | versicolor  |
| 6.3               | 3.3              | virginica  |
| 4.9               | 3.1              | setosa  |


### DSS App (v1): Apache Kafka and  Web Socket Support (/kafka-socket-support)

A user can input flower features through a simple web interface to predict the species.

Apache Kafka consumers log the prediction result and send it back to the web application server.

The web server then instantly delivers the result to the web interface via WebSocket.

* /kafka-socket-support/server.js

```javascript
// ──────────────────────────────────────────────────────────────
// Required Libraries
// ──────────────────────────────────────────────────────────────
const express = require("express");
const bodyParser = require("body-parser");
const { Kafka } = require("kafkajs");
const path = require("path");
const http = require("http");
const socketIo = require("socket.io");

// ──────────────────────────────────────────────────────────────
// Express and HTTP Server Setup (for Socket.IO)
// ──────────────────────────────────────────────────────────────
const app = express();
const server = http.createServer(app);      // HTTP server for WebSocket support
const io = socketIo(server);                // Initialize Socket.IO for real-time communication

app.use(bodyParser.json());                 // Parse incoming JSON requests

// ──────────────────────────────────────────────────────────────
// Kafka Setup
// ──────────────────────────────────────────────────────────────
const kafka = new Kafka({
  clientId: "iris-data-app",
  brokers: ["localhost:9092"]         // Replace with your Kafka broker address
});

const kafkaProducer = kafka.producer();     // Kafka producer instance
const kafkaConsumer = kafka.consumer({ groupId: "iris-data-group" });  // Kafka consumer group

// ──────────────────────────────────────────────────────────────
// Frontend Static Files Setup
// ──────────────────────────────────────────────────────────────
app.use(express.static(path.join(__dirname, 'public')));  // Serve files from /public folder

// ──────────────────────────────────────────────────────────────
// Route: POST /api/ml-model/send
// Purpose: Accept sepal_length and sepal_width, send to Kafka topic for ML processing
// ──────────────────────────────────────────────────────────────
app.post("/api/ml-model/send", async (req, res) => {
  const { sepal_length, sepal_width } = req.body;

  // Validate input
  if (!sepal_length || !sepal_width) {
    return res.status(400).json({ error: "Missing sepal length or width." });
  }

  const message = {
    sepal_length,
    sepal_width
  };

  try {
    // Connect → Send message → Disconnect
    await kafkaProducer.connect();
    await kafkaProducer.send({
      topic: "dss-ml-model-input",
      messages: [{
        key: Date.now().toString(),
        value: JSON.stringify(message)
      }]
    });
    await kafkaProducer.disconnect();

    // Respond with success status
    res.status(201).json({ status: "Sent to Kafka", ...message });

  } catch (err) {
    console.error("Kafka send failed:", err.message);
    res.status(500).json({ error: "Kafka send failed", details: err.message });
  }
});

// ──────────────────────────────────────────────────────────────
// Kafka Consumer Listener Function
// Purpose: Listen to predictions from Kafka and broadcast via WebSocket
// ──────────────────────────────────────────────────────────────
const startKafkaPredictionListener = async () => {
  await kafkaConsumer.connect();
  await kafkaConsumer.subscribe({ topic: "dss-ml-model-output", fromBeginning: true });

  await kafkaConsumer.run({
    eachMessage: async ({ message }) => {
      try {
        const modelResult = JSON.parse(message.value.toString());
        console.log("Received ML output from Kafka:", modelResult);

        // Emit to all connected clients via WebSocket
        io.emit('model-result', modelResult);
      } catch (err) {
        console.error("Error parsing Kafka message:", err.message);
      }
    }
  });
};

// ──────────────────────────────────────────────────────────────
// Start Kafka Listener
// ──────────────────────────────────────────────────────────────
startKafkaPredictionListener().catch(console.error);

// ──────────────────────────────────────────────────────────────
// Start Express + WebSocket Server
// ──────────────────────────────────────────────────────────────
server.listen(3000, () => {
  console.log("🚀 Server is running at http://localhost:3000");
});

```

* /kafka-socket-support/public/index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Analytics Engine</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="/socket.io/socket.io.js"></script> <!-- Include Socket.IO client -->
</head>
<body>

<h2>Model Inputs</h2>
<!-- Form to add a new product -->
<input type="number" id="length" placeholder="sepal_length" required>
<input type="number" id="width" placeholder="sepal_width" required>
<button type="submit" id="submit-button">Submit</button>

<!-- Display Model  Result -->
<h3>Model Result:<span id="model-result" >Waiting for model result...</span></h3>


<script>
    $(function () {
        // Initialize Socket.IO connection
        const socket = io(); // Connect to the Socket.IO server
        $("#model-result").hide();
        // Handle form submission fort model inputs
        $("#submit-button").on("click", function () {
            var sepal_length = parseFloat($("#length").val().trim());
            var sepal_width = parseFloat($("#width").val().trim());

            // Asynchronous request to send data to the server
            $.post({
                url: "/api/ml-model/send",
                contentType: "application/json",
                data: JSON.stringify({ sepal_length, sepal_width }),
                success: function (response) {
                    console.log("Data sent successfully");
                    $("#length").val(""); // Clear input fields
                    $("#width").val(""); // Clear input fields
                },
                error: function (xhr) {
                    console.error("Error:", xhr.responseText);
                }
            });
        });

        // Listen for the 'modelPrediction' event emitted by the server
        socket.on('model-result', function (data) {
            console.log("Received model output:", data);
            $("#model-result").fadeIn();
            // Display the result in the "predictionResult" div
            $("#model-result").html(`

                <strong> ${data?.result}</strong>
            `);
        });
    });
</script>

</body>
</html>

```

* Train ML model /module6/logisticregressiontrainandsavemodel/_init_.py

```shell
# -----------------------------
# Import necessary libraries
# -----------------------------
import numpy as np                     # For numerical operations and array handling
import joblib                          # For saving/loading Python objects like models and scalers
from sklearn import datasets           # To load sample datasets like Iris
from sklearn.model_selection import train_test_split  # For splitting data into train and test sets
from sklearn.preprocessing import StandardScaler      # For standardizing feature values
from sklearn.linear_model import LogisticRegression   # For logistic regression model


# -----------------------------
# Load and inspect the Iris dataset
# -----------------------------
iris = datasets.load_iris()  # Load the Iris dataset (a well-known classification dataset)
print(iris)  # Show the entire dataset structure (for inspection)


# -----------------------------
# Prepare feature and label data
# -----------------------------
X = iris.data[:, :2]  # Use only the first two features: sepal length and width
y = iris.target       # Target labels (0, 1, 2) representing the three iris species

# Print X-independent vars and Y-dependent var
print("Sepal Length\tSepal Width\tClass")
for i in range(len(X)):
    print(f"{X[i][0]:.2f}\t\t{X[i][1]:.2f}\t\t{y[i]}")


# -----------------------------
# Split dataset into training and testing sets
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# -----------------------------
# Standardize input features
# -----------------------------
# Standardize the features to ensure fair and efficient learning during model training.
# Standardize the input features to have zero mean and unit variance — a critical preprocessing
# step to ensure fair and efficient learning during model training.
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # Fit on training data and transform it


# -----------------------------
# Train a logistic regression model
# -----------------------------
log_reg = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=200)
# multi_class='multinomial': This tells the model to perform multiclass classification using a softmax function.
# solver='lbfgs': Specifies the optimization algorithm.
# max_iter=200: Sets the maximum number of iterations the solver should run to find the best model parameters.

log_reg.fit(X_train_scaled, y_train)  # Train the model using the scaled training data


# -----------------------------
# Save trained model and scaler
# -----------------------------
joblib.dump(log_reg, 'logistic_model.pkl')  # Save the trained logistic regression model
joblib.dump(scaler, 'scaler.pkl')           # Save the fitted scaler


# -----------------------------
# Load model and make a prediction
# -----------------------------
# --- Later or in a separate script: load and use the model for prediction ---

model = joblib.load('logistic_model.pkl')   # Load the trained model
scaler = joblib.load('scaler.pkl')          # Load the fitted scaler


# -----------------------------
# Accept user input and make prediction
# -----------------------------
# Get input from the user for sepal dimensions
sepal_length = float(input("Enter Sepal Length (cm): "))  # Input sepal length
sepal_width = float(input("Enter Sepal Width (cm): "))    # Input sepal width

# Prepare the input data as a 2D array and scale it using the same scaler used during training
user_input = np.array([[sepal_length, sepal_width]])       # Create 2D array for prediction
user_input_scaled = scaler.transform(user_input)           # Apply the saved scaler

# Predict the class label using the trained model
prediction = model.predict(user_input_scaled)

# Convert numerical prediction back to class name and display the result
class_names = iris.target_names                            # ['setosa', 'versicolor', 'virginica']
print(f"Predicted Class: {class_names[prediction[0]]}")    # Display the predicted class

```

* Use ML model /module6/logisticregressionwithkafkasupportloadmodel/_init_.py

```shell
# ──────────────────────────────────────────────────────────────
# Required Libraries
# ──────────────────────────────────────────────────────────────
import json
import joblib
import numpy as np
from confluent_kafka import Consumer, Producer

# ──────────────────────────────────────────────────────────────
# Constants and Configuration
# ──────────────────────────────────────────────────────────────
BROKER_ADDRESS = 'localhost:9092'
INPUT_TOPIC = 'dss-ml-model-input'
OUTPUT_TOPIC = 'dss-ml-model-output'
CONSUMER_GROUP_ID = 'iris-group'
MODEL_FILE = 'logistic_model.pkl'
SCALER_FILE = 'scaler.pkl'

# ──────────────────────────────────────────────────────────────
# Load Trained Model and Scaler
# ──────────────────────────────────────────────────────────────
model = joblib.load(MODEL_FILE)
scaler = joblib.load(SCALER_FILE)

# ──────────────────────────────────────────────────────────────
# Kafka Configuration
# ──────────────────────────────────────────────────────────────
conf_consumer = {
    'bootstrap.servers': BROKER_ADDRESS,
    'group.id': CONSUMER_GROUP_ID,
    'auto.offset.reset': 'latest'
}

conf_producer = {
    'bootstrap.servers': BROKER_ADDRESS
}

# ──────────────────────────────────────────────────────────────
# Initialize Kafka Consumer and Producer
# ──────────────────────────────────────────────────────────────
consumer = Consumer(conf_consumer)
producer = Producer(conf_producer)

# Subscribe to the input topic
consumer.subscribe([INPUT_TOPIC])

# ──────────────────────────────────────────────────────────────
# Function to Send Prediction to Output Topic
# ──────────────────────────────────────────────────────────────
def send_prediction(result):
    data = json.dumps({ "result": result })
    producer.produce(OUTPUT_TOPIC, value=data.encode('utf-8'))
    producer.flush()

print(" Listening for sepal length and width...")

# ──────────────────────────────────────────────────────────────
# Main Kafka Polling + ML Prediction Loop
# ──────────────────────────────────────────────────────────────
try:
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            print(f" Consumer error: {msg.error()}")
            continue

        try:
            # Parse the input JSON message
            data = json.loads(msg.value().decode('utf-8'))
            sepal_length = float(data.get("sepal_length"))
            sepal_width = float(data.get("sepal_width"))

            # Scale input and make prediction
            input_scaled = scaler.transform([[sepal_length, sepal_width]])
            prediction = int(model.predict(input_scaled)[0])
            label = ['setosa', 'versicolor', 'virginica'][prediction]

            print(f" Received: {sepal_length}, {sepal_width} → Predicted: {label}")

            # Send prediction result back
            send_prediction(label)

        except Exception as e:
            print(f" Error processing message: {e}")

except KeyboardInterrupt:
    print(" Shutting down...")

finally:
    consumer.close()

```

### DSS App (v2): All-in-One Decision Support System

This fully functional DSS is built upon the following application:

[Download and install the application](https://github.com/cllckn/decision-support-systems/tree/main/module4/part3/version2) and run it.


This project is an **all-in-one Decision Support System (DSS)** that combines secure user access, data management, 
real-time machine learning predictions, and interactive visualization — all in a single, integrated web platform.


**This DSS application brings together:**

- **Data Management**  
  CRUD operations for users, customers, and products are handled through a PostgreSQL-backed REST API with role-based 
access control.

- **Model Management**  
  A Python-based data analytics (ML) engine processes input data sent via Apache Kafka. It supports classification, 
regression, and clustering algorithms.

- **Real-Time Communication**  
  Results from the ML engine are streamed back to the frontend via WebSockets using Socket.IO, ensuring instant 
feedback for user inputs.

- **Interactive, Chart-Supported Interface**  
  The frontend UI uses Tailwind CSS and jQuery to offer responsive forms, live feedback, and the ability to visualize 
analytical results with integrated charts.

This architecture reflects how modern DSS applications are built to support not just historical data reporting, 
but real-time, predictive, and actionable decision-making in a unified platform.


**Key Features**

- **User Authentication**  
  Provides secure login functionality using JWT tokens, with role-based access control (e.g., admin, 
  registered-user, moderator).

- **Interactive Web Interface**  
  Users can input parameters (such as sepal length and width) through a responsive UI styled with Tailwind CSS.

- **Machine Learning Integration**  
  Inputs are sent to a backend data analytics engine via Apache Kafka. The ML engine (built in Python) processes 
  the inputs using models such as classification, regression, or clustering.

- **Real-Time Feedback**  
  Predictions or analytical results from the ML engine are sent back to the client using Socket.IO and displayed 
  immediately.

- **PostgreSQL Database Support**  
  User accounts and customer data are stored securely. Admin roles can access the ml model management page, and 
  also can view, and manage customer data.

- **Apache Kafka for Messaging**  
  Kafka enables reliable, asynchronous communication between frontend services and the backend ML processing pipeline.

- **Visualization**
  ApexCharts is utilized  for generating interactive and visually appealing charts.
