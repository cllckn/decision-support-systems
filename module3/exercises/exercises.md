# **Hands-on Exercise1: Processing Student List in Node.js**

## **Objective**
In this exercise, you will:
1. **Read the CSV file** and convert it into a **JSON object**.
2. **Manipulate JSON data** by:
    - Increasing each student's **Age** by 1.
    - Adding a new field **`ScholarshipStatus`** (randomly assigned `Yes` or `No`).
    - Filtering students **older than 22 years**.
    - **Performing grade-related operations**:
        - Count the number of students in each **grade category (A, B, C, etc.)**.
        - Find the **highest and lowest grades** in the dataset.
        - Calculate the **average grade distribution**.
3. **Save the modified JSON to a new file**.
4. **Extract insights** from the dataset.



## **Tasks**

### **1. Form a CSV File**
- Make a CSV file named `students.csv` containing following 25 students.

```plaintext

Name,Age,Faculty,Grade
Aruzhan Nurtas,20,Engineering,B
Ivan Petrov,22,Mathematics,A
Bolat Zhanibekov,21,Computer Science,B
Natalia Sokolova,23,Physics,A
Daniyar Akhmetov,19,Engineering,C
Sergey Ivanov,22,Mathematics,B
Madina Tulegenova,20,Biology,A
Oleg Smirnov,21,Physics,B
Alia Iskakova,19,Medicine,C
Ruslan Karimov,24,Computer Science,A
Anastasia Fedorova,20,Engineering,B
Zhanar Kairatova,22,Mathematics,A
Vladimir Kuznetsov,21,Physics,C
Saule Mukasheva,20,Medicine,B
Mikhail Romanov,23,Computer Science,A
Aliya Sadykova,21,Engineering,C
Stepan Orlov,19,Mathematics,B
Aiman Yessimova,22,Biology,A
Dmitry Voronin,20,Physics,B
Zarina Abdullina,19,Medicine,C
Nikolay Ponomarev,24,Computer Science,A
Samal Rakhmetova,20,Engineering,B
Ekaterina Ivanova,21,Mathematics,C
Yerlan Mukhtar,23,Physics,A
Polina Andreeva,22,Biology,B
```

### **2. Read the CSV File and Convert to JSON**
- Read the `students.csv` file using Node.js.
- Convert its content into a **JSON array**.

### **3. Modify JSON Data**
- **Add a new field `ScholarshipStatus`**, randomly assigning `"Yes"` or `"No"`.
- **Filter students who are older than 21 years**.

### **4. Save Updated JSON to a File**
- Write the modified JSON data to a new file called `updated_students.json`.

### **5. Extract Insights from Data**
- Count the **total number of students**.
- Count how many students **received a scholarship**.
- **Group students by faculty** and count the number of students in each faculty.

---

### **Additional Challenges (Optional)**
These tasks are for students to implement at home:

- **Sort students by age**.
- **Group students based on their age range** (e.g., 18-20, 21-23, 24+).
- **Find the faculty with the most students**.



---








# Hands-On Exercise 2: Build a Simple Web Application with Node.js, HTML, CSS, and JavaScript

## Objective

Students will develop a basic web application that includes a login form and a dashboard page. The application will utilize:

- **Node.js** to serve static files and handle routing.
- **HTML & CSS** for structuring and styling the pages.
- **JavaScript** for client-side form validation and handling login logic.

## Tasks

### Task 1: Set Up Node.js Server
- Install Node.js (Ensure students have Node.js installed).
- Initialize a Node.js project.
- Install Express.
- Develop a new file for the server and set up routing.
- Set up a `public` folder to store static files (HTML, CSS, JavaScript).

### Task 2: Design HTML & CSS for Login Form
- Inside the `public` folder, develop an HTML file for the login page.
- Add form elements for username, password, and a login button.
- Build a CSS file to style the login form, ensuring a user-friendly design.

### Task 3: Implement JavaScript for Login Validation
- Add JavaScript to validate required fields in the login form.
- Implement client-side logic to check if the username and password match predefined values.
- Display an error message if the credentials are incorrect.
- Redirect to the dashboard upon successful login.

### Task 4: Develop the Dashboard Page
- Develop an HTML file for the dashboard.
- Ensure it includes a welcome message and a logout link.

### Task 5: Run and Test the Application
- Start the Node.js server.
- Open the application in a web browser.
- **Test login:**
   - Enter valid credentials to access the dashboard.
   - Enter incorrect credentials to see an error message.

## Expected Outcome

Students will have a functional login system where:

- Form fields are required.
- JavaScript validates credentials.
- Users are redirected to a dashboard upon successful login.
- Incorrect login displays an error message.


---








# **Hands-on Exercise 3: Extending the Web Application with jQuery**

In this exercise, the web application implemented in Hands-on Exercise 2 will be extended by replacing and enhancing the login validation and dashboard functionality using **jQuery**.

## **Task 3: Implement jQuery for Login Validation**

### **Objective**
Replace JavaScript-based validation with **jQuery** to improve form handling, validation, and interactivity.

### **Steps**
1. **Validate Required Fields**
    - Use jQuery to ensure both username and password fields are not empty.
    - Display an error message if any field is left blank.

2. **Client-side Credential Check**
    - Implement logic in jQuery to check if the entered username and password match predefined values.

3. **Display Error Message for Incorrect Credentials**
    - Show a styled error message if login credentials do not match the predefined values.

4. **Redirect to Dashboard on Successful Login**
    - If login is successful, redirect the user to the dashboard page.


## **Task 4: Develop the Dashboard Page with jQuery**

### **Objective**
Enhance the **Dashboard Page** using **jQuery**.

### **Steps**
1. **Develop an HTML File for the Dashboard**
    - Include a **welcome message** using jQuery.

2. **Provide a Navigation Option to Return to the Login Page**
    - Add a **button** that allows users to return to the login page.
    - Use jQuery to handle the button click event.

3. **Enhance User Experience with jQuery**
    - Apply jQuery effects like **fade-in animation** for the welcome message.


## **Expected Outcome**
By completing this exercise, students will:
- Use **jQuery** for form validation and login handling.
- Enhance the **user experience** with jQuery-based interactivity.
- Implement **basic page navigation** with jQuery.

---







## Hands-on Exercise4 : In-Memory REST API Development in Node.js

##  Objective
In this exercise, students will develop a **RESTful API** in **Node.js** using **Express.js** and an 
**in-memory database** for managing customer data.

## Tasks

### **Setup a Basic Express Server**
- Initialize a new **Node.js project**.
- Install **Express.js**.
- Set up a basic Express server.

### **Define an In-Memory Database**
- Instead of using a database, store customer data in a **JavaScript array**.
- Each customer should have:
    - `id` (integer)
    - `name` (string)
    - `email` (string)
    - `phone` (string)
    - `city` (string)

### **Implement API Endpoints**
Develop the following RESTful routes:

#### **GET /api/customers**
- Return the list of all customers.

#### **GET /api/customers/:id**
- Retrieve a specific customer by ID.
- If the ID is not found, return a **404 error**.

#### **POST /api/customers**
- Accept a **JSON request body** with customer details.
- Add the new customer to the in-memory array.
- Respond with the added customer.

#### **PUT /api/customers/:id**
- Update an existing customer by ID.
- Only modify the provided fields.
- If the ID is not found, return a **404 error**.

#### **DELETE /api/customers/:id**
- Remove a customer by ID.
- Respond with a success message.

### **Test API Using cURL or Postman**
- Use **cURL commands** and **IntelliJ http client** to test each endpoint.
- Verify that customer data updates correctly.

## **Completion Criteria**
- The API should be functional with **GET, POST, PUT, and DELETE** routes.
- The in-memory database should correctly store and modify customer data.
- API should handle errors properly.


### **Additional Challenges (Optional)**
These tasks are for students to implement at home:

- Try using Postman for testing APIs, as it provides an intuitive interface for making HTTP requests and analyzing responses.
- Add validation for **email format** and **phone number** before adding a customer.
- Implement a **search feature** (`GET /api/customers?city=Astana`) to filter customers by city.

---




# **Hands-On Exercise 5: Extending REST API to a Web Application**

## **Objective**
In this exercise, you will extend the REST API developed in **Hands-On Exercise 4**, which manages **customer data**, 
by developing a **web application** with **jQuery-based web pages** to perform **CRUD (Create, Read, Update, Delete) operations**.

Each customer should have:
- `id` (integer)
- `name` (string)
- `email` (string)
- `phone` (string)
- `city` (string)


## **Task 1: Develop the Customer List Page**
This page displays all customers and allows users to **delete a customer**.

### **Steps**
- Retrieve the customer list from the REST API using an asynchronous request.
- Display the customers in a structured format.
- Provide a delete option for each customer, allowing users to remove them.

---

## **Task 2: Implement Add Customer Page**
This page contains a **form to add a new customer**.

### **Steps**
- Capture user input for customer details.
- Send the input data to the REST API.
- Ensure the customer is added and update the displayed list accordingly.

---

## **Task 3: Implement Update Customer Page**
This page allows updating an existing customer's details.

### **Steps**
- Fetch the details of a selected customer from the REST API.
- Prefill the form with existing values.
- Allow users to modify details and send the updated data to the API.

---

## **Task 4: Implement jQuery AJAX Requests**
Use **jQuery AJAX** to handle asynchronous data interactions.

### **Steps**
- Fetch the customer list from the API and update the page dynamically.
- Send new customer data when adding a customer.
- Update customer details when modifications are made.
- Delete a customer and refresh the displayed list.

---

## **Task 5: Test and Verify**
- Open the web pages and check if the data loads correctly.
- Perform add, update, and delete operations.
- Verify the API responses to ensure proper functionality.
- Test the API using cURL or http client.







# **Hands-on Exercise6**

Add search and update functions for the developed app in Exercise 5.







# **Hands-on Exercise 7**
    Style the web app developed in Exercise 6 using Tailwind or another framework.





# Hands-on Exercise 8:  REST API Development With Database Support

Integrate PostgreSQL into the application developed in hands-on exercise 6.

You are required to initialize a new database and construct the relevant table.





# **Hands-On Exercise 9: Real-Time Employee Risk Assessment Using Apache Kafka**

## **Objective**
In this exercise, you will build a **real-time data processing system** using **Apache Kafka, Node.js, and Python**. The system will:
- Accept employee information through a **REST API**.
- Send the data to **Apache Kafka** (`dss-employee` topic).
- Process the data in **Python** and add a risk assessment field (`HighRiskEmployee`).
- Publish the processed data to **Kafka** (`dss-employee-processed` topic).
- Consume the processed data in **Node.js**, store it in memory, and display it on a **web interface using jQuery**.

---

## **System Requirements**

### **REST API (Node.js)**
1. Implement an **Express.js** REST API.
2. Provide a **POST endpoint** (`/api/employee`) that accepts the following employee data:

```json
{
  "Education": "Bachelors",
  "JoiningYear": 2013,
  "City": "Pune",
  "PaymentTier": 1,
  "Age": 28,
  "Gender": "Female",
  "EverBenched": "No",
  "ExperienceInCurrentDomain": 3
}
```
3. Publish this data to Apache Kafka (dss-employee topic).

### Python Kafka Consumer
1. Consume messages from dss-employee topic.
2. Apply the following business logic:
```shell
data["HighRiskEmployee"] = 1 if (data["ExperienceInCurrentDomain"] < 2 and data["Age"] < 30 and data["LeaveOrNot"] == 1) else 0

```
3. Publish the processed data to dss-employee-processed topic.

### Kafka Consumer in Node.js
1. Listen for processed employee data on dss-employee-processed topic.
2. Store the processed data in an in-memory JSON array.
3. Provide an endpoint (GET /api/employees/processed) to retrieve processed employee data.

### Web Interface (jQuery)
1. Build a simple HTML page with a form to submit employee data.
2. Use jQuery and AJAX to:
3. Submit employee data via POST /api/employee.
4. Fetch and display processed employee data from GET /api/employees/processed.

### **Additional Challenges (Optional)**

- **Add database support**.
