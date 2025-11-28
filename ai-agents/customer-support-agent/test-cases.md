# Customer Support Agent - Test Cases

This document lists test queries for validating the hybrid intelligent behaviour of the Customer Support Agent.

---

## ✅ Exact Matches (should succeed immediately)
- What is your return policy?
- How long does shipping take?
- Do you offer discounts?
- What payment methods do you accept?

---

## 🔎 Near Matches (fuzzy should catch them)
- What is the your shipping policy?
- Tell me about return polic
- Do you give discount offers?
- What are payment method options?

---

## ✍️ Typos / Variations
- How long does shiping take?
- Can I cancell my order?
- Is delivry free?

---

## 🚫 Non‑matches (should trigger fallback)
- Do you sell gift cards?
- Can I track my order online?
