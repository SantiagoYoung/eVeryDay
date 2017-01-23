
import os
import os.path


os.chdir('/tmp')
for path in ['.','..', './one/two/three', '../one/two/three',]:
    print '%17s : "%s"' %(path, os.path.abspath(path))
