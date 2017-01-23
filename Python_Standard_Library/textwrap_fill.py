

import textwrap
from textwrap_example import sample_text

print 'No dedent:\n'
print textwrap.fill(sample_text, width=80)




dedented_text = textwrap.dedent(sample_text)
print 'Dedented:'
print dedented_text


