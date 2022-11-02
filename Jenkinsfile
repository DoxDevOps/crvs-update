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
        sh 'git remote set-url origin https://zio-git:squ_24ecf95eacc1cac4121ea3cdd917e69dc966eb75@github.com/zio-git/EGPAFMalawiHIS/crvs_app.git'
        sh 'git clone https://github.com/EGPAFMalawiHIS/crvs_app.git'
      }
    }

  }
  options {
    skipStagesAfterUnstable()
  }
}