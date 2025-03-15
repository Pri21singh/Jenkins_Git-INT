pipeline {
    agent any  // Runs on any available agent
    
    environment {
        VIRTUAL_ENV = 'venv'  // Virtual environment directory
        FLASK_APP = 'app.py'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    echo 'Cloning repository...'
                    checkout scm
                }
            }
        }

        stage('Setup Python') {
            steps {
                script {
                    echo 'Setting up Python environment...'
                    sh 'python3 -m venv $VIRTUAL_ENV'
                    sh 'source $VIRTUAL_ENV/bin/activate && pip install --upgrade pip'
                    sh 'source $VIRTUAL_ENV/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    echo 'Building the application...'
                    sh 'source $VIRTUAL_ENV/bin/activate && python --version'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo 'Running tests...'
                    sh 'source $VIRTUAL_ENV/bin/activate && pytest tests/'  // Adjust this to your test folder
                }
            }
        }

        stage('Deploy (Optional)') {
            when {
                expression { return params.DEPLOY_TO_SERVER == 'true' }  // Optional deployment toggle
            }
            steps {
                script {
                    echo 'Deploying application...'
                    sh 'source $VIRTUAL_ENV/bin/activate && flask run --host=0.0.0.0 --port=5000 &'
                }
            }
        }
    }

    post {
        success {
            script {
                echo "Build Successful!"
                emailext subject: "Build Success: ${env.JOB_NAME}",
                         body: "Build ${env.BUILD_NUMBER} succeeded! View details at: ${env.BUILD_URL}",
                         to: 'priyasingh2103@gmail.com'
            }
        }
        failure {
            script {
                echo "Build Failed!"
                emailext subject: "Build Failed: ${env.JOB_NAME}",
                         body: "Build ${env.BUILD_NUMBER} failed! View details at: ${env.BUILD_URL}",
                         to: 'priyasingh2103@gmail.com'
            }
        }
    }
}
