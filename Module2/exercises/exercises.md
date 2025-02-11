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



---


# **Hands-on Exercise 3: Kafka Data Processing with Employee Records**  

For this hands-on activity, you can extend the exercise2-consumer.py and exercise2-producer.py files located in the exercises/exercise2 folder.

In this exercise, you will extend Kafka integration by implementing **data processing** in addition to streaming. 
You will modify the **Kafka Producer** to send employee records 
and the **Kafka Consumer** to process the data before displaying or storing it.  


## **Task 1: Set Up Kafka and Define a Topic**  
1. Ensure Kafka is installed and running on your local machine.  
2. If you don't have one, define a Kafka topic named **"dss-module2-processing"**.  


## **Task 2: Design the Kafka Producer**  
1. Load the **Employee.csv** dataset using the `pandas` library.  
2. Convert each employee record into a **JSON object**.  
3. Send the JSON data to the Kafka topic **"dss-module2-processing"**, one record at a time, with a 2-second interval between each message.
4. Ensure each message in Kafka has a **unique key** (e.g., generate sequence number or get df sequence number).  
5. Implement a **callback function** to verify successful message delivery.  


## **Task 3: Implement the Kafka Consumer with Data Processing**  
1. Consume records from the **"dss-module2-processing"** topic. 
2. Process each record individually before forwarding the transformed data. 


### Data Cleaning  
- **Standardize categorical fields** to ensure consistency:  
  - `Education` → Convert to lowercase (e.g., `"Bachelor's"` → `"bachelor's"`).  
  - `Gender` → Convert to lowercase and capitalize the first letter (e.g., `"male"` → `"Male"`).  
  - `EverBenched` → Convert `"Yes"` / `"No"` to binary **1** / **0**.  
- **Trim leading and trailing spaces** from text fields (e.g., `City`, `Education`).  

---

### Feature Engineering  
- **Calculate a new feature: `YearsSinceJoining`**  
  - Compute `YearsSinceJoining = CurrentYear - JoiningYear`.  
  - Example: If `CurrentYear = 2025` and `JoiningYear = 2019`, then:  
    ```
    YearsSinceJoining = 2025 - 2019 = 6
    ```

---

### Encoding for ML Models  
- Convert categorical values into numeric representations for ML models:  
  - **Education Mapping**:  
    ```json
    {
      "bachelors": 1,
      "masters": 2,
      "phd": 3
    }
    ```
    - Default to `0` if the value is unknown.  
  - **Gender Mapping**:  
    ```json
    {
      "Male": 0,
      "Female": 1
    }
    ```
    - Default to `-1` if the value is unknown.  

---

### Business Logic / Risk Flagging  
- **Identify high-risk employees** based on specific conditions:  
  - An employee is at **high risk of leaving** if:  
    - **ExperienceInCurrentDomain < 2**  
    - **Age < 30**  
    - **LeaveOrNot = 1**  
  - Assign:  
    ```json
    {
      "HighRiskEmployee": 1
    }
    ```
    - Otherwise, assign `0`.  

---

### Data Validation & Error Handling  
- **Check for missing or incorrect values:**  
  - Ensure required fields (`Age`, `JoiningYear`, `ExperienceInCurrentDomain`) are present.  
  - Verify that numerical values (`Age`, `YearsSinceJoining`, `ExperienceInCurrentDomain`) are **within a valid range**.  
- **Validation rules:**  
  - `Age` should be **between 18 and 65**.  
  - `ExperienceInCurrentDomain` should **not exceed `YearsSinceJoining`**.  
- If a record is invalid, **log an error and skip processing** instead of crashing the pipeline.  

---

3. Display Processed Employee Records in JSON Format  
After processing, the transformed employee data should be displayed in **JSON format**.  

  - Example output:  
    ```json
    {
      "EmployeeID": "12345",
      "Education": 1,
      "Gender": "Female",
      "EverBenched": 0,
      "YearsSinceJoining": 6,
      "HighRiskEmployee": 0
    }
    ```  

4. Implement error handling for invalid records (e.g., missing fields, incorrect data types).  


## **Task 4: Extend the Consumer to Store Processed Data (Optional Bonus Challenge)**  
1. Store processed data into a **PostgreSQL/MySQL database**.  
2. Save only high-risk employees for further analysis.
