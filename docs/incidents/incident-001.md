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

- CPU Usage: 56.6%
- Memory Usage: 85.2%
- Disk Usage: 83.6%
- System Status: WARNING

### Process Investigation

Top CPU-consuming processes:

1. python.exe — 71.10% CPU
2. svchost.exe — 38.60% CPU
3. svchost.exe — 21.70% CPU

### Observations

- System memory utilization is above the configured warning threshold.
- Multiple processes showed significant CPU activity.
- PulseFix successfully collected process-level diagnostic information.

## Findings

PulseFix identified elevated memory utilization and
significant CPU activity as areas requiring further investigation.

These observations are diagnostic evidence only.
No root cause has been confirmed yet.

## Root Cause

Not yet determined.

## Resolution

Not yet resolved.

## Status

Investigating