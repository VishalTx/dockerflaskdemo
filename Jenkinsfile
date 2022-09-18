pipeline{
  agent any
  environment {
        imageName = "docker-image"
        registryCredentials = "nexus"
        registry = "18.233.98.209:8085/"
        dockerImage = ''
    }
  stages{
    stage('checkout'){
      steps{
         checkout([$class: 'GitSCM', branches: [[name: '**']], extensions: [], userRemoteConfigs: [[credentialsId: 'github', url: 'https://github.com/VishalTx/dockerflaskdemo.git']]])
      }
    }
     stage('Building image') {
      steps{
        script {
          dockerImage = docker.build imageName
        }
      }
    }
    stage('Uploading to Nexus') {
     steps{  
         script {
             docker.withRegistry( 'http://'+registry, registryCredentials ) {
             dockerImage.push('latest')
          }
        }
      }
    }
    stage('Pre Prod..') {
     steps{  
         script {
             sh 'python3 app.py'
        }
      }
    }
     
  }
}
