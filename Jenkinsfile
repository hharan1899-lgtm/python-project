pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t django-demo1 .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker stop django-demo || true
                docker rm django-demo || true
                docker run -d -p 8001:8001 --name django-demo django-demo
                '''
            }
        }
    }
}
