import React from 'react';
import { View, Text, StyleSheet, Image, TouchableOpacity } from 'react-native';

const HomeScreen: React.FC = () => {
  return (
    <View style={styles.container}>
      <TouchableOpacity style={styles.checkinContainer}>
        <Image
          source={require('@/assets/images/checkin.png')} // Adjust the path as necessary
          style={styles.checkinImage}
        />
        <Text style={styles.checkinText}>Check-In</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 16,
  },
  checkinContainer: {
    width: '80%',
    height: 200,
    backgroundColor: '#f0f0f0',
    justifyContent: 'center',
    alignItems: 'center',
    borderRadius: 10,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.8,
    shadowRadius: 2,
    elevation: 5,
  },
  checkinImage: {
    width: 100,
    height: 100,
    marginBottom: 16,
  },
  checkinText: {
    fontSize: 24,
    fontWeight: 'bold',
  },
});

export default HomeScreen;