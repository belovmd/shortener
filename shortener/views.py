from django.shortcuts import render, get_object_or_404, redirect

import hashlib

from . import forms
from . import models

# Create your views here.


def create_link(request):
    uri = None

    if request.method == 'POST':
        link_form = forms.LinkForm(request.POST)
        if link_form.is_valid():
            url = link_form.cleaned_data['url']

            link_obj, _ = models.LinkStorage.objects.get_or_create(
                link=url,
                defaults={
                    'link_hash': hashlib.sha256(url.encode()).hexdigest()[:8],
                    'link': url,
                }
            )
            link_obj.save()
            uri = request.build_absolute_uri(
                link_obj.get_absolute_url(),
            )
    else:
        link_form = forms.LinkForm()
    return render(request, 'create_link.html', {'form': link_form,
                                                'link': uri})


def redirect_link(request, hash_):
    obj = get_object_or_404(models.LinkStorage, link_hash=hash_)
    return redirect(obj.link)
