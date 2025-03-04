const express = require("express");
const path = require("path");
const app = express();

app.use(express.json()); // Parse JSON requests

app.use(express.static(path.join(__dirname, 'public')));


// In-memory database: Array to store customer data
let customers = [
    { id: 1, name: "Alice Johnson", email: "alice@example.com", phone: "1234567890", city: "New York" },
    { id: 2, name: "Bob Smith", email: "bob@example.com", phone: "9876543210", city: "Los Angeles" },
];


// GET all customers
app.get("/api/customers", (req, res) => {
    // Accesses the name parameter from the query string in an Express.js request object.
    const query = req.query.name?.toLowerCase() || "";

    if (query) {
        const filteredCustomers = customers.filter(customer =>
            customer.name.toLowerCase().includes(query)
        );
        return res.json(filteredCustomers);
    }

    res.json(customers);
});

// GET a single customer by ID
app.get("/api/customers/:id", (req, res) => {
    const customer = customers.find((c) => c.id === parseInt(req.params.id));
    if (!customer) return res.status(404).json({ error: "Customer not found" });
    res.json(customer);
});

// POST - Add a new customer
app.post("/api/customers", (req, res) => {
    const { name, email, phone, city } = req.body;
    if (!name || !email || !phone || !city) return res.status(400).json({ error: "Invalid input" });

    const newCustomer = { id: customers.length + 1, name, email, phone, city };
    customers.push(newCustomer);
    res.status(201).json(newCustomer);
});

// PUT - Update a customer
app.put("/api/customers/:id", (req, res) => {
    const customer = customers.find((c) => c.id === parseInt(req.params.id));
    if (!customer) return res.status(404).json({ error: "Customer not found" });

    const { name, email, phone, city } = req.body;
    customer.name = name || customer.name;
    customer.email = email || customer.email;
    customer.phone = phone || customer.phone;
    customer.city = city || customer.city;

    res.json(customer);
});

// DELETE - Remove a customer
app.delete("/api/customers/:id", (req, res) => {
    customers = customers.filter((c) => c.id !== parseInt(req.params.id));
    res.json({ message: "Customer deleted" });
});

// Start server
const PORT = 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
