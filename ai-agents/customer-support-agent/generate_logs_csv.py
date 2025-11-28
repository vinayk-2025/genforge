import pandas as pd
from faker import Faker
import random

fake = Faker()

sample_queries = [
    "What is your return policy?",
    "How long does shipping take?",
    "Do you offer discounts?",
    "What payment methods do you accept?",
    "Can I cancel my order?",
    "Is delivery free?",
    "How do I contact support?",
    "Do products have warranty?",
    "How long for refunds?",
    "What are your support hours?"
]

sample_responses = [
    "Our return policy allows returns within 30 days of purchase.",
    "Standard shipping takes 5-7 business days.",
    "Seasonal discounts up to 20% are available during Diwali.",
    "We accept credit cards, debit cards, and UPI.",
    "Orders can be cancelled within 24 hours after placement.",
    "Delivery is free for orders above ₹1000.",
    "Our support team is available 9 AM - 6 PM IST, Monday to Friday.",
    "Products come with a 12 month warranty covering manufacturing defects.",
    "Refunds are processed within 7 business days after approval.",
    "Support is available Monday to Friday, 9 AM - 6 PM IST."
]

records = []
for _ in range(200):  # generate 200 synthetic logs
    query = random.choice(sample_queries)
    response = random.choice(sample_responses)
    records.append({"query": query, "response": response})

df = pd.DataFrame(records)
df.to_csv("../datasets/logs_bulk.csv", index=False)

print("✅ Synthetic logs CSV generated at ../datasets/logs_bulk.csv")
