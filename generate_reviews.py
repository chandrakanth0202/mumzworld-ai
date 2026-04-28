import pandas as pd
import random

print("Starting review generation...")

product_name = "Baby Stroller Pro"

positive_reviews = [
    "Very lightweight and easy to carry",
    "Perfect for travel",
    "Easy to fold and store",
    "Comfortable for babies",
    "Smooth wheels and easy handling",
    "Great quality for price",
    "Very useful for daily use"
]

negative_reviews = [
    "Wheels broke after two months",
    "Plastic feels cheap",
    "Brake stopped working",
    "Not durable for rough roads",
    "Poor build quality",
    "Too expensive"
]

arabic_reviews = [
    "العربة خفيفة جدًا وسهلة الاستخدام",
    "جودة ممتازة وسهلة التنظيف",
    "غير مناسبة للطرق الوعرة",
    "مريحة جدًا للأطفال",
    "العجلات تعطلت بسرعة"
]

reviews = []

# 150 English reviews
for i in range(150):
    if random.random() > 0.3:
        review = random.choice(positive_reviews)
        rating = random.randint(4, 5)
        language = "EN"
    else:
        review = random.choice(negative_reviews)
        rating = random.randint(1, 3)
        language = "EN"

    reviews.append([
        product_name,
        review,
        rating,
        language
    ])

# 50 Arabic reviews
for i in range(50):
    review = random.choice(arabic_reviews)

    reviews.append([
        product_name,
        review,
        random.randint(2, 5),
        "AR"
    ])

df = pd.DataFrame(
    reviews,
    columns=[
        "product_name",
        "review",
        "rating",
        "language"
    ]
)

df.to_csv(
    "data/reviews.csv",
    index=False,
    encoding="utf-8-sig"
)

print("200 reviews generated successfully!")
print("Total reviews:", len(df))
print(df.head())