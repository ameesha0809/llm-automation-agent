import os
import glob

log_dir = "/data/logs/"
output_file = "/data/logs-recent.txt"

# Get all .log files
log_files = glob.glob(os.path.join(log_dir, "*.log"))

# Sort files by modification time (most recent first)
log_files.sort(key=os.path.getmtime, reverse=True)

# Process only the 10 most recent logs
log_entries = []
for log_file in log_files[:10]:
    with open(log_file, "r") as file:
        first_line = file.readline().strip()
        log_entries.append(first_line)

# Write to output file
with open(output_file, "w") as file:
    file.write("\n".join(log_entries))

print(f"Extracted first lines from 10 most recent logs to {output_file}")
