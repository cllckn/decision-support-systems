# Module 6: Integrating Components into a Decision Support System

<!-- TOC -->
* [Module 6: Integrating Components into a Decision Support System](#module-6-integrating-components-into-a-decision-support-system)
  * [Case Study: End-to-End Development of a Decision Support System for a Real-World Problem](#case-study-end-to-end-development-of-a-decision-support-system-for-a-real-world-problem)
    * [Iris Dataset](#iris-dataset)
    * [DSS App (v1): Apache Kafka Integration (/kafka-support)](#dss-app-v1-apache-kafka-integration-kafka-support)
    * [DSS App (v2): Apache Kafka and  Web Socket Support (/kafka-socket-support)](#dss-app-v2-apache-kafka-and--web-socket-support-kafka-socket-support)
    * [DSS App (v3): All-in-One Decision Support System](#dss-app-v3-all-in-one-decision-support-system)
<!-- TOC -->

## Case Study: End-to-End Development of a Decision Support System for a Real-World Problem

This Decision Support System (DSS) application is a web-based platform designed to support data-driven decision-making
by integrating real-time data processing, machine learning, and secure user management.


**Purpose**

The goal of this application is to demonstrate how data collected from a web interface can be processed in 
real-time using a machine learning model, and how the results can be communicated back to the user with minimal delay.
It serves as a practical learning tool that brings together concepts from web development, data engineering, 
and machine learning.


### Iris Dataset

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


### DSS App (v1): Apache Kafka Integration (/kafka-support)

A user can send parameters with a straightforwad web interface. Apache Kafka consumers log the generated model result.


### DSS App (v2): Apache Kafka and  Web Socket Support (/kafka-socket-support)

The model result can immediately be sent to the web interface through web socket.

### DSS App (v3): All-in-One Decision Support System

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
