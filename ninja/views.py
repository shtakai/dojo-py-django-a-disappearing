from django.shortcuts import render

# Create your views here.
def index(request, color):
    if color == 'orange':
        ninja_image = 'michelangelo'
    elif color == 'blue':
        ninja_image = 'leonardo'
    elif color == 'red':
        ninja_image = 'raphael'
    elif color == 'purple':
        ninja_image = 'donatello'
    else:
        ninja_image = 'real_ninja'

    context = {
        'color': color,
        'ninja_image': ninja_image,

    }
    return render(request, 'index.html', context)

def no_ninja(request):
    context = {
        'message': 'No ninjas here',
    }
    return render(request, 'index.html', context)

