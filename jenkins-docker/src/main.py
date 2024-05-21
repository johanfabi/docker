import os

def jenkins_build():
    print(f"Hello from Python - Jenkins Build {os.environ['BUILD_NUMBER']}")
    
jenkins_build()
    