from django.shortcuts import render
from .models import Media, Head
from forms.form import ReplyForm
from forms.models import Reply
from datetime import datetime
import random
from django.shortcuts import redirect
from django.utils import timezone

# Create your views here.
def home(request):
	count1 = Media.objects.count()
	index1 = random.randint(1, count1)
	count2 = Head.objects.count()
	index2 = random.randint(1, count2)
	img = Media.objects.filter(id=index1).first()
	head = Head.objects.filter(id=index2).first()
	return render(request, 'home.html', {'img':img, 'head':head})

def gallery(request):
	count1 = Media.objects.count()
	count2 = Head.objects.count()
	index1 = random.randint(1, count1)
	index2 = random.randint(1, count2)
	country_list = Media.objects.order_by('country').values('country').distinct()
	img_country_list = Media.objects.all().order_by('country', '-date')
	img_time_list = Media.objects.all().order_by('-date', 'country')
	yearmonth_list = []
	for img in img_time_list:
		date = str(img.date).split()[0]
		year = date.split('-')[0]
		month = date.split('-')[1]
		year_month = year + '.' + month
		if year_month not in yearmonth_list:
		 	yearmonth_list.append(year_month)

	if request.method == 'POST':
		form = ReplyForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.published_date = timezone.now()
			post.save()
			return redirect('gallery')
	else:
		form = ReplyForm()

	head = Head.objects.filter(id=index2).first()
	return render(request, 'gallery.html', {
		'country_list':country_list,
		'img_country_list':img_country_list,
		'yearmonth_list':yearmonth_list,
		'img_time_list':img_time_list,
		'head':head,
		'form': form,
		})