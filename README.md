# Failed Login Log Analyzer 🔐

This project scans server log files to detect failed SSH login attempts, helping to spot brute-force attacks. It’s useful for both cybersecurity engineering and system administration.

## 🛠 How It Works
- Looks for lines with `Failed password`
- Extracts IP addresses
- Counts how many times each IP failed

## 📁 Files
- `sample_log.txt` — Example of real-world log entries
- `failed_login_parser.py` — Python script that analyzes logs and prints results

## 📈 Sample Output
Failed Login Summary:

IP Address: 192.168.1.12 — Attempts: 2
IP Address: 192.168.1.23 — Attempts: 2

## 🎯 Why It Matters
This simulates a basic SOC function of log review and helps develop scripting skills for automation, crucial in both cert-aligned roles.
