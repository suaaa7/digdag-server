FROM openjdk:8-jdk

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

RUN apt-get update && apt-get install -y --no-install-recommends \
  curl gettext-base postgresql-client \
  && rm -rf /var/lib/apt/lists/*

# docker client
ENV DOCKER_CLIENT_VERSION=19.03.2 \
    DOCKER_API_VERSION=1.40
RUN curl -fsSL https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_CLIENT_VERSION}.tgz \
  | tar -xzC /usr/local/bin --strip=1 docker/docker

# digdag server
ENV DIGDAG_VERSION=0.9.41
RUN curl -o /usr/local/bin/digdag --create-dirs -L https://dl.digdag.io/digdag-${DIGDAG_VERSION} && \
  chmod +x /usr/local/bin/digdag

ENV POSTGRES_USER=digdag \
    POSTGRES_PASSWORD=digdag \
    POSTGRES_HOST=postgresql \
    POSTGRES_PORT=5432 \
    POSTGRES_DB=digdag \
    LOG_TYPE=local \
    ENCRYPTION_KEY=MDEyMzQ1Njc4OTAxMjM0NQ==

COPY digdag/server.properties /etc/digdag/server.properties
COPY digdag/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

EXPOSE 65432 65433

ENTRYPOINT ["/usr/local/bin/entrypoint.sh","/usr/local/bin/digdag","server","--config","/etc/digdag/server.properties"]
