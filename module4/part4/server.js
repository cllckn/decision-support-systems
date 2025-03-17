const express = require('express');
const path = require('path');
const { Pool } = require('pg');
const cors = require("cors"); // Import CORS


const app = express();
const PORT = 3000;

const pool = new Pool({
    user: 'postgres',
    host: 'localhost',
    database: 'nw6',
    password: 'LecturePassword',
    port: 5432,
});

app.use(cors()); // Enable CORS for all routes
app.use(express.static(path.join(__dirname, 'public')));


app.get('/categories', async (req, res) => {
    try {
        const result = await pool.query(
          'SELECT "CategoryID", COUNT(*) as count FROM products GROUP BY "CategoryID"'
        );
        res.json(result.rows);
    } catch (error) {
        res.status(500).json({ error: 'Database error' });
    }
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
