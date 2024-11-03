from django.shortcuts import render,redirect
from .models import Films_post
from .forms import Films_postForm

# Create your views here.
def home(request):
    films = Films_post.objects.all()

    return render(request, 'films/films.html',{'films':films})


def create_films(request):
    error=""
    if request.method == 'POST':
        form = Films_postForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('films_home')  # Redirect to a success page.
        else:
            error = "Данные были заполнены некорректно"
    form=Films_postForm()
    return render(request, 'films/add_new_film.html',{'form':form,'error':error})


# Create your views here.
