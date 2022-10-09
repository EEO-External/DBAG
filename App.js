import React, { useState, useEffect, Component, useRef } from 'react';
import { View, Text, FlatList } from 'react-native';
import { List, ListView } from 'react-native-elements';

function App() {
  const [DropOff, setDropOff] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const url = "";

  useEffect(() => {
    getDropOffAPI();
  }, []);

  const getDropOffAPI = async () => {
    fetch(url, {
      method: 'GET',
      headers: new Headers({
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      }),
    }).then(response => response.json())
      .then(data => {
        setDropOff(data);
        setError(null);
        setLoading(false);
      }).catch(error => {
        console.error(error);
        setError('Not Working Properly');
        setLoading(false);
      });
  }

  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <List>
        <FlatList>
          data = {DropOff} 
          keyExtractor = {(item) => item.id}
          renderItem = {({ item }) => (
            <ListView>
              {item.name} {' '} {item.distance} {' '} {item.travel_time} {' '} {item.queue_time}
            </ListView>
          )}
          
        </FlatList>
      </List>
    </View>
  )
}


export default App;
