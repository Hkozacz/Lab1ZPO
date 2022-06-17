import random


def decorator(func):
    def wrapper(*args, **kwargs):
        free_items = {
            'mascot': {
                'name': 'mascot',
                'price': 0,
            },
            'lanyard': {
                'name': 'lanyard',
                'price': 1,
            },
            'discount': {
                'name': 'dicount',
                'price': -10,
            },
            'shippment': {
                'name': 'shippment',
                'price': 13
            }

        }
        returned_value = func(*args, **kwargs)
        if len(returned_value) > 2:
            returned_value.append(free_items['shippment'])
            returned_value.append(free_items['mascot'])
        for item in returned_value:
            if item.get('name') == 'monitor':
                returned_value.append(free_items['discount'])
            if item.get('name') == 'pendrive':
                returned_value.append(free_items['lanyard'])
        whole_price = 0
        for item in returned_value:
            whole_price += item.get('price')
        if whole_price < 0:
            whole_price = 0
        returned_value.append({
            'name': 'sum',
            'price': whole_price
        })
        return returned_value

    return wrapper


class Shop:
    items = {
        'phone': {
            'name': 'phone',
            'price': 10,
        },
        'monitor': {
            'name': 'monitor',
            'price': 13,
        },
        'pendrive': {
            'name': 'pendrive',
            'price': 7,
        }
    }

    @decorator
    def buy_items(self):
        basket = []
        for i in range(0,5):
            basket.append(self.items[random.choice(list(self.items.keys()))])
        return basket


if __name__ == '__main__':
    print(Shop().buy_items())