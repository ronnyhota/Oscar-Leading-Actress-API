#!/usr/bin/env bash
set -e

# Build the Docker image
docker build -t oscar-actress-api:latest .

# Run the container
docker run --rm -p 8080:8080 oscar-actress-api:latest