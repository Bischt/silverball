# Use the Python3.7.2 image
FROM python:3.7.2-stretch

# Create user to run uwsgi as
RUN groupadd --gid 1000 uwsgi \
    && useradd --uid 1000 uwsgi --gid uwsgi --shell /bin/bash --create-home uwsgi

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# run the command to start uWSGI
CMD ["uwsgi", "app.ini"]
