# Some standard Django stuff
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, loader
from django.shortcuts import render
from media.models import Media, Head
from forms.form import ReplyForm
from forms.models import Reply
from datetime import datetime
import random
from django.shortcuts import redirect
from django.utils import timezone
from datetime import datetime
from django.conf import settings
import random
import json
import time
from trips.models import Post
from django.shortcuts import redirect

static_base = 'http://127.0.0.1:8000'
static_url = static_base + settings.MEDIA_URL

 
# list of mobile User Agents
mobile_uas = [
	'w3c ','acs-','alav','alca','amoi','audi','avan','benq','bird','blac',
	'blaz','brew','cell','cldc','cmd-','dang','doco','eric','hipt','inno',
	'ipaq','java','jigs','kddi','keji','leno','lg-c','lg-d','lg-g','lge-',
	'maui','maxo','midp','mits','mmef','mobi','mot-','moto','mwbp','nec-',
	'newt','noki','oper','palm','pana','pant','phil','play','port','prox',
	'qwap','sage','sams','sany','sch-','sec-','send','seri','sgh-','shar',
	'sie-','siem','smal','smar','sony','sph-','symb','t-mo','teli','tim-',
	'tosh','tsm-','upg1','upsi','vk-v','voda','wap-','wapa','wapi','wapp',
	'wapr','webc','winw','winw','xda','xda-'
	]
 
mobile_ua_hints = [ 'SymbianOS', 'Opera Mini', 'iPhone' ]
 
 
def mobileBrowser(request):
    ''' Super simple device detection, returns True for mobile devices '''
 
    mobile_browser = False
    ua = request.META['HTTP_USER_AGENT'].lower()[0:4]
 
    if (ua in mobile_uas):
        mobile_browser = True
    else:
        for hint in mobile_ua_hints:
            if request.META['HTTP_USER_AGENT'].find(hint) > 0:
                mobile_browser = True
 
    return mobile_browser

# Create your views here.
def home(request):
	count1 = Media.objects.count()
	index1 = random.randint(1, count1)
	count2 = Head.objects.count()
	index2 = random.randint(1, count2)
	img = Media.objects.filter(id=index1).first()
	head = Head.objects.filter(id=index2).first()

	if mobileBrowser(request):
		t = 'm_home.html'
	else:
		t = 'home.html'

		return render(request, 'm_home.html', {'img':img, 'head':head})

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

	if mobileBrowser(request):
		t = 'm_gallery.html'
	else:
		t = 'gallery.html'

	return render(request, 'm_gallery.html', {
		'country_list':country_list,
		'img_country_list':img_country_list,
		'yearmonth_list':yearmonth_list,
		'img_time_list':img_time_list,
		'head':head,
		'form': form,
		})

# Create your views here.   
def post_detail(request, pk):
    count2 = Head.objects.count()
    index2 = random.randint(1, count2)
    post = Post.objects.get(pk=pk)
    head = Head.objects.filter(id=index2).first()
    if request.method == 'POST':
        form = ReplyForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk = pk)
    else:
        form = ReplyForm()

    if mobileBrowser(request):
        t = 'm_post_detail.html'
    else:
        t = 'post_detail.html'

    return render(request, 'm_post_detail.html', {'post': post, 'head':head, 'form': form,})

def posts(request):
    count1 = Post.objects.count()
    count2 = Head.objects.count()
    index1 = random.randint(1, count1)
    index2 = random.randint(1, count2)
    head = Head.objects.filter(id=index2).first()
    country_list = Post.objects.order_by('country').values('country').distinct()
    post_country_list = Post.objects.all().order_by('country', '-created_at')
    post_time_list = Post.objects.all().order_by('-created_at', 'country')
    yearmonth_list = []
    for post in post_time_list:
        date = str(post.created_at).split()[0]
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
            return redirect('posts')
    else:
        form = ReplyForm()

    head = Head.objects.filter(id=index2).first()

    if mobileBrowser(request):
        t = 'm_post.html'
    else:
        t = 'post.html'

    return render(request, 'm_post.html', {
        'country_list': country_list,
        'post_country_list': post_country_list,
        'yearmonth_list':yearmonth_list,
        'post_time_list':post_time_list,
        'head':head,
        'form': form,
    })

def upload_img(request):
    file = request.FILES['file']
    data = {
        'error':True,
        'path':'',
    }
    if file:
        timenow = int(time.time()*1000)
        timenow = str(timenow)
        try:
            img = Image.open(file)
            img.save(settings.MEDIA_ROOT + "content/" + timenow + unicode(str(file)))
        except Exception as e:
            print (e)
            return HttpResponse(json.dumps(data), content_type="application/json")
        imgUrl = static_url + 'content/' + timenow + str(file)
        data['error'] = False
        data['path'] = imgUrl
    return HttpResponse(json.dumps(data), content_type="application/json")
