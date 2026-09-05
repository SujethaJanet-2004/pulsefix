
import psutil
import time
from datetime import datetime
from pathlib import Path


# Create snapshot directory
snapshot_dir = Path("snapshots")
snapshot_dir.mkdir(exist_ok=True)

# Generate timestamp
timestamp = datetime.now()
formatted_time = timestamp.strftime("%Y-%m-%d %H:%M:%S")
file_timestamp = timestamp.strftime("%Y-%m-%d_%H%M%S")


# System health measurements
cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()
disk = psutil.disk_usage("/")


print("╔══════════════════════════════════════╗")
print("║        PULSEFIX SYSTEM HEALTH        ║")
print("╚══════════════════════════════════════╝")

print(f"Timestamp    : {formatted_time}")
print(f"CPU Usage    : {cpu}%")
print(f"Memory Usage : {memory.percent}%")
print(f"Disk Usage   : {disk.percent}%")


# Store diagnostic findings
findings = []
severity = []


# System-level CPU detection
if cpu > 90:
    findings.append("CPU usage is critically high")
    severity.append("CRITICAL")

elif cpu > 80:
    findings.append("CPU usage is above 80%")
    severity.append("HIGH")


# System-level memory detection
if memory.percent > 90:
    findings.append("Memory usage is critically high")
    severity.append("CRITICAL")

elif memory.percent > 80:
    findings.append("Memory usage is above 80%")
    severity.append("HIGH")


# System-level disk detection
if disk.percent > 95:
    findings.append("Disk usage is critically high")
    severity.append("CRITICAL")

elif disk.percent > 90:
    findings.append("Disk usage is above 90%")
    severity.append("HIGH")


# Determine overall severity
if "CRITICAL" in severity:
    overall_severity = "CRITICAL"

elif "HIGH" in severity:
    overall_severity = "HIGH"

else:
    overall_severity = "NORMAL"


# Determine system status
if findings:
    system_status = f"WARNING ({overall_severity})"
    print(f"Status       : {system_status}")

else:
    system_status = "HEALTHY"
    print(f"Status       : {system_status}")


# Diagnostic findings
print("\n⚠ Diagnostic Findings:")

if findings:

    for finding in findings:
        print(f"- {finding}")

else:
    print("✓ No resource threshold violations detected.")


# Recommended investigations
recommendations = []

if memory.percent > 80:
    recommendations.append(
        "Investigate memory-consuming processes"
    )

if cpu > 80:
    recommendations.append(
        "Investigate CPU-consuming processes"
    )

if disk.percent > 90:
    recommendations.append(
        "Investigate disk usage and available space"
    )


print("\nRecommended Investigation:")

if recommendations:

    for recommendation in recommendations:
        print(f"- {recommendation}")

else:
    print("- No additional investigation recommended.")


# Process collection
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
        process_cpu = process.cpu_percent(None)
        process_memory = process.memory_percent()

        if process.name() == "System Idle Process":
            continue

        process_data.append({
            "pid": process.pid,
            "name": process.name(),
            "cpu_percent": process_cpu,
            "memory_percent": process_memory,
            "status": process.status()
        })


        # Process-level CPU risk detection
        if process_cpu > 80:

            process_findings.append({
                "pid": process.pid,
                "name": process.name(),
                "issue": "High CPU usage",
                "severity": "CRITICAL"
            })

        elif process_cpu > 50:

            process_findings.append({
                "pid": process.pid,
                "name": process.name(),
                "issue": "Elevated CPU usage",
                "severity": "HIGH"
            })


        # Process-level memory risk detection
        if process_memory > 10:

            process_findings.append({
                "pid": process.pid,
                "name": process.name(),
                "issue": "Critical memory usage",
                "severity": "CRITICAL"
            })

        elif process_memory > 5:

            process_findings.append({
                "pid": process.pid,
                "name": process.name(),
                "issue": "High memory usage",
                "severity": "HIGH"
            })


    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass


# Sort processes by CPU usage
process_data.sort(
    key=lambda process: process["cpu_percent"],
    reverse=True
)


# Sort processes by memory usage
memory_processes = sorted(
    process_data,
    key=lambda process: process["memory_percent"],
    reverse=True
)


# Display top memory-consuming processes
print("\nTop 3 Memory-Consuming Processes:")

for process in memory_processes[:3]:

    print(
        f"{process['pid']} | "
        f"{process['name']} | "
        f"CPU: {process['cpu_percent']:.2f}% | "
        f"Memory: {process['memory_percent']:.2f}% | "
        f"Status: {process['status']}"
    )


# Display top CPU-consuming processes
print("\nTop 3 CPU-Consuming Processes:")

for process in process_data[:3]:

    print(
        f"{process['pid']} | "
        f"{process['name']} | "
        f"CPU: {process['cpu_percent']:.2f}% | "
        f"Memory: {process['memory_percent']:.2f}% | "
        f"Status: {process['status']}"
    )


# Display process risk findings
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


# ==========================================================
# CREATE DIAGNOSTIC SNAPSHOT
# ==========================================================

snapshot = []

snapshot.append("PULSEFIX DIAGNOSTIC SNAPSHOT")
snapshot.append("=" * 40)
snapshot.append(f"Timestamp: {formatted_time}")
snapshot.append("")

snapshot.append("SYSTEM HEALTH")
snapshot.append(f"CPU Usage: {cpu}%")
snapshot.append(f"Memory Usage: {memory.percent}%")
snapshot.append(f"Disk Usage: {disk.percent}%")
snapshot.append(f"System Status: {system_status}")
snapshot.append("")


snapshot.append("DIAGNOSTIC FINDINGS")

if findings:

    for finding in findings:
        snapshot.append(f"- {finding}")

else:

    snapshot.append("- No resource threshold violations detected.")

snapshot.append("")


snapshot.append("RECOMMENDED INVESTIGATION")

if recommendations:

    for recommendation in recommendations:
        snapshot.append(f"- {recommendation}")

else:

    snapshot.append("- No additional investigation recommended.")

snapshot.append("")


snapshot.append("TOP 3 MEMORY-CONSUMING PROCESSES")

for process in memory_processes[:3]:

    snapshot.append(
        f"{process['pid']} | "
        f"{process['name']} | "
        f"CPU: {process['cpu_percent']:.2f}% | "
        f"Memory: {process['memory_percent']:.2f}% | "
        f"Status: {process['status']}"
    )

snapshot.append("")


snapshot.append("TOP 3 CPU-CONSUMING PROCESSES")

for process in process_data[:3]:

    snapshot.append(
        f"{process['pid']} | "
        f"{process['name']} | "
        f"CPU: {process['cpu_percent']:.2f}% | "
        f"Memory: {process['memory_percent']:.2f}% | "
        f"Status: {process['status']}"
    )

snapshot.append("")


snapshot.append("PROCESS RISK FINDINGS")

if process_findings:

    for finding in process_findings:

        snapshot.append(
            f"{finding['pid']} | "
            f"{finding['name']} | "
            f"{finding['issue']} | "
            f"Severity: {finding['severity']}"
        )

else:

    snapshot.append("- No process-level resource risks detected.")


# Create snapshot file
snapshot_file = (
    snapshot_dir / f"snapshot_{file_timestamp}.txt"
)


with snapshot_file.open(
    "w",
    encoding="utf-8"
) as file:

    file.write("\n".join(snapshot))


print(
    f"\n✓ Diagnostic snapshot saved to: {snapshot_file}"
)
