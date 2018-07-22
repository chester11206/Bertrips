from django.shortcuts import render
from datetime import datetime
from media.models import Head
from django.conf import settings
from forms.form import ReplyForm
from forms.models import Reply
import random
import json
import time
from django.http import HttpResponse
from trips.models import Post
from django.shortcuts import redirect
from django.utils import timezone

static_base = 'http://127.0.0.1:8000'
static_url = static_base + settings.MEDIA_URL

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
    return render(request, 'post_detail.html', {'post': post, 'head':head, 'form': form,})

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
    return render(request, 'post.html', {
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
