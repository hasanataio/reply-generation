# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3-slim

EXPOSE 8023

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app


# During debugging, this entry point can be overridden. 
CMD ["python", "main.py"]