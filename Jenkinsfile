pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Necrozzyz/Servidor-de-Integra-o-Cont-nua-Build-Quebrado.git'
            }
        }

        stage('Instalar dependências') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
                sh './venv/bin/pytest src/'
            }
        }

        stage('Executar testes') {
            steps {
                sh '''
                export PYTHONPATH=$(pwd)/src
                ./venv/bin/pytest tests/
                '''
            }
        }

        stage('Gerar relatório de testes') {
            steps {
                sh '''
                export PYTHONPATH=$(pwd)/src # Garante que o PYTHONPATH esteja correto para gerar o relatório também
                ./venv/bin/pytest tests/ --junitxml=tests/results.xml
                '''
            }
        }

    }

    post {
        always {
            junit 'tests/results.xml'
        }
    }
}