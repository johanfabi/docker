import os

def jenkins_build():
    print(f"Hello from {os.environ['BUILD_NUMBER']}")
    
jenkins_build()
    