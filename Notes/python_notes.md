# Python Notes for Beginners 🐍

## Why Python for DevOps? 🤔
- Easy to learn and use.
- Rich libraries for DevOps automation (e.g., Paramiko, Boto3).
- Supports scripting, web apps, and data handling.

## Python Basics 📝

### Installation
1. Download from [Python Official Website](https://www.python.org/).
2. Add Python to `PATH` during installation.
3. Verify using:
   ```bash
   python --version
   ```

### Common Data Types
- **int:** Whole numbers (e.g., `42`).
- **float:** Decimal numbers (e.g., `3.14`).
- **str:** Text (e.g., `'Hello'`).
- **list:** Ordered collection (e.g., `[1, 2, 3]`).
- **dict:** Key-value pairs (e.g., `{'key': 'value'}`).

### Basic Syntax
```python
# Print a message
print("Hello, Python!")

# Variables
x = 10
y = 5.5
message = "Welcome to Python!"

# Loop
for i in range(5):
    print(f"Iteration {i}")

# Function
def add(a, b):
    return a + b

print(add(2, 3))
```

### Virtual Environment Setup
1. Create a virtual environment:
   ```bash
   python -m venv myenv
   ```
2. Activate:
   - Windows:
     ```bash
     .\myenv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source myenv/bin/activate
     ```
3. Deactivate:
   ```bash
   deactivate
   ```

### Package Management with pip
- Install a package:
  ```bash
  pip install package_name
  ```
- List installed packages:
  ```bash
  pip list
  ```

## Python Automation Scripts for DevOps 🚀

### 1. SSH Connection to Remote Server
```python
import paramiko

hostname = "your-server-ip"
username = "your-username"
password = "your-password"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, username=username, password=password)
stdin, stdout, stderr = client.exec_command("uptime")
print(stdout.read().decode())
client.close()
```

### 2. Upload File to AWS S3 Bucket
```python
import boto3

s3 = boto3.client('s3')
file_name = "local_file.txt"
bucket_name = "your-bucket-name"
s3.upload_file(file_name, bucket_name, "uploaded_file.txt")
print("File uploaded successfully")
```

### 3. Monitor Disk Usage on a Server
```python
import os

usage = os.statvfs('/')
total = (usage.f_blocks * usage.f_frsize) / (1024 * 1024 * 1024)  # GB
free = (usage.f_bfree * usage.f_frsize) / (1024 * 1024 * 1024)  # GB
print(f"Total Disk Space: {total:.2f} GB")
print(f"Free Disk Space: {free:.2f} GB")
```

### 4. Generate a Secure Password
```python
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

print("Generated Password:", generate_password())
```

### 5. Automate Docker Container Management
```python
import os

# Pull Docker image
os.system("docker pull nginx")

# Run a Docker container
os.system("docker run -d --name my_nginx -p 8080:80 nginx")

# Stop a Docker container
os.system("docker stop my_nginx")

# Remove a Docker container
os.system("docker rm my_nginx")
```

## Additional Resources 🌟
- [Python Official Documentation](https://docs.python.org/3/)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
- [Real Python Tutorials](https://realpython.com/)

