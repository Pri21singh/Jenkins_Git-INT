pipeline {
    agent any

    environment {
        VIRTUAL_ENV = 'venv'
        EC2_SSH_PRIVATE_KEY = credentials('ec2-ssh-key')
        EC2_USER = 'ubuntu'  // Replace with the EC2 instance username
        EC2_HOST = '3.93.65.178' // Replace with the EC2 instance's public IP or hostname
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
            }
            steps {
                echo 'Deploying Python application to EC2...'

                // sh-agent running in the environment
                sh """
                    eval \$(ssh-agent -s)
                    echo "$EC2_SSH_PRIVATE_KEY" | tr -d '\r' | ssh-add -
                    ssh -o StrictHostKeyChecking=no -i ${SSH_KEY} ${EC2_USER}@${EC2_HOST} << EOF C:/Users/singp/OneDrive/Desktop/CICD/Jenkins_Git-INT
                    git pull origin main  #  Pull the latest changes from my Git repository
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