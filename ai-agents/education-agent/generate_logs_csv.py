import pandas as pd
import random

sample_queries = [
    "When are exams scheduled?",
    "How is grading done?",
    "What is the attendance requirement?",
    "How do I access the library?",
    "How can I register for courses?"
]

sample_responses = [
    "Exams are scheduled at the end of each semester.",
    "Grading follows the university's standard policy.",
    "Attendance requirement is 75%.",
    "Library access is available with your student ID.",
    "Course registration is done via the student portal."
]

records = []
for _ in range(200):
    query = random.choice(sample_queries)
    response = random.choice(sample_responses)
    records.append({"query": query, "response": response})

df = pd.DataFrame(records)
df.to_csv("../datasets/education_logs.csv", index=False)
print("✅ Generated 200 synthetic education logs at ../datasets/education_logs.csv")
