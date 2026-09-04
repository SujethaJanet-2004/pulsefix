# Incident 001 — Application Running Slowly

## Customer Report

"The application has become very slow since this morning."

## Symptoms

- Pages take several seconds to load
- Some requests timeout
- Users report slow application performance

## Initial Investigation

PulseFix system diagnostics were used to inspect:

- CPU utilization
- Memory utilization
- Disk utilization
- Running processes
- Top CPU-consuming processes
- Top memory-consuming processes
- Process-level resource risks

## Evidence

### System Health

- CPU Usage: 59.0%
- Memory Usage: 89.0%
- Disk Usage: 83.6%
- System Status: WARNING (HIGH)

### CPU Process Investigation

Top CPU-consuming processes:

1. `python.exe` — 69.80% CPU — 0.24% memory — Running
2. `svchost.exe` — 52.80% CPU — 0.30% memory — Running
3. `Code.exe` — 43.40% CPU — 3.94% memory — Running

### Memory Process Investigation

Top memory-consuming processes:

1. `chrome.exe` — 5.86% memory — 0.30% CPU — Running
2. `Code.exe` — 3.97% memory — 0.00% CPU — Running
3. `Code.exe` — 3.94% memory — 43.40% CPU — Running

## Observations

- Memory utilization reached 89.0%, exceeding the configured warning threshold of 80%.
- CPU utilization was 59.0%, which remained below the system-level HIGH threshold of 80%.
- `python.exe` was the highest observed CPU-consuming process at 69.80%.
- `svchost.exe` also showed elevated CPU activity at 52.80%.
- `Code.exe` showed 43.40% CPU usage but remained below the configured process-level HIGH threshold of 50%.
- `chrome.exe` was the highest individual memory-consuming process at 5.86%.
- PulseFix successfully collected PID, process name, CPU usage, memory usage, and process status for running processes.
- CPU and memory investigations were performed separately to avoid assuming that the highest CPU-consuming process was also responsible for the overall memory pressure.

## Findings

PulseFix detected elevated system memory utilization:

- Memory usage: 89.0%
- Warning threshold: 80%
- Severity: HIGH

The CPU process investigation identified:

- `python.exe` at 69.80% CPU → HIGH
- `svchost.exe` at 52.80% CPU → HIGH

The memory process investigation identified:

- `chrome.exe` at 5.86% memory → HIGH

The top individual memory-consuming processes did not account for the majority of the overall system memory utilization. Therefore, the available process-level evidence does not explain the complete system memory pressure.

These findings provide diagnostic evidence but do not confirm the root cause of the reported application slowdown.

Further investigation is required.

## Recommended Investigation

Based on the detected system and process-level findings, PulseFix recommends:

1. Investigate memory-consuming processes and determine what is contributing to the remaining system memory utilization.
2. Investigate `python.exe` because it exceeded the configured process-level CPU threshold.
3. Investigate `svchost.exe` because it exceeded the configured process-level CPU threshold.
4. Review system and application logs for additional evidence.
5. Determine whether the affected application is experiencing resource contention.
6. Continue monitoring system and process metrics to identify persistent resource issues.

These recommendations are based on threshold-based diagnostics and do not represent a confirmed root cause.

## Process Risk Assessment

PulseFix evaluates individual processes against configured CPU and memory thresholds to identify potential resource-heavy processes.

### Process-Level Thresholds

- CPU > 50% → HIGH
- CPU > 80% → CRITICAL
- Memory > 5% → HIGH
- Memory > 10% → CRITICAL

### Detected Process Risks

Based on the current diagnostic run:

- `python.exe` — 69.80% CPU → HIGH
- `svchost.exe` — 52.80% CPU → HIGH
- `chrome.exe` — 5.86% memory → HIGH

### Interpretation

The detected processes represent potential contributors to system resource pressure.

The process-level threshold violations do not independently establish that any process is the root cause of the reported application slowdown.

Additional evidence from system logs, application logs, networking, and other diagnostic sources is required before determining the root cause.

## Root Cause

Not yet determined.

## Resolution

Not yet resolved.

## Status

Investigating 

