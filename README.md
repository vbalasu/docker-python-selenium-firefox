# docker-python-selenium-firefox

This is a starter project that is designed to be deployed to Google Cloud Run

It consists of a docker container that is based on a Python image. The Dockerfile installs the following software:

1. firefox-esr
2. geckodriver
3. selenium

It also includes `build.sh` that builds the Docker container, and `deploy.sh` that deploys it to Google Cloud Run

The resulting function can be invoked by running `test.sh`
