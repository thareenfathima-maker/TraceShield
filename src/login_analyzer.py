import pandas as pd

# Step 1: Specify the dataset location
file_path = "data/sample_security_logs.csv"

# Step 2: Read the security logs
logs = pd.read_csv(file_path)

# Step 3: Display the loaded data
print("\n===== TRACESHIELD SECURITY LOGS =====")
print(logs)

# Step 4: Select failed login attempts
failed_logins = logs[logs["status"] == "Failed"]

# Step 5: Count failed attempts for each user
failed_counts = failed_logins.groupby("username").size()

# Step 6: Set the alert threshold
threshold = 3

# Step 7: Identify users who meet the threshold
suspicious_users = failed_counts[failed_counts >= threshold]

print("\n===== SUSPICIOUS LOGIN ACTIVITY =====")

if suspicious_users.empty:
    print("No users met the suspicious-login threshold.")
else:
    for username, count in suspicious_users.items():
        print(
            f"ALERT: User '{username}' had "
            f"{count} failed login attempts."
        )

print("\nAnalysis completed!")