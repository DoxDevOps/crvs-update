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
        sh 'git clone -f https://mnaboti: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@github.com/EGPAFMalawiHIS/crvs.git'
      }
    }

  }
}