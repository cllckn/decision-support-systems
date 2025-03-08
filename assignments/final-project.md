# **Final Project: Web-Based Machine Learning Application with Apache Kafka**

## **Objective**
In this final project, you will develop a **web-based application** that integrates **a machine learning model implemented in Python**. 
The system will handle **real-time data streaming using Apache Kafka**, **authenticate users with JWT**, **log all activities in a PostgreSQL database**, and **display graphical data visualizations**.

## **Requirements**

### **1. Machine Learning Model (Python)**
- **Students are free to choose the subject of their model**, but it must differ from those covered in class, and they must incorporate one of the following ML algorithms:
  - **Support Vector Machine (SVM)**
  - **Logistic Regression**
  - **K-Means Clustering**
  - **Artificial Neural Network (ANN)**
- The model must be **stored and loaded** for inference.
- The model should accept user input, make predictions, and return results.

### **2. Web Application (Node.js & PostgreSQL)**
- Implement a **user authentication system** with:
  - User **registration** and **login**.
  - **JWT-based authentication and authorization**.
- Develop **web interfaces** where users:
  - Input data for prediction.
  - View real-time prediction results.
  - Access a log of past requests and responses.
  - **Visualize data through interactive graphs**.

### **3. Real-Time Data Flow (Kafka & WebSockets)**
- **Kafka Producer (Node.js)**:
  - Sends user-input data to an ML processing topic in Kafka.
- **Kafka Consumer (Python)**:
  - Receives data from Kafka.
  - Loads the ML model and performs inference.
  - Sends the prediction result back to Kafka.
- **WebSocket Integration**:
  - The web app listens for ML predictions in real-time.
  - Updates the user interface dynamically with received predictions.

### **4. Logging System & Graph Visualization (Node.js & PostgreSQL)**
- Implement a **Kafka consumer (Node.js)** to:
  - Log all system activities (data sent, predictions received, timestamps).
  - Store logs in a PostgreSQL table:
    ```sql
    CREATE TABLE logs (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        request_data JSONB,
        prediction_result JSONB,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ```
- **Graph Visualization**:
  - Retrieve relevant log data from the database.
  - Display trends or statistics using interactive charts.
  - Graphs should be updated dynamically based on user interactions.

## **Deliverables**
1. **Machine Learning model code** (Python).
2. **Web application source code** (Node.js, PostgreSQL, WebSockets).
3. **Kafka producer & consumer implementations** (Node.js & Python).
4. **PostgreSQL schema for user authentication, logging, and analytics**.
5. **Graph visualizations implemented in the web app**.
6. **README file** explaining setup and usage.


---

## Evaluation Criteria
The assignment will be evaluated based on two primary components:

Project Implementation: The quality and effectiveness of the project you implement.

Oral Exam Performance: Your performance during the oral exam, which will take place during the final exam week(specific day and time to be announced later).

## Oral Exam Requirement

The oral exam is **mandatory** as part of the evaluation process. Students will be assessed based on their understanding of the material presented in their **reports** and **source code**.

### **During the Oral Exam:**
- Reports must be **open** and accessible.
- Source code must be **ready to show** in the IDE.
- Applications must be **ready to run** for demonstration.

## Group Work
Students may form groups of up to two members.

All group members will receive a common grade for the assignment.

Instructors may question any group member during the oral exam, so it is essential that each member has a thorough understanding of all aspects of the project.

## Report Structure
While there is no standard template for the report, it must include the following essential components:

### Cover Page
Student Information: Include your full name, student ID, course name, and date of submission.

Title of the Report: Clearly state the title of your study or project.

### Study Explanation
The report must provide a straightforward explanation of your study, including:

Objective: Clearly outline the purpose and goals of your study.

Methodology: Describe the methods and approaches used in your project.

In the methodology section, include a figure illustrating the overall architecture with its main components, 
similar to the one below, and provide a relevant explanation.

![](./../sample-outline.png)


Conclusion: Summarize the key points and findings of your study.

### Additional Recommendations

Ensure that your report is well-organized and free of grammatical errors.

Use clear headings and subheadings to enhance readability.

## Email Submission

Students are required to **compress** their report and source code into a **single file** (or provide a **GitHub link** to their source code repository) and submit it via **email (cceken@ku.edu.kz)** before oral examination.

* Email Subject: Use the following format for the subject line of your email:
   - dss-final-project-StudentName
* File Naming: Ensure that the compressed file is named appropriately, using the following format:
   - StudentName-Report.zip
* Only **one submission per group** is sufficient.

## Late Submission and Oral Exam Policy
Students must submit their **reports and source code** before the **oral exam**, as the oral exam time is crucial for evaluation.


### By adhering to these guidelines and policies, you will ensure that your submission is complete and meets the evaluation criteria. Good luck with your projects and oral exams!
