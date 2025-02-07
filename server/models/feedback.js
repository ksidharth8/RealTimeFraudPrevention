const { Schema, model } = require("mongoose");

const feedbackSchema = new Schema(
	{
		transcript: {
			type: String,
			required: true,
		},
		isFraudulent: {
			type: Boolean,
			required: true,
			index: true, // Adding index for better query performance
		},
		userFeedback: {
			type: String,
			default: "",
			trim: true, // Trim whitespace
			maxlength: 500, // Example constraint
		},
	},
	{ timestamps: true }
);

module.exports = model("Feedback", feedbackSchema);
