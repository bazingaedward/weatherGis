import requests, bs4, os
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings


def realtime(request):
    return render(request, 'weather/realtime.html', {
        'DEBUG': settings.DEBUG,
    })


def realtime_latest(request):
    content = ''
    filename = os.path.join(settings.DATA_ROOT, 'data_per5min', 'latest.json')
    with open(filename) as f:
        content = f.read()

    return HttpResponse(content, content_type='application/json')


def realtime_data(request, param):
    content = ''
    filename = os.path.join(settings.DATA_ROOT, param)
    with open(filename) as f:
        content = f.read()

    return HttpResponse(content, content_type='application/json')


def radar(request):
    url = 'http://products.weather.com.cn/product/radar/index/procode/JC_RADAR_AZ9311_JB'

    html = '<b>暂时不能获取雷达数据！</b>'

    try:
        r = requests.get(url)
        soup = bs4.BeautifulSoup(r.text, 'html.parser')

        soup.find_all('div', class_='weather_li')[0]['style'] = 'display:none'
        soup.find_all('div', class_='weather_li_head')[0]['style'] = 'display:none'
        soup.find_all('div', class_='footer')[0]['style'] = 'display:none'
        soup.find_all('div', class_='tqyb_left')[0]['style'] = 'display:none'
        soup.find_all('div', class_='lddzcz')[0]['style'] = 'display:none'
        soup.find_all('div', class_='title')[0]['style'] = 'display:none'
        soup.find_all('ul', class_='weather')[0]['style'] = 'display:none'

        html = soup.prettify()
    except:
        pass

    return render(request, 'weather/radar.html', {
        'html': html
    })
