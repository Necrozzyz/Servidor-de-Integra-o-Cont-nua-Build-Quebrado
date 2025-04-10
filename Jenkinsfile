pipeline {
    agent any

    environment {
        // Defina seu ambiente virtual, se necessário
        VENV = ".venv"
    }

    stages {
        stage('Preparar Ambiente') {
            steps {
                echo 'Instalando dependências...'
                sh 'python3 -m venv $VENV'
                sh './$VENV/bin/pip install --upgrade pip'
                sh './$VENV/bin/pip install -r requirements.txt'
            }
        }

        stage('Executar Testes') {
            steps {
                echo 'Executando testes...'
                sh './$VENV/bin/python -m pytest --maxfail=1 --disable-warnings -q'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finalizada.'
        }
        success {
            echo '✅ Build passou com sucesso!'
        }
        failure {
            echo '❌ Build falhou. Verifique os testes.'
        }
    }
}
