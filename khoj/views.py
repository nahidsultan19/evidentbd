from django.shortcuts import render, redirect
from django .views import View
from backend.models import Evident
from .forms import EvidentForm
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    """mainview is index view where populate all data also form view with it."""
    context = {
        'evidents': Evident.objects.all(),
        'form': EvidentForm()
    }
    if request.method == 'POST':
        form = EvidentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'index.html', context)
