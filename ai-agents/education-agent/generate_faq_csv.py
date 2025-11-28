import pandas as pd
import random

topics = [
    "exam schedule", "grading policy", "attendance", "library access",
    "course registration", "internships", "scholarships", "labs", "projects", "faculty office hours"
]

records = []
for _ in range(300):
    topic = random.choice(topics)
    question = f"What is the {topic}?"
    answer = f"Our {topic} information is available on the student portal."
    records.append({"question": question, "answer": answer})

df = pd.DataFrame(records)
df.to_csv("../datasets/education_faq.csv", index=False)
print("✅ Generated 300 education FAQ records at ../datasets/education_faq.csv")
