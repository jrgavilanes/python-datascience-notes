# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY database ./database
COPY features ./features
COPY main.py config.py ./

# Install any needed packages specified in requirements.txt
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Set the entry point to the main file
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main:app"]