

from Queue import Queue
from threading import Thread
import time
import urllib
import urlparse

import feedparser

num_fetch_threads = 2
enclosure_queue = Queue()



feed_urls = [
    'http://advocacy.python.org/podcasts/littlebit.rss',
]



def downloadEnclosures(i, q):

    while 1:
        print '%s: Looking for the next enclosure.'
        url  = q.get()
        parsed_url = urlparse.urlparse(url)
        print '%s: Downloading:' % i, parsed_url.path
        response = urllib.urlopen(url)
        data = response.read()

        outfile_name = url.rpartition('/')[-1]
        with open(outfile_name, 'wb') as outfile:
            outfile.write(data)
        q.task_done()



for i in range(num_fetch_threads):
    worker = Thread(target=downloadEnclosures, args=(i, enclosure_queue))
    worker.setDaemon(True)
    worker.start()


for url in feed_urls:

    response = feedparser.parse(url, agent='fetch')















