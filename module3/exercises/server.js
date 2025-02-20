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
