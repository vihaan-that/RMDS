"""
RMDS - Power Plant Monitoring System Diagram Generator
Generates architecture diagrams using diagrams library (Python)

Install: pip install diagrams
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb
from diagrams.onprem.client import Users, Client
from diagrams.onprem.compute import Server
from diagrams.onprem.database import MongoDB
from diagrams.onprem.network import Nginx
from diagrams.programming.framework import React
from diagrams.programming.language import Nodejs
from diagrams.generic.storage import Storage
from diagrams.generic.network import Firewall

# Diagram 1: System Architecture
with Diagram("RMDS System Architecture", show=False, filename="rmds_architecture", direction="TB"):
    users = Users("Users")
    
    with Cluster("Frontend - Next.js 13+"):
        frontend = React("Next.js App")
        with Cluster("Components"):
            dashboard = Client("Dashboard")
            live_data = Client("Live Data")
            incidents = Client("Incidents")
    
    with Cluster("Backend - Express.js"):
        api = Nodejs("Express Server")
        with Cluster("Controllers"):
            sensor_ctrl = Server("Sensor Controller")
            asset_ctrl = Server("Asset Controller")
            incident_ctrl = Server("Incident Controller")
            live_ctrl = Server("Live Data Controller")
        
        sse = Server("SSE Manager")
    
    with Cluster("Database"):
        mongodb = MongoDB("MongoDB")
    
    users >> frontend
    frontend >> api
    frontend >> Edge(label="SSE", style="dashed") >> sse
    
    api >> sensor_ctrl
    api >> asset_ctrl
    api >> incident_ctrl
    api >> live_ctrl
    
    sensor_ctrl >> mongodb
    asset_ctrl >> mongodb
    incident_ctrl >> mongodb
    live_ctrl >> mongodb
    sse >> mongodb

# Diagram 2: Data Flow
with Diagram("RMDS Real-time Data Flow", show=False, filename="rmds_dataflow", direction="LR"):
    
    with Cluster("Data Sources"):
        sensors = Storage("Sensor Data")
    
    with Cluster("Backend Processing"):
        poller = Server("Polling Service\n(1s interval)")
        event_mgr = Server("SensorEventManager")
    
    with Cluster("Storage"):
        db = MongoDB("MongoDB\nSensorValues")
    
    with Cluster("Clients"):
        c1 = Client("Dashboard Client 1")
        c2 = Client("Dashboard Client 2")
        c3 = Client("Dashboard Client 3")
    
    sensors >> db
    db >> poller
    poller >> event_mgr
    event_mgr >> Edge(label="SSE") >> c1
    event_mgr >> Edge(label="SSE") >> c2
    event_mgr >> Edge(label="SSE") >> c3

# Diagram 3: Authentication Flow
with Diagram("RMDS Authentication Flow", show=False, filename="rmds_auth", direction="TB"):
    
    user = Users("User")
    
    with Cluster("Frontend"):
        login_page = Client("Login Page")
        auth_ctx = Storage("AuthContext")
        dashboard = Client("Dashboard")
    
    with Cluster("Backend"):
        auth_api = Nodejs("/auth/login")
        jwt = Firewall("JWT Token")
        middleware = Server("Auth Middleware")
    
    with Cluster("Database"):
        users_db = MongoDB("Users Collection")
    
    user >> login_page
    login_page >> auth_api
    auth_api >> users_db
    users_db >> auth_api
    auth_api >> jwt
    jwt >> auth_ctx
    auth_ctx >> dashboard
    dashboard >> middleware
    middleware >> jwt

print("Diagrams generated successfully!")
print("Output files: rmds_architecture.png, rmds_dataflow.png, rmds_auth.png")
