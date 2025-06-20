"""
IX-Razor Core Cybersecurity Knowledge Module

Contains essential concepts, terminologies, and defensive strategies related to network security,
intrusion detection, encryption protocols, and threat analysis.
"""

class CyberKnowledge:
    def __init__(self):
        self.facts = {
            "firewall": "A network security device that monitors and filters incoming and outgoing network traffic based on predetermined security rules.",
            "intrusion detection system": "A device or software application that monitors a network or systems for malicious activity or policy violations.",
            "phishing": "A fraudulent attempt to obtain sensitive information by disguising oneself as a trustworthy entity in electronic communication.",
            "ddos attack": "Distributed Denial of Service attack; overwhelms a target system with traffic to disrupt normal operations.",
            "zero day": "A vulnerability unknown to those who should be interested in its mitigation (including the vendor).",
            "encryption": "The process of converting information or data into a code to prevent unauthorized access."
        }

    def get_fact(self, term: str) -> str:
        t = term.lower().strip()
        return self.facts.get(t, f"Unknown cybersecurity concept: '{term}' — not found in Razor’s current base.")

# Standalone test
if __name__ == "__main__":
    ck = CyberKnowledge()
    print(ck.get_fact("firewall"))
    print(ck.get_fact("phishing"))
    print(ck.get_fact("vpn"))
