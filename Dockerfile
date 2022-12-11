FROM python:3.9-slim-buster

# Install Firefox and geckodriver
RUN apt update && apt -y install firefox-esr wget && \
    wget https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-linux64.tar.gz && \
    tar -xvf geckodriver-v0.32.0-linux64.tar.gz && \
    mv geckodriver /usr/local/bin

ENV LAMBDA_TASK_ROOT=/var/task
COPY requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Copy function code
COPY app.py ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.handler" ]