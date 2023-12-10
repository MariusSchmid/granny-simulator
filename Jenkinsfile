pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            agent {
                // Equivalent to "docker build -f Dockerfile.build --build-arg version=1.0.2 ./build/
                dockerfile {
                    filename 'unittest.Dockerfile'
                    dir 'docker/unittest/'
                    args '-v ${PWD}:/data'
                }
            }
            steps {
                    sh 'echo Testing..'
                    sh 'pip3 install -r requirements.txt'
                    sh 'python3 -m pytest --junitxml=./test.xml || true'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}