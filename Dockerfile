# Use a base Python image
FROM python:3.10-slim

# Set the initial working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into /app
COPY . .

# Change to a different working directory
WORKDIR /app/main_src

# Run the application
CMD ["python", "main.py"]