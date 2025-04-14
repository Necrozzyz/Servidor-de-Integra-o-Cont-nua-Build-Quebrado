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
            }
        }

        stage('Executar testes') {
            steps {
                sh './venv/bin/pytest tests/'
            }
        }
    }

    post {
        always {
            junit 'tests/results.xml'  // Se configurar pytest para gerar XML
        }
    }
}
