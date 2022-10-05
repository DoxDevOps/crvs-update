pipeline {
  agent any
  stages {
    stage('Initializing') {
      steps {
        sh 'make'
        echo 'Initializing pipeline...'
      }
    }

    stage('Test') {
      steps {
        echo 'Fetching apps from the repo'
      }
    }

    stage('Deploy') {
      steps {
        sh 'make publish'
      }
    }

  }
  options {
    skipStagesAfterUnstable()
  }
}