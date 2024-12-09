pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                // Clone the Git repository
                git branch: 'master', url: 'https://github.com/<your-repo>'
            }
        }
        stage('Build') {
            steps {
                // Build the Docker image
                sh 'docker build -t flask-app .'
            }
        }
        stage('Test') {
            steps {
                // Run tests using pytest
                sh 'docker run flask-app pytest tests'
            }
        }
        stage('Deploy') {
            steps {
                // Run the Flask app in a Docker container
                sh 'docker run -d -p 5000:5000 flask-app'
            }
        }
    }
}
