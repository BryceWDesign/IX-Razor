"""
IX-Razor CLI Entry Point

Enables command-line interaction for cybersecurity queries,
outputting direct answers to the terminal.
"""

import sys
from core.query_processor import IXRazorQueryProcessor

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"Your cybersecurity question here\"")
        sys.exit(1)

    query = sys.argv[1]
    processor = IXRazorQueryProcessor()
    response = processor.process_query(query)

    print("\n🛡️ IX-Razor Response 🛡️")
    print(response)

if __name__ == "__main__":
    main()
