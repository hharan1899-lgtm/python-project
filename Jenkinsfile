pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t django-demo .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker stop django-demo || true
                docker rm django-demo || true
                docker run -d -p 8000:8000 --name django-demo django-demo
                '''
            }
        }
    }
}
