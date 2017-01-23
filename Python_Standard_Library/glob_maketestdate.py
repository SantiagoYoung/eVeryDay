

import os
import subprocess
# print os.getcwd()
# os.makedirs('dir')
subprocess.call(['cd','/home/neon/eVeryDay/Python_Standard_Library/dir'])
subprocess.call(['touch', 'file.txt'])
subprocess.call(['touch', 'file1.txt'])
subprocess.call(['touch', 'file2.txt'])
subprocess.call(['touch', 'filea.txt'])
subprocess.call(['touch', 'fileb.txt'])
subprocess.call(['cd', '/home/neon/eVeryDay/Python_Standard_Library/dir/subdir'])
subprocess.call(['touch', 'subfile.txt'])
# os.makedirs('dir/subdir')
