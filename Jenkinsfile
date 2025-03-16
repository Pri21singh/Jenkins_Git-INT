pipeline {
    agent any

    environment {
        VIRTUAL_ENV = 'venv'
        EC2_SSH_PRIVATE_KEY = credentials('ec2-ssh-key') // EC2 private key from Jenkins credentials
        EC2_USER = 'ubuntu' // Replace with the EC2 instance username
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
                        sh 'python3 -m venv venv'
                    }
                    sh 'source venv/bin/activate && pip install -r requirements.txt'
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
                    sh 'source venv/bin/activate && python3 -m unittest test_app.py'
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Python application to EC2...'

                withCredentials([sshUserPrivateKey(credentialsId: 'ec2-ssh-key', keyFileVariable: 'EC2_SSH_PRIVATE_KEY')]) {
                    sh '''
                        echo "$EC2_SSH_PRIVATE_KEY" > /tmp/deploy_key.pem
                        chmod 600 /tmp/deploy_key.pem
                        eval $(ssh-agent -s)
                        ssh-add /tmp/deploy_key.pem
                        ssh -i /tmp/deploy_key.pem $EC2_USER@$EC2_HOST "your deployment commands"
                        rm -f /tmp/deploy_key.pem
                    '''
                }
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
