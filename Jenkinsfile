pipeline {
    agent{
        docker{
        args '-e "HOME=/Users/anastasiiamonakhova/.jenkins/workspace/pytest_allure_jenkins"'
        image 'python:3'
        }
    }
  stages {
         stage('get_code') {
            steps {
                 sh 'rm -r *'
                 sh 'git clone https://github.com/an-mengqi/pytest_allure_jenkins.git'
            }
         }
    stage('install_requirements') {
      steps {
        sh 'pip install --user -r pytest_allure_jenkins/requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python -m pytest pytest_allure_jenkins/tests/test_maths.py'
      }
    }
  }
}
