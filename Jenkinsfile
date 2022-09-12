stage('Docker Nexus Auth'){
sh 'docker login -u admin -p admin 3.84.61.0:8085'
}

stage('Push Docker Images to Nexus Registry'){
sh 'docker push http://3.84.61.0:8081/repository/task01/}'
sh 'docker rmi $(docker images --filter=reference="http://3.84.61.0:8081/repository/task01/*" -q)'
sh 'docker logout http://3.84.61.0:8081/repository/task01/'
}
