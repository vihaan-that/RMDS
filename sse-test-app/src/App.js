import React, { useState, useEffect } from "react";
import './App.css';

function App() {
  const [sensorData, setSensorData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    let intervalId;

    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:3001/api/sensor-data');
        const result = await response.json();
        
        if (result.data) {
          setSensorData(result.data);
          setError(null);
        }
      } catch (err) {
        console.error('Error fetching data:', err);
        setError('Failed to fetch sensor data');
      }
    };

    // Fetch immediately
    fetchData();

    // Then fetch every second
    intervalId = setInterval(fetchData, 1000);

    return () => {
      if (intervalId) {
        clearInterval(intervalId);
      }
    };
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-2xl mx-auto">
        <header className="mb-8">
          <h1 className="text-3xl font-bold text-gray-800">Live Sensor Data</h1>
          {error && (
            <div className="mt-2 text-sm text-red-600">
              Error: {error}
            </div>
          )}
        </header>

        {sensorData ? (
          <div className="bg-white rounded-lg shadow-lg p-6">
            <div className="grid grid-cols-2 gap-4">
              <div className="col-span-2">
                <div className="text-6xl font-bold text-gray-800 text-center">
                  {typeof sensorData.value === 'number' ? sensorData.value.toFixed(2) : sensorData.value}
                  <span className="text-2xl text-gray-500 ml-2">{sensorData.unit}</span>
                </div>
              </div>
              <div className="text-gray-600">
                <div className="text-sm font-semibold">Sensor ID</div>
                <div className="text-lg">{sensorData.sensorId}</div>
              </div>
              <div className="text-gray-600">
                <div className="text-sm font-semibold">Last Updated</div>
                <div className="text-lg">
                  {new Date(sensorData.timestamp).toLocaleTimeString()}
                </div>
              </div>
            </div>
          </div>
        ) : (
          <div className="bg-white rounded-lg shadow-lg p-6 text-center text-gray-500">
            Waiting for sensor data...
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
