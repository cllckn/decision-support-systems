# Module 4: Advanced User Interaction, Visualization, and Security


## Part 1: Integrating Software Systems Using REST APIs

### Case Study 1

* /part1/internal/

### Case Study 2

* /part1/external/




## Part 2: Dynamic Forms

```sql
CREATE DATABASE dss;

CREATE TABLE category (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE product_extended (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price NUMERIC(10,2) NOT NULL CHECK (price > 0),
    category_id INTEGER REFERENCES category(id) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO category (name) VALUES ('Electronics'), ('Accessories');

INSERT INTO product_extended (name, price, category_id) VALUES
('Laptop', 999.99, 1),
('Phone', 499.99, 1),
('Headphones', 149.99, 2);

```

* /module4/part2/dynamic-forms/server.js

```javascript
const express = require('express');
const { Pool } = require('pg');
const path = require("path");
const winston = require("winston");
const morgan = require("morgan");

const app = express();
const port = 3000;


app.use(express.json()); // parse json requests
app.use(express.static(path.join(__dirname, 'public'))); // Middleware to serve static files (HTML, CSS, JS) from the 'public' folder

// Log requests in Apache-style format
const logger = winston.createLogger({
    transports: [new winston.transports.File({ filename: 'logs/requests.log' })]
});

app.use(morgan('combined', { stream: { write: message => logger.info(message) } }));


// Initialize a new PostgreSQL connection pool
const pool = new Pool({
    user: 'postgres',
    host: 'localhost',
    database: 'dss',
    password: 'LecturePassword',
    port: 5432,
});

// Route to get all categories
app.get('/categories', async (req, res) => {
    try {
        const result = await pool.query("SELECT * FROM category");
        res.json(result.rows);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Route to get all products with category names
app.get('/products', async (req, res) => {
    try {
        const result = await pool.query(`
            SELECT p.id, p.name, p.price, c.name AS category 
            FROM product_extended p 
            INNER JOIN category c ON p.category_id = c.id
        `);
        res.json(result.rows);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Start the server
app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});

```

* /module4/part2/dynamic-forms/public/index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dynamic Product Form with Database</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="p-6 bg-gray-100 flex items-center justify-center min-h-screen">
<!-- flex: Enables Flexbox.
items-center: Centers content vertically.
justify-center: Centers content horizontally.
min-h-screen: Ensures the body takes up at least the full height of the viewport.
-->

<div class="max-w-lg bg-white p-6 rounded-lg shadow-md">
    <!-- max-w-lg → Sets the maximum width to lg (large), which is 32rem (512px).-->

    <h2 class="text-xl font-bold mb-4">Purchase a Product</h2>

    <form id="productForm">
        <!-- Select Product -->
        <label class="block mb-2 font-semibold">Select Product:</label>
        <select id="productSelect" class="w-full p-2 border rounded">
            <option value="">-- Choose --</option>
        </select>

        <!-- Display Price & Category -->
        <div id="productDetails" class="mt-3 hidden">
            <p><strong>Price:</strong> <span id="productPrice"></span></p>
            <p><strong>Category:</strong> <span id="productCategory"></span></p>
        </div>

        <!-- Payment Method (Radio) -->
        <label class="block mt-4 font-semibold">Payment Method:</label>
        <label class="block"><input type="radio" name="payment" value="credit"> Credit Card</label>
        <label class="block"><input type="radio" name="payment" value="paypal"> PayPal</label>

        <!-- Warranty (Checkbox) -->
        <label class="block mt-4 font-semibold">
            <input type="checkbox" id="warranty"> Add 1-Year Warranty ($29.99)
        </label>

        <!-- Buyer Name (Input) -->
        <label class="block mt-4 font-semibold">Your Name:</label>
        <input type="text" id="buyerName" class="w-full p-2 border rounded" placeholder="Enter your name">

        <!-- Submit Button -->
        <button type="submit" class="w-full mt-4 bg-blue-500 text-white p-2 rounded">
            Submit Order
        </button>
    </form>

    <!-- Order Summary -->
    <div id="orderSummary" class="mt-6 hidden p-4 bg-green-100 border border-green-500 rounded">
        <h3 class="font-bold">Order Summary</h3>
        <p id="summaryText"></p>
    </div>
</div>

<script>
    $(document).ready(function () {
        // Fetch products from database
        $.get("http://localhost:3000/products", function (products) {
            products.forEach(product => {
                $("#productSelect").append(`<option value="${product.id}" data-price="${product.price}" data-category="${product.category}">${product.name}</option>`);
            });
        });

        // Update Product Details
        $("#productSelect").change(function () {
            let selectedOption = $(this).find(":selected");
            let price = selectedOption.data("price");
            let category = selectedOption.data("category");

            if (price && category) {
                $("#productPrice").text(`$${price.toFixed(2)}`);
                $("#productCategory").text(category);
                $("#productDetails").removeClass("hidden");
            } else {
                $("#productDetails").addClass("hidden");
            }
        });

        // Handle Form Submission
        $("#productForm").submit(function (e) {
            e.preventDefault();
            let productId = $("#productSelect").val();
            let productName = $("#productSelect option:selected").text();
            let name = $("#buyerName").val();
            let payment = $("input[name='payment']:checked").val();
            let warranty = $("#warranty").is(":checked") ? "Yes" : "No";

            if (!productId || !name || !payment) {
                alert("Please fill all required fields.");
                return;
            }

            // Display Order Summary
            $("#summaryText").html(`
                    <strong>Buyer:</strong> ${name} <br>
                    <strong>Product:</strong> ${productName} <br>
                    <strong>Payment:</strong> ${payment} <br>
                    <strong>Warranty:</strong> ${warranty}
                `);
            $("#orderSummary").fadeIn(1000);

        });
    });
</script>
</body>
</html>

```


---
## **Hands-on Exercise1**


---



## Part 3: Access Control: Authentication and Authorization with JWT (JSON Web Tokens)

### 3.1.Role Based Access Control

* **Access Control** is the process of controlling the interaction of system actors with resources based on predefined rules, policies, and permissions.

* **Actors (Users/Entities)**: Humans, software, systems, or devices that interact (accessing, modifying, executing, or any other operation on the resource) with the system.

* **Resources** are the objects or assets being interacted with.
  * Operating System: Resources such as memory (read, write), files (read, write, execute), directories, and ports (read, write). 
  * Database: Resources like tables (insert, update, select), views, stored procedures, and functions. 
  * Application Software: Resources such as interfaces (access), web pages (access), and functions (execute).

* **Permissions** are specific rights granted to actors over resources - such as read, write, execute, or delete.

* **Authorization** is the process of granting or restricting permissions for actors to interact with specific resources within a system.

* **Authentication** is the process of verifying the identity of an actor. 


* Extensively used approach is Role-Based Access Control (RBAC):
  * Permissions are typically assigned to roles rather than individual actors to simplify management. 
  * Actors are then assigned to these roles, inheriting the associated permissions.
  * Ensures scalability and ease of administration in systems with many users and resources.


* RBAC


| **Actors**     | M<------->N | **Roles**       | M<------->N | **Permissions** | M<------->1 | **Resources**      |
|----------------|-------------|-----------------|-------------|-----------------|-------------|--------------------|
| user,system... | M<------->N | admin,editor... | M<------->N | read,access...  | M<------->1 | Table, web page... |




* Activity matrix
![Activity Matrix](../resources/figures/activity-matrix.png)



### 3.2.JWT (JSON Web Token)
JWT (JSON Web Token) is a compact, self-contained token used for securely transmitting information between parties 
as a JSON object. It is commonly used for authentication and authorization, relying on signing (not just encoding) 
to ensure data integrity and prevent tampering. However, JWTs are not encrypted by default, so sensitive data should 
not be stored in them unless encrypted separately.



#### **How Does JWT Work?**
1. **User Logs In** → Sends credentials to the server.
2. **Server Generates JWT** → If valid, the server generates a JWT and signs it with a secret key.
3. **Client Stores Token** → The JWT is stored (e.g., in local storage or cookies).
4. **Client Sends Token** → With each request, the token is sent in the `Authorization` header (`Bearer token`).
5. **Server Verifies JWT** → If valid, access is granted; otherwise, it is denied.

![](../resources/figures/authentication-with-jwt.png)

`https://coredevsltd.com/articles/jwt-token-authentication-web-api/`



#### **Structure of a JWT**
A JWT consists of three parts, separated by dots (`.`):  
`Header.Payload.Signature`

- **Header** → Contains the token type and signing algorithm.
```json
{
  "alg": "HS256",
  "typ": "JWT"
}

```
- **Payload** → Holds claims (user data, expiration, etc.).
```json
{
  "id": 1,
  "username": "user1",
  "name": "Jane Lee",
  "role": "admin",
  "exp": 1710000000
}

```
- **Signature** → Verifies the integrity of the token.
  - base64UrlEncode(X) function encodes the X using Base64 URL encoding.

```plain

HMACSHA256(
    base64UrlEncode(header) + "." +  encodes the header using Base64 URL encoding.
    base64UrlEncode(payload),
    secret_key
)

secret_key: my-secret-key-is-this-at-least-256-bits

```

The JWT generated based on the parameters above is:

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJ1c2VyMSIsIm5hbWUiOiJKYW5lIExlZSIsInJvbGUiOiJhZG1pbiIsImV4cCI6MTcxMDAwMDAwMH0.zKrmHfgZQN-bYfiEHYvCoKdcJ_85gcay2-B4CtKSTxU

The above JWT is encoded but not encrypted, meaning anyone can decode it to view the header and payload. 
However, data integrity and tamper prevention are ensured because it is signed, not just encoded.

* [jwt debugger](https://jwt.io/) 


#### **Key Properties of JWT?**
- **Stateless** → No need to store sessions on the server.
- **Compact** → Can be sent in headers (Authorization: `Bearer token`).
- **Secure** → Supports signing and encryption.
- **Scalable** → Works well in distributed systems.


### 3.4.Multifactor Authentication (MFA)

Multifactor Authentication (MFA) is a security method that requires users 
to verify their identity using multiple factors before granting access.

#### **Factors of Authentication**
1. **Something You Know** → Password, PIN.
2. **Something You Have** → OTP (One-Time Password), Security Token.
3. **Something You Are** → Biometrics (Fingerprint, Face ID).

#### **Why Use MFA?**
- Enhances security by requiring multiple verification steps.
- Protects against password breaches and phishing attacks.
- Commonly used in banking, enterprise logins, and cloud services.

#### **Example MFA Process**
1. User enters a password.
2. A one-time code is sent via SMS or authentication app.
3. User enters the code to complete login.

### A Case Study on Authentication and Authorization

* /module4/part3/

```sql
CREATE DATABASE dss;
----------------------------
create table if not exists public.users
(
  id        serial
    primary key,
  username  varchar(50)  not null
    unique,
  password  varchar(255) not null,
  firstname varchar(50)  not null,
  lastname  varchar(50)  not null,
  role      smallint
);

----------------------------
create table if not exists public.customers
(
  id    serial
    primary key,
  name  varchar(50) not null,
  email varchar(50),
  phone varchar(50),
  city  varchar(50)
);


```


####  Application Summary

This is a **Node.js-based web application** with user authentication, role-based access control, and a customer management module.

#####  Main Features

* Redirects users to different dashboards based on their role.  
* Alerts users and redirects them to login if the session expires.  
* Secure API Calls- uses `Authorization: Bearer <token>` in requests.  



#####  Technologies Used
- **Backend:** Node.js, Express, PostgreSQL
- **Authentication:** JWT (JSON Web Tokens), bcrypt for password hashing
- **Frontend:** HTML, jQuery, Tailwind CSS
- **API Requests:** AJAX with jQuery



#####  Routes & Endpoints

###### 🔹 Public Routes
| HTTP Method | Endpoint      | Description |
|------------|--------------|-------------|
| **POST**   | `/register`   | Registers a new user (username, password, first name, last name, role) |
| **POST**   | `/login`      | Authenticates user and returns a JWT token |



###### 🔹 Protected Routes (Requires Bearer Token in Headers)
| HTTP Method | Endpoint      | Description |
|------------|--------------|-------------|
| **GET**    | `/dashboard`  | Verifies token and returns a welcome message with the username |
| **GET**    | `/customers`  | Returns all customer records (Admin-only, `role = 1`) |



##### 🖥️ Web Pages & Access Control

###### 🔹 Page Structure
| Page | Description | Access |
|------|-------------|--------|
| `login.html` | User login page | Public |
| `dashboard.html` | Admin dashboard | Role `1` (Admin) |
| `registered-user.html` | Registered user dashboard | Role `2` (Regular User) |
| `unauthorized.html` | Shown when access is denied | Public |



##### 🛑 Authentication & Authorization

- **JWT Tokens**: Stored in `localStorage` after login.
- **Token Expiry**: Tokens expire in **1 hour** (`expiresIn: "1h"`).
- **Access Control**:
  - `role = 1` → Admin (Full access, including customer management).
  - `role = 2` → Regular User (Limited access).
  - Any **invalid or missing token** → Redirects to `login.html`.
  - Any **unauthorized role** → Redirects to `unauthorized.html`.






---
## **Hands-on Exercise2**
---


## Part 4: Integrating Visualization Components into Web Applications

Data visualization plays a crucial role in making complex information more accessible and understandable. 
One of the most effective ways to represent data is through charts, which help identify patterns, trends, and insights at a glance.

ApexCharts is a powerful JavaScript-based library designed for generating interactive and visually appealing charts. 
It provides a variety of chart types that can be seamlessly integrated into web applications and mobile environments.

This part will focus on utilizing ApexCharts to enhance data presentation. Before implementing charts, the library 
must first be imported into the project. By leveraging ApexCharts, developers can efficiently transform raw data into meaningful 
visual representations, improving the overall user experience.

* https://apexcharts.com/javascript-chart-demos/
