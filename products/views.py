from django.shortcuts import render, redirect

products = [
    {'id': 1, 'name': 'Курсы английского', 'price': 1000},
    {'id': 2, 'name': 'Футболка', 'price': 500},
]


def product_list(request):
    context = {
        'products': products,
    }
    return render(request, 'products/product_list.html', context)


def add_to_cart(request, product_id):
    if 'cart' not in request.session:
        request.session['cart'] = []

    for product in products:
        if product['id'] == product_id:
            cart = request.session['cart']
            cart.append(product)
            request.session['cart'] = cart
            break

    return redirect('cart')


def buy_now(request, product_id):
    for product in products:
        if product['id'] == product_id:
            return redirect('purchase')
    return redirect('product_list')


def cart(request):
    context = {
        'cart': request.session.get('cart', []),
    }
    return render(request, 'products/cart.html', context)


def purchase(request):
    if request.method == 'POST':
        name = request.POST['name']
        request.session['cart'] = []
        return redirect('product_list')

    return render(request, 'products/purchase.html')
