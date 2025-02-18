# Step 1: Use an official Python runtime as a parent image
FROM python:3.8-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the current directory contents into the container at /app
COPY . /app

# Step 4: Install any needed dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose port 8000 for your app to run
EXPOSE 8000

# Step 6: Define environment variable (ensure this matches the one you're using)
ENV AIPROXY_TOKEN=your_token_here

# Step 7: Run the application
CMD ["python", "app.py"]
