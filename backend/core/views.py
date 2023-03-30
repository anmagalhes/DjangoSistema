from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

# @login_required


def home(request):

    context = {
        'home': home,
    }

    return render(request, 'core/index.html', context)
