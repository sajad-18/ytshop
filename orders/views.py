from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .cart import Cart
from ads.models import Ads
from .forms import CartAddForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order, OrderItem


class CartView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'orders/cart.html', {'cart': cart})


class CartAddView(View):
    def post(self, request, ads_id):
        cart = Cart(request)
        ads = get_object_or_404(Ads, id=ads_id)
        form = CartAddForm(request.POST)
        if form.is_valid():
            cart.add(ads, form.cleaned_data['quantity'])
        return redirect('orders:cart')


class CartRemoveView(View):
    def get(self, request, ads_id):
        cart = Cart(request)
        ads = get_object_or_404(Ads, id=ads_id)
        cart.remove(ads)
        return redirect('orders:cart')


class OrderDetailView(LoginRequiredMixin, View):
    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        return render(request, 'orders/order.html', {'order': order})


class OrderCreateView(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user)
        for item in cart:
            OrderItem.objects.create(order=order, ad=item['ad'], price=item['price'], quantity=item['quantity'])
        cart.clear()
        return redirect('orders:order_detail', order.id)
