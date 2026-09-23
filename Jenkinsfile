pipeline {
    agent any

    stages {
        // 1. Checkout Stage
        stage('Checkout') {
            steps {
                echo 'Pulling the latest code from repository...'
                // If using a Pipeline from SCM, Jenkins automatically clones your repository here
            }
        }

        // 2. Parallel Checks Stage
        stage('Parallel Checks') {
            parallel {
                stage('Frontend Execution') {
                    steps {
                        echo 'Launching Frontend Script...'
                        // Executes the python script
                        sh 'python3 frontend_check.py' 
                    }
                }
                stage('Backend Execution') {
                    steps {
                        echo 'Launching Backend Script...'
                        // Executes the python script
                        sh 'python3 backend_check.py'
                    }
                }
            }
        }

        // 3. Archive Reports Stage
        stage('Archive Reports') {
            steps {
                echo 'Persisting report artifacts...'
                // Archives both text files so they are saved long-term
                archiveArtifacts artifacts: 'frontend_report.txt, backend_report.txt', allowEmptyArchive: false
            }
        }
    }
}
