# Module 2: Data Processing and Communication

## Learning Objectives
By the end of this module, students will be able to:
- Perform data manipulation, cleaning, and preprocessing using Python.
- Understand Kafka's role in real-time data streaming for Decision Support Systems.
- Set up Kafka producers and consumers for data communication.
- Integrate Kafka with Python for streaming data processing.

---

## Lesson 1: Data Manipulation with Python
### Topics Covered
- Introduction to `pandas` and `numpy` for data handling.
- Loading and exploring datasets.
- Filtering, sorting, and grouping data.
- Applying functions and transformations.
- JSON standard



### The Pandas Library

The Pandas library in Python is one of the most widely used libraries for data manipulation and analysis. It provides high-performance, easy-to-use data structures and tools for working with structured data. The primary purpose of Pandas is to make data cleaning, exploration, and analysis faster and easier.

Key Abilities of Pandas

    Data Structures: The primary data structures in Pandas are Series (1-dimensional) and DataFrame (2-dimensional). These structures allow for easy handling of heterogeneous data types.
    Data Manipulation: Pandas offers a wide range of functions for data manipulation, including filtering, grouping, merging, reshaping, and pivoting data.
    Handling Missing Data: It provides robust methods for detecting and filling missing values, enabling cleaner datasets.
    Time Series Analysis: Pandas excels in handling time series data, allowing for date-based indexing and operations.
    Data Import/Export: It supports reading from and writing to various file formats such as CSV, Excel, SQL databases, and more.
    Statistical Functions: The library includes built-in functions for statistical analysis, making it easier to perform calculations on datasets.
~~~bash
pip install pandas
~~~

#### Code Examples
[pandas](pandas-fundamentals.py)


### JSON standard

JSON (JavaScript Object Notation) is a lightweight data format used for storing and exchanging data. It represents data in key-value pairs and is commonly used in web applications and APIs.

a JSON structure containing three student records, each with name, surname, age, and address fields:
~~~json
{
  "students": [
    {
      "name": "John",
      "surname": "Doe",
      "age": 20,
      "address": "123 Main St, New York, USA"
    },
    {
      "name": "Alice",
      "surname": "Smith",
      "age": 22,
      "address": "456 Elm St, Los Angeles, USA"
    },
    {
      "name": "Bob",
      "surname": "Johnson",
      "age": 21,
      "address": "789 Oak St, Chicago, USA"
    }
  ]
}

~~~

In this JSON structure:

The root object contains a key "students", which holds an array of student records.

Each student record is an object with four key-value pairs: "name", "surname", "age", and "address".

Strings are enclosed in double quotes (""), and numbers do not require quotes.

This format makes it easy to store and retrieve structured data.

In JSON, elements refer to key-value pairs inside an object. Each student record contains four elements:

    "name" (String)
    "surname" (String)
    "age" (Number)
    "address" (String)



#### Code Examples
[json](json-standard.py)



### The NumPy Library

The NumPy library in Python is a fundamental package for numerical computing. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these data structures efficiently. NumPy is widely used in scientific computing, data analysis, and machine learning applications.

Key Abilities of NumPy

- **N-Dimensional Arrays:** The core data structure in NumPy is the `ndarray`, which allows for efficient storage and manipulation of large datasets.
- **Mathematical Functions:** NumPy provides optimized functions for mathematical operations, including linear algebra, statistical calculations, and Fourier transforms.
- **Broadcasting:** Enables element-wise operations between arrays of different shapes, reducing the need for explicit looping.
- **Indexing and Slicing:** Offers powerful tools for extracting and modifying subsets of arrays.
- **Performance Optimization:** NumPy operations are implemented in C, making them significantly faster than pure Python loops.
- **Integration with Other Libraries:** Many scientific and machine learning libraries, such as Pandas, SciPy, and TensorFlow, rely on NumPy for data handling.

~~~bash
pip install numpy
~~~

### Code Examples
[numpy](numpy-fundamentals.py)

## Lesson 2: Introduction to Kafka and its Role in DSS
### Topics Covered
- What is Kafka and why is it used?
- Kafka’s architecture: Producers, Topics, Brokers, Consumers.
- Kafka’s role in real-time data streaming.

### Apache Kafka
Apache Kafka is a distributed event streaming platform designed for handling real-time data feeds. In Decision Support Systems (DSS), Kafka plays a crucial role in processing and transmitting large volumes of data efficiently, enabling real-time analytics and decision-making.  

Key Aspects of Kafka in DSS  

- **Publish-Subscribe Messaging:** Kafka enables decoupled communication between data producers and consumers, allowing multiple applications to process data independently.  
- **Scalability and Fault Tolerance:** Designed for distributed environments, Kafka can handle high-throughput data streams while ensuring reliability.  
- **Stream Processing:** Supports real-time data transformation and aggregation using Kafka Streams and integration with frameworks like Apache Flink or Spark.  
- **Data Integration:** Acts as a central hub for integrating various data sources, including databases, IoT devices, and enterprise applications.  
- **Event-Driven Architecture:** Enables DSS applications to react dynamically to incoming data, improving responsiveness and automation.  

~~~bash
 pip install confluent-kafka
~~~ 

### Code Examples
[Apache Kafka](consumer1.py)


