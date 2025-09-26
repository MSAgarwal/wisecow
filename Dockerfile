FROM debian:12-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV WISECOW_PORT=4499

# Install prerequisites including netcat
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    cowsay fortune-mod fortunes-min curl bash netcat-openbsd \
 && rm -rf /var/lib/apt/lists/*

# Ensure /usr/games is in PATH for cowsay/fortune
ENV PATH="/usr/games:${PATH}"

WORKDIR /app

COPY wisecow.sh /app/wisecow.sh

# Fix Windows line endings + make executable
RUN sed -i 's/\r$//' /app/wisecow.sh && chmod +x /app/wisecow.sh

EXPOSE ${WISECOW_PORT}

CMD ["/app/wisecow.sh"]
