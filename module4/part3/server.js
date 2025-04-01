const express = require("express");
const jwt = require("jsonwebtoken");
const bcrypt = require("bcrypt");
const bodyParser = require("body-parser");
const { Pool } = require("pg");
const path = require("path");

const app = express();
const PORT = 3000;
const SECRET_KEY = "my-secret-key-is-this-at-least-256-bits"; // Change this in production
const SALT_ROUNDS = 10; // For bcrypt password hashing- Salting Makes Passwords Hard to Guess

// Initialize PostgreSQL connection pool
const pool = new Pool({
    user: 'postgres',
    host: 'localhost',
    database: 'dss',
    password: 'LecturePassword',
    port: 5432,
});

// Middleware
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, "public"))); // Serve static files

// Middleware to verify JWT from the request's Authorization header
// Middlewares in Express.js act as interceptors that sit between the incoming request and the final route handler (or response).
// They can modify, validate, or reject requests before they reach their destination.
const authenticateToken = (req, res, next) => {
    const authHeader = req.headers.authorization;

    if (!authHeader || !authHeader.startsWith("Bearer ")) {
        return res.status(401).json({ error: "Unauthorized: Missing or invalid token" });
    }

    const token = authHeader.split(" ")[1]; // Extract token after "Bearer "

    try {
        const decoded = jwt.verify(token, SECRET_KEY);
        req.decodedToken = decoded; // Store decoded user info in the request
        next() // Token is valid, proceed to the next middleware or route
    } catch (error) {
        return res.status(403).json({ error: "Forbidden: Invalid token" });// Token is not valid, respond with status code 403
    }
};

// Route to Register a New User
app.post("/register", async (req, res) => {
    const { username, password, firstname, lastname, role } = req.body;
    try {
        const hashedPassword = await bcrypt.hash(password, SALT_ROUNDS);
        await pool.query(
          "INSERT INTO users (username, password, firstname, lastname, role) VALUES ($1, $2, $3, $4, $5)",
          [username, hashedPassword, firstname, lastname, role]
        );
        res.json({ message: "User registered successfully!" });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// Login Route (JWT Authentication)
app.post("/login", async (req, res) => {
    const { username, password } = req.body;
    try {
        const result = await pool.query("SELECT * FROM users WHERE username = $1", [username]);
        const user = result.rows[0];

        if (!user || !(await bcrypt.compare(password, user.password))) {
            return res.status(401).json({ error: "Invalid credentials" });
        }

        const token = jwt.sign(
          { id: user.id, username: user.username, firstname: user.firstname, lastname: user.lastname, role: user.role },
          SECRET_KEY,
          { expiresIn: "1h" }
        );
        res.json({ token });
    } catch (err) {
        res.status(500).json({ error: "Server error" });
    }
});

// Protected Route (Dashboard)
app.get("/dashboard", authenticateToken, (req, res) => {
    res.json({ message: `Welcome, ${req.decodedToken.username}!` });
});

// Protected Route: Get All Customers (Admin Only)
app.get("/api/customers", authenticateToken, async (req, res) => {
    const { role } = req.decodedToken; // Extract role from decoded token

    if (role !== 1) {
        return res.status(403).json({ error: "Forbidden: Admins only" });
    }

    try {
        const result = await pool.query("SELECT id, name, email, phone, city FROM customers");
        res.json(result.rows);
    } catch (err) {
        res.status(500).json({ error: "Failed to fetch customers" });
    }
});

// Start Server
app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
