pipeline {
  agent any
  stages {
    stage('Initializing') {
      steps {
        sh 'make'
        echo 'Initializing pipeline...'
      }
    }

    stage('Fetching frontend') {
      steps {
        echo 'Fetching frontend  from the repo'
      }
    }

    stage('Fetching Backend from the repo') {
      steps {
        echo 'Fetching Backend from the repo '
      }
    }

  }
  options {
    skipStagesAfterUnstable()
  }
}