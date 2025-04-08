# **Assignment 2: Developing a Web-Based Streaming Application**

## **Objective**
In this assignment, you will build a web application using **Node.js, PostgreSQL (Pagila sample database), jQuery, and CSS**. The application will provide a user interface to manage **customers** and **payments**, integrate **Kafka-based streaming**, and implement **business logic processing** using a Python consumer.

## **Requirements**

### **1. Database Setup (PostgreSQL - Pagila Sample Database)**
- Use the [**Pagila sample database**](https://github.com/cllckn/database-management-systems/blob/main/resources/dbs/dvdrental.zip).
- Work with the **customer** and **payment** tables.
- construct a new table `logs` to store high-value transactions.  
  - Suggested schema for `logs`:  
    ```sql
    CREATE TABLE logs (
        id SERIAL PRIMARY KEY,
        payment_id INTEGER,
        customer_id INTEGER,
        amount NUMERIC(10,2),
        log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ```

### **2. Backend (Node.js & Express)**
- Implement CRUD operations for **customer** and **payment** tables using **Express Router**.
- Define RESTful API endpoints for:
  - **Customers** (`GET /customers`, `POST /customers`, `PUT /customers/:id`, `DELETE /customers/:id`)
  - **Payments** (`GET /payments`, `POST /payments`, `PUT /payments/:id`, `DELETE /payments/:id`)
  - **Logs** (`GET /logs`) – Retrieves all records from the `logs` table.
- Ensure API responses are in JSON format.

### **3. Frontend (jQuery & CSS)**
- Develop a **user-friendly interface** for managing customers and payments.
- Use **jQuery** for dynamic content updates (AJAX calls to the API).
- Apply **CSS (Pure CSS, Tailwind, or another framework)** for styling.
- Include an interface to display **logs of high-value transactions**.

### **4. Apache Kafka Integration**
#### **Producer (Node.js)**
- Upon **insert/update** in `customer` or `payment`, send the updated data to **Kafka topics**:
  - `"dss-customer-stream"` for customer changes.
  - `"dss-payment-stream"` for payment changes.

#### **Consumer Group (Python)**
- Define a **Kafka consumer group** with two consumers.
- Each consumer should:
  - **Read records** from `"dss-payment-stream"`.
  - Apply **business logic**:
    - **Cleaning**: Handle missing values, replace empty payment types with `"unknown"`, discard records with negative amounts.
    - **Categorization**:
      - `payment_type`: `"cash" → 0, "card" → 1, "unknown" → -1`
      - `customer_active`: `"true" → 1, "false" → 0`
      - `amount_category`: `< 2 → small (1), 2-5 → medium (2), > 5 → large (3)`
    - **Business rule**: If the **amount > 8**, send the transaction to a **Node.js Kafka topic** (`"high-value-transactions"`) for logging.

#### **Consumer (Node.js)**
- Listen to the `"high-value-transactions"` topic.
- Insert high-value transactions into the `logs` table.

### **5. Logging & API Integration**
- Define a **route (`GET /logs`)** to fetch all logs.
- Display logs in the frontend.

## **Deliverables**
1. **Node.js application source code** with Express-based API.
2. **Frontend interface** (jQuery + CSS) for managing customers and payments.
3. **Kafka Producer & Consumers (Node.js and Python)** implementation.
4. **PostgreSQL schema** for `logs` table.
5. **README file** explaining setup and usage.



---

## Evaluation Criteria
The assignment will be evaluated based on two primary components:

Project Implementation: The quality and effectiveness of the project you implement.

Oral Exam Performance: Your performance during the oral exam, which will take place during class in Week 11(specific day and time to be announced later).

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
   - dss-assignment2-StudentName
* File Naming: Ensure that the compressed file is named appropriately, using the following format:
   - StudentName-Report.zip
* Only **one submission per group** is sufficient.

## Late Submission and Oral Exam Policy
Students must submit their **reports and source code** before the **oral exam**, as the oral exam time is crucial for evaluation.
If a student or group is unable to attend the scheduled oral exam, they will be allowed to defend their project one week later during course hours.
However, this late defense of the oral exam will result in a 20% penalty on the total grade.

**Please note that there will not be another opportunity to defend the project beyond this timeframe.**

### By adhering to these guidelines and policies, you will ensure that your submission is complete and meets the evaluation criteria. Good luck with your projects and oral exams!
