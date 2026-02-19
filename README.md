# Simple-TCP-Port-Scanner-
Description

This is a simple multithreaded TCP port scanner built in Python.
It scans a target host to identify open TCP ports within a specified range.
The scanner uses:
.Python’s socket module to perform TCP connect scans
.Multithreading to improve scanning speed
.Input validation to ensure valid host and port range

How It Works

.The program resolves the hostname to an IP address.

.It validates the user-input port range (1–65535).

.A thread is created for each port in the specified range.

.The scanner attempts a TCP connection to each port.

.Open ports are displayed.

.The total scan time is calculated and printed.

How to Run
python port_scanner.py

Then enter:

.Target IP address or hostname

'Starting port

'Ending port
