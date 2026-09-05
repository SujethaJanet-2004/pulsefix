from pathlib import Path

previous_snapshot = Path(
    "snapshots/snapshot_2026-09-04_194515.txt"
)

current_snapshot = Path(
    "snapshots/snapshot_2026-09-05_120539.txt"
)

previous_data = previous_snapshot.read_text(
    encoding="utf-8"
)

current_data = current_snapshot.read_text(
    encoding="utf-8"
)

def extract_metrics(snapshot_text):

    metrics = {}

    for line in snapshot_text.splitlines():

        if line.startswith("CPU Usage:"):
            metrics["cpu"] = float(
                line.split(":")[1].strip().replace("%", "")
            )

        elif line.startswith("Memory Usage:"):
            metrics["memory"] = float(
                line.split(":")[1].strip().replace("%", "")
            )

        elif line.startswith("Disk Usage:"):
            metrics["disk"] = float(
                line.split(":")[1].strip().replace("%", "")
            )

    return metrics

previous = extract_metrics(previous_data)
current = extract_metrics(current_data)

cpu_change = current["cpu"] - previous["cpu"]
memory_change = current["memory"] - previous["memory"]
disk_change = current["disk"] - previous["disk"]

print("╔══════════════════════════════════════╗")
print("║       PULSEFIX SNAPSHOT DIFF         ║")
print("╚══════════════════════════════════════╝")

print("\nMetric       Previous    Current    Change")

print(
    f"CPU          {previous['cpu']:.1f}%       "
    f"{current['cpu']:.1f}%       "
    f"{cpu_change:+.1f} pp"
)

print(
    f"Memory       {previous['memory']:.1f}%       "
    f"{current['memory']:.1f}%       "
    f"{memory_change:+.1f} pp"
)

print(
    f"Disk         {previous['disk']:.1f}%       "
    f"{current['disk']:.1f}%       "
    f"{disk_change:+.1f} pp"
)

print("\nAssessment:")

if memory_change > 5:
    print("- Memory pressure increased significantly.")

elif memory_change > 0:
    print("- Memory utilization increased.")

elif memory_change < 0:
    print("- Memory utilization decreased.")

else:
    print("- Memory utilization remained unchanged.")

if cpu_change > 10:
    print("- CPU utilization increased significantly.")

elif cpu_change > 0:
    print("- CPU utilization increased.")

elif cpu_change < 0:
    print("- CPU utilization decreased.")

else:
    print("- CPU utilization remained unchanged.")

if disk_change > 5:
    print("- Disk utilization increased significantly.")

elif disk_change > 0:
    print("- Disk utilization increased.")

elif disk_change < 0:
    print("- Disk utilization decreased.")

else:
    print("- Disk utilization remained unchanged.")

if memory_change > 5 or cpu_change > 10:
    print("\n⚠ Resource pressure appears to be increasing.")

elif memory_change < 0 and cpu_change < 0:
    print("\n✓ Resource utilization is improving.")

else:
    print("\n• No significant overall resource trend detected.")

    