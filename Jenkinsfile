pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                // Code checkout step goes here (e.g., git checkout)
            }
        }

        stage('Parallel Checks') {
            parallel {
                stage('Frontend Check') {
                    steps {
                        echo 'Starting frontend checks...'
                        // Simulating python frontend_check.py execution
                        sh '''
                            sleep 4
                            echo "Frontend check passed" > frontend_report.txt
                        '''
                    }
                }
                stage('Backend Check') {
                    steps {
                        echo 'Starting backend checks...'
                        // Simulating python backend_check.py execution
                        sh '''
                            sleep 4
                            echo "Backend check passed" > backend_report.txt
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
