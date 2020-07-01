from django.shortcuts import render, HttpResponse
def form(request):
    return render(request, "form.html")


def results(request):
    if request.method == 'POST':
        context = {
            'name' : request.POST['name'],
            'dojo_location' : request.POST['dojo_location'],
            'favorite_language' : request.POST['favorite_language'],
            'comment' : request.POST['comment'],
        }
        return render(request, 'results.html', context)
    return render (request, 'results.html')