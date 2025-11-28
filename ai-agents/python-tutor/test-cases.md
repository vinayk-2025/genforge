# 🐍 Python Tutor Agent — Test Cases

This file contains sample queries to validate the functionality of the Python Tutor agent.  
Each case is categorized by intent: **Explanation**, **Code Generation**, or **Quiz Creation**.

---

## 1. Concept Explanations
- "Explain recursion in Python."
- "What is the difference between a list and a tuple?"
- "How does Python handle memory management?"
- "Explain the concept of decorators with an example."
- "What is the use of `__init__` in Python classes?"

---

## 2. Code Generation
- "Write Python code for bubble sort."
- "Generate a function to check if a number is prime."
- "Give me Python code to reverse a string without using slicing."
- "Create a class for a simple bank account with deposit and withdraw methods."
- "Write Python code to read a CSV file and print the first 5 rows."

---

## 3. Quiz Creation
- "Generate 5 MCQs on Python lists."
- "Create a quiz with 5 questions on Python dictionaries."
- "Give me 5 multiple-choice questions on Python OOP concepts."
- "Generate 5 MCQs on Python exception handling."
- "Create a quiz on Python file handling basics."

---

## 4. Edge Cases (Typos & Variants)
- "Explain recusrion in Python." → should resolve to recursion explanation.
- "What is a tupel in Python?" → should resolve to tuple explanation.
- "Give me code for bubbel sort." → should resolve to bubble sort code.
- "Generate 5 MCQs on Pythn lists." → should resolve to quiz on lists.

---

## Validation Criteria
- ✅ Explanation queries return clear, beginner-friendly answers.
- ✅ Code generation queries produce runnable Python snippets.
- ✅ Quiz creation queries generate MCQs with correct answers and plausible distractors.
- ✅ Typos are handled gracefully with fuzzy matching.
- ✅ Logs record query, response, and intent classification.
