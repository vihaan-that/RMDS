# RMDS Diagram Generation

This folder contains code to generate various architecture diagrams for the RMDS Power Plant Monitoring System.

## Files

| File | Description | Output Format |
|------|-------------|---------------|
| `RMDS_Diagrams.md` | Mermaid diagram code | Markdown/SVG/PNG |
| `generate_diagrams.py` | Python diagrams library | PNG images |
| `plantuml_diagrams.py` | PlantUML definitions | PNG/SVG via PlantUML |
| `drawio_generator.py` | Draw.io XML generator | .drawio files |

## Quick Start

### Option 1: Mermaid (Easiest - No Installation)
1. Open `RMDS_Diagrams.md`
2. Copy any diagram code block
3. Paste at [Mermaid Live Editor](https://mermaid.live/)
4. Export as PNG/SVG

### Option 2: Python Diagrams Library
```bash
pip install diagrams
python generate_diagrams.py
# Output: rmds_architecture.png, rmds_dataflow.png, rmds_auth.png
```

### Option 3: PlantUML
```bash
# Install PlantUML
brew install plantuml  # macOS
# or download from https://plantuml.com/

# Run the script to see diagram definitions
python plantuml_diagrams.py

# Copy output to https://www.plantuml.com/plantuml/uml/
```

### Option 4: Draw.io
```bash
python drawio_generator.py
# Open .drawio files at https://app.diagrams.net/
```

## Available Diagrams

1. **System Architecture** - High-level view of Frontend, Backend, Database
2. **Data Flow (SSE)** - Real-time sensor data streaming flow
3. **Entity Relationship** - Database schema and relationships
4. **Authentication Flow** - JWT-based auth process
5. **Component Architecture** - Frontend component hierarchy
6. **API Routes Structure** - Backend endpoint organization
7. **Deployment Architecture** - Infrastructure layout

## Recommended Tools

- **VS Code Extensions:**
  - Markdown Preview Mermaid Support
  - Draw.io Integration
  - PlantUML

- **Online Tools:**
  - [Mermaid Live](https://mermaid.live/)
  - [Draw.io](https://app.diagrams.net/)
  - [PlantUML Server](https://www.plantuml.com/plantuml/)
