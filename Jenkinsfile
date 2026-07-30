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

        stage('Run Tests with Coverage') {
            steps {
                sh 'coverage run -m pytest test_app.py -v'
                sh 'coverage xml -o coverage-report.xml'
                sh 'coverage report'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh '''
                        sonar-scanner \
                          -Dsonar.projectKey=${JOB_NAME} \
                          -Dsonar.projectName=${JOB_NAME} \
                          -Dsonar.sources=. \
                          -Dsonar.host.url=http://sonarqube:9000 \
                          -Dsonar.python.coverage.reportPaths=coverage-report.xml
                    '''
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
