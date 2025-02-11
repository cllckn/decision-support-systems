# Module 2: Data Processing and Communication

## Learning Objectives
By the end of this module, students will be able to:
- Perform data manipulation, cleaning, and preprocessing using Python.
- Understand Kafka's role in real-time data streaming for Decision Support Systems.
- Set up Kafka producers and consumers for data communication.
- Grasp the essentials of data processing paradigms.
- Integrate Kafka with Python for streaming data processing.

---

## Part 1: Data Manipulation with Python
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
[pandas](part1/pandas-fundamentals.py)


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
[json](part1/json-standard.py)



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
[numpy](part1/numpy-fundamentals.py)

## Part 2: Introduction to Kafka and its Role in DSS
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

[Apache Kafka](dss-module2-apache-kafka.pdf)

~~~bash
 pip install confluent-kafka
~~~ 

#### Code Examples
[kafka consumer1](part2/consumer1.py)
[kafka producer1](part2/producer1.py)

[kafka consumer1](part2/consumer1.py)
[kafka producer1](part2/producer2.py)


##  Part 3: Essentials of Data Processing Paradigms
### Topics Covered 
- What are data processing paradigms?  
- Batch Processing vs. Stream Processing  
- Advanced or Hybrid Techniques  


Data processing paradigms define how data is collected, processed, and analyzed to extract insights. 

They can be broadly categorized into **main techniques** and **advanced or hybrid techniques**. 

The choice of a paradigm depends on factors such as latency requirements, data volume, and processing complexity.

Below is a structured breakdown:


### **Main Techniques**

These are the foundational paradigms used in most data processing systems.


#### 1. **Batch Processing**
Batch processing is the execution of data processing tasks in bulk at scheduled intervals or on-demand. 
It is best suited for handling large volumes of historical data efficiently.
It is ideal for scenarios where real-time processing is not required.

##### **Key Characteristics:**
* Processes data in **batches** (entire dataset at once).  
* **Higher latency** (minutes to hours).  
* Suitable for **historical analysis, reporting, ETL jobs**.  
* Requires **storage** to hold data until processed.  
* Optimized for **throughput rather than real-time speed**. 

##### **Use Cases**  
* Payroll processing (e.g., generating monthly salaries).  
* Data warehouse ETL (Extract, Transform, Load) jobs.  
* Aggregating log files for business intelligence reports. 
##### Technologies:
- **Apache Hadoop:** A framework for distributed storage and processing of large datasets.
- **Apache Spark:** A fast engine for large-scale data processing.


#### 2. **Stream Processing**
Stream processing deals with real-time (or instance) data processing, where data is processed as it arrives.

##### Key Characteristics:
* Processes events in real-time (low latency: milliseconds to seconds).
* Continuous data processing (event-driven).
* Handles high-velocity, high-volume data.
* Suitable for monitoring, fraud detection, IoT, stock trading.
* Often requires message brokers (Kafka, Pulsar) and stream processors (Flink, Spark Streaming).

##### **Use Cases**  
* Fraud detection (e.g., identifying suspicious transactions).
* IoT sensor data processing (e.g., smart factory, smart city).
* Stock market monitoring (real-time price updates).
* Recommendation systems (e.g., suggesting products based on recent activity).


##### Technologies:
- **Apache Kafka:** A distributed event streaming platform.
- **Apache Flink:** A framework for stateful computations over data streams.
- **Apache Storm:** A real-time computation system.



### **Advanced or Hybrid Techniques**

These paradigms build on the main techniques to address more complex use cases or optimize performance.


#### 1. **Micro-Batch Processing**
Micro-batch processing is a hybrid approach that processes data in small batches, offering a balance between batch and stream processing.

#### Key Characteristics:
- **Data Collection:** Data is processed in small, frequent batches.
- **Latency:** Lower latency than batch processing but higher than stream processing.
- **Use Cases:** Real-time analytics with moderate latency requirements.

#### Technologies:
- **Apache Spark Streaming:** Extends Spark for micro-batch processing.
- **Google Dataflow:** A fully managed service for stream and batch processing.

---

### 2. **Event-Driven Processing**
Event-driven processing focuses on triggering actions based on incoming events 
(user actions, system updates, external API calls).


#### Key Characteristics:
* Asynchronous and reactive processing.
* Commonly implemented using message brokers (Kafka, RabbitMQ, AWS SQS).
* Enables microservices-based architectures.

##### **Use Cases**  
* Real-time notifications (e.g., push notifications, email alerts).
* User activity tracking (e.g., logging interactions on websites).
* Order processing systems (e.g., e-commerce transactions).

#### Technologies:
- **Apache Kafka Streams:** A client library for building event-driven applications.
- **AWS Lambda:** A serverless compute service for event-driven processing.

---

### 3. **Distributed Processing**
Distributed processing involves splitting data processing tasks across multiple nodes or machines to handle large-scale data efficiently.

#### Key Characteristics:
- **Data Collection:** Data is distributed across a cluster of machines.
- **Latency:** Depends on the underlying processing paradigm (batch, stream, etc.).
- **Use Cases:** Big data analytics, distributed databases, and large-scale machine learning.

#### Technologies:
- **Apache Hadoop:** Distributed storage and processing.
- **Apache Spark:** Distributed data processing engine.
- **Google BigQuery:** A fully managed, serverless data warehouse.

---

### 4. **In-Memory Processing**
In-memory processing stores data in RAM instead of disk, enabling faster data access and processing.

#### Key Characteristics:
- **Data Collection:** Data is stored and processed in memory.
- **Latency:** Extremely low latency due to fast memory access.
- **Use Cases:** Real-time analytics, caching, and high-speed transactions.

#### Technologies:
- **Apache Ignite:** An in-memory computing platform.
- **Redis:** An in-memory data structure store.

---

### 5. **Lambda Architecture**
Lambda architecture combines batch and stream processing to provide a comprehensive data processing solution.

#### Key Characteristics:
- **Data Collection:** Data is processed in both batch and real-time layers.
- **Latency:** Balances low-latency (stream) and high-throughput (batch) processing.
- **Use Cases:** Systems requiring both real-time and historical data analysis.

#### Technologies:
- **Apache Kafka:** For real-time data ingestion.
- **Apache Hadoop:** For batch processing.
- **Apache Spark:** For both batch and stream processing.

---

### 6. **Kappa Architecture**
Kappa architecture simplifies data processing by using a single stream processing layer for both real-time and historical data.

#### Key Characteristics:
- **Data Collection:** Data is processed as a stream, with historical data replayed when needed.
- **Latency:** Low latency for real-time processing.
- **Use Cases:** Systems where real-time processing is prioritized, and historical data is occasionally reprocessed.

#### Technologies:
- **Apache Kafka:** For data streaming and replay.
- **Apache Flink:** For stream processing.

---

## **Conclusion**
The choice of data processing paradigm depends on the specific requirements of the application, such as latency, throughput, and data volume. 
**Batch** and **stream processing** are the foundational techniques, 
while **advanced or hybrid techniques** like micro-batch, event-driven, distributed, in-memory, Lambda, and Kappa architectures address more complex use cases and optimize performance.

* Batch Processing: Good for large-scale historical data processing but has higher latency.
* Stream Processing: Ideal for real-time analytics, but requires low-latency infrastructure.
* Event-Driven Processing: Useful for asynchronous, microservices-based workflows.
* Hybrid Models: Micro-Batch, Lambda (Batch + Stream), Kappa (Stream-only) architectures balance performance trade-offs.


#### Code Examples
[batch procuder](part3/employee-data-batch-producer.py)
[streaming procuder](part3/employee-data-streaming-producer.py)
[parallel streamin consumer 1](part3/parallel-stream-processing-consumer1.py)
[parallel streamin consumer 1](part3/parallel-stream-processing-consumer2.py)




### Exercises
[Exercises](exercises/exercises.md)

