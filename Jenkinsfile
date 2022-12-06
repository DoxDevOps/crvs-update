pipeline {
  agent any
  stages {
    stage('Initializing') {
      steps {
        echo 'Initializing pipeline...'
      }
    }

    stage('') {
      steps {
        sh 'git clone git@github.com:EGPAFMalawiHIS/crvs.git'
      }
    }

  }
  options {
    skipStagesAfterUnstable()
  }
}