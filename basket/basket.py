class Basket():

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, product, qty):
        """adding updateing the users basket session"""
        product_id = (product.id)
        print(product_id)
        if product_id not in self.basket:
            self.basket[product_id] = {'price': str(product.price), 'qty': int(qty)}
        self.session.modified = True

    def __len__(self):
        """Get the basket data and count the qty item"""

        return sum(item['qty'] for item in self.basket.values())