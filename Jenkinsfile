pipeline {
    agent any

    environment {
        VIRTUAL_ENV = 'venv'
        EC2_USER = 'ubuntu'  // ubuntu instance created
        EC2_INSTANCE_IP = '3.93.65.178'  // Replace with your EC2 instance's public IP
        SSH_KEY = credentials('EC2_SSH_PRIVATE_KEY')  // Private key stored in Jenkins credentials
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

        stage('Deploy to AWS EC2') {
            when {
                branch 'main'
            }
            steps {
                script {
                    sh """
                    echo "Deploying Python app to EC2..."

                    # Copy the application files to EC2 instance
                    scp -o StrictHostKeyChecking=no -i ${SSH_KEY} -r * ${EC2_USER}@${EC2_INSTANCE_IP}:/home/${EC2_USER}/app/

                    # Connect to EC2 and deploy the app
                    ssh -o StrictHostKeyChecking=no -i ${SSH_KEY} ${EC2_USER}@${EC2_INSTANCE_IP} << 'EOF'
                    cd /home/${EC2_USER}/app

                    # Set up virtual environment
                    python3 -m venv venv
                    source venv/bin/activate

                    # Install dependencies
                    pip install -r requirements.txt

                    # Kill any running instance of the app
                    pkill -f "python3 app.py" || true

                    # Start the application in the background
                    nohup python3 app.py > app.log 2>&1 &
                    EOF
                    """

                    echo "Deployment completed successfully!"
                }
            }
        }
    }

    post {
        success {
            mail to: 'priyasingh2103@gmail.com',
                 subject: 'Jenkins Build & Deployment Success',
                 body: "Build #${env.BUILD_NUMBER} was successful. The app is deployed on AWS EC2."
        }
        failure {
            mail to: 'priyasingh2103@gmail.com',
                 subject: 'Jenkins Build & Deployment Failure',
                 body: "Build #${env.BUILD_NUMBER} failed. Check logs for details."
        }
    }
}
