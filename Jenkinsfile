pipeline{
  agent any
  environment {
        imageName = "docker-image"
        registryCredentials = "nexus"
        registry = "http://54.159.13.126:8085/"
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
  }
}
