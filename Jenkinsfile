pipeline {
    agent { label 'jenkins-slave' }
    stages {
        stage('build') {
            steps {
                echo 'build'
                script{
                    if (BRANCH_NAME  == "release") {
                        withCredentials([usernamePassword(credentialsId: 'mariam-dockerHub', usernameVariable: 'USERNAME_ITI', passwordVariable: 'PASSWORD_ITI')]) {
                            sh '''
                                docker login -u ${USERNAME_ITI} -p ${PASSWORD_ITI}
                                docker build -t mariamkasssab/bakehouse:v${BUILD_NUMBER} .
                                docker push mariamkasssab/bakehouse:v${BUILD_NUMBER}
                                echo ${BUILD_NUMBER} > ../build.txt
                            '''
                     }
                    }
                    else {
                        echo "user choosed ${params.BRANCH_NAME}"
                    }
                }
            }
        }
        stage('deploy') {
            steps {
                echo 'deploy'
                script {
                    if (BRANCH_NAME  == "dev" || BRANCH_NAME == "test" || BRANCH_NAME  == "preprod") {
                        withCredentials([file(credentialsId: 'mariam-kubeconfig', variable: 'KUBECONFIG_ITI')]) {
                            sh '''
                                export BUILD_NUMBER=$(cat ../build.txt)
                                mv Deployment/deploy.yaml Deployment/deploy.yaml.tmp
                                cat Deployment/deploy.yaml.tmp | envsubst > Deployment/deploy.yaml
                                rm -f Deployment/deploy.yaml.tmp
                                Helm install app ./Deployment --values ${BRANCH_NAME}-values.yml --kubeconfig ${KUBECONFIG_ITI} --kubeconfig ${KUBECONFIG_ITI} -n ${BRANCH_NAME}
                             '''
                        }
                    }
                }
            }
        }
    }
}
