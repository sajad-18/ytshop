from orders.forms import CartAddForm


def add_cart(request):
    return {'add_cart': CartAddForm}
