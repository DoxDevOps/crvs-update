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
        sh '[ -d "crvs_app" ] && echo "crvs front already cloned." || git clone git@github.com:EGPAFMalawiHIS/crvs_app.git'
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