from django.shortcuts import render


# Request argument is being passed in the background by Django, when it calls this function
# In project settings we can define in which directory templates should be store, but in default they are stored in the templates directory (which I created)

def index(request):
    return render(request, 'index.html')
