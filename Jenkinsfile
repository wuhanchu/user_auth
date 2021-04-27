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

        SERVER_DEV = "192.168.1.152"

        SERVER_TEST = "192.168.1.34"
        SQLALCHEMY_DATABASE_URI_TEST = "postgresql://postgres:dataknown1234@192.168.1.34:31014/dataknown"
        PROXY_SERVER_TEST = "http://192.168.1.34:40020"
        PORT_TEST  = "40016"
        CELERY_BROKER_TEST = "redis://:dataknown1234@server.aiknown.cn:31063"

    }

    stages {
        stage('READY') {
            steps{
                withDockerRegistry(registry: [url: "https://server.aiknown.cn:31003", credentialsId: 'harbor']) {
                      sh 'echo ${BRANCH_NAME}'
                      sh 'echo ${TAG_NAME}'
                      sh 'docker pull server.aiknown.cn:31003/z_ai_frame/alpine-python3:latest'
                }
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
                        sh 'docker build . -f ./Dockerfile  -t server.aiknown.cn:31003/${GROUP}/${PROJECT}:${BRANCH_NAME}'
                    }
                }

                stage('Docker Build Tag') {
                    when { buildingTag()}
                    steps{
                        sh 'docker build . -f ./Dockerfile  -t server.aiknown.cn:31003/${GROUP}/${PROJECT}:${TAG_NAME}'
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
                             sh "ssh  -t  root@${SERVER_DEV} -o StrictHostKeyChecking=no  'cd /root/project/maintenance_script && docker-compose -f ./compose/user_auth.yml -p dataknowon --env-file ./env/dataknown_dev.env pull &&  docker-compose -f ./compose/user_auth.yml -p dataknowon --env-file ./env/dataknown_dev.env up -d'"
                        }
                    }
                }


                stage('Deploy Test') {
                    when {
                        branch 'master'
                     }

                    steps {
                        sshagent(credentials : ['dataknown_test']) {
                             sh "ssh  -t  root@${SERVER_TEST} -o StrictHostKeyChecking=no  'docker pull server.aiknown.cn:31003/${GROUP}/${PROJECT}:${BRANCH_NAME} &&  docker rm -f  ${PROJECT}; docker run --restart=always -d -p ${PORT_TEST}:5000 -e PROXY_SERVER_URL=${PROXY_SERVER_TEST} -e SQLALCHEMY_DATABASE_URI=${SQLALCHEMY_DATABASE_URI_TEST}  -e CELERY_BROKER=${CELERY_BROKER_TEST}  -e FLASK_CONFIG=testing --name ${PROJECT} server.aiknown.cn:31003/${GROUP}/${PROJECT}:${BRANCH_NAME};'"
                        }
                    }
                }
            }
        }
    }
}
