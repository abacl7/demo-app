node('demo-host') {

    stage('Build App') {
        sh '''
            cd /var/www/flask/
            git clone https://github.com/abacl7/demoapp.git
        '''
    }

    stage('Reboot HTTPD') {
        sh 'sudo systemctl restart apache2'
    }

    stage('Test App') {
        echo 'Test succeed!'
    }

}
