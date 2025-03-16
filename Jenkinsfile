pipeline {
    agent any

    environment {
        VIRTUAL_ENV = 'venv'
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
                    sh 'source venv/Scripts/activate && pip install -r requirements.txt'a
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
                    sh '''
                        source venv/Scripts/activate && python -m unittest test_app.py
                    '''
                }
            }
        }

      /**  stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                echo 'Deploying Python application...'
            }
       }**/
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
