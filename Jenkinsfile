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
    stage('Push Docker Images to Nexus Registry'){
    sh 'docker login -u admin -p admin 3.82.121.146:8085'
    sh 'docker push 3.82.121.146:8085/cce2d2bedfe8}'
    sh 'docker rmi $(docker images --filter=reference="3.82.121.146:8085/cce2d2bedfe8*" -q)'
    sh 'docker logout 3.82.121.146:8085'
         }
        
      }
    }
  }
}
}
