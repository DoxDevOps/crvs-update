def servers = ['10.46.0.47', '10.46.0.48']
pipeline {
  agent any
  stages {
    stage('Initialize') {
      steps {
        echo 'Initializing...'
      }
    }
    stage('Deploy') {
      steps {
        echo 'Deploying to production...'
        script {
          for (int i = 0; i < servers.size(); i++) {
            def server = servers[i]
            sh "ssh nbapp-user@${server} 'cd /var/www/app && git pull'"
            sh "ssh nbapp-user@${server} 'cd /var/www/app && bundle install --without development test'"
            sh "ssh nbapp-user@${server} 'cd /var/www/app && rake db:migrate RAILS_ENV=production'"
            sh "ssh nbapp-user@${server} 'sudo systemctl restart app'"
          }
        }

      }
    }

  }
}
