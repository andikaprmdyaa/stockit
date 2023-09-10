from django.shortcuts import render
def show_main(request):
    context = {
        'app_name' : 'stockit' ,
        'name': 'Andika Pramudya Wardana',
        'class': 'KKI'
    }

    return render(request, 'main.html', context)