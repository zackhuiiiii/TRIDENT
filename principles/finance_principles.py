# principles/finance_principles.py
"""
This file contains the full detailed CFA Institute Code of Ethics and Standards of Professional Conduct,
including each Standard and its subparts (e.g., CFA Standard II(A), II(B), etc.).
Each principle includes:
 - A brief summary
 - Common violations
 - Example of proper compliant behavior
"""
from __future__ import annotations

FINANCE_PRINCIPLES: dict[str, dict[str, str | list[str]]] = {
    "Standard I(A) - Knowledge of the Law": {
        "summary": "Understand and comply with all applicable laws, rules, and regulations of any government, regulatory organization, licensing agency, or professional association governing professional activities.",
        "common_violations": [
            "Failing to understand changes in securities law",
            "Participating in activities that violate professional regulations"
        ],
        "good_example": "Stay informed about relevant regulatory changes in all jurisdictions where you operate."
    },
    "Standard I(B) - Independence and Objectivity": {
        "summary": "Use reasonable care and judgment to achieve and maintain independence and objectivity in professional activities.",
        "common_violations": [
            "Accepting gifts that could compromise independence",
            "Allowing external pressures to affect research outcomes"
        ],
        "good_example": "Refuse gifts that could reasonably be expected to influence your decisions."
    },
    "Standard I(C) - Misrepresentation": {
        "summary": "Do not knowingly make any misrepresentations relating to investment analysis, recommendations, actions, or other professional activities.",
        "common_violations": [
            "Claiming performance results without proper basis",
            "Falsely stating academic qualifications"
        ],
        "good_example": "Accurately cite all data sources in investment presentations."
    },
    "Standard I(D) - Misconduct": {
        "summary": "Do not engage in any professional conduct involving dishonesty, fraud, or deceit.",
        "common_violations": [
            "Theft of client or employer property",
            "Fraudulent activities"
        ],
        "good_example": "Report any observed misconduct to appropriate authorities within your firm."
    },
    "Standard II(A) - Material Nonpublic Information": {
        "summary": "Do not act or cause others to act on material nonpublic information that could affect the value of an investment.",
        "common_violations": [
            "Trading securities based on insider information",
            "Sharing nonpublic information with others"
        ],
        "good_example": "Implement firm-wide restricted trading lists for securities discussed internally."
    },
    "Standard II(B) - Market Manipulation": {
        "summary": "Do not engage in practices that distort prices or artificially inflate trading volume.",
        "common_violations": [
            "Pump-and-dump schemes",
            "Spreading false rumors to manipulate stock prices"
        ],
        "good_example": "Base all public investment commentary on verifiable, truthful information."
    },
    "Standard III(A) - Loyalty, Prudence, and Care": {
        "summary": "Act for the benefit of clients and place client interests before your own or your employer’s interests.",
        "common_violations": [
            "Recommending unsuitable investments for personal gain",
            "Neglecting fiduciary responsibilities"
        ],
        "good_example": "Prioritize investment choices that best fit client goals and risk tolerance."
    },
    "Standard III(B) - Fair Dealing": {
        "summary": "Deal fairly and objectively with all clients when providing investment analysis, recommendations, or actions.",
        "common_violations": [
            "Favoring certain clients with earlier access to recommendations",
            "Providing selective investment opportunities"
        ],
        "good_example": "Disseminate investment recommendations to all clients simultaneously."
    },
    "Standard III(C) - Suitability": {
        "summary": "Ensure that investment advice is suitable to the client's financial situation and investment objectives.",
        "common_violations": [
            "Advising high-risk products to low-risk clients",
            "Failure to reassess suitability over time"
        ],
        "good_example": "Conduct annual reviews of client risk profiles and investment goals."
    },
    "Standard III(D) - Performance Presentation": {
        "summary": "Present investment performance information fairly, accurately, and completely.",
        "common_violations": [
            "Cherry-picking best performing periods",
            "Omitting disclaimers about model or back-tested results"
        ],
        "good_example": "Clearly state assumptions and periods for all presented performance results."
    },
    "Standard III(E) - Preservation of Confidentiality": {
        "summary": "Keep information about current, former, and prospective clients confidential unless disclosure is required by law."
        ,
        "common_violations": [
            "Discussing client information in public spaces",
            "Sharing client information for personal benefit"
        ],
        "good_example": "Encrypt client data and limit access internally on a need-to-know basis."
    },
    "Standard IV(A) - Loyalty": {
        "summary": "Act for the benefit of your employer and do not deprive your employer of your skills and abilities, divulge confidential information, or otherwise harm your employer."
        ,
        "common_violations": [
            "Soliciting clients before leaving a firm",
            "Misappropriating employer assets"
        ],
        "good_example": "Disclose intentions to compete openly and follow contractual obligations after leaving."
    },
    "Standard IV(B) - Additional Compensation Arrangements": {
        "summary": "Do not accept gifts, benefits, compensation, or consideration that competes with or might create a conflict of interest with employer interests without written consent."
        ,
        "common_violations": [
            "Accepting side payments without disclosure",
            "Receiving bonuses from third parties without employer approval"
        ],
        "good_example": "Obtain written employer approval before accepting external compensation arrangements."
    },
    "Standard IV(C) - Responsibilities of Supervisors": {
        "summary": "Make reasonable efforts to ensure that anyone subject to your supervision complies with applicable laws, regulations, and the Code and Standards.",
        "common_violations": [
            "Failure to detect misconduct",
            "Inadequate compliance training"
        ],
        "good_example": "Implement compliance policies and conduct regular staff training."
    },
    "Standard V(A) - Diligence and Reasonable Basis": {
        "summary": "Exercise diligence, independence, and thoroughness in investment analysis and recommendations.",
        "common_violations": [
            "Basing recommendations solely on rumors",
            "Skipping necessary research"
        ],
        "good_example": "Perform independent analysis and document all assumptions and findings."
    },
    "Standard V(B) - Communication with Clients and Prospective Clients": {
        "summary": "Disclose to clients and prospective clients the basic format and principles of the investment processes, and promptly disclose any changes."
        ,
        "common_violations": [
            "Failing to disclose significant changes in investment strategy",
            "Withholding known risks from clients"
        ],
        "good_example": "Clearly explain methodologies and all known material risks in client communications."
    },
    "Standard V(C) - Record Retention": {
        "summary": "Develop and maintain appropriate records to support investment analysis, recommendations, actions, and other investment-related communications."
        ,
        "common_violations": [
            "Failing to keep research notes",
            "Inadequate client recordkeeping"
        ],
        "good_example": "Retain investment reports and correspondence for the legally required duration."
    },
    "Standard VI(A) - Disclosure of Conflicts": {
        "summary": "Make full and fair disclosure of all matters that could reasonably be expected to impair independence and objectivity."
        ,
        "common_violations": [
            "Not disclosing beneficial ownerships",
            "Failing to reveal personal interests that could affect objectivity"
        ],
        "good_example": "Disclose personal holdings that overlap with client investment recommendations."
    },
    "Standard VI(B) - Priority of Transactions": {
        "summary": "Clients and employers must be given priority over personal investments."
        ,
        "common_violations": [
            "Front-running client trades",
            "Delaying client orders for personal gain"
        ],
        "good_example": "Execute client transactions before engaging in personal trading."
    },
    "Standard VI(C) - Referral Fees": {
        "summary": "Disclose to employers, clients, and prospective clients any compensation, consideration, or benefit received from, or paid to, others for recommendations."
        ,
        "common_violations": [
            "Receiving undisclosed commissions for client referrals",
            "Paying hidden referral fees"
        ],
        "good_example": "Inform clients in writing about referral fee arrangements upfront."
    },
    "Standard VII(A) - Conduct as Members and Candidates in the CFA Program": {
        "summary": "Do not engage in conduct that compromises the reputation or integrity of CFA Institute or the CFA designation."
        ,
        "common_violations": [
            "Cheating on CFA exams",
            "Improperly using the CFA designation"
        ],
        "good_example": "Follow all CFA Program Candidate Rules, including exam confidentiality."
    },
    "Standard VII(B) - Reference to CFA Institute, the CFA Designation, and the CFA Program": {
        "summary": "When referring to CFA Institute, CFA membership, or candidacy in the CFA Program, do not misrepresent or exaggerate the meaning or implications."
        ,
        "common_violations": [
            "Misstating progress towards earning the CFA charter",
            "Using the CFA designation improperly before completion"
        ],
        "good_example": "Only use 'CFA charterholder' once you have officially received the designation."
    }
}


def list_finance_principles() -> list[str]:
    return list(FINANCE_PRINCIPLES.keys())


def get_finance_principle(name: str) -> dict[str, str | list[str]]:
    key = next((k for k in FINANCE_PRINCIPLES if k.lower() == name.lower()), None)
    if key is None:
        raise KeyError(f"Unknown Finance principle: {name}")
    return FINANCE_PRINCIPLES[key]
