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
        sh 'git clone  https://github.com/EGPAFMalawiHIS/crvs.git'
      }
    }

  }
  options {
    skipStagesAfterUnstable()
  }
}