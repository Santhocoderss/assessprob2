pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                // Code checkout step goes here
            }
        }

        stage('Parallel Checks') {
            parallel {
                stage('Frontend Check') {
                    steps {
                        echo 'Starting frontend checks...'
                        // Jenkins native platform-independent sleep
                        sleep time: 4, unit: 'SECONDS'
                        
                        // Writes the file cleanly on Windows or Linux
                        writeFile file: 'frontend_report.txt', text: 'Frontend check completed successfully.'
                    }
                }
                stage('Backend Check') {
                    steps {
                        echo 'Starting backend checks...'
                        // Jenkins native platform-independent sleep
                        sleep time: 4, unit: 'SECONDS'
                        
                        // Writes the file cleanly on Windows or Linux
                        writeFile file: 'backend_report.txt', text: 'Backend check completed successfully.'
                    }
                }
            }
        }

        stage('Archive Reports') {
            steps {
                echo 'Archiving build artifacts...'
                archiveArtifacts artifacts: '*_report.txt', followSymlinks: false
            }
        }
    }
}
