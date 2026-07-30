FROM jenkins/jenkins:lts

USER root

RUN apt-get update && \
    apt-get install -y \
    docker.io \
    wget \
    unzip

# Install SonarScanner CLI
RUN wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-7.1.0.4889-linux-x64.zip && \
    unzip sonar-scanner-7.1.0.4889-linux-x64.zip -d /opt && \
    mv /opt/sonar-scanner-* /opt/sonar-scanner && \
    ln -s /opt/sonar-scanner/bin/sonar-scanner /usr/local/bin/sonar-scanner && \
    rm sonar-scanner-7.1.0.4889-linux-x64.zip

USER jenkins

RUN jenkins-plugin-cli --plugins \
    git \
    git-client \
    workflow-aggregator \
    workflow-job \
    workflow-cps \
    pipeline-stage-view \
    docker-workflow \
    sonar