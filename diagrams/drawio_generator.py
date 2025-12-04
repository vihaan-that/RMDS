"""
RMDS - Draw.io/diagrams.net XML Generator
Generate professional diagrams for the Power Plant Monitoring System
Run this script to generate XML files that can be imported into draw.io
"""

import json

def create_drawio_xml():
    """Generate draw.io compatible XML for system architecture"""
    
    xml = '''<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net">
  <diagram name="RMDS Architecture" id="rmds-arch">
    <mxGraphModel dx="1422" dy="794" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1169" pageHeight="827" math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Title -->
        <mxCell id="title" value="&lt;b&gt;RMDS - Power Plant Monitoring System Architecture&lt;/b&gt;" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;fontSize=18;" vertex="1" parent="1">
          <mxGeometry x="350" y="20" width="450" height="30" as="geometry"/>
        </mxCell>
        
        <!-- Frontend Cluster -->
        <mxCell id="frontend-cluster" value="Frontend - Next.js 13+" style="swimlane;childLayout=stackLayout;horizontal=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="40" y="80" width="300" height="200" as="geometry"/>
        </mxCell>
        <mxCell id="dashboard" value="Dashboard UI" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="frontend-cluster">
          <mxGeometry x="20" y="40" width="120" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="authctx" value="AuthContext" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="frontend-cluster">
          <mxGeometry x="160" y="40" width="120" height="40" as="geometry"/>
        </mxCell>
        <mxCell id="hooks" value="Custom Hooks&#xa;useSensorData&#xa;useAssetData" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="frontend-cluster">
          <mxGeometry x="20" y="100" width="120" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="sseclient" value="SSE Client" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="frontend-cluster">
          <mxGeometry x="160" y="100" width="120" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Backend Cluster -->
        <mxCell id="backend-cluster" value="Backend - Express.js" style="swimlane;childLayout=stackLayout;horizontal=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="400" y="80" width="350" height="250" as="geometry"/>
        </mxCell>
        <mxCell id="routes" value="API Routes&#xa;/api/live/sensor, /api/sensor-values&#xa;/api/incidents, /auth/login" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;" vertex="1" parent="backend-cluster">
          <mxGeometry x="20" y="40" width="150" height="70" as="geometry"/>
        </mxCell>
        <mxCell id="middleware" value="Middleware&#xa;Auth | Validation&#xa;Error Handler" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;" vertex="1" parent="backend-cluster">
          <mxGeometry x="180" y="40" width="150" height="70" as="geometry"/>
        </mxCell>
        <mxCell id="controllers" value="Controllers&#xa;sensor | asset | incident&#xa;liveData | auth" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;" vertex="1" parent="backend-cluster">
          <mxGeometry x="20" y="130" width="150" height="70" as="geometry"/>
        </mxCell>
        <mxCell id="eventmgr" value="SensorEventManager&#xa;SSE Broadcasting&#xa;Polling Service" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;" vertex="1" parent="backend-cluster">
          <mxGeometry x="180" y="130" width="150" height="70" as="geometry"/>
        </mxCell>
        
        <!-- Database Cluster -->
        <mxCell id="db-cluster" value="Database - MongoDB" style="swimlane;childLayout=stackLayout;horizontal=1;fillColor=#ffe6cc;strokeColor=#d79b00;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="800" y="80" width="160" height="250" as="geometry"/>
        </mxCell>
        <mxCell id="assets-coll" value="Assets" style="shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#fff;strokeColor=#d79b00;" vertex="1" parent="db-cluster">
          <mxGeometry x="10" y="40" width="60" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="sensors-coll" value="Sensors" style="shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#fff;strokeColor=#d79b00;" vertex="1" parent="db-cluster">
          <mxGeometry x="90" y="40" width="60" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="sensorvals-coll" value="SensorValues" style="shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#fff;strokeColor=#d79b00;" vertex="1" parent="db-cluster">
          <mxGeometry x="10" y="110" width="60" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="incidents-coll" value="Incidents" style="shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#fff;strokeColor=#d79b00;" vertex="1" parent="db-cluster">
          <mxGeometry x="90" y="110" width="60" height="50" as="geometry"/>
        </mxCell>
        <mxCell id="users-coll" value="Users/Roles" style="shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#fff;strokeColor=#d79b00;" vertex="1" parent="db-cluster">
          <mxGeometry x="50" y="180" width="60" height="50" as="geometry"/>
        </mxCell>
        
        <!-- Connections -->
        <mxCell id="conn1" value="REST API" style="endArrow=classic;html=1;exitX=1;exitY=0.5;entryX=0;entryY=0.5;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="340" y="180" as="sourcePoint"/>
            <mxPoint x="400" y="180" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        <mxCell id="conn2" value="SSE Stream" style="endArrow=classic;html=1;dashed=1;exitX=1;exitY=0.5;entryX=0;entryY=0.5;strokeColor=#b85450;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="340" y="220" as="sourcePoint"/>
            <mxPoint x="580" y="220" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        <mxCell id="conn3" value="" style="endArrow=classic;html=1;exitX=1;exitY=0.5;entryX=0;entryY=0.5;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="750" y="200" as="sourcePoint"/>
            <mxPoint x="800" y="200" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        
        <!-- Legend -->
        <mxCell id="legend" value="Legend:&#xa;→ REST API Request&#xa;⇢ SSE Real-time Stream" style="text;html=1;strokeColor=#666666;fillColor=#f5f5f5;align=left;verticalAlign=top;fontSize=10;fontColor=#333333;rounded=1;" vertex="1" parent="1">
          <mxGeometry x="40" y="350" width="150" height="60" as="geometry"/>
        </mxCell>
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    
    return xml


def create_data_flow_xml():
    """Generate draw.io XML for data flow diagram"""
    
    xml = '''<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net">
  <diagram name="RMDS Data Flow" id="rmds-dataflow">
    <mxGraphModel dx="1422" dy="794" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1169" pageHeight="827">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Title -->
        <mxCell id="title" value="&lt;b&gt;RMDS Real-time Sensor Data Flow&lt;/b&gt;" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;fontSize=16;" vertex="1" parent="1">
          <mxGeometry x="400" y="20" width="350" height="30" as="geometry"/>
        </mxCell>
        
        <!-- User -->
        <mxCell id="user" value="User" style="shape=actor;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="80" y="100" width="40" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Frontend -->
        <mxCell id="frontend" value="Next.js&#xa;Dashboard" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="200" y="100" width="100" height="60" as="geometry"/>
        </mxCell>
        
        <!-- SSE Connection -->
        <mxCell id="sse" value="SSE&#xa;Connection" style="ellipse;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="380" y="100" width="80" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Event Manager -->
        <mxCell id="eventmgr" value="Sensor&#xa;Event&#xa;Manager" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;" vertex="1" parent="1">
          <mxGeometry x="540" y="100" width="100" height="60" as="geometry"/>
        </mxCell>
        
        <!-- Polling Service -->
        <mxCell id="poller" value="Polling Service&#xa;(1s interval)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="540" y="220" width="100" height="60" as="geometry"/>
        </mxCell>
        
        <!-- MongoDB -->
        <mxCell id="mongodb" value="MongoDB&#xa;SensorValues" style="shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1">
          <mxGeometry x="720" y="150" width="80" height="80" as="geometry"/>
        </mxCell>
        
        <!-- Flow arrows -->
        <mxCell id="arr1" value="1. Open page" style="endArrow=classic;html=1;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="120" y="130" as="sourcePoint"/>
            <mxPoint x="200" y="130" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        
        <mxCell id="arr2" value="2. Connect SSE" style="endArrow=classic;html=1;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="300" y="130" as="sourcePoint"/>
            <mxPoint x="380" y="130" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        
        <mxCell id="arr3" value="3. Register client" style="endArrow=classic;html=1;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="460" y="130" as="sourcePoint"/>
            <mxPoint x="540" y="130" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        
        <mxCell id="arr4" value="4. Poll DB" style="endArrow=classic;html=1;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="640" y="250" as="sourcePoint"/>
            <mxPoint x="720" y="210" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        
        <mxCell id="arr5" value="5. New values" style="endArrow=classic;html=1;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="720" y="170" as="sourcePoint"/>
            <mxPoint x="640" y="130" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        
        <mxCell id="arr6" value="6. Broadcast" style="endArrow=classic;html=1;dashed=1;strokeColor=#b85450;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="540" y="110" as="sourcePoint"/>
            <mxPoint x="300" y="110" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        
        <!-- Info box -->
        <mxCell id="info" value="Real-time Flow:&#xa;1. User opens live data page&#xa;2. Frontend establishes SSE connection&#xa;3. EventManager registers client&#xa;4. Polling service queries DB every 1s&#xa;5. New sensor values returned&#xa;6. Data broadcast to all connected clients" style="text;html=1;strokeColor=#82b366;fillColor=#d5e8d4;align=left;verticalAlign=top;fontSize=10;rounded=1;" vertex="1" parent="1">
          <mxGeometry x="200" y="320" width="250" height="120" as="geometry"/>
        </mxCell>
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    
    return xml


if __name__ == "__main__":
    # Generate architecture diagram
    arch_xml = create_drawio_xml()
    with open("rmds_architecture.drawio", "w") as f:
        f.write(arch_xml)
    
    # Generate data flow diagram
    flow_xml = create_data_flow_xml()
    with open("rmds_dataflow.drawio", "w") as f:
        f.write(flow_xml)
    
    print("Draw.io diagrams generated successfully!")
    print("Files created:")
    print("  - rmds_architecture.drawio")
    print("  - rmds_dataflow.drawio")
    print("\nOpen these files at https://app.diagrams.net/ or in VS Code with Draw.io extension")
