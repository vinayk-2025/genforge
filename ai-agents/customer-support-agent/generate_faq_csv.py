import pandas as pd
from faker import Faker
import random

fake = Faker()

topics = [
    "returns", "shipping", "payment", "discounts", "support",
    "warranty", "cancellation", "delivery", "membership", "refunds"
]

records = []

for _ in range(300):  # generate 300 records
    topic = random.choice(topics)
    question = f"What is your {topic} policy?"
    
    # Generate synthetic but meaningful answers
    if topic == "returns":
        answer = f"Our return policy allows returns within {random.randint(7,30)} days of purchase."
    elif topic == "shipping":
        answer = f"Standard shipping takes {random.randint(3,10)} business days. Express shipping is also available."
    elif topic == "payment":
        answer = f"We accept {random.choice(['credit cards','debit cards','UPI','net banking'])} for all purchases."
    elif topic == "discounts":
        answer = f"Seasonal discounts up to {random.randint(10,50)}% are available during {fake.month_name()}."
    elif topic == "support":
        answer = f"Our support team is available {random.randint(8,12)} hours daily, Monday to Friday."
    elif topic == "warranty":
        answer = f"Products come with a {random.randint(6,24)} month warranty covering manufacturing defects."
    elif topic == "cancellation":
        answer = f"Orders can be cancelled within {random.randint(1,24)} hours after placement."
    elif topic == "delivery":
        answer = f"Delivery is free for orders above ₹{random.randint(500,2000)}."
    elif topic == "membership":
        answer = f"Membership offers {random.randint(5,20)}% discounts and free shipping for premium users."
    elif topic == "refunds":
        answer = f"Refunds are processed within {random.randint(3,15)} business days after approval."
    else:
        answer = f"Our {topic} policy is {fake.sentence(nb_words=10)}"
    
    records.append({"question": question, "answer": answer})

df = pd.DataFrame(records)
df.to_csv("../datasets/faq_bulk.csv", index=False)

print("✅ Generated 300 domain-relevant FAQ records at datasets/faq_bulk.csv")
