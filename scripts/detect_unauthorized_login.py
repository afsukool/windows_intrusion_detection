# scripts/detect_unauthorized_login.py
```python
import os
import re

def analyze_logs(log_path):
    if not os.path.exists(log_path):
        print(f"Log file not found: {log_path}")
        return

    with open(log_path, 'r') as log_file:
        logs = log_file.readlines()

    unauthorized_attempts = [line for line in logs if "Failed login" in line]

    if unauthorized_attempts:
        print("Unauthorized login attempts detected:")
        for attempt in unauthorized_attempts:
            print(attempt.strip())
    else:
        print("No unauthorized login attempts found.")

if __name__ == "__main__":
    log_path = input("Enter the path to the system logs: ")
    analyze_logs(log_path)
```
