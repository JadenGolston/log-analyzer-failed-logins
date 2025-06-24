from collections import defaultdict

# Open the sample log file
with open('sample_log.txt', 'r') as log_file:
    lines = log_file.readlines()

failed_attempts = defaultdict(int)

for line in lines:
    if "Failed password" in line:
        parts = line.split()
        ip = parts[-4]
        failed_attempts[ip] += 1

# Output results
print("📋 Failed Login Summary:")
for ip, count in failed_attempts.items():
    print(f"IP Address: {ip} — Attempts: {count}")
