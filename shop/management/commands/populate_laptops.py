from django.core.management.base import BaseCommand
from shop.models import Laptop
import random


class Command(BaseCommand):
    help = 'Автоматически добавляет 35 ноутбуков'

    def handle(self, *args, **kwargs):
        Laptop.objects.all().delete()

        brands = ['ASUS', 'Acer', 'Lenovo', 'HP', 'MSI', 'Apple', 'Dell']
        processors = ['Intel Core i5', 'Intel Core i7', 'AMD Ryzen 7', 'Apple M2', 'Intel Core i9']
        screens = ['15.6 IPS 144Hz', '14.0 OLED 90Hz', '17.3 QHD 240Hz', '13.3 Retina']

        laptops_to_create = []
        for i in range(1, 41):
            brand = random.choice(brands)
            model = f"Model-{i * 100}"
            price = round(random.uniform(450.0, 2500.0), 2)

            laptop = Laptop(
                brand=brand,
                model_name=model,
                price=price,
                description="Мощный ноутбук для учебы и игр.",
                processor=random.choice(processors),
                ram=random.choice([8, 16, 32]),
                storage=random.choice([256, 512, 1000]),
                screen_size=random.choice(screens)
            )
            laptops_to_create.append(laptop)

        Laptop.objects.bulk_create(laptops_to_create)
        self.stdout.write(self.style.SUCCESS('Успешно добавлено 40 ноутбуков!'))