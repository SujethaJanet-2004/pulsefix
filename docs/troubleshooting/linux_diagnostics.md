# Linux Diagnostics — PulseFix

## Purpose

PulseFix Linux Diagnostics collects system-level information from a Linux environment to help a Technical/Product Support Engineer investigate system resource issues.

## Diagnostic Areas

PulseFix currently investigates:

- Operating system information
- Kernel information
- System architecture
- CPU cores
- Memory utilization
- Disk utilization
- System uptime
- Running processes
- System-level resource risks
- Recommended investigations

## System Information

PulseFix collects:

- Operating system
- Kernel release
- System architecture
- Number of CPU cores

### Information Sources

- Python `platform` module
- Python `os` module

## Memory Investigation

PulseFix uses the Linux `free` command to collect memory information.

Command used:

```bash
free -b

PulseFix calculates overall memory utilization using:

Memory Usage = Used Memory / Total Memory × 100

## Memory Thresholds

Memory > 80% → HIGH
Memory > 90% → CRITICAL

## Disk Investigation

PulseFix checks the root filesystem / and collects:

Total disk space
Used disk space
Free disk space
Disk utilization

## Disk Thresholds

Disk > 90% → HIGH
Disk > 95% → CRITICAL

## System Uptime

PulseFix reads:

/proc/uptime

to determine how long the Linux system has been running.

The uptime value is converted from seconds into hours.

## Process Investigation

PulseFix uses:

ps aux --sort=-%cpu

to identify processes with the highest CPU utilization.

The process information is used as supporting evidence during resource investigations.

## Diagnostic Findings

PulseFix compares system resource utilization against configured thresholds.

If a threshold is exceeded, PulseFix generates a diagnostic finding with an associated severity.

Example:

[HIGH] Memory usage is above 80%.

or:

[CRITICAL] Memory usage is above 90%.

## Recommended Investigations

PulseFix provides investigation recommendations based on detected resource conditions.

## High Memory

Recommended action:

Investigate memory-consuming processes.

## High Disk Usage

Recommended action:

Investigate disk usage and large files.

## Current Diagnostic Workflow

Linux System
      ↓
Collect System Information
      ↓
Collect Memory / Disk / Process Data
      ↓
Calculate Resource Utilization
      ↓
Compare Against Thresholds
      ↓
Generate Diagnostic Findings
      ↓
Recommend Investigation

## Current Limitations

The current Linux Diagnostics module does not yet investigate:

Individual process memory consumption
Linux services
File permissions
System logs
Application logs
Network connectivity
Open ports
Disk-intensive processes
Application-specific failures

These capabilities will be added in later development stages.

## Status

Linux Diagnostics v0.1 — Initial implementation