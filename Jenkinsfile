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
        sh 'make check'
        junit 'reports/**/*.xml'
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