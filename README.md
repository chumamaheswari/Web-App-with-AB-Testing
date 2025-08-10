# Flask A/B Testing Web App

## Overview
This project implements a simple Flask-based web application with:
- Intro page → login page → randomly assigned Home Version A or B
- A/B testing logic with session "stickiness"
- Click tracking for buttons on each version
- Metrics stored in `metrics.csv` (Username, Version, IP, Timestamp)
- `/metrics` page to view captured interactions

---

## Requirements
- Python 3.8+ installed
- Visual Studio 2022 with Python workload OR any IDE with Python support
- Internet browser for testing

---

## Setup Instructions

1. **Clone or download this project**  
   - If downloading as ZIP, extract to a known folder.
   - If cloning via Git:  
     ```bash
     git clone https://github.com/<chumamaheswari>/<repo-name>.git
     ```

2. **Open the folder in Visual Studio 2022**  
   - Go to **File → Open → Folder...** and select the project folder.

3. **Create and activate a virtual environment**  
   In the Visual Studio Terminal (PowerShell):
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate
4. **open Your Browser at**
   ```Browser
   http://127.0.0.1:5000
   ```
