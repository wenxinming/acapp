from django.http import HttpResponse

def index(request):
    line1 = '<h1 style=text-align:center>球球大作战</h1>'
    line2 = '<img width=1520 src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fdynamic-image.yesky.com%2F600x-%2FuploadImages%2F2021%2F126%2F55%2F3NSX9MY58N37.png&refer=http%3A%2F%2Fdynamic-image.yesky.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1674462471&t=6f845f0974b86d22d31c7e2ae867d0e0">'
    return HttpResponse(line1 + line2)
