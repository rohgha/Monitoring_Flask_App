FROM python:3.9-slim-buster

WORKDIR /app

# Copy requirements file and install dependencies
COPY Information.txt .
RUN pip3 install --no-cache-dir -r Information.txt

# Copy the rest of the application code
COPY . .

# Set environment variables
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port on which the Flask app will run
EXPOSE 5000

# Command to run the Flask application
CMD ["flask", "run"]
