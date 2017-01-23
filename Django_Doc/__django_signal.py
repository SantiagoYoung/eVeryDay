
import django.dispatch


delete_done = django.dispatch.Signal(providing_args=['obj'])



from django.db.models.signals import pre_save
from django.db import models
import logging


class Article(models.Model):
    title = models.CharField(max_length=2300)
    content = models.TextField()
    is_public = models.BooleanField(default=True, blank=True)

    def delete(self, using=None):
        delete_done.send(sender=Article, object=self)

    def __unicode__(self):
        return self.title

def zhutao(sender, **kwargs):
    logging.debug(kwargs)
    if 'obj' in kwargs:
        obj = kwargs.get('obj')
        logging.debug(obj.is_public)
        obj.is_public = False
        obj.save()
        logging.debug('jjj')
        logging.debug(obj.is_public)

delete_done.connect(zhutao, sender=Article)






def index(request):
    articles = Article.mro().all().order_by('id')
    return render_to_response('index.html',{'artialces':articles})

def add(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get("content", "")
        if title and content:
            article = Article(title=title, content=content)
            article.save()
            article.delete()
            return HttpResponseRedirect(reverse(index))
    return render_to_response("add.html", {})








































