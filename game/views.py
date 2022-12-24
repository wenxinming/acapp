from django.http import HttpResponse

def index(request):
    line1 = '<h1 style=text-align:center>英雄联盟手游</h1>'
    line4 = '<a href="/play/">进入游戏界面</a>'
    line2 = '<hr>'
    line3 = '<img width=1500 src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fn.sinaimg.cn%2Fsinakd20210829ac%2F165%2Fw640h325%2F20210829%2Ff1d6-ed8b3f71ea7d6fdc66d6196cf2149fd1.png&refer=http%3A%2F%2Fn.sinaimg.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1674464105&t=ae13d6aa9895cf7c025053361b8a3bbe">'
    return HttpResponse(line1 + line4 + line2 + line3)

def play(request):
    line1 = '<h1 style="text-align:center">游戏界面</h1>'
    line4 = '<a href="/">返回主界面</a>'
    line2 = '<hr>'
    line3 = '<img width=1500 src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fp9.itc.cn%2Fimages01%2F20210523%2F015fedd774e246f3bcf0f22aa39ff537.png&refer=http%3A%2F%2Fp9.itc.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1674464333&t=ef8b8885606172ca48f7ba78c03fb876">'
    return HttpResponse(line1 + line4 + line2 + line3)
