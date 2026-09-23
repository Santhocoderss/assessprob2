pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
            }
        }

        stage('Parallel Checks') {
            parallel {
                stage('Frontend Check') {
                    steps {
                        echo 'Starting frontend checks...'
                        // Simulating the 4-second delay and report creation on Windows
                        bat '''
                            timeout /t 4 /nobreak
                            echo Frontend check passed > frontend_report.txt
                        '''
                    }
                }
                stage('Backend Check') {
                    steps {
                        echo 'Starting backend checks...'
                        bat '''
                            timeout /t 4 /nobreak
                            echo Backend check passed > backend_report.txt
                        '''
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
