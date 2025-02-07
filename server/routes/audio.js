// Import the required modules
const express = require("express");
const router = express.Router();

// Import the audio controller
const { analyzeAudio, updateFeedback } = require('../controllers/audio');

// Define the routes

// Analyze audio (initial call processing)
router.post('/analyze', analyzeAudio);

// Update user feedback (after the call)
router.put('/feedback/:feedbackId', updateFeedback);


// Export the router
module.exports = router;