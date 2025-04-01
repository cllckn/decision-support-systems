# **Hands-On Exercise 1: Extending the Product Selection Application**

#### **Objective**
Enhance the existing product selection application by integrating a customer selection feature and saving purchase records to a database.

#### **Tasks**

1. **Extend the Database Schema**
    - Add a `customers` table to store customer information.
    - Add a `customer_products` table to track customer purchases.

2. **Enhance the Form**
    - Add a **customer selection dropdown** which retrieves customers from `customers` table.
    - Maintain the existing product selection functionality.

3. **Handle Form Submission**
    - On form submission, store the selected **customer, product, quantity, and total price** in the `customer_products` table.

4. **Update the Backend**
    - Implement API endpoints in **Node.js + Express** to:
        - Fetch customers.
        - Save purchase records.

5. **Improve Frontend with jQuery**
    - Fetch and display customer data dynamically.
    - Handle form submission via AJAX.

---

## **Hands-on Exercise2**

Introducing the moderator role with id:3. Moderators will have distinct permissions, separate from admins and registered users.

### Steps to Implement

* Design Moderator Page – Copy registered-user.html, rename it to moderator.html, and update relevant UI elements.

* Modify Login Handling – Update the authentication function to handle moderator login.

* Adjust Access Control – Ensure only users with role ID 3 can access moderator.html.

* Allow Customer Listing – Update the relevant route in the server to allow moderators to retrieve and list customers.


---


# **Hands-On Exercise 3: Extending the Application in /module4/part3 (or Exercise 2) With User Profile Management Feature**


## **Assignment Overview**
In this assignment, you will extend the existing web application to implement a **user profile management feature**. Users should be able to view and update their personal details.

## **Requirements**

### **1️⃣ Web Interface Enhancements**
- Add a **clickable username** at the top-right corner of the page in `dashboard.html` and `registered-user.html`.
- When clicked, display a **user information form** in the main content area.

### **2️⃣ User Information Form**
- Display the following fields:
   - **Username** (read-only)
   - **First Name** (editable)
   - **Last Name** (editable)
   - **City** (editable)
- Include a **Save** button to update the information.

### **3️⃣ Backend Services**
Implement the following API endpoints in `server.js`:

| HTTP Method | Endpoint        | Description |
|------------|----------------|-------------|
| **GET**    | `/user/profile` | Fetches the logged-in user's details (Only authenticated users can access this). |
| **PUT**    | `/user/update`  | Updates the first name, last name, and city (Only authenticated users can update their own data). |

- Both endpoints should verify the **JWT token** and ensure the user is authenticated.
- The **PUT request** should allow updates only for the logged-in user.

### **4️⃣ Client-Side AJAX Requests**
- Use **jQuery AJAX** to:
   - Fetch user details when clicking the username.
   - Send an update request when the **Save** button is clicked.

### **5️⃣ Authorization Rules**
- **Admin (role = 1)** and **Registered Users (role = 2)** can view and update their own profile.
- No user should be able to view or edit another user's information.

### **6️⃣ Design Considerations**
- The user form should be **responsive and visually consistent** with the existing UI.
- Provide **user-friendly messages** on success or failure.
- Implement **form validation** before sending the update request.


---
