from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField(null=True,blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True,blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog,null=True,blank=True)
    headline = models.CharField(max_length=255,null=True,blank=True)
    body_text = models.TextField(null=True,blank=True)
    pub_date = models.DateField(null=True,blank=True)
    mod_date = models.DateField(null=True,blank=True)
    authors = models.ManyToManyField(Author,null=True,blank=True)
    n_comments = models.IntegerField(null=True,blank=True)
    n_pingbacks = models.IntegerField(null=True,blank=True)
    rating = models.IntegerField(null=True,blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.headline




one_entry = Entry.objects.get(pk=1)
Entry.objects.all()[:5]
Entry.objects.order_by('headline')[0] == Entry.objects.order_by('headline')[0:1].get()
Entry.objects.filter(pub_date__lt='2006-01-01')

Entry.objects.get(headline__exact='Man bites dog')

Blog.objects.get(id__exact=14)
Blog.objects.get(id=14)

Blog.objects.get(name__iexact='beatles blog')
Entry.objects.get(headline__contains='lennon')
Entry.objects.get(headline__icontains='lennon')

Entry.objects.filter(blog__name='Beatles Blog')
Blog.objects.filter(entry__headline__contains='lennon')
Blog.objects.filter(entry__authors__name='lennon')

Blog.objects.filter(entry__authors__name__isnull=True)

Blog.objects.filter(entry__authors__isnull=False,
					entry__authors__name=True)

#############
Blog.objects.filter(entry__headline__contains='lennon',
					enter__pub_date__year=2008)

Blog.objects.filter(entry__headline__contains='lennon').filter(
					entry__pub_date__year=2008)

Blog.objects.exclude(
					entry__headline__contains='lennon',
					entry__pub_date__year=2008,)
Blog.objects.exclude(
					entry=Entry.objects.filter(
						headline__contains='lennon',
						pub_date__year=2008))

from django.models.db import F
Entry.objects.filter(n_comments__gt=F('n_pingbacks')*2)

Entry.objects.filter(rating__lt=F('n_comments')+F('n_pingbacks'))

Entry.objects.filter(authors__name = F('blog__name'))

Entry.objects.filter(mod_date__gt=F('pub_date') + timedelta(days=3))

***********************************************************
Blog.objects.get(id__exact=14)
Blog.objects.get(id=14)
Blog.objects.get(pk=14)

Blog.objects.filter(pk__in=[1,4,7])
Blog.objects.filter(pk__gt=14)

Entry.objects.filter(blog__id__exact=3)
Entry.objects.filter(blog__id=3)
Entry.objects.filter(blog__pk=3)


****************************************
print( [e.headline for e in Entry.objects.all()] )
print( [e.pub_date for e in Entry.objects.all()] )
##########
queryset = Entry.objects.all()
print( [ p.headline for p in queryset ])
print( [ p.pub_date for p in queryset ])
##########
*****************************************
queryset = Entry.objects.all()
print queryset[5]
print queryset[5]

queryset = Entry.objects.all()
[ entry for entry in queryset ]
print queryset[5]
print queryset[5]

*******************************************
from django.models.db import Q 
Q(question__startwith='What')

Q(question__startwith="Who") | Q(question__startwith='What')

Q(question__startwith='Who') | ~Q(pub_date__year=2005)

Poll.objects.get(
	Q(question__startwith='Who'),
	Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6)))
#right
Poll.objects.get(
	Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6)),
	question__startwith='Who')
# wrong
#Invalid query
Poll.objects.get(
	question__startwith='Who',
	Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 9, 2)))
****************************************************************
#比较对象
some_entry == other_entry
some_entry.id == other_entry.id

# delete 

e.delete()

Entry.objects.all().delete()
Entry.objects.filter(pub_date__year=2005).delete()

###拷贝模型实力
blog = Blog(name='My blog',tagline='Blogging is easy')
blog.save() ---- blog.pk=1

blog.pk = None
blog.save() ---- blog.pk=2


###
Entry.objects.filter(pub_date__year=2007).update(headline='Everything is the same')

Entry.objects.all().update(n_pingbacks=F('n_pingbacks')+1)


##一对多关系
e = Entry.objects.get(id=2)
e.blog

e = Entry.objects.get(id=2)
e.blog = some_blog
e.save()

***********************
e = Entry.objects.get(id=2)
print (e.blog)
print (e.blog)

e = Entry.objects.select_related().get(id=2)
print (e.blog)
print (e.blog)

***********************

#反向查询

b = Blog.objects.get(id=1)
b.entry_set.all()

b.entry_set.filter(headline__contains='lennon')
b.entry_set.count()


***************************
from django.db import models

class Entry(models.Model):
	objects = models.Manager()
	entries = EntryManager()

b = Blog.objects.get(id=1)

b.entry_set(manager='entries').all()
b.entry_set(manager='entries').is_published()

**********************************************
e = Entry.objects.get(id=3)
e.authors.all()
e.authors.count()
e.authors.filter(name__contains="Jhon")

*********************************************

# 查询集求值 hit database
for e in Entry.objects.all():
    print(e.headline)

if Entry.objects.filter(headline="Test"):
    print 'there is at least one entry '

************
# Pickle 
import pickle
query = pickle.loads(s)
qs = MyModel.objects.all()
qs.query = query

*******************
from django.db.models import Count
q = Blog.objects.annotate(Count('entry'))
q[0].name
q[0].entry__count

q = Blog.objects.annotate(number_of_entries=Count('entry'))
q[0].number_of_entries

Entry.objects.filter(pub_date__year=2005).order_by('-pub_date',
        'headline')
Entry.objects.order_by('?')

Entry.objects.order_by('blog__name', 'headline')

Entry.objects.order_by('blog')
== Entry.objects.order_by('blog_id')

Entry.objects.order_by(Coalesce('summary','headline').desc())

********************************
class Event(Model):
    parent = models.ForeignKey('self',related_name='children')
    date = models.DateField()

Event.objects.order_by('children__date')
****************************

Entry.objects.order_by(Lower('headline').desc())

Entry.objects.order_by('headline').order_by('pub_date')

# reverse
my_queryset.reverse()[:5]

#distinct

Author.objects.distinct()

Entry.objects.order_by('pub_date').distinct('pub_date')


# values
Blog.objects.filter(name__startswith='Beatles')
Blog.objects.filter(name__startswith='Beatles').values()

Blog.objects.values()
Blog.objects.values('id','name')

Entry.objects.values()
Entry.objects.values('blog')
Entry.objects.values('blog_id')

Blog.objects.values().order_by('id')
Blog.objects.order_by('id').values()

# OTO , ForeignKey , M2M
Blog.objects.values('name','entry_-headline')

# values_list
Entry.objects.values_list('id', 'headline')
[(1,'first entry'),...]

Entry.objects.values_list('id').order_by('id')
[(1,),(2,),(3,),...]
Entry.objects.values_list('id',flat=True).order_by('id')
[1, 2, 3,..]


Entry.objects.datess('pub_date', 'year')
[datetime.date(2005, 1, 1)]
Entry.objects.dates('pub_date','month')
Entry.objects.dates('pub_date','day')
Entry.objects.dates('pub_date','day',order='DESC')
Entry.objects.filter(headline__contains'lennon').dates('pub_date', 'day')

# none 
Entry.objects.none()
[]

from django.db.models.query import EmptyQuerySet
isinstance(Entry.objects.none(), EmptyQuerySet)
True

# all


#select_related
e = Entry.objects.select_related('blog').get(id=5)

b = e.blog

from django.utils import timezone
blogs =- set()

for e in Entry.objects.filter(pub_date__gt=timezone.now()).select_related('blog'):
    blogs.add(e.blog)

**
Entry.objects.filter(pub_date__gt=timezone.now()).select_related('blog')
Entry.objects.select_related('blog').filter(pub_date__gt=timezone.now())
**

b = Book.objects.select_related('author__hometown').get(id=4)
p = b.author  #don't hit the database
c = p.hometown #don't hit the database

b = Book.objects.get(id=4)
p = b.author # hit the database
c = p.hometown # hit the database

## prefetch_related
#########################################################################################
from django.db import models

class Topping(models.Model):
    name = models.CharField(max_length=30)

class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):              # __unicode__ on Python 2
        return "%s (%s)" % (self.name, ", ".join(topping.name
                                                 for topping in self.toppings.all()))


Pizza.objects.all()

Pizza.objects.all().prefetch_related('toppings')

pizzas = Pizza.objects.prefetch_related('toppings')
[list(pizza.toppings.filter(spicy=True)) for pizza in pizzas]

*****************************************************
class Restaurant(models.Model):
    pizzas = models.ManyToMany(Pizza, related_name='restaurants')
    best_pizza = models.ForeignKey(Pizza, related_name='championed_by')
# 3 database queries
Restaurant.objects.prefetch_related('pizzas_toppings')
Restaurant.objects.prefetch_related('best_pizza__toppings')

Restaurant.objects.select_related('best_pizza').prefetch_related('best_pizza__toppings')

### extra 

Entry.objects.extra(select={'is_recent':'pub_date > "2006-01-01"'})

Blog.objects.extra(
    select={
    'entry_count':'SELECT COUNT(*)  FROM blog_entry WHERE blog_entry.blog_id = blog_blog.id'
    },)



# defer
Entry.objects.defer('headline', 'body')

Entry.objects.defer('body').filter(rating=5).defer('headline')
Blog.objects.select_related().defer('entry__headline','entry__body')

#only 
Person.objects.defer('age', 'biography')
Person.objects.only('name')
Person.objects.only('body','rating').only('headline')

#using
# queries the database with the 'default' alias.
>>> Entry.objects.all()

# queries the database with the 'backup' alias
>>> Entry.objects.using('backup')



###  get(**kwargs)
Entry.objects.get(id='foo')  # raise Entry.DoesNotExist 

from django.core.exceptions import ObjectDoesNotExist
try:
    e = Entry.objects.get(id=3)
    b = Blog.objects.get(id=1)
except ObjectDoesNotExist:
    print "Either the entry or blog doesn't exist"


##create 
p  =  Person.objects.create(first_name='Bruce', last_name='Springsteen')

p = Person(first_name='Bruce', last_name='Springsteen')
p.save(force_insert=True)

# get_or_create

try:
    obj = Person.objects.get(first_name='Jhon', last_name='Lennon')
except Person.DoesNotExist:
    obj = Person(first_name='john', last_name='lennon', birthday=date(1940, 10, 9))
    obj.save()

obj, created = Person.objects.get_or_create(first_name='Jhon', last_name='Lennon', 
        defaults={'birthday'; date(1940, 10, 9)}
    })

# update_or_create

obj, created = Person.objects.update_or_create(
    first_name='john', last_name='lennon', defaults=updated_values)


## bulk_create
>>> Entry.objects.bulk_create([
...     Entry(headline="Django 1.0 Released"),
...     Entry(headline="Django 1.1 Announced"),
...     Entry(headline="Breaking: Django is awesome")
... ])

# count
Entry.objects.count()
Entry.objects.filter(headline__contains='lennon').count()

#in_bulk
>>> Blog.objects.in_bulk([1])
{1: <Blog: Beatles Blog>}
>>> Blog.objects.in_bulk([1, 2])
{1: <Blog: Beatles Blog>, 2: <Blog: Cheddar Talk>}
>>> Blog.objects.in_bulk([])
{}

# latest

Entry.objects.latest('pub_date')

# first()
p = Article.objects.order_by('title', 'pub_date').first()


# aggregate
>>> from django.db.models import Count
>>> q = Blog.objects.aggregate(Count('entry'))
{'entry__count': 16}


>>> q = Blog.objects.aggregate(number_of_entries=Count('entry'))
{'number_of_entries': 16}

# update
Entry.objects.filter(pub_date__year=2010).update(comments_on = False)
>>> Entry.objects.filter(pub_date__year=2010).update(comments_on=False, headline='This is old')

You can’t do this, for example:
>>> Entry.objects.update(blog__name='foo') # Won't work!
Filtering based on related fields is still possible, though:
>>> Entry.objects.filter(blog__id=1).update(comments_on=True)




# range 
import datetime
start_date = datetime.date(1090, 1, 1)
end_date = datetime.date(2300, 2, 32)
Entry.objects.filter(pub_date__range=(start_date, end_date))



# 聚合查询
Book.objects.count()

Book.objects.filter(publisher__name="BaloneyPress").count()

from django.db.models import Avg
Book.order_by.all().aggregate(Avg('price'))
{'price__avg': 34.35}

from django.db.models import Max, Sum
Book.objects.all().aggregate(Max('price'))
{'price__max': Decimal('81.20')}

Book.objects.all().aggregate(
    price_per_page = Sum(F('price')/F('page'),output_field=FloatField()))
{'price_per_page': 0.4470664529184653}

from django.db.models import Count
pubs = Publisher.objects.annotate(num_books=Count('book'))
>>> pubs
[<Publisher BaloneyPress>, <Publisher SalamiPress>, ...]
>>> pubs[0].num_books
73

***************
Book.objects.all().aggregate(Avg('price'))s
Book.objects.aggregate(Avg('price'))
Book.objects.aggregate(average_price=Avg('price'))


>>> from django.db.models import Avg, Max, Min
>>> Book.objects.aggregate(Avg('price'), Max('price'), Min('price'))
{'price__avg': 34.35, 'price__max': Decimal('81.20'), 'price__min': Decimal('12.99')}