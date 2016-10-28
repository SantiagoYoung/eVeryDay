

import re
import os

query = re.compile('\w+')


word_list = []
for text in os.listdir('filepath'):
    with open('text.txt', 'r') as f:
        content = f.read()
        result = query.findall(content)
        summary= {}
        for word in result:
            if not summary.get(word):
                summary[word] = 1
            else:
                summary[word] += 1

        final = sorted(summary.items(), key=lambda x: x[word], reverse=True)[0]

        word_list.append(final)



