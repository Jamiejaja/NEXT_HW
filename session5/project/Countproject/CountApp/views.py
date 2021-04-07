from django.shortcuts import render

# Create your views here.
def count(request):
    return render(request, 'count.html')

def result(request):
    text = request.POST['text']
    total_len = len(text)
    origin = text
    blank = len(text.replace(" ", ""))
    words = (len(text.split(' ')))

    return render(request, 'result.html', {'total_len' : total_len, 'origin' : origin, 'blank' : blank, 'words' : words} )
