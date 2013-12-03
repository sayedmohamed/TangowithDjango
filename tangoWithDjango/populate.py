import os

def populate():
	python_cat=add_cat(name='python',views=128,likes=64)

	add_page(cat=python_cat,
		title="official python tutorial" , 
		url="http://docs.python.org/2/tutorial/",views=244)

	add_page(cat=python_cat,
		title="how to think like a computer scientist",
		url="http://www.greenteapress.com/thinkpython",views=155)

	add_page(cat=python_cat,
		title="learn python in 10 minutes",
		url="http://www.korokithakis.net/tutorials/python/",views=373)


	django_cat=add_cat(name='django',views=64,likes=32)

	add_page(cat=django_cat,
		title="officical django tutorial",
		url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/",views=232)

	add_page(cat=django_cat,
		title="django rocks",
		url="http://www.djangorocks.com",views=211)

	add_page(cat=django_cat,
		title="how to tango with django",
		url="http://www.tangowithdjango.com/",views=122)

	frame_cat=add_cat(name="other framework",views=32,likes=16)

	add_page(cat=frame_cat,
		title="bottle",
		url="http://bottlepy.org/docs/dev/",views=177)

	add_page(cat=frame_cat,
		title="flask",
		url="http://flask.pocoo.org",views=188)

	for c in Category.objects.all():
		for p in Page.objects.filter(category=c):
			print "- {0} - {1}".format(str(c),str(p))

def add_page(cat,title,url,views=0):
	p=Page.objects.get_or_create(category=cat,title=title,url=url,views=views)[0]
	return p

def add_cat(name,views,likes):
	c=Category.objects.get_or_create(name=name,views=views,likes=likes)[0]
	return c


if __name__=='__main__':
	print "starting django populating script...."
	os.environ.setdefault('DJANGO_SETTINGS_MODULE','tangoWithDjango.settings')
	from rango.models import Category,Page
	populate()