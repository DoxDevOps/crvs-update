pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'bundle install'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                sh 'rails test'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying to production...'
                sh 'ssh user@prodserver "cd /var/www/app && git pull"'
                sh 'ssh user@prodserver "cd /var/www/app && bundle install --without development test"'
                sh 'ssh user@prodserver "sudo systemctl restart app"'
            }
        }
    }
}
