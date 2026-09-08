from decimal import Decimal
from .models import Laptop


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, laptop, quantity=1):
        laptop_id = str(laptop.id)
        if laptop_id not in self.cart:
            self.cart[laptop_id] = {'quantity': 0, 'price': str(laptop.price)}
        self.cart[laptop_id]['quantity'] += quantity
        self.save()

    def remove(self, laptop):
        laptop_id = str(laptop.id)
        if laptop_id in self.cart:
            del self.cart[laptop_id]
            self.save()

    def save(self):
        self.session.modified = True

    def clear(self):
        del self.session['cart']
        self.save()

    def __iter__(self):
        laptop_ids = self.cart.keys()
        laptops = Laptop.objects.filter(id__in=laptop_ids)
        cart = self.cart.copy()

        for laptop in laptops:
            cart[str(laptop.id)]['laptop'] = laptop

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())