import os

print("In this program we are going to learn about the Os Module in Python")

# # Get the current working directory
# current_directory = os.getcwd()
# print("Current Directory:", current_directory)

# # List files in the current directory
# files = os.listdir(current_directory)
# print("Files in Directory:", files)

# # # Create a new directory
# # os.mkdir("new_folder")
import os

# Get the current working directory
current_dir = os.getcwd()
print("Current Directory:", current_dir)

# List files and directories in the current directory
print("Files and Directories:", os.listdir(current_dir))

# Create a new directory
new_dir = "example_dir"
os.mkdir(new_dir)
print(f"Directory '{new_dir}' created.")

# Rename the directory
renamed_dir = "renamed_example_dir"
os.rename(new_dir, renamed_dir)
print(f"Directory renamed to '{renamed_dir}'.")

# Remove the directory
os.rmdir(renamed_dir)
print(f"Directory '{renamed_dir}' removed.")

import os

# Join paths
path = os.path.join("folder", "subfolder", "file.txt")
print("Joined Path:", path)

# Split a path
dir_name, file_name = os.path.split(path)
print("Directory:", dir_name)
print("File Name:", file_name)

# Check if a path exists
print("Path exists?", os.path.exists(path))

print("Environment Variables:", os.environ)

# Get a specific environment variable
home_dir = os.getenv("HOME")  # On Windows, use "USERPROFILE"
print("Home Directory:", home_dir)



# Run a system command
os.system("ls -l")  # On Windows, use "dir"

# Capture command output
output = os.popen("echo Hello, World!").read()
print("Command Output:", output)



# Walk through a directory tree
for root, dirs, files in os.walk("."):
    print(f"Root: {root}")
    print(f"Directories: {dirs}")
    print(f"Files: {files}")
    print("-" * 40)



# Get current directory
current_dir = os.getcwd()
print("Current Directory:", current_dir)

# Create a new directory
new_dir = "test_dir"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"Directory '{new_dir}' created.")
else:
    print(f"Directory '{new_dir}' already exists.")

# Create a file in the new directory
file_path = os.path.join(new_dir, "test_file.txt")
with open(file_path, "w") as file:
    file.write("Hello, OS Module!")

# List files in the new directory
print("Files in Directory:", os.listdir(new_dir))

# Remove the file and directory
os.remove(file_path)
os.rmdir(new_dir)
print(f"File and directory '{new_dir}' removed.")