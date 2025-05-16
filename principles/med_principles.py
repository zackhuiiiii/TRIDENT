"""
American Medical Association (AMA) Principles of Medical Ethics.
Each principle includes:
 - A brief summary
 - Common violations
 - Example of proper compliant behavior
"""
from __future__ import annotations

MEDICAL_PRINCIPLES: dict[str, dict[str, str | list[str]]] = {
    "Principle I - Competence and Compassion": {
        "summary": "A physician shall provide competent medical care with compassion and respect for human dignity and rights.",
        "common_violations": [
            "Providing care beyond competence level",
            "Displaying lack of empathy or respect",
            "Ignoring patient dignity in procedures",
            "Discriminatory treatment practices"
        ],
        "good_example": "Maintain current medical knowledge and treat all patients with equal respect and dignity."
    },
    "Principle II - Professional Integrity": {
        "summary": "A physician shall uphold professionalism, be honest, and report deficient physicians to appropriate entities.",
        "common_violations": [
            "Covering up medical errors",
            "Failing to report incompetent colleagues",
            "Dishonest documentation",
            "Fraudulent billing practices"
        ],
        "good_example": "Document accurately and report concerns about colleagues through proper channels."
    },
    "Principle III - Legal Compliance": {
        "summary": "A physician shall respect law while advocating for patient interests.",
        "common_violations": [
            "Violating healthcare regulations",
            "Ignoring mandatory reporting requirements",
            "Improper prescribing practices",
            "Failing to maintain proper records"
        ],
        "good_example": "Follow all regulations while advocating for necessary policy changes through proper channels."
    },
    "Principle IV - Patient Privacy": {
        "summary": "A physician shall respect rights and privacy of patients, colleagues, and other health professionals.",
        "common_violations": [
            "HIPAA violations",
            "Unauthorized disclosure of information",
            "Improper social media posts",
            "Discussing patients in public areas"
        ],
        "good_example": "Maintain strict confidentiality and secure all patient information."
    },
    "Principle V - Continued Education": {
        "summary": "A physician shall continue studying, advance knowledge, and share information appropriately.",
        "common_violations": [
            "Neglecting continuing education",
            "Using outdated practices",
            "Failing to consult specialists",
            "Withholding important information"
        ],
        "good_example": "Regularly attend CME courses and maintain current medical knowledge."
    },
    "Principle VI - Professional Choice": {
        "summary": "A physician shall be free to choose whom to serve, except in emergencies.",
        "common_violations": [
            "Refusing emergency treatment",
            "Discriminatory patient selection",
            "Inappropriate patient abandonment",
            "Improper referral practices"
        ],
        "good_example": "Exercise professional judgment in patient selection while ensuring emergency care for all."
    },
    "Principle VII - Community Health": {
        "summary": "A physician shall participate in improving community and public health.",
        "common_violations": [
            "Ignoring public health responsibilities",
            "Failing to report infectious diseases",
            "Disregarding community health initiatives",
            "Not participating in disaster response"
        ],
        "good_example": "Actively participate in public health initiatives and community education."
    },
    "Principle VIII - Patient Priority": {
        "summary": "A physician shall regard responsibility to the patient as paramount.",
        "common_violations": [
            "Prioritizing financial interests over patient care",
            "Letting external pressures affect treatment",
            "Compromising care for efficiency",
            "Ignoring patient preferences"
        ],
        "good_example": "Make all clinical decisions based on patient's best interests."
    },
    "Principle IX - Universal Access": {
        "summary": "A physician shall support access to medical care for all people.",
        "common_violations": [
            "Refusing care based on ability to pay",
            "Discriminating against certain populations",
            "Not participating in access programs",
            "Ignoring underserved communities"
        ],
        "good_example": "Participate in programs providing care to underserved populations."
    }
}

def list_medical_principles() -> list[str]:
    """Return list of all medical principle names."""
    return list(MEDICAL_PRINCIPLES.keys())

def get_medical_principle(name: str) -> dict[str, str | list[str]]:
    """Get details for a specific medical principle."""
    key = next((k for k in MEDICAL_PRINCIPLES if k.lower() == name.lower()), None)
    if key is None:
        raise KeyError(f"Unknown Medical principle: {name}")
    return MEDICAL_PRINCIPLES[key]