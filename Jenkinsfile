pipeline {
  agent any
  stages {
    stage('Initializing') {
      steps {
        sh 'make'
        echo 'Initializing pipeline...'
      }
    }

    stage('Fetch and build frontend') {
      steps {
        echo 'Fetching frontend  from the repo'
      }
    }

    stage('Fetching Backend ') {
      steps {
        echo 'Fetching Backend from the repo '
      }
    }

  }
  options {
    skipStagesAfterUnstable()
  }
}