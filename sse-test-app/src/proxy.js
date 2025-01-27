const express = require('express');
const { spawn } = require('child_process');
const cors = require('cors');

const app = express();
app.use(cors());

// Cache for the latest sensor data
let sensorDataCache = null;

// Function to start curl and handle the data stream
function startCurlStream(sensorId) {
    const curl = spawn('curl', ['-N', `http://localhost:4000/api/live/sensor/${sensorId}`]);
    
    curl.stdout.on('data', (data) => {
        const lines = data.toString().split('\n');
        
        for (let line of lines) {
            if (line.startsWith('data: ')) {
                const dataContent = line.substring(6);
                if (dataContent !== ':ok' && dataContent !== ':ping') {
                    try {
                        sensorDataCache = JSON.parse(dataContent);
                        console.log('Updated cache:', sensorDataCache);
                    } catch (err) {
                        console.error('Error parsing data:', err);
                    }
                }
            }
        }
    });

    curl.stderr.on('data', (data) => {
        console.error(`curl error: ${data}`);
    });

    curl.on('close', (code) => {
        console.log(`curl process exited with code ${code}`);
        // Restart the curl process after a delay
        setTimeout(() => startCurlStream(sensorId), 5000);
    });

    return curl;
}

// Start the curl stream
const sensorId = "678a263e813f95d91777a309";
let curlProcess = startCurlStream(sensorId);

// Endpoint to get the latest cached data
app.get('/api/sensor-data', (req, res) => {
    res.json({
        timestamp: Date.now(),
        data: sensorDataCache
    });
});

const PORT = 3001;
app.listen(PORT, () => {
    console.log(`Proxy server running on port ${PORT}`);
});

// Handle process termination
process.on('SIGINT', () => {
    if (curlProcess) {
        curlProcess.kill();
    }
    process.exit();
});
