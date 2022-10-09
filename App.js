/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow strict-local
 */

import React, {useState} from 'react';
import {
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  useColorScheme,
  View,
  FlatList, 
} from 'react-native';

export default function App() {
  const [dropOff, setDropOff] = useState([
    {
      location: 'BWI',
      key: '0',
      distance: '0 miles',
      exTime: '1 minutes',
    },

    {
      location: 'Laurel',
      key: '1',
      distance: '1 miles',
      exTime: '10 minutes',
    },

    {
      location: 'Ellicot City',
      key: '2',
      distance: '8 miles',
      exTime: '5 minutes',
    },

    {
      location: 'Bay Area',
      key: '3',
      distance: '2 miles',
      exTime: '8 minutes',
    },

    {
      location: 'Glenn Dale',
      key: '4',
      distance: '15 miles',
      exTime: '13 minutes',
    },

    {
      location: 'Columbia',
      key: '5',
      distance: '23 miles',
      exTime: '9 minutes',
    },
    {
      location: 'Aundrel Mills',
      key: '6',
      distance: '12.3 miles',
      exTime: '17 minutes',
    },
  ]);

  return (
    <View style={styles.container}>
      {dropOff.map(item => {
        return (
        <View key={item.key}>
            <Text style={styles.item}>
              {item.location} <Text> {item.distance} </Text>{' '}
              <Text> {item.exTime} </Text>
            </Text>
        </View>
      )
     })}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    //justifyContent: 'center',
    //alignItems: 'center',
    paddingTop: 40,
    paddingHorizontal: 20,
  },

  item: {
    textAlign: 'auto',
    padding: 30,
    backgroundColor: 'lightBlue',
    fontSize: 15,
    marginTop: 20,
  },
});
