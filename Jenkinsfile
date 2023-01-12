pipeline{
  agent any
  environment {
  PATH = "{$path}:${getTerraformPath()}"
}

stages{
  stage('terraform init'){
    steps{
      sh 'terraform init'
      sh 'terraform apply -auto-approve'
    }
  }
  
  }
  }
  def getTerraformPath(){
  tfHome = tool name: 'terraform', type: 'terraform'
  return tfHome
  }


pipeline {
  agent any
  stages {
   stage('Terminate Machine') {
      steps {
        script {
          sh(script: 'aws lambda invoke  --function-name terminate-instance --payload  '{"private_ip_address":"${instance_ip}" }')          
        }            
      }
    }
  }
}  
