pipeline {
    triggers {
        pollSCM ('* * * * *')
    }

    agent {
        label 'master'
    }

    environment {
        GROUP = "z_ai_frame"
        PROJECT = "user_auth"

        SERVER_DEV = "192.168.1.150"
        PORT_DEV  = "32024"

        SERVER_TEST = "192.168.1.34"
        SQLALCHEMY_DATABASE_URI_TEST = "postgresql://postgres:dataknown1234@172.17.0.1:32021/dataknown"
        PROXY_SERVER_TEST = "http://172.17.0.1:40020"
        PORT_TEST  = "40016"
    }

    stages {
        stage('READY') {
            steps{
                sh 'echo ${BRANCH_NAME}'
                sh 'echo ${TAG_NAME}'
                sh 'docker pull frolvlad/alpine-python3'
            }
        }

        stage('Docker Build') {
            parallel {
                stage('Docker Build Branch') {
                     when {
                         anyOf {

                            branch 'master'
                            branch 'develop'
                        }
                    }
                    steps{
                        sh 'docker build . -f ./frame/docker/Dockerfile.source  -t server.aiknown.cn:31003/${GROUP}/${PROJECT}:${BRANCH_NAME}'
                    }
                }

                stage('Docker Build Tag') {
                    when { buildingTag()}
                    steps{
                        sh 'docker build . -f ./frame/docker/Dockerfile.source  -t server.aiknown.cn:31003/${GROUP}/${PROJECT}:${TAG_NAME}'
                    }
                }
            }
        }

        stage('Push') {
            when {
              expression {
                currentBuild.result == null || currentBuild.result == 'SUCCESS'
              }
            }

            parallel {
                stage('Push Branch') {
                    when {
                         anyOf {
                            branch 'master'
                            branch 'develop'
                        }
                    }
                    steps {
                        withDockerRegistry(registry: [url: "https://server.aiknown.cn:31003", credentialsId: 'harbor']) {
                            sh 'docker push server.aiknown.cn:31003/${GROUP}/${PROJECT}:${BRANCH_NAME}'
                            sh 'docker rmi server.aiknown.cn:31003/${GROUP}/${PROJECT}:${BRANCH_NAME}'
                        }
                    }
                }

                stage('Push Tag') {
                    when { buildingTag() }

                    steps{
                        withDockerRegistry(registry: [url: "https://server.aiknown.cn:31003", credentialsId: 'harbor']) {
                            sh 'docker push server.aiknown.cn:31003/${GROUP}/${PROJECT}:${TAG_NAME}'
                            sh 'docker rmi server.aiknown.cn:31003/${GROUP}/${PROJECT}:${TAG_NAME}'
                        }
                    }
                }
            }
        }

        stage('Deploy') {
            parallel {
                stage('Deploy Develop') {
                    when {
                        branch 'develop'
                     }

                    steps {
                        sshagent(credentials : ['dataknown_dev']) {
                             sh "ssh  -t  root@${SERVER_DEV} -o StrictHostKeyChecking=no  'docker pull server.aiknown.cn:31003/${GROUP}/${PROJECT}:${BRANCH_NAME} &&  docker rm -f  ${PROJECT}; docker run --restart=always -d -p ${PORT_DEV}:5000  --name ${PROJECT} server.aiknown.cn:31003/${GROUP}/${PROJECT}:${BRANCH_NAME};'"
                        }
                    }
                }


                stage('Deploy Test') {
                    when {
                        branch 'master'
                     }

                    steps {
                        sshagent(credentials : ['dataknown_test']) {
                             sh "ssh  -t  root@${SERVER_TEST} -o StrictHostKeyChecking=no  'docker pull server.aiknown.cn:31003/${GROUP}/${PROJECT}:${BRANCH_NAME} &&  docker rm -f  ${PROJECT}; docker run --restart=always -d -p ${PORT_TEST}:5000 -e PROXY_SERVER_URL=${PROXY_SERVER_TEST} -e SQLALCHEMY_DATABASE_URI=${SQLALCHEMY_DATABASE_URI_TEST} -e FLASK_CONFIG=testing --name ${PROJECT} server.aiknown.cn:31003/${GROUP}/${PROJECT}:${BRANCH_NAME};'"
                        }
                    }
                }
            }
        }
    }
}
