from ads.models import Ads


CART_SESSION_ID = 'cart'


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        ad_ids = self.cart.keys()
        ads = Ads.objects.filter(id__in=ad_ids)
        cart = self.cart.copy()
        for ad in ads:
            cart[str(ad.id)]['ad'] = ad

        for item in cart.values():
            item['total_price'] = int(item['price']) * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, ads, quantity):
        ads_id = str(ads.id)
        if ads_id not in self.cart:
            self.cart[ads_id] = {'quantity': 0, 'price': str(ads.price)}
        self.cart[ads_id]['quantity'] += quantity
        self.save()

    def remove(self, ads):
        ad_id = str(ads.id)
        if ad_id in self.cart:
            del self.cart[ad_id]
            self.save()

    def save(self):
        self.session.modified = True

    def get_total_price(self):
        return sum(int(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[CART_SESSION_ID]
        self.save()


