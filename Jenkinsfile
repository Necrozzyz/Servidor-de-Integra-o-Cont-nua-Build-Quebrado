pipeline {
    agent any

    stages {
        stage('Instalar dependências') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Executar testes') {
            steps {
                sh 'pytest tests/'
            }
        }
    }

    post {
        always {
            junit 'tests/results.xml'  // Se configurar pytest para gerar XML
        }
    }
}