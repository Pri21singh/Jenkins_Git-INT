pipeline {
    agent any  // Runs on any available agent

    environment {
        VIRTUAL_ENV = 'venv'  // Virtual environment directory
        FLASK_APP = 'app.py'
    }

    parameters {
        booleanParam(name: 'DEPLOY_TO_SERVER', defaultValue: false, description: 'Deploy application after successful build')
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
                    sh '''
                        python3 -m venv $VIRTUAL_ENV
                        source $VIRTUAL_ENV/bin/activate && pip install --upgrade pip
                        source $VIRTUAL_ENV/bin/activate && pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    echo 'Building the application...'
                    sh '''
                        source $VIRTUAL_ENV/bin/activate
                        python --version
                    '''
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo 'Running tests...'
                    sh '''
                        source $VIRTUAL_ENV/bin/activate
                        pytest tests/ --disable-warnings --maxfail=3
                    '''
                }
            }
        }

        stage('Deploy') {
            when {
                expression { return params.DEPLOY_TO_SERVER }  
            }
            steps {
                script {
                    echo 'Deploying application...'
                    sh '''
                        source $VIRTUAL_ENV/bin/activate
                        nohup python -m flask run --host=0.0.0.0 --port=5000 > flask.log 2>&1 &
                        echo $! > flask.pid
                    '''
                }
            }
        }
    }

    post {
        success {
            script {
                echo "Build Successful!"
                emailext subject: "[SUCCESS] Build #${env.BUILD_NUMBER} - ${env.JOB_NAME}",
                         body: """<p><strong>Build Successful! 🎉</strong></p>
                                  <p>Project: ${env.JOB_NAME}</p>
                                  <p>Build Number: ${env.BUILD_NUMBER}</p>
                                  <p>View details: <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>""",
                         mimeType: 'text/html',
                         to: 'priyasingh2103@gmail.com'
            }
        }
        failure {
            script {
                echo "Build Failed!"
                emailext subject: "[FAILURE] Build #${env.BUILD_NUMBER} - ${env.JOB_NAME}",
                         body: """<p><strong>Build Failed! </strong></p>
                                  <p>Project: ${env.JOB_NAME}</p>
                                  <p>Build Number: ${env.BUILD_NUMBER}</p>
                                  <p>View details: <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>""",
                         mimeType: 'text/html',
                         to: 'priyasingh2103@gmail.com'
            }
        }
    }
}
