const express = require("express");
const axios = require("axios");
const cors = require("cors");
const path = require('path');

const app = express();
const PORT = 4000; // Running on different port than the REST API

app.use(express.json()); // Parse JSON
app.use(cors()); // Allow cross-origin requests

app.use(express.static(path.join(__dirname, 'public'))); // Middleware to serve static files (HTML, CSS, JS) from the 'public' folder


const API_URL = "http://localhost:3000/api/products"; // Your REST API URL

// Fetch all products from the REST API
app.get("/client/products", async (req, res) => {
  try {
    const response = await axios.get(API_URL);
    res.json(response.data);
  } catch (error) {
    res.status(500).json({ error: "Failed to fetch products" });
  }
});

// Add a new product using the REST API
app.post("/client/products", async (req, res) => {
  try {
    const { name, price } = req.body;
    console.log("Request body:", req.body); // Debug log

    axios.post(API_URL, { name, price })
      .then((response) => {
        console.log(response.data);
        res.status(201).json(response.data);
      })
      .catch((error) => {
        console.error("Error:", error);
      });

  } catch (error) {
    console.error("Error occurred:", error); // Detailed logging
    res.status(500).json({ error: "Failed to add product" });
  }
});

// Start the client server
app.listen(PORT, () => {
  console.log(`Client service running on http://localhost:${PORT}`);
});
