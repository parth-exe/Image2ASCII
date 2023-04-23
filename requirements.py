import subprocess
import os
subprocess.run(["pip", 
                "install", 
                "-r", 
                os.path.join('Image2ASCII', 
                             'requirements.txt')])