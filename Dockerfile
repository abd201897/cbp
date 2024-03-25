# Use an official Python runtime as a parent image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --upgrade pip

RUN pip3 install -r requirements.txt

# Expose the port Django runs on
EXPOSE 80

# Run Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
