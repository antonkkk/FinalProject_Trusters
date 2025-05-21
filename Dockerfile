FROM jenkins/jenkins
USER root

# Установка необходимых пакетов
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-venv \
    git \
    curl \
    unzip \
    wget \
    gnupg2 \
    ca-certificates \
    libnss3 \
    libgconf-2-4 \
    libxi6 \
    libxrender1 \
    libxcomposite1 \
    libxtst6 \
    libxrandr2 \
    libasound2 \
    libatk1.0-0 \
    libcups2 \
    libxss1 && \
    rm -rf /var/lib/apt/lists/*


ENV VENV_PATH=/opt/venv
RUN python3 -m venv $VENV_PATH
ENV PATH="$VENV_PATH/bin:$PATH"

RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends google-chrome-stable

RUN wget -O /tmp/chromedriver-linux64.zip https://storage.googleapis.com/chrome-for-testing-public/136.0.7103.94/linux64/chromedriver-linux64.zip \
    && unzip /tmp/chromedriver-linux64.zip -d /tmp/chromedriver_temp \
    && mv /tmp/chromedriver_temp/chromedriver /usr/local/bin/chromedriver \
    && chmod +x /usr/local/bin/chromedriver \
    && rm -rf /tmp/chromedriver_temp /tmp/chromedriver-linux64.zip

# Обновление pip и установка зависимостей для тестов
RUN pip install --upgrade pip setuptools wheel
RUN pip install pytest allure-pytest requests selenium

USER jenkins
WORKDIR /home/jenkins/workspace

