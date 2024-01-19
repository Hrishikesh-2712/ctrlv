from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseBadRequest
from v.models import Clipboard
from django.template import loader
import datetime
from .forms import ClipboardForm
from django.contrib import messages

# Create your views here.

# from .models import Article, Reporter
# r = Reporter(full_name='John Smith')
# r.save()
# print(r.id,'\n', Reporter.objects.all(),r.full_name)


# print('\n\n\n\n',Reporter.objects.get(id=1))
def ex_date(d):
    if 'week' in d:
        ds = 7
    elif 'month' in d:
        ds = 30
    elif 'year' in d:
        ds = 365
    else:
        ds = 999
    return datetime.datetime.now() + datetime.timedelta(ds)


def index(request):

    if (request.method == 'POST'):
        form = ClipboardForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('clip', id=obj.id)
        else:
            messages.info(request, "failed to save form")

        # clip = clipboard(text=request.POST['text'], topic=request.POST['topic'], expire_date=ex_date(request.POST['date']))
        # clip.save()
        # print(clip, clip.id)

    form = ClipboardForm()
    return render(request, 'index.html', {'form': form})


def clip(request, id=None):
    if (id == None):
        return HttpResponseBadRequest('bad request')

    data = Clipboard.objects.filter(id=id)
    if len(data) > 0:
        return render(request, 'clip.html', {'data': data[0]})

    return render(request, 'clip.html', {})

def colab(request, id = None):
    return render(request, 'colab.html')