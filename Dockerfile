FROM python:3.6

# Set Working Directory
WORKDIR /usr/src/app

# Install app dependencies
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
