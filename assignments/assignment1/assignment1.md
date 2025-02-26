# Assignment 1: Processing and Analyzing Payment & Customer Data
### Objective:
In this assignment, you will work with the **payment.csv** and **customer.csv** datasets. Your task is to merge these datasets, perform statistical calculations, 
process the combined data using **Pandas** , and transfer the data between processing units as a stream.

### Task 1: Batch Processing with Pandas


1. **Merge the Datasets**  
   - Load **payment.csv** and **customer.csv** datasets using Pandas.  
   - Merge them on the `customer_id` column.  
   - The final dataset should contain all **payment information** along with the **customer's first name, last name, and address**.

2. **Save the Merged Dataset**  
   - After merging, save the resulting dataset as a **JSON file** named:  
     ```
     merged_payments_customers.json
     ```

3. **Batch Statistical Calculations**  
   Perform the following statistical calculations on the merged dataset:  
   - **Total Payment Amount**: Compute the sum of all `amount` values.  
   - **Average Payment Per Customer**: Compute the mean payment amount per customer.  
   - **Payment Type Distribution**: 
     - Count occurrences of each payment type (e.g., cash, card). 
     - Handle missing or null values in the `payment_type` column appropriately.
     - **Plot a bar chart** or **pie chart** to visualize the distribution. 
   - **Top 5 Customers by Total Payment**: Identify the five customers who made the highest total payments.  


### Task 2: Stream Processing with Apache Kafka

1. **Define an Apache Kafka Producer**
   - Read the dataset `merged_payments_customers.json` **one record at a time**.
   - Send each record to the Kafka topic **"dss-payment-stream"**.
   - Introduce a **0.5-second delay** between messages to simulate real-time streaming.

2. **Define an Apache Kafka Consumer Group**
   - Define a consumer group with **two consumers**.
   - Each consumer should:
     - **Read** incoming records from the **"dss-payment-stream"** topic.
     - **For each record apply data processing**:
       - **Cleaning:** Handle missing or invalid values.
         - Replace empty payment types with "unknown".
         - Discard records with a negative amount value. 
       - **Category transformation:** Convert categorical values to numerical encoding.
         - payment_type	"cash" / "card"	cash → 0, card → 1, unknown → -1
         - customer_active	"true", "false"	true → 1, false → 0
         - amount_category	< 2, 2-5, > 5	small → 1, medium → 2, large → 3
       - **Business logic:** Identify high-value transactions (`amount > 8`).
     - **Write processed data to the console**.
3. **Define a Logging Consumer**
   - Implement a **logging consumer** that listens to **"dss-payment-stream"**.
   - Write all received records to a **CSV file** in **append mode** with a timestamp.

---

## Evaluation Criteria
The assignment will be evaluated based on two primary components:

Project Implementation: The quality and effectiveness of the project you implement.

Oral Exam Performance: Your performance during the oral exam, which will take place during class in Week 6(specific day and time to be announced later).

## Oral Exam Requirement

The oral exam is **mandatory** as part of the evaluation process. Students will be assessed based on their understanding of the material presented in their **reports** and **source codes**.

### **During the Oral Exam:**
- Reports must be **open** and accessible.
- Source codes must be **ready to show** in the IDE.
- Tests must be **ready to run** for demonstration.

## Group Work
Students may form groups of up to two members.

All group members will receive a common grade for the assignment.

Instructors may ask questions to any group member during the oral exam, so it is essential that every member understands all aspects of the project. 
Therefore, each group member must be well-versed in every detail related to the project.

## Report Structure
While there is no standard template for the report, it must include the following essential components:

### Cover Page
Student Information: Include your full name, student ID, course name, and date of submission.

Title of the Report: Clearly state the title of your study or project.

### Study Explanation
The report must provide a straightforward explanation of your study, including:

Objective: Clearly outline the purpose and goals of your study.

Methodology: Describe the methods and approaches used in your research or project.

Conclusion: Summarize the key points and findings of your study.

### Additional Recommendations

Ensure that your report is well-organized and free of grammatical errors.

Use clear headings and subheadings to enhance readability.

## Email Submission

Students are required to **compress** their report and source codes into a **single file** (or provide a **GitHub link** to their source code repository) and submit it via **email** before oral examination.

* Email Subject: Use the following format for the subject line of your email:
   - dss-assignment1-StudentName
* File Naming: Ensure that the compressed file is named appropriately, using the following format:
   - StudentName-Report.zip
* Only **one submission per group** is sufficient.

## Technology Requirements
Students are **required** to use the following technologies for their project:
- **Python-pandas** for implementation
- **Apache** for messaging

## Late Submission and Oral Exam Policy
Students must submit their **reports and source codes** before the **oral exam** (during class in **Week 6**), as the oral exam time is crucial for evaluation.
If a student or group is unable to attend the scheduled oral exam, they will be allowed to defend their project one week later during course hours.
However, this late defense of the oral exam will result in a 20% penalty on the total grade.

**Please note that there will not be another opportunity to defend the project beyond this timeframe.**

### By adhering to these guidelines and policies, you will ensure that your submission is complete and meets the evaluation criteria. Good luck with your projects and oral exams!
