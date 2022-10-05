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