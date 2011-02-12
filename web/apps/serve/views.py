import os

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

from web.settings import MEDIA_ROOT, STATIC_URL
from serve.forms import AttachmentForm

def safe_rtr(request, template, context={}):
    context.update(csrf(request))
    return render_to_response(template, context)

def homepage(request, rname='quickorgmode'):
    if request.method == 'POST':
        form = AttachmentForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['attachment_name']
            uploaded_file = request.FILES.get('attachment_file')
            if uploaded_file:
                filename = uploaded_file.name
                path = os.path.join(MEDIA_ROOT, 'replays', name)
            else:
                return safe_rtr(request, 'index.html', {
                    'files': request.FILES,
                    'form': form,
                    'replay_name': rname,
                    'STATIC_URL': STATIC_URL,
                })
            if not os.path.exists(path):
                os.mkdir(path)
            destfile = open(os.path.join(path, filename), 'wb')
            for chunk in uploaded_file.chunks():
                destfile.write(chunk)
            destfile.close()
            return HttpResponseRedirect('/%s' % (name, ))
        else:
            return safe_rtr(request, 'index.html', {
                    'form': form,
                    'replay_name': rname,
                    'STATIC_URL': STATIC_URL,
                    })
    else:
        form = AttachmentForm()
        

        return safe_rtr(request, 'index.html', {
                'form': form,
                'replay_name': rname,
                'STATIC_URL': STATIC_URL,
                })
