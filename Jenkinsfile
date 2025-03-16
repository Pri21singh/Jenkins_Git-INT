pipeline {
    agent any

    environment {
        VIRTUAL_ENV = 'venv'
        EC2_SSH_PRIVATE_KEY = credentials('ec2-ssh-key')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: 'github-pat', url: 'https://github.com/Pri21singh/Jenkins_Git-INT'
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    if (!fileExists('venv')) {
                        sh 'python -m venv venv'
                    }
                    sh 'source venv/Scripts/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Build') {
            steps {
                echo 'Building Python application...'
            }
        }

        stage('Test') {
            steps {
                script {
                    sh 'source venv/Scripts/activate && python -m unittest test_app.py'
                }
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                echo 'Deploying Python application to EC2...'

                // sh-agent running in the environment
                sh """
                    eval \$(ssh-agent -s)
                    echo "$EC2_SSH_PRIVATE_KEY" | tr -d '\r' | ssh-add -
                    ssh -o StrictHostKeyChecking=no ec2-user@3.93.65.178 'cd C:/Users/singp/OneDrive/Desktop/CICD/Jenkins_Git-INT && git pull && source venv/bin/activate && pip install -r requirements.txt && python app.py'
                """
            }
        }
    }

    post {
        success {
            mail to: 'priyasingh2103@gmail.com',
                 subject: 'Jenkins Build Success',
                 body: "Build #${env.BUILD_NUMBER} was successful."
        }
        failure {
            mail to: 'priyasingh2103@gmail.com',
                 subject: 'Jenkins Build Failure',
                 body: "Build #${env.BUILD_NUMBER} failed. Check logs."
        }
    }
}
