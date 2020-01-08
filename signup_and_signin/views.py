from django.shortcuts import render
from .forms import JoinForm
from django.http import JsonResponse

def home(request):
    template="signup_and_signin\home.html"
    context ={}
    form = JoinForm(request.POST or None)
    if form.is_valid():
        #obj = form.save(commit=False)
        if request.is_ajax():
            print("ajax true")
            print(form.cleaned_data)
            data = {
                'message': "Successfully submitted form data"
            }
            return JsonResponse(data)
        else:
            print("ajax false")
        form = JoinForm()
    context["form"] = form
    return render(request, template, context)
