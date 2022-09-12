pipeline{
  agent any
  environment {
        imageName = "docker-image"
        registryCredentials = "nexus"
        registry = "http://54.165.226.72:8085/"
        dockerImage = ''
    }
  stages{
    stage('checkout'){
      steps{
         checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '', url: 'https://github.com/VishalTx/dockerflaskdemo.git']]])
      }
    }
    stage('Build image') {
      steps{
        script{
                dockerImage = docker.build imageName
        
      }
    }
  }
}
}
