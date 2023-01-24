pipeline {
  agent any
  stages {
    stage('Initialize') {
      steps {
        echo 'Intitializing...'
      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploying to production...'
        sh 'ssh nbapp-user@10.46.0.48 "cd /var/www/app && git pull"'
        sh 'ssh nbapp-user@10.46.0.48 "cd /var/www/app && bundle install --without development test"'
        sh 'ssh nbapp-user@10.46.0.48 "sudo systemctl restart nginx"'
      }
    }

  }
}