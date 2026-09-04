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

## Evidence

### System Health

- CPU Usage: 67.3%
- Memory Usage: 85.4%
- Disk Usage: 83.6%
- System Status: WARNING

### Process Investigation

Top CPU-consuming processes:

1. python.exe — 66.90% CPU — 0.23% memory — Running
2. svchost.exe — 45.40% CPU — 0.25% memory — Running
3. Code.exe — 21.80% CPU — 4.61% memory — Running

### Observations

- Memory utilization reached 85.2%, exceeding the configured warning threshold.
- The highest observed CPU-consuming process was `python.exe` at 71.10%.
- Two `svchost.exe` processes also showed notable CPU activity.
- PulseFix successfully collected PID, process name, CPU usage,
  memory usage, and process status for running processes.

## Findings

PulseFix detected elevated memory utilization:

- Memory usage: 85.4%
- Warning threshold: 80%

The process investigation also identified python.exe
as the highest CPU-consuming process at 66.90%.

These findings provide diagnostic evidence but do not
confirm the root cause of the reported application slowdown.

Further investigation is required.

## Root Cause

Not yet determined.

## Resolution

Not yet resolved.

## Status

Investigating