from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *

def DripImageView(request):
    if request.method == 'POST':
        form = DripForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = DripForm()
    return render(request, 'drip_img_form.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')