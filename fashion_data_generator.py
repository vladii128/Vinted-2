
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(42)

countries = ['France', 'Germany', 'Lithuania', 'Netherlands', 'Spain', 'Poland']
categories = ['Tops', 'Jeans', 'Sneakers', 'Dresses', 'Jackets', 'Bags']
brands = ['Zara', 'Nike', 'Adidas', 'H&M', 'Levi’s', 'Gucci', 'Balenciaga']
shipping_types = ['Standard', 'Pickup', 'Drop-off']

sell_probabilities = {
    'Drop-off': 0.85,
    'Pickup': 0.70,
    'Standard': 0.65
}

n = 10000
data = []

for i in range(n):
    item_id = 10000 + i
    user_id = f"u{np.random.randint(1000, 9999)}"
    country = np.random.choice(countries)
    category = np.random.choice(categories)
    brand = np.random.choice(brands)
    
    price = round(np.random.normal(loc=30, scale=15), 2)
    price = max(price, 3.0)

    posted = datetime.strptime('2024-01-01', '%Y-%m-%d') + timedelta(days=np.random.randint(0, 550))
    
    shipping = np.random.choice(shipping_types)
    sell_prob = sell_probabilities[shipping]
    sold_chance = np.random.rand()

    if sold_chance < sell_prob:
        days_to_sell = np.random.randint(1, 30)
        sold_date = posted + timedelta(days=days_to_sell)
    else:
        sold_date = None

    likes = np.random.poisson(5)
    rating = round(np.random.normal(4.5, 0.4), 1)
    rating = min(max(rating, 1.0), 5.0)

    data.append([
        item_id, user_id, country, category, brand,
        price, posted.date(), sold_date.date() if sold_date else None,
        shipping, likes, rating
    ])

df = pd.DataFrame(data, columns=[
    'item_id', 'user_id', 'country', 'item_category', 'brand',
    'price_eur', 'date_posted', 'date_sold',
    'shipping_type', 'likes_count', 'user_rating'
])

df.to_csv('european_fashion_trends.csv', index=False)
print("CSV file 'european_fashion_trends.csv' saved.")
