


class EmailThread(threading.Thread):
    def __init__(self, subject, body, sender, receiver, fail_silent, html):

        self.subject = subject
        self.body = body
        self.receiver = receiver
        self.sender = sender
        self.fail_silent = fail_silent
        self.html = html
        super(EmailThread, self).__init__()

    def run(self):
        while 1:
            msg = EmailMultiAlternative(self.subject, self.body, self.sender,
                                        self.receiver)
            if self.html:
                msg.attach_alternative(self.body, self.html)
            msg.send()
def send_mail(subject, body, from_email, recipient_list, fail_silently=False, html=None, *args, **kwargs):
　　EmailThread(subject, body, from_email, recipient_list, fail_silently, html).start()



def send_mail(subject, body, from_email, recipient_list, fail_silently=False, html=None, *args, **kwargs):
　　EmailThread(subject, body, from_email, recipient_list, fail_silently, html).start()























