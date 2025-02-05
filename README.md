# Power Plant Monitoring System

A real-time monitoring system for power plant assets and sensors, featuring a modern Next.js frontend and Express.js backend.

## Features

- Real-time asset monitoring with SSE (Server-Sent Events)
- Interactive dashboard for asset visualization
- Authentication and authorization
- Sensor data management and tracking
- Project and asset organization
- Responsive modern UI built with Next.js 13+

## Prerequisites

- Node.js (v16 or higher)
- MongoDB
- npm or yarn package manager

## Project Structure

```
PowerPlant_human/
├── RMDS-Backend/         # Express.js backend
├── RMDS-FrontEnd/       # Next.js frontend
```

## Installation

1. Clone the repository:
```bash
git clone --recursive [repository-url]
cd PowerPlant_human
```

2. Install Backend Dependencies:
```bash
cd RMDS-Backend
npm install
```

3. Install Frontend Dependencies:
```bash
cd ../RMDS-FrontEnd
npm install
```

4. Set up environment variables:

For Backend (create `.env` in RMDS-Backend directory):
```

PORT=4000
NODE_ENV=development

# MongoDB Configuration
MONGODB_URI=mongodb://localhost:27017/powerplant

# JWT Configuration
JWT_SECRET=your_jwt_secret_here
JWT_EXPIRE=24h

# Admin Configuration
ADMIN_EMAIL=admin@example.com
ADMIN_PASSWORD=SecureAdminPassword123

# Logging Configuration
LOG_LEVEL=debug

# CORS Configuration (optional)
# CORS_ORIGIN=http://localhost:3000

```

For Frontend (create `.env.local` in RMDS-FrontEnd directory):
```
NEXT_PUBLIC_API_URL=http://localhost:4000
NEXT_PUBLIC_WS_URL=ws://localhost:4000

```

## Running the Application

1. Start the Backend Server:
```bash
cd RMDS-Backend
npm start
```
The backend server will start on port 3001 (or as configured in .env)

2. Start the Frontend Development Server:
```bash
cd RMDS-FrontEnd
npm run dev
```
The frontend will be available at `http://localhost:3000`

## Development

- Backend API routes are in `RMDS-Backend/routes/`
- Frontend pages are in `RMDS-FrontEnd/src/app/`
- Authentication middleware is in `RMDS-Backend/middleware/`
- Real-time sensor management is handled by `RMDS-Backend/utils/SensorEventManager.js`

## Technologies Used

- **Frontend:**
  - Next.js 13+
  - React
  - Radix UI Components
  - TailwindCSS

- **Backend:**
  - Express.js
  - MongoDB with Mongoose
  - JWT Authentication
  - Server-Sent Events (SSE)

## License

[Your License Here]
