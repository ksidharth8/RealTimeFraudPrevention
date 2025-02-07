import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, Alert } from 'react-native';
import axios from 'axios';

const CallScreen = ({ navigation }) => {
    const [isCallActive, setIsCallActive] = useState(false);
    const [transcript, setTranscript] = useState('');
    const [isFraudulent, setIsFraudulent] = useState(false);
    const [feedbackId, setFeedbackId] = useState(null);

    // Simulate call audio capture (replace with actual implementation)
    const simulateCall = async () => {
        setIsCallActive(true);
        const audioStream = "base64-encoded-audio-stream"; // Replace with actual audio

        try {
            // Send audio to backend for analysis
            const response = await axios.post('http://localhost:5000/api/audio/analyze', {
                audio: audioStream,
            });

            setTranscript(response.data.transcript);
            setIsFraudulent(response.data.isFraudulent);
            setFeedbackId(response.data.feedbackId);

            // Show scam alert if fraudulent
            if (response.data.isFraudulent) {
                Alert.alert(
                    'Scam Alert',
                    'This call may be a scam. Do not share personal information.',
                    [
                        { text: 'OK', onPress: () => navigation.navigate('Feedback') },
                    ]
                );
            }
        } catch (error) {
            console.error(error);
        } finally {
            setIsCallActive(false);
        }
    };

    useEffect(() => {
        simulateCall();
    }, []);

    return (
        <View style={styles.container}>
            <Text style={styles.title}>Call Screen</Text>
            {isCallActive ? (
                <Text>Analyzing call...</Text>
            ) : (
                <>
                    <Text>Transcript: {transcript}</Text>
                    <Text>Fraudulent: {isFraudulent ? 'Yes' : 'No'}</Text>
                </>
            )}
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
    title: {
        fontSize: 24,
        marginBottom: 20,
    },
});

export default CallScreen;
