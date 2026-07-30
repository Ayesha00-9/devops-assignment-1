pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Python Check') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install --break-system-packages -r requirements.txt || true'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    if (env.SONAR_TOKEN) {
                        withSonarQubeEnv('SonarQube') {
                            sh 'sonar-scanner -Dsonar.projectKey=${JOB_NAME} -Dsonar.projectName=${JOB_NAME} -Dsonar.sources=. -Dsonar.host.url=http://sonarqube:9000'
                        }
                    } else {
                        echo 'Skipping SonarQube: SONAR_TOKEN not configured in Jenkins'
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${JOB_NAME} .'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
