import psutil

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

for process in psutil.process_iter(["name", "memory_percent"]):
    processes.append(process.info)

processes.sort(key=lambda process: process["memory_percent"], reverse=True)

print("\nTop 3 Memory-Consuming Processes:")

for process in processes[:3]:
    print(f"{process['name']} : {process['memory_percent']:.2f}%")