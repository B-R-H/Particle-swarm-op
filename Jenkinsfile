pipeline{
        agent any
        stages{
            stage('Run App'){
                steps{
                    sh "docker stack deploy --compose-file docker-swarm.yaml pso"
                }
            }
        }    
}