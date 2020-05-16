from alpine:latest
RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

WORKDIR /app
COPY . /app

ENTRYPOINT ["python3"]
CMD ["send.py","receive.app.svc.cluster.local","4000"]
