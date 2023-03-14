from django.contrib.auth import login
from django.http import JsonResponse
from django.contrib.auth.models import User
from game.models.player.player import Player


def register(request):
    data = request.GET
    username = data.get("username", "").strip()
    password = data.get("password", "").strip()
    password_confirm = data.get("password_confirm", "").strip()
    if not username or not password:
        return JsonResponse({
            'result': "用户名和密码为空"
        })
    if password != password_confirm:
        return JsonResponse({
            'result': "两个密码不一致"
        })
    if User.objects.filter(username=username).exists():
        return JsonResponse({
            'result': "用户名已存在"
        })

    user = User(username=username)
    user.set_password(password)
    user.save()
    Player.objects.create(user=user, photo="https://img0.baidu.com/it/u=1669839829,1453308967&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=457")
    login(request, user)
    return JsonResponse({
        'result': "success"
    })
