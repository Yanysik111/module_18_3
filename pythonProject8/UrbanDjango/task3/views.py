from django.shortcuts import render

# Create your views here.
def main_page(request):
    headline = 'Главная страница'
    text1= 'Главная'
    text2 = 'Магазин'
    text3 = 'Корзина'
    context = {'headline': headline,
               'text1': text1,
               'text2': text2,
               'text3': text3,}
    return render(request,'third_task/sh1.html', context)

def first_page(request):
    name = 'Игры'
    game1 = 'Atomic Heart'
    game2 = 'Cyberpank 2077'
    game3 = 'PayDay 2'
    ret = 'Вернуться обратно'
    context = {'name': name,
               'game1': game1,
               'game2': game2,
               'game3': game3,
               'ret': ret}
    return render(request, 'third_task/sh2.html', context)

def second_page(request):
    text = 'Извините, Ваша корзина пуста'
    ret = 'Вернуться обратно'
    context = {'text': text,
               'ret': ret}
    return render(request, 'third_task/sh3.html', context)