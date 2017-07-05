node('master') {
    def python_path = '/var/www/flask/venv'

    stage('Clone') {
        checkout scm
    }

    stage('Copy') {
        sh 'echo copy'
    }

    stage('Test') {
        sh 'curl http://localhost/'
    }

}
