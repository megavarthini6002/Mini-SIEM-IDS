# Mini SIEM Integrated with Intrusion Detection System (IDS)

## About the Project
This project implements a basic Security Information and Event Management (SIEM) system integrated with an Intrusion Detection System (IDS) using Python.

It monitors security logs and detects suspicious activities such as repeated failed login attempts.

## Features
- Security log monitoring
- Failed login attempt detection
- IP address-based tracking
- Rule-based intrusion detection
- Automatic alert generation
- Alert storage in a separate file

## Technologies Used
- Python
- File Handling
- Collections Module
- Time Module

## Working Process
1. Reads security events from a log file.
2. Analyzes login activities.
3. Tracks failed login attempts by IP address.
4. Generates an alert after three or more failed attempts.
5. Resets the counter after a successful login.

## How to Run

1. Install Python 3.
2. Keep `main.py` and `logs.txt` in the same folder.
3. Open the terminal in the project folder.
4. Execute:

```bash
python main.py
```

## Project Type
Academic Cybersecurity Project

## Disclaimer
This is an educational prototype demonstrating basic SIEM and IDS concepts.