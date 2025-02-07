import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet, Alert } from 'react-native';
import axios from 'axios';

const FeedbackScreen = ({ route, navigation }) => {
    const [userFeedback, setUserFeedback] = useState('');
    const { feedbackId } = route.params;

    const submitFeedback = async () => {
        try {
            await axios.put(`http://localhost:5000/api/audio/feedback/${feedbackId}`, {
                userFeedback: userFeedback,
            });
            Alert.alert('Success', 'Thank you for your feedback!');
            navigation.navigate('Home');
        } catch (error) {
            console.error(error);
            Alert.alert('Error', 'Failed to submit feedback.');
        }
    };

    return (
        <View style={styles.container}>
            <Text style={styles.title}>Provide Feedback</Text>
            <TextInput
                style={styles.input}
                placeholder="Was this call a scam? Please provide feedback."
                value={userFeedback}
                onChangeText={setUserFeedback}
                multiline
            />
            <Button title="Submit Feedback" onPress={submitFeedback} />
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        padding: 20,
    },
    title: {
        fontSize: 24,
        marginBottom: 20,
    },
    input: {
        width: '100%',
        height: 100,
        borderColor: '#ccc',
        borderWidth: 1,
        borderRadius: 5,
        padding: 10,
        marginBottom: 20,
    },
});

export default FeedbackScreen;
