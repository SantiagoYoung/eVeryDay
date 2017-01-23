
import subprocess



cat = subprocess.Popen(['cat', 'index.rst'],
                       stdout=subprocess.PIPE,)
grep = subprocess.Popen(['grep', '.. include::'],
                        stdin=cat.stdout,
                        stdout=subprocess.PIPE)
cut = subprocess.Popen(['cut', '-f', '3', '-d:'],
                       stdin=grep.stdout,
                       stdout=subprocess.PIPE,)

end_of_pipe = cut.stdout
print 'Include files:'
for line in end_of_pipe:
    print '\t', line.strip()

2 // "server": "v1.see-world.club",
3 // "server_port": 13474,
4
5
"server": "hk.server.sqzryang.com",
6
"server_port": 1433,
7
"local_address": "127.0.0.1",
8
"local_port": 1080,
9
10 // "password": "Nc5XrVow",
11
"password": "sqzr",
12 // "method": "aes-256-cfb",
13
"method": "chacha20",
14
"fast_open": true,
15
"workers": 1
