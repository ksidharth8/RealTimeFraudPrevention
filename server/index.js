// express-backend/app.js
const express = require("express");
const app = express();

// import dotenv and configure it
require("dotenv").config();

// import routes
const audioRoutes = require("./routes/audio");

const cors = require("cors"); // enabling cors for frontend requests
const bodyParser = require("body-parser"); // parsing incoming requests
const axios = require('axios'); // making http requests

const PORT = process.env.PORT || 4000; // define the port

// database connection
require("./config/database")();

// middlewares
app.use(cors(
    {
        origin: "http://localhost:3000",
        credentials: true,
    }
));
app.use(bodyParser.json());

// mount the routes
app.use("/api/v1/audio", audioRoutes);

// default route
app.get("/", (req, res) => {
	res.send("Real-Time Fraud Detection Backend");
});

// start the server
app.listen(PORT, () => {
	console.log(`Server is running on http://localhost:${PORT}`);
});
