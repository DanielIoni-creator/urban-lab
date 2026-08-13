/**
 * 🛴 Urban Lab Scooter - Mobile App
 * Controllo e monitoraggio del monopattino
 * React Native + Expo
 */

import React, { useState, useEffect } from 'react';
import {
  StyleSheet,
  Text,
  View,
  TouchableOpacity,
  ScrollView,
  Switch,
  Alert,
  ActivityIndicator,
} from 'react-native';
import { BleManager } from 'react-native-ble-plx';
import { Ionicons } from '@expo/vector-icons';

// Configurazione BLE
const SERVICE_UUID = '4fafc201-1fb5-459e-8fcc-c5c9c331914b';
const CHARACTERISTIC_UUID = 'beb5483e-36e1-4688-b7f5-ea07361b26a8';

const App = () => {
  const [connected, setConnected] = useState(false);
  const [scanning, setScanning] = useState(false);
  const [scooterData, setScooterData] = useState({
    speed: 0,
    battery: 100,
    temperature: 25,
    gps: { lat: 44.0576, lon: 12.5653 },
    locked: false,
    errors: 0,
  });
  const [loading, setLoading] = useState(false);

  // Inizializza BLE Manager
  const bleManager = new BleManager();

  // Scan dispositivi
  const scanDevices = () => {
    setScanning(true);
    setLoading(true);
    
    bleManager.startDeviceScan(null, null, (error, device) => {
      if (error) {
        console.error(error);
        setScanning(false);
        setLoading(false);
        Alert.alert('Errore', 'Impossibile scansionare dispositivi');
        return;
      }
      
      if (device.name && device.name.includes('UrbanLab')) {
        connectDevice(device);
      }
    });

    // Ferma scan dopo 5 secondi
    setTimeout(() => {
      bleManager.stopDeviceScan();
      setScanning(false);
      setLoading(false);
    }, 5000);
  };

  // Connetti al dispositivo
  const connectDevice = async (device) => {
    try {
      setLoading(true);
      const connectedDevice = await device.connect();
      await connectedDevice.discoverAllServicesAndCharacteristics();
      
      // Leggi caratteristica
      const characteristic = await connectedDevice.readCharacteristicForService(
        SERVICE_UUID,
        CHARACTERISTIC_UUID
      );
      
      // Parsing dati
      const data = parseData(characteristic.value);
      setScooterData(data);
      setConnected(true);
      
      Alert.alert('Connesso', 'Scooter connesso con successo!');
    } catch (error) {
      console.error(error);
      Alert.alert('Errore', 'Connessione fallita');
    } finally {
      setLoading(false);
      setScanning(false);
    }
  };

  // Parsing dati dal BLE
  const parseData = (value) => {
    if (!value) return scooterData;
    
    const parts = value.split(',');
    if (parts.length >= 5) {
      return {
        speed: parseFloat(parts[0]) || 0,
        battery: parseFloat(parts[1]) || 100,
        temperature: parseFloat(parts[2]) || 25,
        gps: {
          lat: parseFloat(parts[3]) || 44.0576,
          lon: parseFloat(parts[4]) || 12.5653,
        },
      };
    }
    return scooterData;
  };

  // Invia comando (lock/unlock)
  const sendCommand = async (command) => {
    if (!connected) {
      Alert.alert('Errore', 'Scooter non connesso');
      return;
    }
    
    try {
      setLoading(true);
      // Implementa invio comando via BLE
      Alert.alert('Comando inviato', `Comando: ${command}`);
    } catch (error) {
      console.error(error);
      Alert.alert('Errore', 'Invio comando fallito');
    } finally {
      setLoading(false);
    }
  };

  // Disconnetti
  const disconnect = () => {
    bleManager.stopDeviceScan();
    bleManager.destroy();
    setConnected(false);
    setScooterData({
      speed: 0,
      battery: 100,
      temperature: 25,
      gps: { lat: 44.0576, lon: 12.5653 },
      locked: false,
      errors: 0,
    });
    Alert.alert('Disconnesso', 'Scooter disconnesso');
  };

  // UI principale
  return (
    <View style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollView}>
        {/* Header */}
        <View style={styles.header}>
          <Text style={styles.title}>🛴 Urban Lab</Text>
          <Text style={styles.subtitle}>Monopattino del Futuro</Text>
          <View style={[styles.statusBadge, connected ? styles.connected : styles.disconnected]}>
            <Text style={styles.statusText}>
              {connected ? '● Connesso' : '○ Disconnesso'}
            </Text>
          </View>
        </View>

        {/* Connetti / Disconnetti */}
        {!connected ? (
          <TouchableOpacity
            style={styles.connectButton}
            onPress={scanDevices}
            disabled={loading}
          >
            <Text style={styles.buttonText}>
              {loading ? 'Connessione...' : '🔌 Connetti Scooter'}
            </Text>
          </TouchableOpacity>
        ) : (
          <TouchableOpacity
            style={styles.disconnectButton}
            onPress={disconnect}
          >
            <Text style={styles.buttonText}>⛔ Disconnetti</Text>
          </TouchableOpacity>
        )}

        {/* Dati in tempo reale */}
        <View style={styles.dataContainer}>
          <View style={styles.dataCard}>
            <Ionicons name="speedometer" size={30} color="#4CAF50" />
            <Text style={styles.dataLabel}>Velocità</Text>
            <Text style={styles.dataValue}>{scooterData.speed.toFixed(1)} km/h</Text>
          </View>

          <View style={styles.dataCard}>
            <Ionicons name="battery-full" size={30} color="#4CAF50" />
            <Text style={styles.dataLabel}>Batteria</Text>
            <Text style={styles.dataValue}>{scooterData.battery.toFixed(0)}%</Text>
          </View>

          <View style={styles.dataCard}>
            <Ionicons name="thermometer" size={30} color="#FF9800" />
            <Text style={styles.dataLabel}>Temp. Motore</Text>
            <Text style={styles.dataValue}>{scooterData.temperature.toFixed(1)}°C</Text>
          </View>

          <View style={styles.dataCard}>
            <Ionicons name="location" size={30} color="#2196F3" />
            <Text style={styles.dataLabel}>GPS</Text>
            <Text style={styles.dataValueSmall}>
              {scooterData.gps.lat.toFixed(4)}°N
            </Text>
            <Text style={styles.dataValueSmall}>
              {scooterData.gps.lon.toFixed(4)}°E
            </Text>
          </View>
        </View>

        {/* Controlli */}
        <View style={styles.controlsContainer}>
          <Text style={styles.sectionTitle}>🎮 Controlli</Text>
          
          <View style={styles.controlRow}>
            <TouchableOpacity
              style={[styles.controlButton, styles.lockButton]}
              onPress={() => sendCommand('lock')}
            >
              <Ionicons name="lock-closed" size={24} color="white" />
              <Text style={styles.controlButtonText}>Blocca</Text>
            </TouchableOpacity>

            <TouchableOpacity
              style={[styles.controlButton, styles.unlockButton]}
              onPress={() => sendCommand('unlock')}
            >
              <Ionicons name="lock-open" size={24} color="white" />
              <Text style={styles.controlButtonText}>Sblocca</Text>
            </TouchableOpacity>
          </View>

          <View style={styles.controlRow}>
            <TouchableOpacity
              style={[styles.controlButton, styles.lightButton]}
              onPress={() => sendCommand('light')}
            >
              <Ionicons name="bulb" size={24} color="white" />
              <Text style={styles.controlButtonText}>Luci</Text>
            </TouchableOpacity>

            <TouchableOpacity
              style={[styles.controlButton, styles.hornButton]}
              onPress={() => sendCommand('horn')}
            >
              <Ionicons name="volume-high" size={24} color="white" />
              <Text style={styles.controlButtonText}>Clacson</Text>
            </TouchableOpacity>
          </View>
        </View>

        {/* AI Assistant */}
        <View style={styles.aiContainer}>
          <Text style={styles.sectionTitle}>🤖 AI Assistant</Text>
          <TouchableOpacity
            style={styles.aiButton}
            onPress={() => Alert.alert('AI', 'Richiesta diagnostica in corso...')}
          >
            <Ionicons name="chatbubbles" size={24} color="white" />
            <Text style={styles.aiButtonText}>Chiedi a Pytho AI</Text>
          </TouchableOpacity>
        </View>

        {/* Loading overlay */}
        {loading && (
          <View style={styles.loadingOverlay}>
            <ActivityIndicator size="large" color="#4CAF50" />
            <Text style={styles.loadingText}>Caricamento...</Text>
          </View>
        )}
      </ScrollView>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#121212',
  },
  scrollView: {
    padding: 20,
    paddingBottom: 40,
  },
  header: {
    alignItems: 'center',
    marginBottom: 30,
  },
  title: {
    fontSize: 32,
    fontWeight: 'bold',
    color: '#4CAF50',
  },
  subtitle: {
    fontSize: 16,
    color: '#888',
    marginTop: 5,
  },
  statusBadge: {
    marginTop: 10,
    paddingHorizontal: 15,
    paddingVertical: 5,
    borderRadius: 20,
  },
  connected: {
    backgroundColor: '#1B5E20',
  },
  disconnected: {
    backgroundColor: '#B71C1C',
  },
  statusText: {
    color: 'white',
    fontWeight: 'bold',
  },
  connectButton: {
    backgroundColor: '#4CAF50',
    padding: 15,
    borderRadius: 10,
    alignItems: 'center',
    marginBottom: 20,
  },
  disconnectButton: {
    backgroundColor: '#f44336',
    padding: 15,
    borderRadius: 10,
    alignItems: 'center',
    marginBottom: 20,
  },
  buttonText: {
    color: 'white',
    fontSize: 18,
    fontWeight: 'bold',
  },
  dataContainer: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
    marginBottom: 20,
  },
  dataCard: {
    backgroundColor: '#1E1E1E',
    padding: 15,
    borderRadius: 10,
    width: '48%',
    marginBottom: 10,
    alignItems: 'center',
  },
  dataLabel: {
    color: '#888',
    fontSize: 14,
    marginTop: 5,
  },
  dataValue: {
    color: '#4CAF50',
    fontSize: 24,
    fontWeight: 'bold',
  },
  dataValueSmall: {
    color: '#4CAF50',
    fontSize: 14,
  },
  controlsContainer: {
    backgroundColor: '#1E1E1E',
    padding: 15,
    borderRadius: 10,
    marginBottom: 20,
  },
  sectionTitle: {
    color: 'white',
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 15,
  },
  controlRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 10,
  },
  controlButton: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 12,
    borderRadius: 8,
    marginHorizontal: 5,
  },
  lockButton: {
    backgroundColor: '#f44336',
  },
  unlockButton: {
    backgroundColor: '#4CAF50',
  },
  lightButton: {
    backgroundColor: '#FF9800',
  },
  hornButton: {
    backgroundColor: '#2196F3',
  },
  controlButtonText: {
    color: 'white',
    marginLeft: 8,
    fontWeight: 'bold',
  },
  aiContainer: {
    backgroundColor: '#1E1E1E',
    padding: 15,
    borderRadius: 10,
  },
  aiButton: {
    backgroundColor: '#9C27B0',
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 15,
    borderRadius: 8,
  },
  aiButtonText: {
    color: 'white',
    marginLeft: 10,
    fontSize: 16,
    fontWeight: 'bold',
  },
  loadingOverlay: {
    position: 'absolute',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    backgroundColor: 'rgba(0,0,0,0.7)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  loadingText: {
    color: 'white',
    marginTop: 10,
    fontSize: 16,
  },
});

export default App;
