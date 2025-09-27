#!/usr/bin/env python3
import psutil
import datetime

# Thresholds
CPU_THRESHOLD = 80       # %
MEM_THRESHOLD = 80       # %
DISK_THRESHOLD = 90      # %

def check_system_health():
    alerts = []

    # CPU Usage
    cpu = psutil.cpu_percent(interval=1)
    if cpu > CPU_THRESHOLD:
        alerts.append(f"High CPU usage: {cpu}%")

    # Memory Usage
    mem = psutil.virtual_memory()
    if mem.percent > MEM_THRESHOLD:
        alerts.append(f"High Memory usage: {mem.percent}%")

    # Disk Usage
    disk = psutil.disk_usage('/')
    if disk.percent > DISK_THRESHOLD:
        alerts.append(f"High Disk usage: {disk.percent}%")

    # Running processes count
    processes = len(psutil.pids())
    alerts.append(f"Running processes: {processes}")

    # Log alerts
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if alerts:
        print(f"[{now}] ALERTS:")
        for alert in alerts:
            print(f"  - {alert}")
    else:
        print(f"[{now}] System is healthy.")

if __name__ == "__main__":
    check_system_health()
