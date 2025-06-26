FROM python:3.11-slim

WORKDIR /workspace

RUN apt-get update \
 && apt-get install -y --no-install-recommends gcc \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

# DEBUG: show the contents of requirements.txt
RUN echo "---- requirements.txt ----" \
 && cat requirements.txt \
 && echo "--------------------------"

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8888
