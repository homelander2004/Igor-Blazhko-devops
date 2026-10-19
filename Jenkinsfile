pipeline {
    agent any

    environment {
        STUDENT_NAME = 'Igor'
        STUDENT_SURNAME = 'Blazhko'
        STUDENT_GROUP = 'IT2-2313'
        STUDENT_ID = '38325'
        IMAGE_NAME = 'Igor_Blazhko_Devops'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo "Building project for ${STUDENT_NAME} ${STUDENT_SURNAME}"
                sh 'ls -la'
            }
        }

        stage('Test') {
            steps {
                echo 'Checking application files'
                sh 'test -f app/app.py'
                sh 'test -f Dockerfile'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t "$IMAGE_NAME" .'
            }
        }

        stage('Docker Run') {
            steps {
                sh '''
                    docker rm -f devops-pipeline-test || true
                    docker run -d --name devops-pipeline-test \
                      -p 8002:8000 \
                      -e STUDENT_NAME="$STUDENT_NAME" \
                      -e STUDENT_SURNAME="$STUDENT_SURNAME" \
                      -e STUDENT_GROUP="$STUDENT_GROUP" \
                      -e STUDENT_ID="$STUDENT_ID" \
                      "$IMAGE_NAME"
                    sleep 3
                    docker ps
                    docker logs devops-pipeline-test
                '''
            }
        }
    }
}
