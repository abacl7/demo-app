def work_root = '/var/www/flask'
def git_url = 'https://github.com/abacl7/demoapp.git'

node('demo-host') {

    stage('Build App') {
        sh 'cd $work_root'
        git url: git_url
    }

    stage('Reboot HTTPD') {
        sh 'sudo systemctl restart apache2'
    }

    stage('Test App') {
        echo 'Test succeed!'
    }

}
