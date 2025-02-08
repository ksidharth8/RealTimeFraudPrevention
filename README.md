# Real-Time Fraud Detection System

This project aims to build an AI-powered real-time fraud detection system to protect users from scam phone calls. The system uses machine learning models to analyze audio transcripts and detect fraudulent behavior. It also provides a feedback mechanism for users to report scam calls and improve the model. The system can be deployed as a mobile app or web app to help users identify and avoid scam calls.
For more information, please refer to [Pdf Preview](ProblemStatement.pdf)

## Tech Stack

-  **Frontend**: React Native (Android)
-  **Backend**: Node.js, Express.js, Flask
-  **Database**: MongoDB
-  **Machine Learning**: Python, TensorFlow, Keras
-  **Speech-to-Text**: OpenAI Whisper API

## Project Structure

The project is divided into four main components:

1. **Datasets**: Contains scam-related datasets for training the machine learning model.
2. **Frontend**: Contains the React Native or web app for users to interact with the system.
3. **Python Service**: Contains the Python ML/NLP service for processing audio transcripts and detecting fraud.
4. **Server**: Contains the Express.js backend for handling user requests and storing feedback data.

## Directory Structure

```
RealTimeFraudDetection/
├── datasets/                   # Scam-related datasets
│   └── data                    # Data files
│       ├── dataset.json        # Example dataset
│       ├── dataset.py          # Python script to load dataset
│       └── transcripts.csv     # Transcripts of scam calls
│
├── frontend/                   # React Native or web app
│   └── FraudDetectionApp/      # React Native app
│       ├── App.tsx             # Main app file
│       ├── package.json        # App dependencies
│       └── src/                # App source code
│           └── screens/        # App screens
│
├── python-service/             # Python ML/NLP service
│   ├── venv/                   # Python virtual environment
│   ├── app.py                  # Main Flask app file
│   ├── requirements.txt        # Python dependencies
│   └── model/                  # Machine learning models
│       ├── train_model.py      # Python script to train model
│       ├── test_model.py       # Python script to test model
│       └── requirements.txt    # Python dependencies
│
├── server/                     # Express.js backend
│   ├── node_modules/           # Node.js dependencies
│   ├── config/                 # Configuration files
│       └── db.js               # MongoDB connection
│   ├── controllers/            # Express controllers
│       └── audio.js            # Audio processing controller
│   ├── models/                 # MongoDB models
│       └── feedback.js         # Feedback model
│   ├── routes/                 # Express routes
│       └── audio.js            # Audio processing routes
│   ├── app.js                  # Main Express app file
│   ├── package.json            # Node.js dependencies
│   └── .env                    # Environment variables
│
└── README.md                   # Project documentation
```

## Getting Started

To get started with the Real-Time Fraud Detection System, follow these steps:

1. **Clone the Repository**: Clone the repository to your local machine:
   ```bash
   git clone https://github.com/ksidharth8/RealTimeFraudPrevention.git
   ```
2. **Navigate to the Project Directory**: Change to the project directory:
   ```bash
   cd RealTimeFraudPrevention
   ```
3. **Set Up Environment Variables**: Create a `.env` file (can take help with `.env.sample`) in the `server` directory and add the necessary environment variables.
4. **Install Dependencies**: Install the required dependencies for each component:
   -  **Frontend**: Navigate to the `frontend/FraudDetectionApp` directory and run:
      ```bash
      cd frontend/FraudDetectionApp
      npm install
      ```
   -  **Python Service**: Navigate to the `python-service` directory, create and activate a virtual environment, and install the dependencies:
      ```bash
      cd python-service
      python -m venv venv
      source venv/bin/activate  # On Windows use `venv\Scripts\activate`
      pip install -r requirements.txt
      ```
   -  **Server**: Navigate to the `server` directory and run:
      ```bash
      cd server
      npm install
      ```
5. **Train the Model**: Navigate to the `python-service/model` directory and run:
   ```bash
   cd python-service/model
   python train_model.py
   ```
6. **Start the Services**: Start each service in separate terminal windows:
   -  **Frontend**: Navigate to the `frontend/FraudDetectionApp` directory and run:
      ```bash
      cd frontend/FraudDetectionApp
      npm run android
      ```
   -  **Python Service**: Navigate to the `python-service` directory and run:
      ```bash
      cd python-service
      python app.py
      ```
   -  **Server**: Navigate to the `server` directory and run:
      ```bash
      cd server
      node app.js
      ```
7. **Access the Application**: Access the frontend app on your Android device or emulator.

Once you have completed these steps, you should have the Real-Time Fraud Detection System up and running on your local machine.

## Deployment

The frontend will be served as an Android app. Follow the instructions in the "Getting Started" section to set up and run the app on an Android device or emulator.

## How to Run

1. **Install Dependencies**: Install the required dependencies for the frontend, Python service, and server.
2. **Train Model**: Train the machine learning model using the scam-related datasets.
3. **Start Services**: Start the Python service, server, and frontend app.
4. **Test System**: Test the system by making a request to the server and receiving a response from the machine learning model.

## How to Use

1. **User Registration**: Users can register for an account using their phone number and email address.
2. **Audio Transcription**: Users can upload an audio file of a scam call to the system.
3. **Fraud Detection**: The system will analyze the audio transcript and detect fraudulent behavior.
4. **Feedback Mechanism**: Users can provide feedback on the accuracy of the fraud detection model.
5. **Scam Reporting**: Users can report scam calls to help improve the model and protect other users.

## Testing

To test the Real-Time Fraud Detection System, follow these steps:

### Backend Testing
For testing the backend, you can use tools like Postman to make requests to the server and check the responses:
1. Start the server by running `npm run dev` in the `server` directory.
2. Go to following URL for the public Workspace of Postman:
   [![Run in Postman](https://run.pstmn.io/button.svg)](https://www.postman.com/material-operator-85503474/workspace/realtimefraudprevention)
3. Click on the "Run in Postman" button to import the collection.
4. Run the requests in the collection to test the backend API.
5. Check the responses to ensure that the system is working correctly.

### Frontend Testing
For testing the frontend, you can use the React Native app to interact with the system:
1. Start the frontend app by running `npm run android` in the `frontend/FraudDetectionApp` directory.
2. Use the app to register for an account, upload an audio file, and provide feedback on the fraud detection model.
3. Check the app for any errors or issues while using the system.

### Python Service Testing (Machine Learning Model)
For testing the Python service, you can use the test script to evaluate the machine learning model:
1. Navigate to the `python-service/model` directory.
2. Ensure that the model has been trained by running `python train_model.py`.
3. Run the test script to evaluate the model:
   ```bash
   python test_model.py
   ```
4. Check the output to see the accuracy of the model.

## Troubleshooting

If you encounter any issues while setting up or running the Real-Time Fraud Detection System, please follow these steps:

1. **Check Dependencies**: Make sure that all the dependencies for the frontend, Python service, and server have been installed.
2. **Environment Variables**: Check that the environment variables in the `.env` file are correct.
3. **Training Model**: Ensure that the machine learning model has been trained successfully.
4. **Start Services**: Start each service in separate terminal windows and check for any error messages.
5. **Test System**: Test the system by making a request to the server and checking the response from the machine learning model.

## Future Work

-  **Improve Model Accuracy**: Train the machine learning model on more scam-related datasets to improve accuracy.
-  **Enhance User Experience**: Add more features to the frontend app, such as real-time notifications and scam alerts.
-  **Scale System**: Deploy the system on a cloud platform to handle a large number of users and requests.
-  **Integrate with Phone Apps**: Integrate the system with phone apps to automatically detect scam calls and block them.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

-  [OpenAI](https://www.openai.com/)
-  [TensorFlow](https://www.tensorflow.org/)
-  [MongoDB](https://www.mongodb.com/)
-  [React Native](https://reactnative.dev/)
-  [Node.js](https://nodejs.org/)
-  [Express.js](https://expressjs.com/)
-  [Flask](https://flask.palletsprojects.com/)
-  [Python](https://www.python.org/)
-  [Icons8](https://icons8.com/)

## Contributors

-  [Kumar Sidharth](https://github.com/ksidharth8)
-  [Nischay Mishra](https://github.com/NishV72005)
-  [Rishit Aryan](https://github.com/aryanrishit)

## How to Contribute

1. Fork the repository
2. Create a new branch (`git checkout -b feature`)
3. Make changes and commit them (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature`)
5. Create a new pull request

## Support or Contact

For support, please contact the project maintainers Kumar Sidharth, Nischay Mishra, and Rishit Aryan.

Kumar Sidharth - [@Ksidharth88](https://twitter.com/Ksidharth88) - [kumarsidharth333@gmail.com](mailto:kumarsidharth333@gmail.com)
Project Link: [https://github.com/ksidharth8/RealTimeFraudPrevention](https://github.com/ksidharth8/RealTimeFraudPrevention)

## References

-  [Real-Time Fraud Detection Using Machine Learning](https://www.researchgate.net/publication/344073073_Real-Time_Fraud_Detection_Using_Machine_Learning)
-  [Machine Learning for Fraud Detection](https://www.sciencedirect.com/science/article/pii/S221201731930091X)
-  [Fraud Detection Using Machine Learning](https://www.researchgate.net/publication/344073073_Real-Time_Fraud_Detection_Using_Machine_Learning)
-  [Real-Time Fraud Detection System](https://www.researchgate.net/publication/344073073_Real-Time_Fraud_Detection_Using_Machine_Learning)
-  [Machine Learning Models for Fraud Detection](https://www.sciencedirect.com/science/article/pii/S221201731930091X)

## Disclaimer

This project is for educational purposes only and should not be used for any illegal activities. The project maintainers are not responsible for any misuse of the system by users.

🚀 Happy Coding! 🎉
