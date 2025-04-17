# Module 5: Machine Learning for Decision Support Systems

<!-- TOC -->
* [Module 5: Machine Learning for Decision Support Systems](#module-5-machine-learning-for-decision-support-systems)
* [Artificial Intelligence (AI)](#artificial-intelligence-ai)
* [Introduction To Machine Learning?](#introduction-to-machine-learning)
  * [Types of Machine Learning](#types-of-machine-learning)
    * [Supervised Learning Algorithms](#supervised-learning-algorithms)
    * [Unsupervised Learning Algorithms](#unsupervised-learning-algorithms)
    * [Neural Networks & Deep Learning](#neural-networks--deep-learning)
    * [Key Concepts](#key-concepts)
  * [A General Framework for Developing Machine Learning-Based Algorithms](#a-general-framework-for-developing-machine-learning-based-algorithms)
    * [Case Study: Linear Regression for Estimating House Prices](#case-study-linear-regression-for-estimating-house-prices)
<!-- TOC -->


# Artificial Intelligence (AI)

AI is a broad field of computer science focused on building machines that can perform tasks that typically require human intelligence.

AI is about making machines behave like humans — think, learn, and solve problems.

AI systems aim to mimic human thinking—whether through rules, learning, or problem-solving.



# Introduction To Machine Learning?

Machine Learning (ML) is a subfield of Artificial Intelligence (AI) focused on developing algorithms that can learn 
from data and generalize to new, unseen data. This allows systems to perform tasks without being explicitly programmed. So, ML is a way to teach computers to learn from data instead of giving them step-by-step instructions.


## Types of Machine Learning

Machine learning algorithms can generally be grouped into three major categories: supervised learning, 
unsupervised learning, and reinforcement learning.

**Supervised Learning**

In supervised learning, models are trained on labeled data — where both input and output are known. 
Supervised learning problems are generally divided into two main types:


- **Classification problem**  
Used when the output is a discrete category or class.
The goal is to assign inputs to one of several predefined categories.
  
  * Predicts **discrete categories** (e.g., classifying an iris flower as *Setosa*, *Versicolor*, or *Virginica*).  
  * **Example:** Spam detection, disease diagnosis.

- **Regression problem**  
Used when the output is a continuous value.
The model predicts a numeric quantity based on the input features.
  * Predicts **continuous values** (e.g., predicting house prices based on area and location).  
  * **Example:** Stock price prediction, temperature forecasting.



**Unsupervised Learning**

Unsupervised learning deals with unlabeled data — the goal is to find hidden patterns or groupings.

- **Clustering problem**  
  Groups similar data points based on similarity (e.g., grouping flowers into species based on petal measurements without predefined labels).  
  **Example:** Grouping emails into categories without predefined labels, customer profiling, market segmentation, clustering similar users....

**Reinforcement Learning**  

Reinforcement learning (RL) is a type of machine learning where an agent learns to make decisions by interacting with an environment.

### Supervised Learning Algorithms

**Linear Regression**

- Predicts a continuous numeric output.
- Fits a line that minimizes the sum of squared errors.

**Logistic Regression**

- Used for binary classification.
- Uses a sigmoid function to predict probabilities.

**Support Vector Machine (SVM)**

- Classifies data by finding the optimal decision boundary.
- Uses kernel functions for non-linear classification.

**K-Nearest Neighbors (KNN)**

- Non-parametric algorithm for regression and classification.
- Predicts based on the average (or majority) of K nearest neighbors.

**Naive Bayes**

- Based on Bayes’ Theorem.
- Assumes feature independence.
- Common in spam filtering.

**Decision Trees**

- Series of conditional questions leading to a prediction.
- Splits data based on feature values.

**Random Forest**

- Ensemble of multiple decision trees.
- Reduces overfitting by averaging results.

**Boosting (e.g., AdaBoost, XGBoost)**

- Trains models sequentially.
- Each model focuses on correcting the errors of the previous one.


### Unsupervised Learning Algorithms

**Clustering**

- Groups similar data points.

**K-Means**

- Partitions data into K clusters based on proximity.
- Iteratively updates cluster centers.

**Others**

- Hierarchical Clustering
- DBSCAN

### Neural Networks & Deep Learning

- Inspired by the human brain, composed of layers (input, hidden, output).
- Learns hidden features and complex patterns automatically.
- Deep Learning = multiple hidden layers.
- Common in image and speech recognition.
- Can be used for classification, regression. With unsupervised variations like Autoencoders, Self-Organizing Maps (SOMs), and Deep Embedded Clustering (DEC) allow ANNs to perform clustering.



### Key Concepts

- **Overfitting**: Good performance on training data but poor on unseen data.
- **Underfitting**: Model is too simple, fails to learn patterns.
- **Hyperparameters**: Tunable settings like `K` in KNN.
- **Feature Engineering**: Creating new input features to improve model performance.


## A General Framework for Developing Machine Learning-Based Algorithms

In a typical machine learning application, the procedure is composed of two main steps. The first step 
involves training and building the model using historical data. In supervised learning, this data is 
labeled — meaning it includes both inputs and their corresponding correct outputs — which enables the 
model to learn the mapping between them. In contrast, unsupervised learning relies on unlabeled data, 
where the model explores the structure or patterns in the data without predefined outputs. Once the model 
is trained, it is saved for future use. The second step involves loading the trained model and introducing 
new, unseen inputs to make predictions or extract insights, depending on the learning type.
This enables the model to provide insights or decisions in real-time without retraining. This separation of training 
and inference makes machine learning systems efficient and scalable in practical applications.


### Case Study: Linear Regression for Estimating House Prices

**First Step: Training Algorithm Pseudocode**

1. Start

2. Define input feature matrix `X` with:
   - square footage
   - number of bedrooms

3. Define output target vector `y` with:
   - corresponding house prices

4. Initialize a Linear Regression model

5. Train the model using `model.fit(X, y)`

6. Print the model's:
   - Coefficients (for sqft and bedrooms)
   - Intercept

7. Save the trained model to disk using `joblib.dump()`

8. End

* House Price Training Application
```python
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib  # For saving/loading the trained model

#  Input features: [square_footage, num_bedrooms]
X = np.array([
    [1000, 2],
    [1500, 3],
    [2000, 3],
    [2500, 4],
    [3000, 4]
])

#  Output prices in $1000s (i.e., 200 => $200,000)
y = np.array([200, 250, 300, 350, 400])

# Create a linear regression model and train it on the data
model = LinearRegression()
model.fit(X, y)  #  Learn coefficients (a, b) and intercept (c)

#  Predict the price for a new house: 2200 sqft, 3 bedrooms
new_house = np.array([[2200, 3]])
predicted_price = model.predict(new_house)
print(f"Predicted price: ${predicted_price[0]}")

#  Display learned coefficients and intercept
print("Coefficient for sqft (a):", model.coef_[0])        # Effect of square footage
print("Coefficient for bedrooms (b):", model.coef_[1])     # Effect of number of bedrooms
print("Intercept (c):", model.intercept_)                  # Base price with 0 sqft & 0 bedrooms

#  Save the trained model to a file
joblib.dump(model, 'linear_house_model.pkl')               # Save model to disk
print("Model saved as 'linear_house_model.pkl'")


# The model learns a linear function of:

# price = a * sqft + b * bedrooms + c

# LEarning is finding the best values for the coefficients ( a, b, and c) that minimize the error between the predicted
# prices and the actual prices.


# What the model does during training:
# Starts with random values for a, b, and c
# Predicts the prices for the training data
# Measures the error (difference from actual prices)
# Adjusts a, b, and c to reduce the error
# Repeats until the error is minimized

```


**Second Step:Prediction Application Pseudocode**

1. Start

2. Load the trained model from disk using `joblib.load()`

3. Display "House Price Predictor is ready"

4. LOOP:
    a. Ask user to enter:
       - square footage
       - number of bedrooms

    b. Convert input to numeric values

    c. Create input array for prediction: `[[sqft, bedrooms]]`

    d. Predict house price using `model.predict()`

    e. Display predicted price

    f. Ask user if they want to make another prediction
       - If NO, exit the loop

5. Print "Goodbye"

6. End


* House Price Prediction Console App: User Input from Console
```python
import numpy as np
import joblib

#  Load the saved model
model = joblib.load('linear_house_model.pkl')
print(" House Price Predictor is ready!")

while True:
    try:
        #  Ask user for input
        sqft = float(input("Enter square footage (e.g., 2200): "))
        bedrooms = int(input("Enter number of bedrooms (e.g., 3): "))

        #  Prepare input and make prediction
        user_input = np.array([[sqft, bedrooms]])
        predicted_price = model.predict(user_input)

        #  Display result
        print(f"Predicted house price: ${predicted_price[0]:,.2f}")

        # ➕ Ask if the user wants to continue
        cont = input("Do you want to predict another house? (yes/no): ").strip().lower()
        if cont not in ['yes', 'y']:
            print("Goodbye ")
            break

    except Exception as e:
        print(f" Error: {e}. Please try again.\n")

```

* House Price Prediction Application: User Input via Apache Kafka

```python
import json

import numpy as np
import joblib
from confluent_kafka import Consumer, KafkaException, KafkaError

# Load the saved model
model = joblib.load('linear_house_model.pkl')
print("House Price Predictor is ready!")

# Kafka consumer setup
conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'house-price-consumer-group',
    'auto.offset.reset': 'latest'
}

consumer = Consumer(conf)
consumer.subscribe(['dss-ml-house-price-model-input'])

try:
    while True:
        # Poll for messages
        msg = consumer.poll(timeout=1.0)  # Timeout in seconds

        if msg is None:
            # No message received
            continue
        elif msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition
                print(f"End of partition reached {msg.partition} at offset {msg.offset}")
            else:
                # Other errors
                raise KafkaException(msg.error())

        else:
            # Extract data from the Kafka message (assumes the message value is JSON or string)
            try:
                message_value = msg.value().decode('utf-8')
                # sqft, bedrooms = map(float, message_value.split(','))  # Assuming message format: "2200,3"
                message_json = json.loads(message_value)

                sqft = message_json['sqft']
                bedrooms = message_json['bedrooms']

                # Prepare input and make prediction
                user_input = np.array([[sqft, bedrooms]])
                predicted_price = model.predict(user_input)

                # Display the result
                print(f"Predicted house price: ${predicted_price[0]:,.2f}")

            except Exception as e:
                print(f"Error processing message: {e}. Please check input format.\n")

except KeyboardInterrupt:
    print("Exiting...")
finally:
    # Close the consumer to clean up resources
    consumer.close()

# Receiving a Message from the Kafka Cluster in the following format:
# { "sqft": 2200, "bedrooms": 3 }

```
