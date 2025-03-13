# Module 3: Web Applications And Web Services

## Part 1: Fundamentals Of Web Applications And Web Services

There are several services on the Internet, and the **Web (World Wide Web)** is one of the most widely used. The web consists of websites, web pages, and online resources that people can access using a web browser.

### **What is a URL?**
A **URL (Uniform Resource Locator)** is the address of a webpage or resource on the web. It tells your browser **where to find** and **how to access** a specific resource.

### **Parts of a URL:**
A URL typically consists of:
- **Protocol:** Defines how to access the resource (e.g., `https://`, `http://`).
- **Domain Name:** The website's name (e.g., `example.com`).
- **Path (Optional):** Specifies a specific page or file (e.g., `/about`).

#### **Example URL:**
`https://www.example.com/about`
- `https://` → Secure protocol
- `www.example.com` → Website domain
- `/about` → Specific page

A URL acts like an address for finding and retrieving web resources, allowing users to navigate the internet efficiently.  

### Client Server Architecture
![Client Server Architecture](../resources/figures/client-server.png)

### Three-tier Web Architecture


The **Three-Tier Web Architecture** is a software architecture pattern that separates an application into three logical layers:

1. **Presentation Tier (Client Layer)** – The front-end where users interact with the application (e.g., web browser, mobile app).
2. **Application Tier (Business Logic Layer)** – The back-end server that processes requests and enforces business rules.
3. **Data Tier (Database Layer)** – The database that stores and retrieves data.


```plaintext
+---------------------------+
|   Presentation Tier       |
|  [ HTML / CSS / JS ]      |
+---------------------------+
            │
            ▼
+---------------------------+
|   Application Tier        |
|  [ Node.js / Python ]     |
+---------------------------+
            │
            ▼
+---------------------------+
|   Data Tier               |
|  [ MySQL/PostgreSQL]      |
+---------------------------+

Diagram Representation of Three-Tier Web Architecture

```

### Web Application Architecture - Synchronous Communication
![Web Application Architecture](../resources/figures/web-application-architecture-synchronous.png)


### Web Application Architecture - Asynchronous Communication
![Web Application Architecture](../resources/figures/web-application-architecture-asynchronous.png)


### Scalable Web Application Architecture 
![Web Application Architecture](../resources/figures/scalable-web-architecture.png)


### Service-Oriented Architecture (SOA)

**Service-Oriented Architecture (SOA)** is a design pattern where software components (services) provide functionality to other components over a network. Each service is a discrete unit of functionality, which can be independently developed, deployed, and maintained. Services communicate with each other using well-defined interfaces and protocols, typically over HTTP or messaging queues.

#### Key Characteristics of SOA:
- **Loose Coupling**: Services are designed to be independent, minimizing dependencies.
- **Interoperability**: Services can work across different platforms and technologies.
- **Reusability**: Services can be reused in different applications.
- **Scalability**: Services can be scaled independently based on demand.

#### Simple Two-Service Communication Diagram

```plaintext
+----------------+       HTTP/Message Queue       +----------------+
|  Service A     | <----------------------------> |  Service B     |
| (Client)       |                                | (Provider)     |
+----------------+                                +----------------+
```
In this diagram:

* Service A acts as a client that sends a request to Service B.
* Service B processes the request and sends back a response to Service A.
* Communication between the services can be done using HTTP (e.g.RESTful) or a messaging queue (e.g. Apache Kafka).

### Microservice Architecture

**Microservice Architecture** is a design approach where an application is composed of small, independent services that communicate over a network. 
Each service is responsible for a specific business capability and can be developed, deployed, and scaled independently.

### Key Characteristics of Microservice Architecture:
- **Decentralization**: Each service has its own database and business logic.
- **Independence**: Services can be developed and deployed independently.
- **Scalability**: Services can be scaled individually based on demand.
- **Resilience**: Failure in one service does not necessarily affect the entire system.
- **Technology Diversity**: Different services can use different technologies and programming languages.

![Web Application Architecture](../resources/figures/micro-service-architecture.png)






## Part 2: Introduction to Node.js

### Node.js

Node.js is an open-source, cross-platform runtime environment that allows you to run JavaScript code on the server side. 
It uses the V8 JavaScript engine, which is also used by Google Chrome, to execute code outside of a web browser.

Key Features of Node.js:

    Asynchronous and Event-Driven: Node.js uses an event-driven, non-blocking I/O model, making it efficient and suitable for real-time applications.
    Single-Threaded: Despite being single-threaded, Node.js can handle many connections concurrently thanks to its event loop.
    NPM (Node Package Manager): Node.js comes with NPM, which is the largest ecosystem of open-source libraries in the world.
    Scalability: Node.js is designed to build scalable network applications.


Use Cases:

    Web Servers: Building fast and scalable web servers.
    APIs: Creating RESTful APIs for web and mobile applications.
    Real-Time Applications: Developing chat applications, online gaming, and collaborative tools.

**For the details of Node.js, refer to https://www.w3schools.com/nodejs/**

### NPM (Node Package Manager) 
it is a package manager for JavaScript, and it is the default package manager for Node.js. 
It allows developers to install, share, and manage dependencies (libraries and tools) for their projects.

* Key Features of NPM:
  - Package Management: Easily install and manage third-party libraries and tools. 
  - Version Control: Keep track of different versions of packages to ensure compatibility.
  - Dependency Management: Automatically handle dependencies required by installed packages.
  - Script Running: Define and run scripts for various tasks, such as building, testing, and deploying applications.
* Basic Commands:
  - npm init: Initialize a new Node.js project. 
  - npm install <package>: Install a package and add it to the project's dependencies. 
  - npm update: Update all installed packages to their latest versions. 
  - npm run: Run a script defined in the package.json file.

### Node.js & npm Installation

[Take a look at this web address](https://github.com/cllckn/software-testing/blob/main/module1/setting-up-the-development-environment.md) -> NodeJS

* Initialize a new Node.js project

[Take a look at this web address](https://github.com/cllckn/software-testing/blob/main/module1/setting-up-the-development-environment.md) -> NodeJS

### Traditional synchronous operation

* Each operation is executed in sequence, and the script waits for each operation to complete before moving on to the next one. 
* This can lead to blocking, where the script is unable to perform other tasks while waiting for an operation to complete.

```javascript
const fs = require('fs');

// Writing messages to the console
console.log('Start');

console.log('Message 1');

console.log('Message 2');
// Reading a file (Synchronous)
try {
    const data = fs.readFileSync('sample-data.md', 'utf8');
    console.log('File content:', data);
} catch (err) {
    console.error('Error reading file:', err);
}

console.log('End');

```

### Asynchronous and non-blocking operation

```javascript
const fs = require('fs');

// Writing messages to the console
console.log('Start');

// Wait 2 sec (asynchronous / non-blocking)
setTimeout(() => {
    console.log('Message 1');
}, 2000);

// Wait 10 ms (asynchronous / non-blocking)
setTimeout(() => {
    console.log('Message 2');
}, 10);

// Reading a file (asynchronous / non-blocking)
fs.readFile('sample-data.md', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log('File content:', data);
});

console.log('End');
```
**Explanation of Execution Order**

1. "Start" is printed to the console first (synchronous).
2. setTimeout is registered but executed 2 seconds later. When the time is up, the statements inside setTimeout are executed.
3. setTimeout is registered but executed 10 ms later. When the time is up, the statements inside setTimeout are executed.
4. fs.readFile is non-blocking, so the file-reading operation starts immediately, and the callback is executed after the operation is completed.
5. "end" is printed to the console (synchronous).
6. The event loop handles setTimeout, setTimeout, and fs.readFile callbacks after the main script execution is completed.

#### Node.js Event Loop Demonstration

```plaintext
+-----------------------------+
|        Start Script         |
+-----------------------------+
            │
            ▼
+-----------------------------+
|  console.log('Start')       |
+-----------------------------+
            │
            ▼
+-----------------------------+
|  setTimeout() registered    |
|  (Moves to Timer Queue)     |
+-----------------------------+
            │
            ▼
+-----------------------------+
|  setTimeout() registered    |
|  (Moves to Timer Queue)     |
+-----------------------------+
            │
            ▼
+-----------------------------+
|  fs.readFile() registered   |
|  (Moves to Thread Pool)     |
+-----------------------------+
            │
            ▼
+-----------------------------+
|  console.log('End')         |
+-----------------------------+
            │
            ▼
+-----------------------------+
|  Event Loop Checks Queues   |
+-----------------------------+
       │             │
       ▼             ▼
+----------------+  +----------------+
|  setTimeout()  |  |  fs.readFile()  |
| (Timer Queue)  |  | (I/O Queue)     |
+----------------+  +----------------+
       │             │
       ▼             ▼
+-----------------------------+
|  Callback Execution Begins  |
+-----------------------------+
```


### Basic JSON Operations
```javascript
const fs = require('fs'); // Import File System module

// Sample product JSON object
const product = {
    id: 1,
    name: "Laptop",
    category: "Electronics",
    price: 1000,
    stock: 50
};

// Convert JSON to string and write it to a file
fs.writeFileSync('product.json', JSON.stringify(product, null, 2));
console.log("JSON file has been stored successfully.");

// Read JSON data from the file
const rawData = fs.readFileSync('product.json', 'utf8');
const productData = JSON.parse(rawData); // Convert JSON string to JavaScript object
console.log("\nRead JSON from file:", productData);

// Basic JSON Operations

// 1. Access properties
console.log("Product Name:", productData.name);
console.log("Category:", productData["category"]);

// 2. Modify properties
productData.price = 1200;  // Update price
productData.stock += 10;  // Increase stock by 10

// 3. Add a new property
productData.discount = 10;

// 4. Delete a property
delete productData.stock;


// Write the updated JSON back to the file
fs.writeFileSync('product.json', JSON.stringify(productData, null, 2));
console.log("\nUpdated JSON file saved.");

```


### Process Employee.csv 
Download the **Employee.csv** dataset from the following address and update csvFilePath properly
   [Employee Dataset](https://www.kaggle.com/datasets/tawfikelmetwally/employee-dataset)
```javascript
// Import required built-in and external modules
const fs = require('fs'); // File System module to read/write files
const path = require('path'); // Path module to handle file paths
const csv = require('csv-parser'); // CSV parser to read CSV files. It converts csv record to JSON

// Define file paths for input CSV and output JSON
const csvFilePath = path.join(__dirname, '../../dataset/employee.csv'); // __dirname gives the current directory
const jsonFilePath = path.join(__dirname, 'employee.json'); // Output JSON file

let employees = []; // Array to store CSV data as JSON objects

// Read CSV file and convert to JSON using streams
fs.createReadStream(csvFilePath) // Form a readable stream to read the file
    .pipe(csv()) // Pipe the stream output to the csv-parser. converts csv record to JSON automatically
    .on('data', (row) => {
        employees.push(row); // Push each row (employee record) to the array
    })
    .on('end', () => {
        console.log('CSV file successfully read and converted to JSON.');

        // Write the JSON output to a file- pretty json
        fs.writeFileSync(jsonFilePath, JSON.stringify(employees, null, 2));

        // Perform JSON operations
        performJSONOperations(employees);
    });


// Function to perform basic JSON operations
function performJSONOperations(data) {
    console.log("\n--- Basic JSON Operations ---");

    //console.log(data)

    // Counting total employees
    console.log(`Total Employees: ${data.length}`);

    // Filtering employees who joined before 2015
    let earlyJoiners = data.filter(emp => parseInt(emp.JoiningYear) < 2013);
    console.log("Employees who joined before 2013:->", earlyJoiners.length);
    console.table(earlyJoiners);

    // Finding an employee by city
    let searchCity = "Pune";
    let employeesInCity = data.filter(emp => emp.City === searchCity);
    console.log(`Employees in ${searchCity}:`);
    console.table(employeesInCity);

    // Sorting employees by experience in current domain (Descending)
    let sortedByExperience = [...data].sort((a, b) => parseInt(b.ExperienceInCurrentDomain) - parseInt(a.ExperienceInCurrentDomain));
    console.log("Employees sorted by Experience in Current Domain:");
    console.table(sortedByExperience.slice(0, 5)); // Displaying top 5 employees

    // Extracting unique education levels - group by Education
    let educationLevels = [...new Set(data.map(emp => emp.Education))];
    console.log("Unique Education Levels:", educationLevels);

    // Counting employees who were ever benched
    let benchedEmployees = data.filter(emp => emp.EverBenched.toLowerCase() === 'yes');
    console.log(`Total Employees Ever Benched: ${benchedEmployees.length}`);

    // Counting employees who left
    let employeesLeft = data.filter(emp => emp.LeaveOrNot === '1');
    console.log(`Total Employees Who Left: ${employeesLeft.length}`);
}

```
---
## **Hands-on Exercise1**

---







## Part 3: Developing web applications using HTML,CSS, JS and Node.js

A simple web server
```javascript
/**
 * This is a straightforward web server built with Express.js.
 * Express.js is a lightweight and fast web framework for Node.js that simplifies building web applications and APIs.
 * It serves static HTML pages from the "views" folder.
 */

const express = require('express'); // Import the Express.js framework
const path = require('path'); // Import the built-in Node.js 'path' module

const app = express(); // Initialize an Express application
const PORT = 3000; // Define the port number where the server will listen

// Middleware
app.use(express.static(path.join(__dirname, 'views'))); // Middleware to serve static files (HTML, CSS, JS) from the 'views' folder

// Start the server
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
Hello World !
</body>
</html>
```
### HTML (HyperText Markup Language)

    HTML (HyperText Markup Language) is the standard language for crafting web pages. 
    It structures content using elements like headings, paragraphs, links, images, and forms. 
    Browsers interpret HTML to display web pages visually. 
    It works alongside CSS for styling and JavaScript for interactivity.

**For the details of HTML, refer to https://www.w3schools.com/html/**

### CSS (Cascading Style Sheets)

    CSS (Cascading Style Sheets) is a stylesheet language used to define the appearance of HTML elements. 
    CSS is used to control the layout, colors, fonts, spacing, and responsiveness of web pages to ensure a consistent and attractive design across different devices and screen sizes.

**For the details of CSS, refer to https://www.w3schools.com/css/**

## JavaScript

    JavaScript is a programming language used to make web pages interactive and dynamic. 
    It allows developers to manipulate HTML and CSS, handle events like clicks or keyboard input, and fetch data from servers without reloading the page. 

**For the details of JavaScript, refer to https://www.w3schools.com/js/**


---
## **Hands-on Exercise2**

---






## Part 4: jQuery and Basic Form Operations for User Interaction

### **What is jQuery?**
jQuery is a fast, small, and feature-rich JavaScript library designed to simplify:
- HTML DOM traversal and manipulation
- Event handling
- Animations
- AJAX interactions

### **Why Use jQuery?**
- **Simplifies JavaScript code** – Reduces the need for writing long vanilla JavaScript functions.
- **Cross-browser compatibility** – Works across different browsers without issues.
- **Powerful event handling** – Allows easy manipulation of events like clicks, keypresses, and form submissions.
- **AJAX support** – Enables smooth data loading without refreshing the page.

### **Adding jQuery to a Web Page**
You can include jQuery in your project via a **CDN**:

`<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>`

or download and reference it locally:

`<script src="js/jquery.min.js"></script>`



### **2. Basic jQuery Syntax**

jQuery follows a simple syntax:

`$(selector).action();`

- **`$`** – The jQuery function.
- **`selector`** – Selects an HTML element (e.g., `#id`, `.class`, `tag`).
- **`action()`** – The operation to perform (e.g., `hide()`, `show()`, `click()`).

**For the following jQuery code snippets, you are required to use a Node.js-based web application. 
You must embed these code snippets into a HTML file.**

### **Example: Hiding a Paragraph on Click**
1. Add a button and a paragraph in your HTML.
2. Use jQuery to hide the paragraph when the button is clicked.

```javascript
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<button id="hide-btn">Hide</button>
<p id="text">This is a paragraph.</p>

<script>
    $(document).ready(function(){
        $("#hide-btn").click(function(){
            $("#text").hide();
        })
    });
</script>

```


### **3.1 Handling Form Input Fields**

#### **Selecting Form Elements**
You can get and set values in form fields using `.val()`:

1. Form an input field and a button.
2. When the button is clicked, retrieve the value entered in the input field.
3. Display the value dynamically.

```javascript
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<input type="text" id="name" placeholder="Enter your name">
<button id="get-name">Get Name</button>
<p id="output"></p>

<script>
    $(document).ready(function(){
        $("#get-name").click(function(){
            var name = $("#name").val();
            $("#output").text("Hello, " + name);
        })
    });
</script>

```

### **3.2 Form Events Handling**

jQuery provides event handlers for form elements, such as:

- `focus()` – When an input field is focused.
- `blur()` – When an input field loses focus.
- `change()` – When the value of an input field changes.
- `submit()` – When a form is submitted.

#### **Example: Form Submission Handling**
```javascript
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<form id="user-form">
    <input type="text" id="username" placeholder="Enter username" required>
    <input type="password" id="password" placeholder="Enter password" required>
    <button type="submit">Submit</button>
</form>
<p id="message"></p>

<script>
    $(document).ready(function(){
        $("#user-form").submit(function(event){
            event.preventDefault(); // Prevents page reload
            var username = $("#username").val();
            $("#message").text("Form submitted! Welcome, " + username);
        });
    });
</script>

```


### **3.3 Enabling and Disabling Form Fields**
Use `.prop()` to enable or disable input fields dynamically.

```javascript
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<input type="text" id="email" disabled>
<button id="enable-btn">Enable Input</button>

<script>
    $(document).ready(function(){
        $("#enable-btn").click(function(){
            $("#email").prop("disabled", false);
        });
    });
</script>
```

### **3.4 Real-time Input Validation**

Validate user input dynamically using the `.keyup()` event.

```javascript
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<input type="text" id="phone" placeholder="Enter phone number">
<p id="validation-msg"></p>

<script>
    $(document).ready(function(){
        $("#phone").keyup(function(){
            var input = $(this).val();
            if (/^\d{10}$/.test(input)) {
                $("#validation-msg").text("Valid number").css("color", "green");
            } else {
                $("#validation-msg").text("Invalid number").css("color", "red");
            }
        });
    });
</script>
```


**For the details of JQuery, refer to https://api.jquery.com/** or **https://www.w3schools.com/jquery** 


---
## **Hands-on Exercise3**

---







## Part 5: Developing RESTful APIs for DSS

### **1. What is a RESTful API?**


A RESTful API (Representational State Transfer API) is a way to allow different software applications 
to communicate with each other over the internet using standard HTTP methods. 
Here are some key points about RESTful APIs:

#### Key Characteristics

1. **HTTP Methods**: RESTful APIs use standard HTTP methods to perform operations on resources:
   | **HTTP Method** | **Usage** |
   |---------------|---------|
   | `GET`        | Retrieve resource (Read) |
   | `POST`       | Add new resource (Insert) |
   | `PUT`        | Update existing resource (Replace) |
   | `PATCH`      | Update a specific part of resource (Modify) |
   | `DELETE`     | Remove resource |

2. **Resource-Based**: RESTful APIs use resources, which are identified by URLs. 
A resource could be a user, a product, or a function to control a heating system.

3. **JSON or XML**: Data is typically exchanged in JSON or XML format, with JSON being more common due to its simplicity and ease of use.

4. **Stateless**: The server does not store any client context between requests.

### Example Endpoints

- **GET /users**: Retrieve a list of users.
- **POST /users**: Add a new user.
- **GET /users/{id}**: Retrieve a specific user by ID.
- **PUT /users/{id}**: Update a specific user by ID.
- **DELETE /users/{id}**: Delete a specific user by ID.
- **GET /heating-system/status**: Retrieve the current status of the heating system.
- **POST /heating-system/on**: Turn on the heating system.
- **POST /heating-system/off**: Turn off the heating system.
- **PUT /heating-system/temperature**: Set the desired temperature of the heating system.

### A simple REST API 

Save the file as simple-rest-api.js
```javascript
const express = require("express");
const app = express();

app.use(express.json()); // Parse JSON requests

// In-memory database: JSON array for products
let products = [
  { id: 1, name: "Laptop", price: 999.99 },
  { id: 2, name: "Phone", price: 499.99 },
];

// Route definations
//Routes are the connection points (addresses) in a web service where clients send requests to interact with the server.
// GET all products
app.get("/api/products", (req, res) => {
  res.json(products); // Respond with the list of all products
});

// GET a single product by ID
app.get("/api/products/:id", (req, res) => {
  const product = products.find((p) => p.id === parseInt(req.params.id)); // Find the product by ID
  if (!product) return res.status(404).json({ error: "Product not found" }); // If not found, respond with 404
  res.json(product); // Respond with the found product
});

// POST - Add a new product
app.post("/api/products", (req, res) => {
  const { name, price } = req.body; // Extract name and price from the request body
  if (!name || !price) return res.status(400).json({ error: "Invalid input" }); // Validate input

  const newProduct = { id: products.length + 1, name, price }; // Add a new product with a unique ID
  products.push(newProduct); // Add the new product to the list
  res.status(201).json(newProduct); // Respond with the added product
});

// PUT - Update a product
app.put("/api/products/:id", (req, res) => {
  const product = products.find((p) => p.id === parseInt(req.params.id)); // Find the product by ID
  if (!product) return res.status(404).json({ error: "Product not found" }); // If not found, respond with 404

  const { name, price } = req.body; // Extract name and price from the request body
  product.name = name || product.name; // Update the product name if provided
  product.price = price || product.price; // Update the product price if provided
  res.json(product); // Respond with the updated product
});

// DELETE - Remove a product
app.delete("/api/products/:id", (req, res) => {
  products = products.filter((p) => p.id !== parseInt(req.params.id)); // Remove the product by ID
  res.json({ message: "Product deleted" }); // Respond with a deletion message
});

// Start server
const PORT = 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`)); // Start the server on port 3000
```

### Endpoints (Routes) of the developed API

        GET http://localhost:3000/api/products

        GET http://localhost:3000/api/products/1

        POST http://localhost:3000/api/products
        Content-Type: application/json
        {
        "name": "Tablet",
        "price": 299.99
        }

        PUT http://localhost:3000/api/products/2
        Content-Type: application/json
        {
        "name": "Smartphone",
        "price": 550.00
        }
    
        DELETE http://localhost:3000/api/products/1


### REST Clients - Testing REST api using cURL and http client

    curl --version
    if not installed -> Download cURL from: https://curl.se/windows/


```sh
# Retrieves a list of all products from the database.

curl -X GET http://localhost:3000/api/products

---

# Fetches details of a specific product using its ID.

curl -X GET http://localhost:3000/api/products/1

---

# Adds a new product to the database. The request body must contain name and price in JSON format.

curl -X POST http://localhost:3000/api/products \
     -H "Content-Type: application/json" \
     -d '{"name": "Tablet", "price": 299.99}'


---

# Updates the details of an existing product using its ID. Any missing fields will retain their previous values.

curl -X PUT http://localhost:3000/api/products/1 \
     -H "Content-Type: application/json" \
     -d '{"name": "Updated Laptop", "price": 1099.99}'

---

# Deletes a product from the database by specifying its ID.

curl -X DELETE http://localhost:3000/api/products/1


```

---
## **Hands-on Exercise4**
---



## **Converting a Simple REST API into a Web Application with jQuery**


This section explains how to convert the existing **REST API** into a **web application** by developing web pages that allow users to interact with the API using **jQuery**.

The web application will provide:
- A **product list** fetched from the API.
- A **form to add new products**.
- Options to **update and delete products** dynamically.
- jQuery-based **AJAX requests** to communicate with the API.


### **Steps to Convert the API into a Web Application**
1. **Retain the existing REST API** as the backend.
2. **Develop frontend web pages** to interact with the API.
3. **Use jQuery** to fetch, display, add, update, and delete products.
4. **Implement event handling** using jQuery to interact with the API.
5. **Enhance user experience** with jQuery effects.


### Step 1: Modify the API (`simple-rest-api.js`)
We will slightly modify the existing API to serve **static HTML files** in addition to handling RESTful requests.

* /part5/rest-api-web-app-crd/server.js

```javascript

const express = require("express");
const path = require("path");
const app = express();
const cors = require("cors"); // Import CORS


app.use(express.json()); // parse json requests
app.use(express.static(path.join(__dirname, 'public'))); // Middleware to serve static files (HTML, CSS, JS) from the 'public' folder


app.use(cors()); // Enable CORS for all routes
// The browser blocks cross-origin requests unless the server explicitly allows them.
// Cross-Origin means that the protocol, domain, or port is different between the frontend and backend.

// In-memory database: JSON array for products
let products = [
    { id: 1, name: "Laptop", price: 999.99 },
    { id: 2, name: "Phone", price: 499.99 },
];

// Route definations
//Routes are the connection points (addresses) in a web service where clients send requests to interact with the server.
// GET all products
app.get("/api/products", (req, res) => {
    res.json(products);
});

// GET a single product by ID
app.get("/api/products/:id", (req, res) => {
    const product = products.find((p) => p.id === parseInt(req.params.id));
    if (!product) return res.status(404).json({ error: "Product not found" });
    res.json(product);
});

// POST - Add a new product
app.post("/api/products", (req, res) => {
    const { name, price } = req.body;
    if (!name || !price) return res.status(400).json({ error: "Invalid input" });

    const newProduct = { id: products.length + 1, name, price };
    products.push(newProduct);
    res.status(201).json(newProduct);
});

// PUT - Update a product
app.put("/api/products/:id", (req, res) => {
    const product = products.find((p) => p.id === parseInt(req.params.id));
    if (!product) return res.status(404).json({ error: "Product not found" });

    const { name, price } = req.body;
    product.name = name || product.name;
    product.price = price || product.price;
    res.json(product);
});

// DELETE - Remove a product
app.delete("/api/products/:id", (req, res) => {
    products = products.filter((p) => p.id !== parseInt(req.params.id));
    res.json({ message: "Product deleted" });
});

// Start server
const PORT = 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```


### Step 2: Develop Frontend Web Pages
Inside a folder named public/, add an index.html file. This will be the main page where users 
can view, add, update, and delete products using jQuery.

* /part5/rest-api-web-app-crd/public/index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Management</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; }
        table { width: 50%; margin: auto; border-collapse: collapse; }
        th, td { border: 1px solid black; padding: 10px; }
        .error { color: red; display: none; }
    </style>
</head>
<body>
    <h2>Product List</h2>
    <!-- Table to display products -->
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Price</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody id="product-list"></tbody> <!-- Products will be dynamically inserted here -->
    </table>

    <h2>Add Product</h2>
    <!-- Form to add a new product -->
    <form id="add-product-form">
        <input type="text" id="name" placeholder="Product Name" required>
        <input type="number" id="price" placeholder="Price" required>
        <button type="submit">Add Product</button>
    </form>
    <p class="error" id="error-msg">Invalid inputtttttttt</p> <!-- Error message for validation -->

    <script>
        $(document).ready(function(){
            // Function to load products asynchronously using AJAX (GET request)
            function loadProducts() {
                $.get("/api/products", function(products){
                    $("#product-list").empty(); // Clear the existing list
                    products.forEach(product => {
                        $("#product-list").append(`
                            <tr>
                                <td>${product.id}</td>
                                <td>${product.name}</td>
                                <td>${product.price}</td>
                                <td>
                                    <button class="delete-btn" data-id="${product.id}">Delete</button>
                                </td>
                            </tr>
                        `);
                    });
                });
            }

            // Handle form submission to add a new product (AJAX POST request)
            $("#add-product-form").submit(function(event){
                event.preventDefault(); // Prevent default form submission
                var name = $("#name").val().trim(); // Get product name
                var price = parseFloat($("#price").val().trim()); // Get product price

                // Validate input: Ensure name is not empty and price is valid
                if (!name || isNaN(price) || price <= 0) {
                    $("#error-msg").fadeIn().delay(5000).fadeOut();
                    return;
                }

                // Asynchronous request to add a product
                $.post({
                    url: "/api/products",
                    contentType: "application/json", // Ensure JSON is sent correctly
                    data: JSON.stringify({ name, price }),
                    success: function(response) {
                        loadProducts(); // Refresh product list after adding
                        console.log("Product added:", response);
                        $("#name").val(""); // Clear input fields
                        $("#price").val("");
                    },
                    error: function(xhr) {
                        console.error("Error:", xhr.responseText);
                    }
                });
            });

            // Handle product deletion (AJAX DELETE request)
            $("#product-list").on("click", ".delete-btn", function() {
                var id = $(this).data("id");
                // Perform the deletion logic here
                $.ajax({
                    url: `/api/products/${id}`,
                    type: "DELETE",
                    success: function() {
                        loadProducts();
                    }
                });
            });

            loadProducts(); // Initial load of products (asynchronous)
        });
    </script>
</body>
</html>

```

---
## **Hands-on Exercise5**
---


**********************************************************************************************************

### Step 3: Add search and update functionalities to the web app

* /part5/rest-api-web-app-crd/server.js

```javascript
// GET all products
app.get("/api/products", (req, res) => {
    // Accesses the name parameter from the query string in an Express.js request object.
    const query = req.query.name?.toLowerCase() || ""; 

    if (query) {
        const filteredProducts = products.filter(product =>
            product.name.toLowerCase().includes(query)
        );
        return res.json(filteredProducts);
    }

    res.json(products);
});

```


* /part5/rest-api-web-app-crd/public/index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Management</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; }
        table { width: 50%; margin: auto; border-collapse: collapse; }
        th, td { border: 1px solid black; padding: 10px; }
        .error { color: red; display: none; }
    </style>
</head>
<body>
<h2>Product List</h2>

<!-- Live Search Input -->
<input type="text" id="search" placeholder="Search by name">
<p class="error" id="search-error">No products found</p>

<!-- Table to display products -->
<table>
    <thead>
    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Price</th>
        <th>Actions</th>
    </tr>
    </thead>
    <tbody id="product-list"></tbody>
</table>

<h2>Add Product</h2>
<form id="add-product-form">
    <input type="text" id="name" placeholder="Product Name" required>
    <input type="number" id="price" placeholder="Price" required>
    <button type="submit">Add Product</button>
</form>
<p class="error" id="error-msg">Invalid input</p>

<div id="updateform" hidden="true">
    <h2>Update Product</h2>
    <form id="update-product-form">
        <input type="number" id="update-id" placeholder="Product ID" readonly required>
        <input type="text" id="update-name" placeholder="New Name">
        <input type="number" id="update-price" placeholder="New Price">
        <button type="submit">Update Product</button>
    </form>
    <p class="error" id="update-error-msg">Invalid input</p>
</div>
<script>
    $(document).ready(function(){
        let debounceTimer;

        function loadProducts(query = "") {
            let url = query ? `/api/products?name=${encodeURIComponent(query)}` : "/api/products";
            $.get(url, function(products){
                $("#product-list").empty();
                if (products.length === 0) {
                    $("#search-error").show();
                } else {
                    $("#search-error").hide();
                    products.forEach(product => {
                        $("#product-list").append(`
                                <tr>
                                    <td>${product.id}</td>
                                    <td>${product.name}</td>
                                    <td>${product.price}</td>
                                    <td>
                                        <button class="edit-btn" data-id="${product.id}">Edit</button>
                                        <button class="delete-btn" data-id="${product.id}">Delete</button>
                                    </td>
                                </tr>
                            `);
                    });
                }
            });
        }

        $("#add-product-form").submit(function(event){
            event.preventDefault();
            let name = $("#name").val().trim();
            let price = parseFloat($("#price").val().trim());

            if (!name || isNaN(price) || price <= 0) {
                $("#error-msg").fadeIn().delay(5000).fadeOut();
                return;
            }

            $.post({
                url: "/api/products",
                contentType: "application/json",
                data: JSON.stringify({ name, price }),
                success: function() {
                    loadProducts();
                    $("#name, #price").val("");
                }
            });
        });

        $("#product-list").on("click", ".delete-btn", function() {
            let id = $(this).data("id");
            $.ajax({
                url: `/api/products/${id}`,
                type: "DELETE",
                success: function() {
                    loadProducts();
                }
            });
        });

     
        //$("#search"):This is a jQuery selector that selects an HTML element with the id of search.
        // The .on() method is used to attach an event handler to the selected element(s).
        // "keyup" is the event type being listened for. The keyup event is triggered when a keyboard key is released after being pressed.
        // function() { ... } is the callback function that will be executed when the keyup event occurs.
        
        $("#search").on("keyup", function() { // attaches an event listener to the search input field (#search). The event triggers whenever the user releases a key (keyup event).
            clearTimeout(debounceTimer); // Clears any previously set timer (debounceTimer) to prevent multiple requests being sent in quick succession.
            let query = $(this).val().trim();
            debounceTimer = setTimeout(() => { //Sets a delay of 300 milliseconds before calling loadProducts(query).
                loadProducts(query);
            }, 300);
        });

        $("#update-product-form").submit(function(event){
            event.preventDefault();
            let id = parseInt($("#update-id").val().trim());
            let name = $("#update-name").val().trim();
            let price = parseFloat($("#update-price").val().trim());

            if (isNaN(id) || id <= 0 || (!name && isNaN(price))) {
                $("#update-error-msg").fadeIn().delay(5000).fadeOut();
                return;
            }

            $.ajax({
                url: `/api/products/${id}`,
                type: "PUT",
                contentType: "application/json",
                data: JSON.stringify({ name, price }),
                success: function() {
                    loadProducts();
                    $("#update-id, #update-name, #update-price").val("");
                }
            });
        });

        // Load product data into update form when "Edit" is clicked
        $("#product-list").on("click", ".edit-btn", function() {
            let id = $(this).data("id");
            $("#updateform").fadeIn(2000);
            $.get(`/api/products/${id}`, function(product) {
                $("#update-id").val(product.id);
                $("#update-name").val(product.name);
                $("#update-price").val(product.price);
            });
        });

        loadProducts();
    });
</script>
</body>
</html>

```




---
## **Hands-on Exercise6**

Add search and update functions for the developed app in Exercise 5.

---





## Styling Web Applications with Tailwind CSS

Tailwind CSS is a utility-first CSS framework that allows developers to style their HTML elements using pre-designed utility classes.

* [For the details](https://v3.tailwindcss.com/docs)

* To use in a html file:
```html
<head>
    <meta charset="UTF-8">

    <!-- This line enables responsive web design by allowing the layout to adapt 
    to different screen sizes without requiring manual zooming or horizontal scrolling. -->
   <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
   <title>Tailwind Example</title>
   <!-- Tailwind CSS via CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
</head>
```

* Try tailwind here:

https://play.tailwindcss.com/


```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tailwind Flex Layout</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100"> <!-- Sets the background color to a light gray (Tailwind's gray-100 shade) -->

    <!-- Navbar -->
    <nav class="bg-blue-600 text-white p-4 shadow-md"> <!-- 
        Sets the background color to blue (Tailwind's blue-600 shade), 
        text color to white, adds padding of 1rem (4 * 0.25rem), 
        and applies a medium-sized shadow
    -->
        <div class="max-w-7xl mx-auto flex justify-between items-center"> <!-- 
            Sets a maximum width of 80rem, centers the content horizontally, 
            enables flexbox layout, distributes space evenly between items, 
            and vertically aligns items to the center
        -->
            <h1 class="text-xl font-bold">My Dashboard</h1> <!-- Sets font size to extra large (1.25rem) and font weight to bold -->
            <ul class="hidden md:flex space-x-4"> <!-- 
                Hides the list by default, displays as flex on medium screens and larger, 
                and adds horizontal space of 1rem (4 * 0.25rem) between items
            -->
                <li><a href="#" class="hover:underline">Home</a></li> <!-- Applies underline on hover -->
                <li><a href="#" class="hover:underline">About</a></li> <!-- Applies underline on hover -->
                <li><a href="#" class="hover:underline">Contact</a></li> <!-- Applies underline on hover -->
            </ul>
            <button class="md:hidden text-white focus:outline-none" id="menu-btn">☰</button> <!-- 
                Hides the button on medium screens and larger, sets text color to white, 
                and removes default focus outline
            -->
        </div>
    </nav>

    <!-- Sidebar + Main Content Container -->
    <div class="flex h-screen"> <!-- Enables flexbox layout and sets height to 100% of screen height -->
        <!-- Sidebar -->
        <aside class="bg-gray-800 text-white w-64 space-y-6 py-6 px-4 hidden md:block"> <!-- 
            Sets background color to dark gray (Tailwind's gray-800 shade), 
            text color to white, width to 16rem, vertical space of 1.5rem (6 * 0.25rem), 
            vertical padding of 1.5rem, horizontal padding of 1rem, 
            hides by default, and displays as block on medium screens and larger
        -->
            <h2 class="text-xl font-semibold">Menu</h2> <!-- Sets font size to extra large (1.25rem) and font weight to semi-bold -->
            <nav>
                <a href="#" class="block py-2 px-4 hover:bg-gray-700 hover:bold">Dashboard</a> <!-- 
                    Sets display to block, vertical padding of 0.5rem, horizontal padding of 1rem, 
                    changes background color to a lighter gray on hover, and applies bold font on hover
                -->
                <a href="#" class="block py-2 px-4 hover:bg-gray-700">Products</a> <!-- 
                    Sets display to block, vertical padding of 0.5rem, horizontal padding of 1rem, 
                    changes background color to a lighter gray on hover
                -->
                <a href="#" class="block py-2 px-4 hover:bg-gray-700">Users</a> <!-- 
                    Sets display to block, vertical padding of 0.5rem, horizontal padding of 1rem, 
                    changes background color to a lighter gray on hover
                -->
                <a href="#" class="block py-2 px-4 hover:bg-gray-700">Settings</a> <!-- 
                    Sets display to block, vertical padding of 0.5rem, horizontal padding of 1rem, 
                    changes background color to a lighter gray on hover
                -->
            </nav>
        </aside>

        <!-- Main Content -->
        <main class="flex-1 p-6"> <!-- Allows main content to grow and take up remaining space, adds padding of 1.5rem -->
            <h2 class="text-2xl font-bold mb-4">Welcome to the Dashboard</h2> <!-- 
                Sets font size to 2xl (1.5rem), font weight to bold, and adds bottom margin of 1rem
            -->
            <p class="text-gray-700"> <!-- Sets text color to medium gray (Tailwind's gray-700 shade) -->
                This is a simple dashboard layout built with Tailwind CSS. 
                The sidebar is collapsible on smaller screens, and the layout is fully responsive.
            </p>

            <!-- Example Cards -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mt-6"> <!-- 
                Enables CSS Grid layout, constructs one column on small screens, 
                three columns on medium screens and larger, adds gap of 1rem, 
                and adds top margin of 1.5rem
            -->
                <div class="bg-white p-4 shadow rounded"> <!-- 
                    Sets background color to white, adds padding of 1rem, 
                    applies default-sized shadow, and adds rounded corners
                -->
                    <h3 class="font-semibold">Card 1</h3> <!-- Sets font weight to semi-bold -->
                    <p class="text-gray-600">Some content...</p> <!-- Sets text color to a slightly darker gray (Tailwind's gray-600 shade) -->
                </div>
                <div class="bg-white p-4 shadow rounded"> <!-- 
                    Sets background color to white, adds padding of 1rem, 
                    applies default-sized shadow, and adds rounded corners
                -->
                    <h3 class="font-semibold">Card 2</h3> <!-- Sets font weight to semi-bold -->
                    <p class="text-gray-600">Some content...</p> <!-- Sets text color to a slightly darker gray (Tailwind's gray-600 shade) -->
                </div>
                <div class="bg-white p-4 shadow rounded"> <!-- 
                    Sets background color to white, adds padding of 1rem, 
                    applies default-sized shadow, and adds rounded corners
                -->
                    <h3 class="font-semibold">Card 3</h3> <!-- Sets font weight to semi-bold -->
                    <p class="text-gray-600">Some content...</p> <!-- Sets text color to a slightly darker gray (Tailwind's gray-600 shade) -->
                </div>
            </div>
        </main>
    </div>

    <!-- Footer -->
    <footer class="bg-gray-900 text-white text-center py-4 mt-auto"> <!-- 
        Sets background color to very dark gray (Tailwind's gray-900 shade), 
        text color to white, centers text horizontally, adds vertical padding of 1rem, 
        and sets margin top to auto
    -->
        <p> 2025 My Dashboard. All rights reserved.</p>
    </footer>

    <!-- Script for Mobile Menu -->
    <script>
        document.getElementById('menu-btn').addEventListener('click', function() {
            document.querySelector('aside').classList.toggle('hidden'); // Toggles the 'hidden' class on the sidebar
        });
    </script>

</body>
</html>

```

* [/src/dss/module3/part5/structured-web-app](https://github.com/cllckn/decision-support-systems/tree/main/module3/part5)


---
## **Hands-on Exercise 7**
    Style the web app developed in Exercise 6 using Tailwind or another framework.
---



### Routers and Routes in Express.js

A **route** in Express.js defines an endpoint that a client can access via **HTTP methods** 
(GET, POST, PUT, DELETE, etc.). Each route consists of:

1. **A URL pattern** (e.g., `/api/customers/:id`)
2. **An HTTP method** (GET, POST, etc.)
3. **A callback function** to handle the request

Example of a simple route in Express.js:
```javascript
app.get("/api/customers", (req, res) => {
    res.json({ message: "List of customers" });
});
```
An **Express Router** helps organize routes by grouping them into separate files. This makes the code modular, manageable, and scalable.

Benefits of Using a Router
* Code organization – Keeps server.js clean and structured.
* Reusability – Routes can be modular and reusable across different parts of the application.
* Easier maintenance – Adding new routes does not clutter the main server file.

* /src/dss/module3/part5/routers/server.js
```javascript
const express = require("express");
const productRoutes = require("./routes/products"); // Import product routes

const app = express();

app.use(express.json()); // Parse JSON requests


// Use product routes
app.use("/api/products", productRoutes);

// Start server
const PORT = 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));

```

/routes/product.js
```javascript
const express = require("express");
const router = express.Router();

// In-memory database: Array to store product data
let products = [
    { id: 1, name: "Laptop", price: 999.99 },
    { id: 2, name: "Phone", price: 499.99 },
];

// GET all products
router.get("/", (req, res) => {
    res.json(products);
});

// GET a single product by ID
router.get("/:id", (req, res) => {
    const product = products.find((p) => p.id === parseInt(req.params.id));
    if (!product) return res.status(404).json({ error: "Product not found" });
    res.json(product);
});

// POST - Add a new product
router.post("/", (req, res) => {
    const { name, price } = req.body;
    if (!name || !price) return res.status(400).json({ error: "Invalid input" });

    const newProduct = { id: products.length + 1, name, price };
    products.push(newProduct);
    res.status(201).json(newProduct);
});

// PUT - Update a product
router.put("/:id", (req, res) => {
    const product = products.find((p) => p.id === parseInt(req.params.id));
    if (!product) return res.status(404).json({ error: "Product not found" });

    const { name, price } = req.body;
    product.name = name || product.name;
    product.price = price || product.price;
    res.json(product);
});

// DELETE - Remove a product
router.delete("/:id", (req, res) => {
    products = products.filter((p) => p.id !== parseInt(req.params.id));
    res.json({ message: "Product deleted" });
});

module.exports = router;
```


## Part 6: Providing database support for the modules

To perform database operations using application programs, **database drivers** are essential. 
Drivers facilitate communication between the programming language and the database.

### **Database Drivers Provide the Following Core Functions:**
- **Establishing a connection** to the database.
- **Executing queries** (such as SELECT, INSERT, UPDATE, DELETE).
- **Closing the connection** after operations are completed.


### **Database Operations with Node.js and PostgreSQL**

* Setting up PostgreSQL
```sql
CREATE DATABASE dss;
---------------------------
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    price NUMERIC(10, 2) NOT NULL
);

```

* A simple REST API with CRUD operations
```javascript
//npm install express pg
// Import necessary modules

const express = require("express");
const { Pool } = require("pg"); // PostgreSQL client

const app = express();

// Initialize a new PostgreSQL connection pool

const pool = new Pool({
    user: 'postgres',
    host: 'localhost',
    database: 'dss',
    password: 'LecturePassword',
    port: 5432,
});

/*const pool = new Pool({
    connectionString: "postgresql://postgres:LecturePassword@localhost:5432/dss",
});*/


// Middleware to parse JSON request bodies
app.use(express.json());

// ------------------------ GET all products ------------------------
app.get("/api/products", async (req, res) => {
    try {
        // Fetch all products from the database
        const result = await pool.query("SELECT * FROM products ORDER BY id ASC");

        // Respond with JSON data
        res.json(result.rows);
    } catch (err) {
        res.status(500).json({ error: "Database error" }); // Handle errors
    }
});

// ------------------------ GET a single product by ID ------------------------
app.get("/api/products/:id", async (req, res) => {
    try {
        const { id } = req.params; // Extract product ID from URL

        // Query database for the given product ID
        const result = await pool.query("SELECT * FROM products WHERE id = $1", [id]);

        if (result.rows.length === 0)
            return res.status(404).json({ error: "Product not found" });

        // Respond with the found product
        res.json(result.rows[0]);
    } catch (err) {
        res.status(500).json({ error: "Database error" });
    }
});

// ------------------------ POST - Add a new product ------------------------
app.post("/api/products", async (req, res) => {
    try {
        const { name, price } = req.body; // Extract product details from request body

        // Validate input (ensure name and price are provided)
        if (!name || !price)
            return res.status(400).json({ error: "Invalid input" });

        // Insert new product into the database
        const result = await pool.query(         //executes the query asynchronously using the PostgreSQL connection pool.
            "INSERT INTO products (name, price) VALUES ($1, $2) RETURNING *", //$1, $2 are placeholders for parameterized queries, preventing SQL injection. // RETURNING * makes PostgreSQL return the newly inserted row.
            [name, price] //name, price] is an array of values that replaces $1 and $2 in the query.
        );

        // Respond with the newly added product
        res.status(201).json(result.rows[0]);
    } catch (err) {
        res.status(500).json({ error: "Database error" });
    }
});

// ------------------------ PUT - Update a product ------------------------
app.put("/api/products/:id", async (req, res) => {
    try {
        const { id } = req.params;
        const { name, price } = req.body;

        // Update the product in the database if it exists
        const result = await pool.query(
            "UPDATE products SET name = COALESCE($1, name), price = COALESCE($2, price) WHERE id = $3 RETURNING *",
            [name, price, id]   //COALESCE($1, name) ensures that if $1 (the provided value for name) is NULL or not given, the existing name value in the database remains unchanged.
        );

        if (result.rows.length === 0)
            return res.status(404).json({ error: "Product not found" });

        // Respond with the updated product
        res.json(result.rows[0]);
    } catch (err) {
        res.status(500).json({ error: "Database error" });
    }
});

// ------------------------ DELETE - Remove a product ------------------------
app.delete("/api/products/:id", async (req, res) => {
    try {
        const { id } = req.params;

        // Delete the product from the database
        const result = await pool.query("DELETE FROM products WHERE id = $1 RETURNING *", [id]);

        if (result.rows.length === 0)
            return res.status(404).json({ error: "Product not found" });

        // Respond with a success message
        res.json({ message: "Product deleted" });
    } catch (err) {
        res.status(500).json({ error: "Database error" });
    }
});

// ------------------------ Start server ------------------------
const PORT = 3000;
app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));

```

---
## **Hands-on Exercise 8**

---



## Part 7: Integrating Web Applications with Apache Kafka

* /part7/simple-producer.js

```javascript
const { Kafka } = require('kafkajs');

// Initialize Kafka client
const kafka = new Kafka({
clientId: 'my-producer',
brokers: ['localhost:9092'] // Replace with your Kafka broker address
});

// Create a Kafka producer instance
const producer = kafka.producer();

const sendMessage = async () => {
await producer.connect(); // Connect to Kafka broker
console.log("Producer connected.");

    setInterval(async () => {
        const timestamp = new Date().toISOString(); // Get the current timestamp
        const messageValue = `Message sent at ${timestamp}`;

        await producer.send({
            topic: 'dss-test-topic1',
            messages: [
                { key: 'timestamp', value: messageValue }
            ]
        });

        console.log(`Sent: ${messageValue}`);
    }, 1000); // Send a message every second
};

// Run the producer
sendMessage().catch(console.error);

```

* /part7/simple-consumer.js

```javascript
const { Kafka } = require('kafkajs');

// Initialize Kafka client
const kafka = new Kafka({
    clientId: 'my-consumer',
    brokers: ['localhost:9092'] // Replace with your Kafka broker address
});

// Create a Kafka consumer instance
const consumer = kafka.consumer({ groupId: 'test-group' });

const runConsumer = async () => {
    await consumer.connect(); // Connect to Kafka broker
    console.log("Consumer connected.");

    await consumer.subscribe({ topic: 'dss-test-topic1', fromBeginning: false });
    //If true, the consumer will start reading from the beginning of the topic (including old messages).
    //If false (default), the consumer will only receive new messages (ignoring previous ones).

    await consumer.run({
        eachMessage: async ({ topic, partition, message }) => {
            console.log(`Received message: ${message.value.toString()} `);
        }
    });
};

// Run the consumer
runConsumer().catch(console.error);

```

* /part7/simple-consumer.py
```shell
from confluent_kafka import Consumer, KafkaError

# Kafka broker configuration
conf = {
    'bootstrap.servers': 'localhost:9092',  # Kafka broker address
    'group.id': 'my-group',                 # Consumer group ID
    'auto.offset.reset': 'latest'         # Start reading from the beginning of the topic
}

# Initialize a Kafka consumer
consumer = Consumer(conf)

# Subscribe to the 'dss-test-topic1' topic
consumer.subscribe(['dss-test-topic1'])

# Poll for messages
try:
    while True:
        msg = consumer.poll(timeout=1.0)  # Wait for messages
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition event
                print(f"Reached end of partition {msg.partition()}")
            else:
                print(f"Error: {msg.error()}")
        else:
            # Print the message key and value
            print(f"Consumed: key={msg.key()}, value={msg.value().decode('utf-8')}")
except KeyboardInterrupt:  # catch "Ctrl + C" interrupt
    print("Consumer interrupted")
finally:
    # Close the consumer
    consumer.close()
```


* Implement the Node.js Python integration given above



### Case Study: Real-time Price Validation and Adjustment Algorithm Using Apache Kafka, Node.js (kafkajs), and Python (confluent-kafka)

A detailed explanation and implementation of a real-time price validation and adjustment algorithm utilizing Apache Kafka, Node.js (kafkajs), 
and Python (confluent-kafka).

* Figure: Overview of the system

![](../resources/figures/web-app-kafka-integration.png)



#### Algorithm Overview
The algorithm follows an event-driven architecture where product data is processed asynchronously using Kafka.


Steps:
* New Product Submission (Node.js API)
  - When a new product is added (POST /api/products), it is sent to Kafka (dss-products topic).
* Kafka Consumer (Python)
  - A Python service listens to the dss-products topic.
  - It applies business logic:
    - Validates the product.
    - Adjusts the price (e.g., adds tax, applies discounts).
  - The updated product is published to the dss-validated-products topic.
* Kafka Consumer (Node.js)
  - A Node.js Kafka consumer listens to dss-validated-products.
  - The updated product data is stored in an in-memory array.


* /module3/part7/server-with-kafka-support.js

```javascript
const express = require("express");
const bodyParser = require("body-parser");
const { Kafka } = require("kafkajs");
const path = require("path");

const app = express();
app.use(bodyParser.json());

const kafka = new Kafka({
    clientId: "product-service",
    brokers: ["localhost:9092"]
});

const producer = kafka.producer();
const consumer = kafka.consumer({ groupId: "product-group" });

let products = [];

app.use(express.static(path.join(__dirname, 'public'))); // Middleware to serve static files (HTML, CSS, JS) from the 'public' folder

// Kafka Producer - Send Product Data
app.post("/api/products", async (req, res) => {
    const { name, price } = req.body;
    if (!name || !price) {
        return res.status(400).json({ error: "Invalid input" });
    }

    const newProduct = { id: products.length + 1, name, price };
    //products.push(newProduct);

    await producer.connect();
    await producer.send({
        topic: "dss-products",
        messages: [{ key: String(newProduct.id), value: JSON.stringify(newProduct) }]
    });
    await producer.disconnect();

    res.status(201).json(newProduct);
});

// Kafka Consumer - Receive and Save Validated Products
const consumeValidatedProducts = async () => {
    await consumer.connect();
    await consumer.subscribe({ topic: "dss-validated-products", fromBeginning: true });

    await consumer.run({
        eachMessage: async ({ message }) => {
            const validatedProduct = JSON.parse(message.value.toString());

            /* const index = products.findIndex(p => p.id === validatedProduct.id);
             if (index !== -1) {
                 products[index] = validatedProduct;
             } else {*/
            products.push(validatedProduct);
            //}
        }
    });
};

consumeValidatedProducts();

// Retrieve all products
app.get("/api/products", (req, res) => {
    res.json(products);
});

app.listen(3000, () => console.log("Server running on port 3000"));

```
* /module3/part7/public/index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Management</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; }
        table { width: 50%; margin: auto; border-collapse: collapse; }
        th, td { border: 1px solid black; padding: 10px; }
        .error { color: red; display: none; }
    </style>
</head>
<body>
<h2>Product List</h2>

<!-- Live Search Input -->
<input type="text" id="search" placeholder="Search by name">
<p class="error" id="search-error">No products found</p>
<!-- Table to display products -->
<table>
    <thead>
    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Price</th>
        <th>Actions</th>
    </tr>
    </thead>
    <tbody id="product-list"></tbody> <!-- Products will be dynamically inserted here -->
</table>

<h2>Add Product</h2>
<!-- Form to add a new product -->
<form id="add-product-form">
    <input type="text" id="name" placeholder="Product Name" required>
    <input type="number" id="price" placeholder="Price" required>
    <button type="submit">Add Product</button>
</form>
<p class="error" id="error-msg">Invalid input</p> <!-- Error message for validation -->


<div id="updateform" hidden="true">
    <h2>Update Product</h2>
    <form id="update-product-form">
        <input type="number" id="update-id" placeholder="Product ID" readonly required>
        <input type="text" id="update-name" placeholder="New Name">
        <input type="number" id="update-price" placeholder="New Price">
        <button type="submit">Update Product</button>
    </form>
    <p class="error" id="update-error-msg">Invalid input</p>
</div>

<script>
    $(document).ready(function(){
        // Function to load products asynchronously using AJAX (GET request)
        let debounceTimer;

        function loadProducts(query = "") {
            let url = query ? `/api/products?name=${encodeURIComponent(query)}` : "/api/products";
            $.get(url, function(products){
                $("#product-list").empty();
                if (products.length === 0) {
                    $("#search-error").show();
                } else {
                    $("#search-error").hide();
                    products.forEach(product => {
                        $("#product-list").append(`
                                <tr>
                                    <td>${product.id}</td>
                                    <td>${product.name}</td>
                                    <td>${product.price}</td>
                                    <td>
                                        <button class="edit-btn" data-id="${product.id}">Edit</button>
                                        <button class="delete-btn" data-id="${product.id}">Delete</button>
                                    </td>
                                </tr>
                            `);
                    });
                }
            });
        }

        $("#search").on("keyup", function() { // attaches an event listener to the search input field (#search). The event triggers whenever the user releases a key (keyup event).
            clearTimeout(debounceTimer); // Clears any previously set timer (debounceTimer) to prevent multiple requests being sent in quick succession.
            let query = $(this).val().trim();
            debounceTimer = setTimeout(() => { //Sets a delay of 300 milliseconds before calling loadProducts(query).
                loadProducts(query);
            }, 1000);
        });

        // Handle form submission to add a new product (AJAX POST request)
        $("#add-product-form").submit(function(event){
            event.preventDefault(); // Prevent default form submission
            var name = $("#name").val().trim(); // Get product name
            var price = parseFloat($("#price").val().trim()); // Get product price

            // Validate input: Ensure name is not empty and price is valid
            if (!name || isNaN(price) || price <= 0) {
                $("#error-msg").fadeIn().delay(5000).fadeOut();
                return;
            }

            // Asynchronous request to add a product
            $.post({
                url: "/api/products",
                contentType: "application/json", // Ensure JSON is sent correctly
                data: JSON.stringify({ name, price }),
                success: function(response) {
                    setTimeout(function() {
                        loadProducts(); // Refresh product list after 2000 seconds
                    }, 2000);
                    console.log("Product added:", response);
                    $("#name").val(""); // Clear input fields
                    $("#price").val("");
                },
                error: function(xhr) {
                    console.error("Error:", xhr.responseText);
                }
            });
        });

        // Handle product deletion (AJAX DELETE request)
        $("#product-list").on("click", ".delete-btn", function() {
            var id = $(this).data("id");
            // Perform the deletion logic here
            $.ajax({
                url: `/api/products/${id}`,
                type: "DELETE",
                success: function() {
                    loadProducts();
                }
            });
        });

        $("#update-product-form").submit(function(event){
            event.preventDefault();
            let id = parseInt($("#update-id").val().trim());
            let name = $("#update-name").val().trim();
            let price = parseFloat($("#update-price").val().trim());

            if (isNaN(id) || id <= 0 || (!name && isNaN(price))) {
                $("#update-error-msg").fadeIn().delay(5000).fadeOut();
                return;
            }

            $.ajax({
                url: `/api/products/${id}`,
                type: "PUT",
                contentType: "application/json",
                data: JSON.stringify({ name, price }),
                success: function() {
                    loadProducts();
                    $("#update-id, #update-name, #update-price").val("");
                }
            });
        });

        // Load product data into update form when "Edit" is clicked
        $("#product-list").on("click", ".edit-btn", function() {
            let id = $(this).data("id");
            $("#updateform").fadeIn(2000);
            $.get(`/api/products/${id}`, function(product) {
                $("#update-id").val(product.id);
                $("#update-name").val(product.name);
                $("#update-price").val(product.price);
            });
        });

        loadProducts(); // Initial load of products (asynchronous)
    });
</script>
</body>
</html>
```

/module3/part7/product-processor.py
```bash
from confluent_kafka import Consumer, Producer
import json

KAFKA_BROKER = "localhost:9092"
PRODUCTS_TOPIC = "dss-products"
VALIDATED_TOPIC = "dss-validated-products"


# Kafka Producer for sending validated products
def send_validated_product(product):
    producer = Producer({'bootstrap.servers': KAFKA_BROKER})
    producer.produce(VALIDATED_TOPIC, key=str(product['id']), value=json.dumps(product))
    producer.flush()

# Process product
def process_product(product):
    """Business logic: Validate and adjust price."""
    price = product["price"]

    # Example rules
    if price < 500:
        price *= 0.9  # Apply 10% discount
    price *= 1.05  # Add 5% tax

    product["price"] = round(price, 2)
    return product


# Kafka Consumer for receiving products to process
# Kafka Consumer Configuration
consumer_conf = {
    'bootstrap.servers': KAFKA_BROKER,
    'group.id': 'product-processor',
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(consumer_conf)
consumer.subscribe([PRODUCTS_TOPIC])

print("Python Kafka Consumer listening...")

# Processing Loop
while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print(f"Consumer error: {msg.error()}")
        continue

    product = json.loads(msg.value().decode('utf-8'))
    print(f"Received: {product}")

    # Apply business logic
    # Process product
    validated_product = process_product(product)
    print(f"Processed: {validated_product}")

    send_validated_product(validated_product)

consumer.close()

```


---
## **Hands-on Exercise 9**

---
