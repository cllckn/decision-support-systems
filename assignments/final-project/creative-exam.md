# **Final Project Assignment: Design and Implementation of a Relational Database System Using PostgreSQL**

## **Objective**

In this project, you are required to develop a web-based application that integrates a machine learning model 
implemented in Python. The system must support real-time data streaming using Apache Kafka, authenticate users 
through JWT, log all activities in a PostgreSQL database, and display graphical data visualizations.

## **Project Requirements**

**Machine Learning Model (Python)**
* You must develop a model related to your assigned topic using one of the following ML algorithms:
  * Support Vector Machine (SVM)
  * Logistic Regression
  * K-Means Clustering
  * Artificial Neural Network (ANN)
* The model must be stored and loaded for inference.
* The model should accept user input, make predictions, and return results.

**Web Application (Node.js & PostgreSQL)**
* Implement a user authentication system with:
  * User registration and login.
  * JWT-based authentication and authorization.
* Develop web interfaces where users:
  * Input data for prediction.
  * View real-time prediction results.
  * Access a log of past requests and responses.
  * Visualize data through interactive graphs.
  
**Real-Time Data Flow (Kafka & WebSockets)**
* Kafka Producer (Node.js):
  * Sends user-input data to an ML processing topic in Kafka.
* Kafka Consumer (Python):
  * Receives data from Kafka.
  * Loads the ML model and performs inference.
  * Sends the prediction result back to Kafka.
* WebSocket Integration:
  * The web app listens for ML predictions in real-time.
  * Updates the user interface dynamically with received predictions.

**Logging System & Graph Visualization (Node.js & PostgreSQL)**
* Implement a Kafka consumer (Node.js) to:
  * Log all system activities (data sent, predictions received, timestamps).
  * Store logs in a PostgreSQL table.
* Graph Visualization:
  * Retrieve relevant data from the database.
  * Display trends or statistics using interactive charts.

**Evaluation**

As part of the evaluation, each student is required to prepare and present the following:

- A **written report** detailing the project  
- A **presentation slide deck**  
- A **5-minute oral defense** summarizing the work  
- A **live demonstration** of the project on a personal laptop using localhost, to be shown to the committee

- Report Guidelines

  The **report** should provide a clear and concise explanation of your study and must include the following sections:

  * Objective

  Clearly state the purpose and goals of your project. What problem are you addressing, and what do you aim to achieve?

  * Methodology

  Describe the methods, tools, and technologies used in the development of your project.

  In this section, also include a diagram that illustrates the overall architecture of your system, showing its main components and their interactions. Be sure to accompany the figure with a short, relevant explanation.

![](./../../resources/final-project-components.png)
