"""
IX-Razor Utilities Module

Helper functions to sanitize, validate, and process cybersecurity queries,
ensuring consistent input format and error checking within the IX-Razor domain.
"""

import re

def clean_query(query: str) -> str:
    """
    Normalize the query by trimming whitespace, collapsing spaces,
    and removing disallowed characters.
    """
    query = query.strip()
    query = re.sub(r'\s+', ' ', query)
    query = re.sub(r'[^\w\s\-\.\@\:\']+', '', query)
    return query

def is_valid_query(query: str) -> bool:
    """
    Basic validation to check query length and presence of alphanumeric characters.
    """
    return bool(query and len(query) > 3 and any(c.isalnum() for c in query))

# Example usage
if __name__ == "__main__":
    tests = [
        "   What is firewall?  ",
        "???",
        "Explain zero day!",
        "Phishing attack details"
    ]

    for q in tests:
        cleaned = clean_query(q)
        valid = is_valid_query(cleaned)
        print(f"Original: '{q}' → Cleaned: '{cleaned}' | Valid: {valid}")
