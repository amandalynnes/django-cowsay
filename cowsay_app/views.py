from django.shortcuts import render

from cowsay_app.models import TextItem
from cowsay_app.forms import AddTextForm
import subprocess
# Create your views here.

# Cesar Ramos helped me get my cow to show up. I was close but needed to tweak some things.
# Figured out was able to make the sorby work in study hall


def index_view(request):
    form = AddTextForm()

    if request.method == "POST":
        form = AddTextForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            TextItem.objects.create(
                text=data['text'],
            )
            cow_say = subprocess.run(['cowsay', data['text']], capture_output=True)
            print(cow_say.stdout.decode('utf-8'))
            cow = cow_say.stdout.decode('utf-8')
            form = AddTextForm()
            return render(request, "index.html", {
                "heading": "Welcome to Cowsay, 'MOOOOOOO!'", 'form': form, 'cow': cow}
            )

    form = AddTextForm()
    return render(request, "index.html", {
        "heading": "Welcome to Cowsay, 'MOOOOOOO!'", 'form': form}
    )


def history_view(request):
    submissions = TextItem.objects.all().order_by('-id')[:10]
    return render(request, "history.html", {
        "heading": "What does the cow say? DOO DOO DOO DOO DOO DOO DOO... :",
        "submissions": submissions
    })
