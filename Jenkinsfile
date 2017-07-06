node('demo-host') {

    stage('Build App') {
        sh '''
            if [ -d /var/www/flask/demoapp]; then
                cd /var/www/flask/demoapp
                git pull
            else
                cd /var/www/flask/
                git clone https://github.com/abacl7/demoapp.git
            fi
        '''
    }

    stage('Reboot HTTPD') {
        sh 'sudo systemctl restart apache2'
    }

    stage('Test App') {
        echo 'Test succeed!'
    }

}
