from django.shortcuts import render, HttpResponseRedirect, reverse


from cowsay_app.models import TextItem
from cowsay_app.forms import AddTextForm
# Create your views here.


def index_view(request):
    form = AddTextForm()

    if request.method == "POST":
        form = AddTextForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_text = TextItem.objects.create(
                text=data['text'],
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = AddTextForm()
    return render(request, "index.html", {
        "heading": "Welcome to Cowsay, 'MOOOOOOO!'", 'form': form}
    )


def history_view(request):
    submissions = TextItem.objects.all()[:10]
    return render(request, "history.html", {
        "heading": "What does the cow say? DOO DOO DOO DOO DOO DOO DOO... :",
        "submissions": submissions
    })


# def add_text(request):
#     if request.method == "POST":
#         form = AddTextForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             new_text = TextItem.objects.create(
#                 text=data['text'],
#             )
#             return HttpResponseRedirect(reverse('homepage', args=[new_text.id]))

#     form = AddTextForm()
#     return render(request, "generic_form.html", {'form': form})
