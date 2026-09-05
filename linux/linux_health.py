import os
import platform
import shutil
import subprocess


print("╔══════════════════════════════════════╗")
print("║       PULSEFIX LINUX DIAGNOSTICS    ║")
print("╚══════════════════════════════════════╝")


# OS / Kernel Information
print("\n[OS INFORMATION]")

print(f"Operating System : {platform.system()}")
print(f"Kernel Release   : {platform.release()}")
print(f"Architecture     : {platform.machine()}")


# CPU Information
print("\n[CPU INFORMATION]")

cpu_cores = os.cpu_count()

print(f"CPU Cores        : {cpu_cores}")


# Memory Information
print("\n[MEMORY INFORMATION]")

memory = subprocess.check_output(
    ["free", "-b"],
    text=True
)

memory_line = next(
    line for line in memory.splitlines()
    if line.startswith("Mem:")
)

memory_values = memory_line.split()

total_memory = int(memory_values[1])
used_memory = int(memory_values[2])

memory_usage = (used_memory / total_memory) * 100

print(f"Memory Usage    : {memory_usage:.1f}%")


# Disk Information
print("\n[DISK INFORMATION]")

disk = shutil.disk_usage("/")

total = disk.total / (1024 ** 3)
used = disk.used / (1024 ** 3)
free = disk.free / (1024 ** 3)

disk_usage = (disk.used / disk.total) * 100

print(f"Total Disk       : {total:.2f} GB")
print(f"Used Disk        : {used:.2f} GB")
print(f"Free Disk        : {free:.2f} GB")
print(f"Disk Usage       : {disk_usage:.1f}%")


# System Uptime
print("\n[SYSTEM UPTIME]")

with open("/proc/uptime", "r") as file:
    uptime_seconds = float(file.read().split()[0])

uptime_hours = uptime_seconds / 3600

print(f"Uptime           : {uptime_hours:.2f} hours")


# Running Processes
print("\n[TOP CPU PROCESSES]")

processes = subprocess.check_output(
    ["ps", "aux", "--sort=-%cpu"],
    text=True
)

lines = processes.splitlines()

for line in lines[:6]:
    print(line)


# Diagnostic Findings
print("\n[DIAGNOSTIC FINDINGS]")

findings = []

if memory_usage > 90:
    findings.append(
        ("CRITICAL", "Memory usage is above 90%.")
    )

elif memory_usage > 80:
    findings.append(
        ("HIGH", "Memory usage is above 80%.")
    )

if disk_usage > 95:
    findings.append(
        ("CRITICAL", "Disk usage is above 95%.")
    )

elif disk_usage > 90:
    findings.append(
        ("HIGH", "Disk usage is above 90%.")
    )

if not findings:
    print("✓ No significant resource issues detected.")

else:
    for severity, finding in findings:
        print(f"[{severity}] {finding}")


# Recommendations
print("\n[RECOMMENDED INVESTIGATIONS]")

if memory_usage > 80:
    print("→ Investigate memory-consuming processes.")

if disk_usage > 90:
    print("→ Investigate disk usage and large files.")

if not findings:
    print("→ No immediate resource investigation required.")