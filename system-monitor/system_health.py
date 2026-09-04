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

findings = []
severity = []

if cpu > 90:
    findings.append("CPU usage is critically high")
    severity.append("CRITICAL")

elif cpu > 80:
    findings.append("CPU usage is above 80%")
    severity.append("HIGH")

if memory.percent > 90:
    findings.append("Memory usage is critically high")
    severity.append("CRITICAL")

elif memory.percent > 80:
    findings.append("Memory usage is above 80%")
    severity.append("HIGH")

if disk.percent > 95:
    findings.append("Disk usage is critically high")
    severity.append("CRITICAL")

elif disk.percent > 90:
    findings.append("Disk usage is above 90%")
    severity.append("HIGH")

if "CRITICAL" in severity:
    overall_severity = "CRITICAL"

elif "HIGH" in severity:
    overall_severity = "HIGH"

else:
    overall_severity = "NORMAL"

if findings:
    print(f"Status      : WARNING ({overall_severity})")
else:
    print("Status      : HEALTHY")


if findings:
    print("\n⚠ Diagnostic Findings:")

    for finding in findings:
        print(f"- {finding}")
else:
    print("\n✓ No resource threshold violations detected.")

print("\nRecommended Investigation:")

if memory.percent > 80:
    print("- Investigate memory-consuming processes")

if cpu > 80:
    print("- Investigate CPU-consuming processes")

if disk.percent > 90:
    print("- Investigate disk usage and available space")

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
process_findings = []

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

        if cpu > 80:
            process_findings.append({
                "pid": process.pid,
                "name": process.name(),
                "issue": "High CPU usage",
                "severity": "CRITICAL"
            })

        elif cpu > 50:
            process_findings.append({
                "pid": process.pid,
                "name": process.name(),
                "issue": "Elevated CPU usage",
                "severity": "HIGH"
            })

        if process.memory_percent() > 10:
            process_findings.append({
                "pid": process.pid,
                "name": process.name(),
                "issue": "Critical memory usage",
                "severity": "CRITICAL"
            })

        elif process.memory_percent() > 5:
            process_findings.append({
                "pid": process.pid,
                "name": process.name(),
                "issue": "High memory usage",
                "severity": "HIGH"
            })

    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass

# Sort by CPU usage
process_data.sort(
    key=lambda process: process["cpu_percent"],
    reverse=True
)

memory_processes = sorted(
    process_data,
    key=lambda process: process["memory_percent"],
    reverse=True
)

print("\nTop 3 Memory-Consuming Processes:")

for process in memory_processes[:3]:
    print(
        f"{process['pid']} | "
        f"{process['name']} | "
        f"CPU: {process['cpu_percent']:.2f}% | "
        f"Memory: {process['memory_percent']:.2f}% | "
        f"Status: {process['status']}"
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

print("\nProcess Risk Findings:")

if process_findings:

    for finding in process_findings:
        print(
            f"{finding['pid']} | "
            f"{finding['name']} | "
            f"{finding['issue']} | "
            f"Severity: {finding['severity']}"
        )

else:
    print("✓ No process-level resource risks detected.")
