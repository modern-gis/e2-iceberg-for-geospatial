FROM python:3.11-slim

WORKDIR /workspace

# Install system deps: gcc + git
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      gcc \
      git \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

# (Optional) Debug print
RUN echo "---- requirements.txt ----" && cat requirements.txt && echo "--------------------------"

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8888
