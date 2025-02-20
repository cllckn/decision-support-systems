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
