import time
from collections import defaultdict

LOG_FILE = "logs.txt"
ALERT_FILE = "alerts.txt"

# Store failed login count
failed_attempts = defaultdict(int)

# Track last read position
last_position = 0

def analyze_logs():
    global last_position

    with open(LOG_FILE, "r") as file:
        file.seek(last_position)
        new_logs = file.readlines()
        last_position = file.tell()

    for log in new_logs:
        parts = log.strip().split("|")

        if len(parts) != 3:
            continue

        timestamp = parts[0].strip()
        ip = parts[1].strip()
        activity = parts[2].strip()

        print(f"Analyzing: {timestamp} | {ip} | {activity}")

        if activity == "FAILED LOGIN":
            failed_attempts[ip] += 1

            if failed_attempts[ip] >= 3:
                generate_alert(ip, timestamp)

        elif activity == "SUCCESSFUL LOGIN":
            failed_attempts[ip] = 0


def generate_alert(ip, timestamp):

    alert = f"ALERT: Suspicious activity from IP {ip} at {timestamp}\n"

    print(alert)

    with open(ALERT_FILE, "a") as file:
        file.write(alert)


def monitor():
    print("Mini SIEM with IDS Started...")
    print("Monitoring logs...\n")

    while True:
        analyze_logs()
        time.sleep(2)


if __name__ == "__main__":
    monitor()