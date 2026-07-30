pipeline {
    agent any

    environment {
        REPO_NAME = sh(
            script: "echo ${env.GIT_URL} | sed -E 's/.*\\/([^/]+)(\\.git)?$/\\1/'",
            returnStdout: true
        ).trim()
        SONAR_PROJECT_KEY = "${REPO_NAME}"
        DOCKER_IMAGE = "${REPO_NAME}"
    }

    stages {

        stage('Check Python') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    if (fileExists('requirements.txt')) {
                        sh 'pip3 install --break-system-packages -r requirements.txt'
                    } else {
                        echo 'No requirements.txt found, skipping pip install'
                    }
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonarqube') {
                    sh '''
                        sonar-scanner \
                          -Dsonar.projectKey=${SONAR_PROJECT_KEY} \
                          -Dsonar.projectName=${SONAR_PROJECT_KEY} \
                          -Dsonar.sources=. \
                          -Dsonar.host.url=http://sonarqube:9000
                    '''
                }
            }
        }

        stage('Verify Workspace') {
            steps {
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }
    }

    post {
        success {
            echo 'Pipeline Successful'
        }
        failure {
            echo 'Pipeline Failed'
        }
        always {
            cleanWs()
        }
    }
}
