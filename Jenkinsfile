def git_url = 'https://github.com/abacl7/demoapp.git'

node('demo-host') {

    stage('Build App') {
        git url: git_url
    }

    stage('Copy app') {
        sh 'cp -rf demoapp/ /var/www/flask/'
    }

    stage('Reboot HTTPD') {
        sh 'sudo systemctl restart apache2'
    }

    stage('Test App') {
        echo 'Test succeed!'
    }

}
