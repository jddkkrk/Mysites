
from django.shortcuts import redirect, render

from .models import Product, Review


import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = telebot.TeleBot(BOT_TOKEN)

# Create your views here.
def home(requests):

    search = requests.GET.get('search')

    if search:
        products = Product.objects.filter(name__contains=search).all()
    else:
        products = Product.objects.all()

    return render(requests, "index.html", {
        'products': products,
        'products_found': len(products) > 0,
        'search': search if search else '',
        
    })

def view_product(request, id):
    product = Product.objects.filter(id=id) .first()
    
    if request.method == 'POST':
        author = request.POST.get('author')
        rating = request.POST.get('rating')
        usage_duration = request.POST.get('duration')
        text = request.POST.get('review')
    
        review = Review(
            product=product,
            author=author,
            rating=rating,
            usage_duration=usage_duration,
            text=text,

        )
        review.save()

    reviews = product.review_set.all()
    return render(request, 'product.html', {
        'product': product,
        'reviews': reviews,
    })

def payment(request,id):
   product = Product.objects.filter(id=id) .first()
   if request.method == 'POST':
        address = request.POST.get('address')
        name = request.POST.get('name')
        bot.send_message(CHAT_ID, f"""📦Новый Заказ!📦
                         
Товар:  {product.name} 

Цена товара:  {product.price} 

Свободный остаток:  {product.amount}

ФИО Покупателя:  {name}
Адрес Доставки:  {address}
""")
        return redirect('/success')
    
   return render(request, 'payment.html',{
        'product':product
    })


def success(request):
    return render(request, 'success.html')
