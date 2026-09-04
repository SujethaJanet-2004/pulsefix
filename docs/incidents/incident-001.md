# Incident 001 — Application Running Slowly

## Customer Report

"The application has become very slow since this morning."

## Symptoms

* Pages take several seconds to load
* Some requests timeout
* Users report slow application performance

## Initial Investigation

PulseFix system diagnostics were used to inspect:

* CPU utilization
* Memory utilization
* Disk utilization
* Running processes
* Top CPU-consuming processes
* Top memory-consuming processes

## Evidence

### System Health

* CPU Usage: 57.4%
* Memory Usage: 84.9%
* Disk Usage: 83.6%
* System Status: WARNING (HIGH)

### CPU Process Investigation

Top CPU-consuming processes:

1. `python.exe` — 71.10% CPU — 0.23% memory — Running
2. `svchost.exe` — 28.30% CPU — 0.25% memory — Running
3. `dwm.exe` — 18.90% CPU — 0.84% memory — Running

### Memory Process Investigation

Top memory-consuming processes:

1. `chrome.exe` — 5.87% memory
2. `Code.exe` — 4.73% memory
3. `chrome.exe` — 3.48% memory

## Observations

* Memory utilization reached 84.9%, exceeding the configured warning threshold of 80%.
* The highest observed CPU-consuming process was `python.exe` at 71.10%.
* `svchost.exe` and `dwm.exe` also showed notable CPU activity.
* `chrome.exe` was the highest individual memory-consuming process at 5.87%.
* PulseFix successfully collected PID, process name, CPU usage, memory usage, and process status for running processes.
* CPU and memory investigations were performed separately to avoid assuming that the highest CPU-consuming process was also responsible for the overall memory pressure.

## Findings

PulseFix detected elevated memory utilization:

* Memory usage: 84.9%
* Warning threshold: 80%
* Severity: HIGH

The CPU process investigation identified `python.exe` as the highest observed CPU-consuming process at 71.10%.

The memory process investigation identified `chrome.exe` as the highest individual memory-consuming process at 5.87%.

The top three processes together represented approximately 14.08% of total physical system memory according to their individual process-level memory percentages.

This does not explain the remaining system memory utilization, so further investigation is required.

These findings provide diagnostic evidence but do not confirm the root cause of the reported application slowdown.

## Recommended Investigation

Based on the detected high memory utilization, PulseFix recommends:

1. Investigate memory-consuming processes.
2. Determine whether the affected application is consuming excessive resources.
3. Review system and application logs for additional evidence.
4. Continue investigating CPU-consuming processes if high CPU activity persists.

These recommendations are based on threshold-based diagnostics and do not represent a confirmed root cause.

## Root Cause

Not yet determined.

## Resolution

Not yet resolved.

## Status

Investigating
