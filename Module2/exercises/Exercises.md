# Exercises
## **Hands-on Exercise 1: Employee Data Analysis with Pandas**

### **Objective**
In this exercise, you will practice data analysis using the pandas library by working with an employee dataset. You will calculate statistical metrics, group data, and convert the dataset into JSON format.

### **Task 1: Download and Load the Dataset**
1. Download the **Employee.csv** dataset from the following address:  
   [Employee Dataset](https://www.kaggle.com/datasets/tawfikelmetwally/employee-dataset)
2. Load the dataset using the `pandas` library in Python.

### **Task 2: Perform Data Analysis**
Using pandas, perform the following operations:
1. Calculate the **minimum, maximum, and average age** of employees.
2. Calculate the **average age by gender** using grouping.
3. Count how many employees belong to each **education group**.

### **Task 3: Convert Data to JSON**
1. Convert the dataset into JSON format.
2. Store the JSON data in a file named `employee_data.json`.

### **Additional Challenges (Optional)**
- Visualize the age distribution using a histogram.

---

## **Hands-on Exercise 2: Kafka Integration with Employee Data**

In this exercise, you will integrate Apache Kafka to stream employee data. You will create a **Kafka Producer** to send employee records and a **Kafka Consumer** to receive and display the data.  


### **Task 1: Set Up Kafka and Create a Topic**  
1. Install and run Kafka on your local machine or use a cloud Kafka service.  
2. Form a Kafka topic named **"dss-module2-exercise"**.  


### **Task 2: Design the Kafka Producer**  
1. Load the **Employee.csv** dataset using the `pandas` library.  
2. Convert each employee record into a JSON object.  
3. Send the JSON data to the Kafka topic **"dss-module2-exercise"**.  


### **Task 3: Design the Kafka Consumer**  
1. Develop a Kafka Consumer that subscribes to the **"dss-module2-exercise"** topic.  
2. Receive and print each employee record to the screen.  


### **Task 4: Run the Producer and Consumer**  
- Start the **Producer** to send employee data.  
- Run the **Consumer** to receive and display messages in real time.  


### **Additional Challenges (Optional)**  
- Modify the consumer to store the received data into a database or a JSON file.  

