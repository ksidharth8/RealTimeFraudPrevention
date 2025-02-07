// controllers/audioController.js
const axios = require("axios");
const Feedback = require("../models/feedback");

// Analyze audio and save initial result (without user feedback)
const analyzeAudio = async (req, res) => {
	// Extract audio from the request body
	const { audio } = req.body;

	try {
		// // Send audio to Python ML/NLP service
		// const pythonResponse = await axios.post(
		// 	`${process.env.PYTHON_SERVICE_URL}/analyze`,
		// 	{
		// 		audio: audio,
		// 	}
		// );

		// const { transcript, isFraudulent } = pythonResponse.data;

		// For testing purposes, use hardcoded values
		const { transcript, isFraudulent } = {
			transcript: "sample transcript",
			isFraudulent: false,
		};

		// Save initial feedback (userFeedback is empty)
		const feedback = new Feedback({
			transcript,
			isFraudulent,
			userFeedback: "", // Initially empty
		});
		await feedback.save();

		// Send response to frontend (include feedback ID for future updates)
		res.json({
			transcript,
			isFraudulent,
			feedbackId: feedback._id, // Send feedback ID to frontend
		});
	} catch (error) {
		console.error(error);
		res.status(500).json({ error: "Failed to analyze audio" });
	}
};

// Update user feedback after the call
const updateFeedback = async (req, res) => {
	const { feedbackId } = req.params;
	const { userFeedback } = req.body;

	try {
		// Find the feedback entry by ID and update it
		const feedback = await Feedback.findByIdAndUpdate(
			feedbackId,
			{ userFeedback },
			{ new: true } // Return the updated document
		);

		if (!feedback) {
			return res.status(404).json({ error: "Feedback not found" });
		}

		res.json(feedback);
	} catch (error) {
		console.error(error);
		res.status(500).json({ error: "Failed to update feedback" });
	}
};

module.exports = { analyzeAudio, updateFeedback };
