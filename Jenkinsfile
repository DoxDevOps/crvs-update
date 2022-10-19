pipeline {
  agent any
  stages {
    stage('Initializing') {
      steps {
        echo 'Initializing pipeline...'
      }
    }

    stage('Fetch and build frontend') {
      steps {
        echo 'Fetching frontend  from the repo'
        sh '[ -d "crvs_app" ] && echo "crvs front already cloned." || git clone  git@github.com:EGPAFMalawiHIS/crvs_app.git'
      }
    }

  }
  options {
    skipStagesAfterUnstable()
  }
}