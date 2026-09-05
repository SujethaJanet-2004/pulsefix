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
- Diagnostic snapshots
- Resource trends between diagnostic snapshots

## Evidence

### System Health

Previous diagnostic snapshot:

- CPU Usage: 55.0%
- Memory Usage: 85.5%
- Disk Usage: 83.6%
- System Status: WARNING (HIGH)

Current diagnostic snapshot:

- CPU Usage: 46.0%
- Memory Usage: 89.7%
- Disk Usage: 82.5%

### CPU Process Investigation

Top CPU-consuming processes from the previous diagnostic run:

1. `python.exe` — 67.90% CPU — 0.24% memory — Running
2. `svchost.exe` — 36.40% CPU — 0.27% memory — Running
3. `Code.exe` — 26.20% CPU — 5.21% memory — Running

### Memory Process Investigation

Top memory-consuming processes from the previous diagnostic run:

1. `chrome.exe` — 5.93% memory — 0.30% CPU — Running
2. `Code.exe` — 5.21% memory — 26.20% CPU — Running
3. `Code.exe` — 3.56% memory — 0.70% CPU — Running

## Observations

- Previous system memory utilization was 85.5%, exceeding the configured system-level warning threshold of 80%.
- Current system memory utilization increased to 89.7%.
- CPU utilization decreased from 55.0% to 46.0%.
- Disk utilization decreased from 83.6% to 82.5%.
- The previous process investigation identified `python.exe` as the highest observed CPU-consuming process at 67.90%.
- `chrome.exe` was the highest individual memory-consuming process at 5.93% during the previous diagnostic run.
- CPU and memory investigations were performed separately to avoid assuming that the highest CPU-consuming process was also responsible for the overall memory pressure.
- PulseFix preserved diagnostic evidence through timestamped snapshots.

## Findings

PulseFix previously detected elevated system memory utilization:

- Previous memory usage: 85.5%
- Warning threshold: 80%
- Severity: HIGH

The latest diagnostic comparison shows:

- CPU decreased by 9.0 percentage points.
- Memory increased by 4.2 percentage points.
- Disk decreased by 1.1 percentage points.

Memory utilization remains the primary system-level resource concern because it increased from 85.5% to 89.7% and remains above the configured warning threshold.

However, the 4.2 percentage-point increase does not exceed the configured threshold for a significant memory trend.

CPU and disk utilization decreased between the two diagnostic runs.

The available evidence therefore does not establish a significant overall worsening or improvement in system resource utilization.

These findings provide diagnostic evidence but do not confirm the root cause of the reported application slowdown.

Further investigation is required.

## Recommended Investigation

Based on the detected system and process-level findings, PulseFix recommends:

1. Investigate memory-consuming processes and determine what is contributing to the remaining system memory utilization.
2. Investigate `python.exe` because it exceeded the configured process-level CPU threshold during the previous diagnostic run.
3. Investigate `chrome.exe` and `Code.exe` because they exceeded the configured process-level memory threshold during the previous diagnostic run.
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

Based on the previous diagnostic run:

- `python.exe` — 67.90% CPU → HIGH
- `chrome.exe` — 5.93% memory → HIGH
- `Code.exe` — 5.21% memory → HIGH

### Interpretation

The detected processes represent potential contributors to system resource pressure.

The process-level threshold violations do not independently establish that any process is the root cause of the reported application slowdown.

Additional evidence from system logs, application logs, networking, and other diagnostic sources is required before determining the root cause.

## Snapshot Comparison

PulseFix compared two diagnostic snapshots to identify changes in system resource utilization.

| Metric | Previous | Current | Change |
|---|---:|---:|---:|
| CPU | 55.0% | 46.0% | -9.0 pp |
| Memory | 85.5% | 89.7% | +4.2 pp |
| Disk | 83.6% | 82.5% | -1.1 pp |

### Trend Assessment

- **CPU:** Decreased by 9.0 percentage points.
- **Memory:** Increased by 4.2 percentage points.
- **Disk:** Decreased by 1.1 percentage points.
- **Overall:** No significant overall resource trend detected.

### Trend Thresholds

For snapshot comparison:

- Memory increase > 5 percentage points → Significant increase
- CPU increase > 10 percentage points → Significant increase
- Disk increase > 5 percentage points → Significant increase

### Interpretation

Memory utilization increased and remains above the configured warning threshold.

However, the increase of 4.2 percentage points does not exceed the configured threshold for a significant memory trend.

CPU and disk utilization decreased between the two snapshots.

The comparison provides temporal evidence about changes in system resource utilization but does not establish the root cause of the reported application slowdown.

## Diagnostic Snapshot

PulseFix generates timestamped diagnostic snapshots for each investigation run.

Each snapshot preserves:

- Timestamp
- System resource utilization
- System severity
- Diagnostic findings
- Recommended investigations
- Top CPU-consuming processes
- Top memory-consuming processes
- Process-level risk findings

The snapshots allow PulseFix to compare system conditions across diagnostic runs and identify potential resource trends.

## Root Cause

Not yet determined.

## Resolution

Not yet resolved.

## Status

Investigating


