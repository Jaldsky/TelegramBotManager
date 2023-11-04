FROM redhat/ubi8-minimal

# Prepare image
RUN microdnf install -y tar gzip gcc findutils make

# Install python
RUN microdnf install -y sqlite-devel openssl-devel bzip2-devel libffi-devel && \
    curl -O https://www.python.org/ftp/python/3.9.7/Python-3.9.7.tgz && \
    tar -xvf Python-3.9.7.tgz && \
    cd Python-3.9.7 && ./configure --enable-optimizations && make && make install && \
    cd .. && rm -rf Python-3.9.7.tgz Python-3.9.7

WORKDIR /app

COPY TelegramBotManager /app

RUN pip3 install -r requirements.txt --no-cache-dir

# Run service
RUN python3 main.py
