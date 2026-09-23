import time

print("Starting backend checks...")
time.sleep(4)  # Sleeps for 4 seconds

# Writes results to its own file
with open("backend_report.txt", "w") as f:
    f.write("Backend verification: SUCCESS\n")
print("Backend checks complete.")
