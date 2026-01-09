# Visualizing Data Flow Through the OSI Model

## Author
**Aadip Thapaliya**  
Matriculation Number: **92710466**

## Degree Program
BSc Digital Business & Data Science

## University
University of Europe for Applied Sciences

## Subject
IT Platform – Mini Project

## Presentation Link 
https://www.canva.com/design/DAG9cxbV-rc/4KYyi1jQ8d6-EPLUKK_jag/edit?utm_content=DAG9cxbV-rc&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
---
## Video link of Explanation 
##T
https://youtu.be/oXZ0KEVGwfY
## Project Overview

This project simulates and visualizes how data is processed, encapsulated,
transmitted, and received across all **seven layers of the OSI (Open Systems
Interconnection) model**.

The implementation follows a **clean, object-oriented architecture** where
each OSI layer is represented by its own Python class.  
The project demonstrates both:

- **Forward transmission** (Application → Physical)
- **Reverse transmission** (Physical → Application)

No real network communication is performed. All networking behavior is
**simulated for academic purposes only**.

---

## Objectives

- Understand the role and responsibility of each OSI layer
- Demonstrate encapsulation and decapsulation of data
- Simulate transport-layer reliability mechanisms
- Apply professional software engineering practices
- Provide clear, step-by-step visualization suitable for demonstrations

---

## Key Features

- Full OSI layer simulation (7 layers)
- Object-Oriented design (one class per layer)
- Application-layer protocol simulation (HTTP)
- Presentation-layer encryption and encoding
- Session management using unique session IDs
- Transport-layer segmentation (10-character segments)
- **Packet loss simulation and retransmission**
- Error detection using checksums (CRC32)
- Network-layer IP addressing (simulated)
- Data Link framing with MAC addresses (simulated)
- Physical-layer binary transmission
- Reverse flow with reassembly and message recovery
- Professional logging using Loguru
- Log file generation for debugging and reporting

---

## Project Structure

osi_simulator/
│
├── main.py
├── README.md
│
├── core/
│ ├── application.py
│ ├── presentation.py
│ ├── session.py
│ ├── transport.py
│ ├── network.py
│ ├── datalink.py
│ └── physical.py
│
├── models/
│ ├── transport_models.py
│ └── stats.py
│
└── utils/
├── logger.py
├── checksum.py
├── crypto.py
└── binary.py
