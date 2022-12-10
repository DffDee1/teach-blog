from django.shortcuts import render, redirect
from .models import Link
from .forms import VideoForm
from users.models import CustomUser


def index(request):
    links = Link.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Домашняя', 'links': links})


def add_video(request):
    error = ''
    if request.method == 'POST':
        form = VideoForm(request.POST)

        if form.is_valid():

            obj = form.save(commit=False)
            obj.user_id = CustomUser.objects.get(
                pk=request.user.id)
            obj.save()

            form.save()
            print('CLEAR - \n', form.cleaned_data)
            return redirect('home')

        else:
            error = 'Что-то не так с формой'

    form = VideoForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add_video.html', context)
