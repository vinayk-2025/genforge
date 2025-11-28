# Education Agent - Specification

## Goal
Provide intelligent, conversational support for student queries using a local MySQL backend.  
The agent retrieves educational FAQ answers, handles fuzzy queries, and logs all interactions.

## Inputs
- Student query (text)
- FAQ entries stored in MySQL

## Outputs
- Suggested answer from FAQ table
- Escalation recommendation if no match found

## Features
- Streamlit frontend for student interaction
- PyMySQL connection to MySQL (XAMPP, root/no password)
- Hybrid retrieval: exact SQL match + fuzzy matching (`difflib`)
- Logging queries and responses to `logs` table
- Dashboard for monitoring FAQs and logs
