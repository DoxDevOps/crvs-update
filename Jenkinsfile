pipeline {
  agent any
  stages {
    stage('Initialize') {
      steps {
        echo 'Intitializing...'
      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploying to production...'
        sh '#python3 setup.py'
        sh '''[ -d "crvs" ] && echo "API already cloned." || git clone https://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@github.com/EGPAFMalawiHIS/crvs.git
'''
      }
    }

  }
}