pipeline {
  agent any
  stages {
    stage('Initializing') {
      steps {
        echo 'Initializing pipeline...'
      }
    }

    stage('Fetching CRVS front') {
      steps {
        sh 'git clone git@github.com:EGPAFMalawiHIS/crvs_app.git'
      }
    }

  }
  options {
    skipStagesAfterUnstable()
  }
}