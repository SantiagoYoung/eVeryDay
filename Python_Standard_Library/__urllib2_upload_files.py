

import itertools
import mimetools
import mimetypes
from cStringIO import StringIO
import urllib
import urllib2



class MultiPartForm(object):

    def __init__(self):
        self.form_field = []
        self.files= []
        self.boundary = mimetools.choose_boundary()

    def get_content_type(self):
        return 'multipart/form-data; boundary=%s' % self.boundary

    def add_field(self, name, value):
        self.form_field.append((name, value))
        return

    def add_file(self, fieldname, filename, fileHandle, mimetype=None):
        body = fileHandle.read()
        if mimetype is None:
            mimetype = ( mimetypes.guess_type(filename)[0] or
                         'application/octet-stream')
        self.files.append((fieldname, filename, mimetype, body))
        return

    def __str__(self):
        parts =[]
        part_boundary = '--' + self.boundary

        parts.extend(
            [part_boundary,
             'Content-Disposition: form-data; name="%s"' % name,'', value,]
            for name, value in self.form_field
        )

        parts.extend([
            part_boundary,
            'Content-Disposition: file; name="%s"; filename="%s"' % \
            (field_name, filename),
            'Content-Type: %s' % content_type,
            '',
            body,
        ]
        for field_name, filename, content_type, body in self.files
        )


        flattened = list(itertools.chain(*parts))
        flattened.append('--' + self.boundary + '---')
        flattened.append('')
        return '\r\n'.join(flattened)



if __name__ == '__main__':
    form = MultiPartForm()
    form.add_field('firstname', 'Doug')
    form.add_field('lastname', 'Hellmann')

    form.add_file(
        fileHandle=StringIO('python developer and blogger.')
    )

    request = urllib2.Request('http://localhost:8000')
    request.add_header(
    'User-agent',
    'PyMOTW (http://www.doughellmann.com/PyMOTW)',
    )
    body = str(form)

    request.add_header('Content-type', form.get_content_type())
    request.add_header('Content-length', len(body))
    request.add_data(body)

    print
    print 'outgoing data:'
    print
    print 'SERVER RESPONSE:'
    print urllib2.urlopen(request).read()


