# Customer Support Agent - Specification

## Goal
Provide intelligent, conversational support for customer queries using a local MySQL backend, without relying on paid APIs.

## Inputs
- User query (text)
- FAQ entries stored in MySQL

## Outputs
- Suggested answer from FAQ table
- Escalation recommendation if no match found

## Features
- Streamlit frontend for user interaction
- PyMySQL connection to MySQL (XAMPP, root/no password)
- Hybrid retrieval: exact SQL match + fuzzy matching (`difflib`)
- FastAPI endpoints for modular backend services (optional)
- Logging queries and responses to `logs` table
- Dashboard for monitoring FAQs and logs
