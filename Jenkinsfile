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
        sh 'git clone git@github.com:EGPAFMalawiHIS/crvs.git'
      }
    }

  }
}