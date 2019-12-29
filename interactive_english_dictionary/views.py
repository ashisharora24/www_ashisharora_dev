from django.shortcuts import render
from .forms import DictionaryQueryModelForms
from .models import DictionaryQuery

# Create your views here.


def home_page(request):
    form = DictionaryQueryModelForms(request.POST or None)
    if form.is_valid():
        form.save(commit=False)
        word = form.cleaned_data.get("word")
        user = None
        if word:
            if request.user.is_authenticated:
                user = request.user

            DictionaryQuery.objects.create(user=user, word=word,result="result")
        form = DictionaryQueryModelForms()

    template_name = "interactive_english_dictionary/home_page.html"
    context = {'form':form}

    return render(request, template_name, context)
