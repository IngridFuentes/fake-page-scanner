# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .
RUN echo 'ingrid fuentes log:'
RUN ls
RUN pwd 

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container (optional)
EXPOSE 80

# Run main.py when the container launches
CMD ["python", "./main.py"]

