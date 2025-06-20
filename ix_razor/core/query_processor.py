"""
IX-Razor Domain-Specific Query Processor

Parses and handles cybersecurity-related queries, routing them to the knowledge base
and generating responses focused on network defense, threat analysis, and security protocols.
"""

from core.cyber_knowledge import CyberKnowledge

class IXRazorQueryProcessor:
    def __init__(self):
        self.knowledge = CyberKnowledge()

    def process_query(self, query: str) -> str:
        query_lower = query.lower().strip()

        if query_lower.startswith("what is "):
            term = query_lower[8:].strip()
            return self.knowledge.get_fact(term)
        elif "define" in query_lower:
            term = query_lower.split("define")[-1].strip()
            return self.knowledge.get_fact(term)
        elif "explain" in query_lower:
            term = query_lower.split("explain")[-1].strip()
            return self.knowledge.get_fact(term)
        elif "attack" in query_lower:
            # Simple pattern recognition for attack types
            if "ddos" in query_lower:
                return self.knowledge.get_fact("ddos attack")
            else:
                return "Specify attack type more clearly."
        else:
            return (
                "I am IX-Razor, your cybersecurity AI. Ask me about network security, threat types, encryption, and defensive strategies. "
                "Examples: 'Define firewall', 'What is phishing?', 'Explain DDoS attack'."
            )

# Standalone test
if __name__ == "__main__":
    qp = IXRazorQueryProcessor()
    print(qp.process_query("Define firewall"))
    print(qp.process_query("Explain phishing"))
    print(qp.process_query("What is DDoS attack?"))
