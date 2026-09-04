import psutil
import time

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()
disk = psutil.disk_usage("/")

print("╔══════════════════════════════════════╗")
print("║        PULSEFIX SYSTEM HEALTH        ║")
print("╚══════════════════════════════════════╝")

print(f"CPU Usage    : {cpu}%")
print(f"Memory Usage : {memory.percent}%")
print(f"Disk Usage   : {disk.percent}%")

if cpu > 80 or memory.percent > 80 or disk.percent > 90:
    print("Status      : WARNING")
else:
    print("Status      : HEALTHY")


processes = []

# Take the first CPU measurement
for process in psutil.process_iter(
    ["pid", "name", "memory_percent", "status"]
):
    try:
        process.cpu_percent(None)
        processes.append(process)
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass

# Wait so psutil can measure CPU activity
time.sleep(1)

# Take the second measurement
process_data = []

for process in processes:
    try:
        cpu = process.cpu_percent(None)

        if process.name() == "System Idle Process":
            continue

        process_data.append({
            "pid": process.pid,
            "name": process.name(),
            "cpu_percent": cpu,
            "memory_percent": process.memory_percent(),
            "status": process.status()
        })

    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass

# Sort by CPU usage
process_data.sort(
    key=lambda process: process["cpu_percent"],
    reverse=True
)

print("\nTop 3 CPU-Consuming Processes:")

for process in process_data[:3]:
    print(
        f"{process['pid']} | "
        f"{process['name']} | "
        f"CPU: {process['cpu_percent']:.2f}% | "
        f"Memory: {process['memory_percent']:.2f}% | "
        f"Status: {process['status']}"
    ) 

