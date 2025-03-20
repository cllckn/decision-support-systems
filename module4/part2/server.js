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
