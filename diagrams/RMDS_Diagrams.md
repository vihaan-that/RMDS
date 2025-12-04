# RMDS - Power Plant Monitoring System Diagrams

This document contains Mermaid diagram code for visualizing the RMDS architecture.

## 1. System Architecture Diagram

```mermaid
graph TB
    subgraph "Frontend - Next.js 13+"
        UI[Dashboard UI]
        Auth[Auth Context]
        Hooks[Custom Hooks<br/>useSensorData, useAssetData]
        Components[React Components]
    end

    subgraph "Backend - Express.js"
        API[API Routes]
        Controllers[Controllers]
        Middleware[Middleware Layer<br/>Auth, Validation, Error Handler]
        EventMgr[SensorEventManager<br/>SSE Broadcasting]
    end

    subgraph "Database - MongoDB"
        Assets[(Assets)]
        Sensors[(Sensors)]
        SensorValues[(SensorValues)]
        Incidents[(Incidents)]
        Users[(Users)]
        Roles[(Roles)]
    end

    UI --> Auth
    UI --> Hooks
    Hooks --> |REST API| API
    Hooks --> |SSE Stream| EventMgr
    Auth --> |JWT Token| API
    
    API --> Middleware
    Middleware --> Controllers
    Controllers --> Assets
    Controllers --> Sensors
    Controllers --> SensorValues
    Controllers --> Incidents
    Controllers --> Users
    
    EventMgr --> |Real-time Updates| Hooks
```

## 2. Data Flow Diagram - Real-time Sensor Streaming

```mermaid
sequenceDiagram
    participant Client as Next.js Frontend
    participant SSE as SSE Connection
    participant EventMgr as SensorEventManager
    participant Poller as Polling Service
    participant DB as MongoDB

    Client->>SSE: Connect to /api/live/sensor/:id
    SSE->>EventMgr: addClient(response, [sensorId])
    EventMgr-->>Client: Initial sensor value
    
    loop Every 1 second
        Poller->>DB: Query new SensorValues
        DB-->>Poller: New values since last poll
        Poller->>EventMgr: broadcastSensorData(sensorId, data)
        EventMgr-->>Client: SSE Event: sensor data
    end
    
    loop Every 30 seconds
        EventMgr-->>Client: Heartbeat ping
    end
    
    Client->>SSE: Connection close
    SSE->>EventMgr: removeClient(clientId)
```

## 3. Entity Relationship Diagram

```mermaid
erDiagram
    USER ||--o{ ROLE : has
    ASSET ||--|{ SENSOR : contains
    SENSOR ||--|{ SENSOR_VALUE : generates
    INCIDENT }|--|| ASSET : related_to
    
    USER {
        ObjectId _id PK
        string email UK
        string username UK
        string password
        string firstName
        string lastName
        ObjectId role FK
        timestamp createdAt
        timestamp updatedAt
    }
    
    ROLE {
        ObjectId _id PK
        string name UK
        array permissions
    }
    
    ASSET {
        ObjectId _id PK
        string projectName
        string assetName
        array sensors FK
        timestamp createdAt
    }
    
    SENSOR {
        ObjectId _id PK
        string tagName UK
        string tagDescription
        string unit
        timestamp createdAt
    }
    
    SENSOR_VALUE {
        ObjectId _id PK
        ObjectId sensor FK
        number value
        timestamp timestamp
    }
    
    INCIDENT {
        ObjectId _id PK
        string KpiId
        string Kpi
        date startDate
        date endDate
        string VariableName
        string Equipment
        string System
        enum Priority
        enum Severity
        string Owner
    }
```

## 4. Authentication Flow Diagram

```mermaid
flowchart TD
    A[User visits /login] --> B{Has valid token?}
    B -->|Yes| C[Redirect to /dashboard]
    B -->|No| D[Show login form]
    
    D --> E[User enters credentials]
    E --> F[POST /auth/login]
    F --> G{Valid credentials?}
    
    G -->|No| H[Show error toast]
    H --> D
    
    G -->|Yes| I[Server returns JWT token]
    I --> J[Store token in Cookie + localStorage]
    J --> K[Set user in AuthContext]
    K --> C
    
    C --> L[Protected Route Access]
    L --> M{Token valid?}
    M -->|Yes| N[Render dashboard]
    M -->|No| O[Redirect to /login]
    
    subgraph "Middleware Check"
        P[middleware.js] --> Q{Check cookie token}
        Q -->|Missing| O
        Q -->|Present| N
    end
```

## 5. Component Architecture Diagram

```mermaid
graph TD
    subgraph "Pages - App Router"
        Page[page.jsx - Landing]
        Login[login/page.jsx]
        Dashboard[dashboard/page.jsx]
        LiveData[live-data/page.jsx]
        AssetMon[asset-monitoring/page.jsx]
        Incidents[incidents/page.jsx]
        Reports[reports/page.jsx]
    end

    subgraph "Layout Components"
        RootLayout[layout.js]
        DashboardLayout[dashboard/layout.jsx]
        Sidebar[app-sidebar.jsx]
    end

    subgraph "Feature Components"
        LiveDataTable[live-data-table.jsx]
        PlantDataTable[plant-data-table.jsx]
        PlantInfo[plant-info.jsx]
        Breadcrumbs[dynamic-breadcrumbs.jsx]
    end

    subgraph "UI Components - shadcn/ui"
        Card[card.jsx]
        Table[table.jsx]
        Chart[chart.jsx]
        Dialog[dialog.jsx]
        Button[button.jsx]
        Select[select.jsx]
    end

    subgraph "Hooks & Context"
        AuthCtx[AuthContext]
        UseSensor[useSensorData]
        UseAsset[useAssetData]
        UseToast[useToast]
    end

    RootLayout --> DashboardLayout
    DashboardLayout --> Sidebar
    DashboardLayout --> Dashboard
    Dashboard --> LiveData
    Dashboard --> AssetMon
    
    LiveData --> LiveDataTable
    LiveDataTable --> UseSensor
    LiveDataTable --> Table
    LiveDataTable --> Chart
    
    UseSensor --> AuthCtx
```

## 6. API Routes Structure

```mermaid
graph LR
    subgraph "Public Routes"
        A1[GET /api/project-assets]
        A2[GET /api/live/sensor/:sensorId]
        A3[GET /api/live/asset/:assetId]
        A4[GET /api/sensor-values]
        A5[GET /api/sensor-stats]
    end

    subgraph "Auth Routes"
        B1[POST /auth/login]
        B2[GET /auth/profile]
    end

    subgraph "Protected Routes"
        C1[GET /api/incidents]
        C2[GET /api/asset-data]
    end

    subgraph "Middleware Pipeline"
        M1[validateRequest]
        M2[authenticate]
        M3[errorHandler]
    end

    A1 --> M1
    A2 --> M1 --> |SSE| EventMgr[SensorEventManager]
    A3 --> M1 --> |SSE| EventMgr
    
    C1 --> M2 --> M1
    C2 --> M2 --> M1
```

## 7. Deployment Architecture

```mermaid
graph TB
    subgraph "Client Layer"
        Browser[Web Browser]
    end

    subgraph "Frontend - Vercel/Netlify"
        NextJS[Next.js App<br/>Port 3000]
    end

    subgraph "Backend - Node Server"
        Express[Express.js Server<br/>Port 5000]
        SSE[SSE Endpoint]
    end

    subgraph "Database Layer"
        MongoDB[(MongoDB<br/>Atlas/Local)]
    end

    Browser --> |HTTPS| NextJS
    NextJS --> |REST API| Express
    NextJS --> |SSE Stream| SSE
    Express --> MongoDB
    SSE --> MongoDB

    style NextJS fill:#0070f3
    style Express fill:#68a063
    style MongoDB fill:#4db33d
```

## 8. Server-Sent Events (SSE) Architecture

```mermaid
graph TB
    subgraph "SensorEventManager"
        ClientMap[clients: Map<br/>clientId -> response, sensors]
        AddClient[addClient]
        RemoveClient[removeClient]
        SendToClient[sendToClient]
        Broadcast[broadcastSensorData]
    end

    subgraph "Polling Service"
        Interval[setInterval 1s]
        Query[Query new SensorValues]
        Group[Group by sensor]
    end

    subgraph "Connected Clients"
        C1[Client 1<br/>sensors: all]
        C2[Client 2<br/>sensors: sensor123]
        C3[Client 3<br/>sensors: sensor456]
    end

    Interval --> Query
    Query --> Group
    Group --> Broadcast
    
    Broadcast --> |Match sensors| C1
    Broadcast --> |Match sensors| C2
    Broadcast --> |Match sensors| C3
    
    AddClient --> ClientMap
    RemoveClient --> ClientMap
```

---

## How to Use These Diagrams

### Option 1: Mermaid Live Editor
1. Go to [Mermaid Live Editor](https://mermaid.live/)
2. Copy any diagram code block
3. Paste and export as PNG/SVG

### Option 2: VS Code Extension
1. Install "Markdown Preview Mermaid Support" extension
2. Open this file and preview

### Option 3: GitHub/GitLab
Both platforms render Mermaid diagrams natively in markdown files.

### Option 4: Generate with Python
```python
# Install: pip install mermaid-py
from mermaid import Mermaid

diagram_code = """
graph TB
    A[Start] --> B[End]
"""

mermaid = Mermaid(diagram_code)
mermaid.to_png("diagram.png")
```
