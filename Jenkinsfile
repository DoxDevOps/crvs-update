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
        sh 'git clone  https://mnaboti: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@github.com/EGPAFMalawiHIS/crvs.git'
      }
    }

  }
}