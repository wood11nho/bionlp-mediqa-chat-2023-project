import csv
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--task', type=str, required=True, help='Task name (taskA, taskB, taskC)')
parser.add_argument('--file', type=str, required=True, help='Path to the submission file')
args = parser.parse_args()

filepath = args.file
filename = os.path.basename(filepath)

# Check that the file path exists
if not os.path.exists(filepath):
    raise ValueError("File path does not exist")

# Check that the file name starts with "taskA", "taskB", or "taskC"
if not (filename.startswith("taskA") or filename.startswith("taskB") or filename.startswith("taskC")):
    raise ValueError("File name must start with 'taskA', 'taskB', or 'taskC'")

# Check that the file is a CSV file
if not filename.endswith(".csv"):
    raise ValueError("File must be a CSV file")

# Open the file and check the number of columns and test IDs
if filename.startswith("taskA"):
    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)
        if header != ["TestID", "SystemOutput1", "SystemOutput2"]:
            raise ValueError("Task A run file must have 3 columns: TestID, SystemOutput1, and SystemOutput2.")
        for row in reader:
            if not row or not row[0].isdigit():
                raise ValueError("First column must contain numeric TestIDs.")
else:
    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)
        if header != ["TestID", "SystemOutput"]:
            raise ValueError("Task B/C run file must have 2 columns: TestID and SystemOutput.")
        for row in reader:
            if not row or not row[0].startswith("D2N"):
                raise ValueError("First column must contain TestIDs starting with 'D2N' for Task B/C.")

print("✅ Run file is valid.")