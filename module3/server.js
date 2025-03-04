
const express = require("express");
const path = require("path");
const app = express();
//const cors = require("cors"); // Import CORS


app.use(express.json()); // parse json requests
app.use(express.static(path.join(__dirname, 'public'))); // Middleware to serve static files (HTML, CSS, JS) from the 'public' folder


//app.use(cors()); // Enable CORS for all routes
// The browser blocks cross-origin requests unless the server explicitly allows them.
// Cross-Origin means that the protocol, domain, or port is different between the frontend and backend.

// In-memory database: JSON array for products
let products = [
    { id: 1, name: "Laptop", price: 999.99 },
    { id: 2, name: "Phone", price: 499.99 },
];

// GET all products
app.get("/api/products", (req, res) => {
    const query = req.query.name?.toLowerCase() || "";

    if (query) {
        const filteredProducts = products.filter(product =>
            product.name.toLowerCase().includes(query)
        );
        return res.json(filteredProducts);
    }

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