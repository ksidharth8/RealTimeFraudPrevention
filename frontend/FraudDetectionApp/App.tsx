import 'react-native-gesture-handler';
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import HomeScreen from './src/screens/HomeScreen';
import CallScreen from './src/screens/CallScreen';
import FeedbackScreen from './src/screens/FeedbackScreen';

const Stack = createStackNavigator();

const App = () => {
    return (
        <NavigationContainer>
            <Stack.Navigator initialRouteName="Home">
                <Stack.Screen name="Home" component={HomeScreen} />
                <Stack.Screen name="Call" component={CallScreen} />
                <Stack.Screen name="Feedback" component={FeedbackScreen} />
            </Stack.Navigator>
        </NavigationContainer>
    );
};

export default App;
