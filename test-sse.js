import fetch from 'node-fetch';
import EventSource from 'eventsource';

// Function to connect to a sensor's SSE stream
function connectToSensor(sensorId, sensorName) {
    return new Promise((resolve) => {
        console.log(`Connecting to sensor ${sensorName} (${sensorId})...`);
        
        const eventSource = new EventSource(`http://localhost:4000/api/live/sensor/${sensorId}`);

        eventSource.onopen = () => {
            console.log(`Connected to sensor ${sensorName}`);
        };

        eventSource.onmessage = (event) => {
            try {
                const data = JSON.parse(event.data);
                console.log(`[${new Date().toISOString()}] ${sensorName}:`, {
                    value: data.value,
                    timestamp: data.timestamp,
                    unit: data.unit
                });
            } catch (e) {
                if (event.data !== ':ok' && event.data !== ':ping') {
                    console.error(`Error parsing data for ${sensorName}:`, e);
                }
            }
        };

        eventSource.onerror = (error) => {
            if (error.status === 404) {
                console.error(`Sensor ${sensorName} not found`);
                eventSource.close();
                resolve();
            } else if (error.message) {
                console.error(`Error with sensor ${sensorName}:`, error.message);
            } else {
                console.error(`Error with sensor ${sensorName}:`, error);
            }
        };

        // Close the connection after 30 seconds
        setTimeout(() => {
            console.log(`Closing connection to ${sensorName}`);
            eventSource.close();
            resolve();
        }, 30000);
    });
}

// First, fetch the list of sensors
async function main() {
    try {
        console.log('Fetching project assets...');
        const response = await fetch('http://localhost:4000/api/project-assets');
        const data = await response.json();
        
        const sensors = data.project.assets.reduce((acc, asset) => {
            return [...acc, ...asset.sensors.map(sensor => ({
                id: sensor._id,
                name: sensor.tagName,
                unit: sensor.unit
            }))];
        }, []);

        console.log('Found sensors:', sensors);

        // Connect to each sensor
        const promises = sensors.map(sensor => connectToSensor(sensor.id, sensor.name));
        
        // Wait for all connections
        await Promise.all(promises);
        console.log('All connections closed');

    } catch (error) {
        console.error('Error:', error);
    }
}

// Handle script termination
process.on('SIGINT', () => {
    console.log('\nClosing connections...');
    process.exit();
});

main();
