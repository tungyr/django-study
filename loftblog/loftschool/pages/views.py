from django.shortcuts import render
from django.http import HttpResponse
from datetime import *
from .models import Post


def my_third_simple_view(request, post_id):
    if post_id % 2 == 0:
        result = 'EVEN!'
    else:
        result = 'ODD!'
    return render(
        request,
        'pages/post.html',
        {
            'post_id': post_id,
            'result': result,
        }
    )

def my_first_simple_view(request):
    return render(
        request,
        'pages/index.html',
        {
            'header': 'Index',
            'posts': Post.objects.all()
            # 'posts': [
            #     {
            #     'header': 'qwertyuio',
            #     'text': 'asdfghjkl'
            #     },
            #     {
            #     'header': '123456789',
            #     'text': 'zxcvbnm,.'
            #     } ,
            #
            #     {
            #     'header': 'sfgasg647879',
            #     'text': 'some another text'
            #     },
            # ]

        }
    )

def my_second_simple_view(request):
    power = 2**10000
    return render(
        request,
        'pages/index.html',
        {
            'power': power, 'date': datetime.now()
        }
    )