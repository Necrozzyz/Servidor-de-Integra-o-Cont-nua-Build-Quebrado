pipeline {
    agent any
    stages {
        stage('Instalar dependências') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Executar testes') {
            steps {
                sh './venv/bin/python -m pytest tests/'
            }
        }
    }

    post {
        always {
            junit 'tests/**/test-*.xml'
        }
    }
}
