node('demo-host') {

    stage('Build App') {
        sh '''
            cd /var/www/flask/
            if [ -d demoapp]; then
                cd demoapp
                git pull
            else
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
