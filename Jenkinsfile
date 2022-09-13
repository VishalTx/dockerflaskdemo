pipeline{
  agent any
  environment {
        imageName = "docker-image"
        registryCredentials = "nexus"
        registry = "http://3.82.121.146:8085/"
        dockerImage = ''
    }
  stages{
    stage('checkout'){
      steps{
         checkout([$class: 'GitSCM', branches: [[name: '**']], extensions: [], userRemoteConfigs: [[credentialsId: 'github', url: 'https://github.com/VishalTx/dockerflaskdemo.git']]])
      }
    }
    stage('Build image') {
      steps{
        script{
               dockerImage = docker.build ("getintodevops/hellonode")
        
      }
    }
  }
}
}
