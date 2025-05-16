"""
This file contains key American Bar Association (ABA) Model Rules of Professional Conduct.
Each principle includes:
 - A brief summary
 - Common violations
 - Example of proper compliant behavior
"""
from __future__ import annotations

LAW_PRINCIPLES: dict[str, dict[str, str | list[str]]] = {
    "Rule 1.1 - Competence": {
        "summary": "A lawyer shall provide competent representation, requiring legal knowledge, skill, thoroughness and preparation.",
        "common_violations": [
            "Taking cases beyond expertise without proper study",
            "Failing to stay current with legal developments",
            "Inadequate case preparation",
            "Missing critical deadlines"
        ],
        "good_example": "Regularly attend continuing legal education and seek mentor guidance for unfamiliar areas."
    },
    "Rule 1.2 - Scope of Representation": {
        "summary": "A lawyer shall abide by client's decisions concerning objectives and consult on means to pursue them.",
        "common_violations": [
            "Making decisions without client consent",
            "Pursuing unauthorized settlement offers",
            "Knowingly assisting in criminal conduct",
            "Ignoring client objectives"
        ],
        "good_example": "Document client objectives and obtain written consent for settlement authority."
    },
    "Rule 1.3 - Diligence": {
        "summary": "A lawyer shall act with reasonable diligence and promptness in representing a client.",
        "common_violations": [
            "Neglecting client matters",
            "Excessive delays in case handling",
            "Poor communication with clients",
            "Pattern of missed deadlines"
        ],
        "good_example": "Maintain organized calendaring system and regular client updates."
    },
    "Rule 1.4 - Communication": {
        "summary": "A lawyer shall keep clients reasonably informed and explain matters to permit informed decisions.",
        "common_violations": [
            "Failing to respond to client inquiries",
            "Not explaining significant developments",
            "Withholding settlement offers",
            "Poor documentation of client communications"
        ],
        "good_example": "Provide regular case status updates and promptly return client communications."
    },
    "Rule 1.5 - Fees": {
        "summary": "A lawyer's fee shall be reasonable and communicated clearly to the client.",
        "common_violations": [
            "Excessive or unreasonable fees",
            "Unclear fee agreements",
            "Improper fee sharing",
            "Undisclosed cost markups"
        ],
        "good_example": "Use written fee agreements with clear terms and billing practices."
    },
    "Rule 1.6 - Confidentiality": {
        "summary": "A lawyer shall not reveal information relating to client representation without informed consent.",
        "common_violations": [
            "Unauthorized disclosure of client information",
            "Social media oversharing",
            "Unsecured client data storage",
            "Casual conversations about cases"
        ],
        "good_example": "Implement strict data security and train staff on confidentiality."
    },
    "Rule 1.7 - Conflict of Interest": {
        "summary": "A lawyer shall not represent a client if representation involves a concurrent conflict of interest.",
        "common_violations": [
            "Representing opposing parties",
            "Undisclosed business relationships",
            "Personal interests conflicting with client's",
            "Improper multiple representations"
        ],
        "good_example": "Maintain comprehensive conflict checking system and obtain informed consent when appropriate."
    },
    "Rule 1.8 - Business Transactions with Clients": {
        "summary": "A lawyer shall not enter into business transactions with clients unless terms are fair and disclosed in writing.",
        "common_violations": [
            "Improper financial dealings with clients",
            "Accepting gifts from clients",
            "Acquiring interest in client's cause of action",
            "Using client information for personal gain"
        ],
        "good_example": "Advise clients to seek independent counsel for any business transactions."
    },
    "Rule 1.9 - Duties to Former Clients": {
        "summary": "A lawyer shall not represent a new client in the same or a substantially related matter adverse to a former client without informed consent.",
        "common_violations": [
            "Reusing confidential info against former clients",
            "Failing to check prior representations",
            "Ignoring conflict from lateral hiring",
            "Not obtaining written consent"
        ],
        "good_example": "Conduct thorough conflict checks when onboarding new clients."
    },
    "Rule 1.10 - Imputation of Conflicts of Interest": {
        "summary": "Conflicts of interest of one lawyer in a firm may be imputed to others in the same firm.",
        "common_violations": [
            "Failing to screen conflicted lawyers",
            "Ignoring firm-wide conflict checks",
            "Conflicted representation without waiver",
            "Inadequate communication of conflicts"
        ],
        "good_example": "Implement firm-wide conflict screening software and protocols."
    },
    "Rule 1.11 - Special Conflicts for Former and Current Government Officers": {
        "summary": "Restricts lawyers' conduct after government service, especially regarding matters they were personally involved in.",
        "common_violations": [
            "Switching sides on the same case",
            "Using confidential government information",
            "Improper influence from former colleagues",
            "Conflicted hiring of ex-government lawyers"
        ],
        "good_example": "Screen former government lawyers from related matters and disclose conflicts."
    },
    "Rule 1.12 - Former Judge or Arbitrator": {
        "summary": "A lawyer shall not represent a party in a matter in which the lawyer participated as a judge or other adjudicator.",
        "common_violations": [
            "Failing to withdraw from former adjudication roles",
            "Participating without full disclosure",
            "Improper negotiation for employment during arbitration",
            "Conflicted representation post-arbitration"
        ],
        "good_example": "Disclose prior roles and obtain consent when required."
    },
    "Rule 1.13 - Organization as Client": {
        "summary": "A lawyer employed by an organization represents the organization, not individual officers or employees.",
        "common_violations": [
            "Taking direction from individual employees over entity interests",
            "Not reporting internal misconduct",
            "Failing to clarify representation scope",
            "Unauthorized disclosures to outsiders"
        ],
        "good_example": "Use Upjohn warnings and clarify who the client is in internal investigations."
    },
    "Rule 1.14 - Client with Diminished Capacity": {
        "summary": "When a client's capacity is diminished, a lawyer shall take protective action while maintaining a normal client relationship as much as possible.",
        "common_violations": [
            "Ignoring signs of incapacity",
            "Failing to involve guardians or courts when needed",
            "Breaching confidentiality without basis",
            "Not documenting concerns"
        ],
        "good_example": "Document capacity concerns and consider protective measures like involving a guardian ad litem."
    },
    "Rule 1.15 - Safekeeping Property": {
        "summary": "A lawyer shall hold client property separately in a trust account and promptly deliver what the client is entitled to receive.",
        "common_violations": [
            "Commingling client funds",
            "Delaying disbursement",
            "Inadequate accounting records",
            "Misuse of trust funds"
        ],
        "good_example": "Use IOLTA accounts with strict record-keeping and regular audits."
    },
    "Rule 1.16 - Declining or Terminating Representation": {
        "summary": "A lawyer shall withdraw when required and may withdraw under certain conditions, ensuring no harm to the client’s interests.",
        "common_violations": [
            "Withdrawing improperly mid-case",
            "Abandoning client without notice",
            "Failing to return client property",
            "Not notifying court appropriately"
        ],
        "good_example": "Follow formal procedures when withdrawing and ensure client is not prejudiced."
    },
    "Rule 1.17 - Sale of Law Practice": {
        "summary": "A lawyer may sell a law practice, including goodwill, if certain conditions are met to protect clients.",
        "common_violations": [
            "Failing to notify clients",
            "Improperly disclosing confidential info",
            "Violating restrictions on fees",
            "Selling partial practice without full disclosure"
        ],
        "good_example": "Notify all clients in writing and provide an opportunity to retain other counsel."
    },
    "Rule 1.18 - Duties to Prospective Client": {
        "summary": "Even if no client-lawyer relationship ensues, a lawyer shall not use or reveal information from a prospective client.",
        "common_violations": [
            "Using confidential info against the prospect",
            "Failing to screen conflicted attorneys",
            "Improper solicitation",
            "Lack of documentation of intake process"
        ],
        "good_example": "Implement prospective client intake forms and conflict screens."
    },"Rule 2.1 - Advisor": {
        "summary": "In representing a client, a lawyer shall exercise independent professional judgment and render candid advice, considering moral, economic, social, and political factors.",
        "common_violations": [
            "Giving overly narrow legal advice without context",
            "Failing to warn client of broader consequences",
            "Withholding honest assessment to please client",
            "Ignoring non-legal considerations when advising"
        ],
        "good_example": "Offer a client realistic legal options along with potential reputational and financial impacts."
    },
    "Rule 2.3 - Evaluation for Use by Third Persons": {
        "summary": "A lawyer may provide an evaluation of a matter affecting a client for third-party use if it is compatible with the lawyer’s other responsibilities to the client.",
        "common_violations": [
            "Failing to obtain client consent when evaluation poses material risk",
            "Providing misleading or incomplete evaluations",
            "Acting without clear understanding of evaluator vs. advocate roles",
            "Improperly disclosing confidential client information"
        ],
        "good_example": "Secure written client consent and clarify the scope before providing third-party evaluations."
    },
    "Rule 2.4 - Lawyer Serving as Third-Party Neutral": {
        "summary": "A lawyer serving as a neutral between parties shall inform unrepresented parties that the lawyer is not representing them.",
        "common_violations": [
            "Misleading parties into thinking lawyer is their advocate",
            "Failing to disclose role as neutral",
            "Overstepping neutral boundaries",
            "Not managing conflicts in multiparty mediation"
        ],
        "good_example": "Clearly explain neutral role at the outset and confirm in writing to all participants."
    },
    "Rule 3.1 - Meritorious Claims and Contentions": {
        "summary": "A lawyer shall not bring or defend a proceeding unless there is a basis in law and fact that is not frivolous.",
        "common_violations": [
            "Filing baseless lawsuits",
            "Using litigation to harass or delay",
            "Ignoring factual investigation before filing",
            "Continuing claims lacking legal merit"
        ],
        "good_example": "Conduct thorough legal and factual research before initiating litigation."
    },
    "Rule 3.2 - Expediting Litigation": {
        "summary": "A lawyer shall make reasonable efforts to expedite litigation consistent with the interests of the client.",
        "common_violations": [
            "Deliberately delaying proceedings",
            "Using dilatory tactics to gain advantage",
            "Failing to meet procedural deadlines",
            "Avoiding court communications"
        ],
        "good_example": "File timely pleadings and cooperate on scheduling with opposing counsel."
    },
    "Rule 3.5 - Impartiality and Decorum of the Tribunal": {
        "summary": "A lawyer shall not seek to influence judges or jurors improperly and must maintain courtroom decorum.",
        "common_violations": [
            "Improper ex parte communications",
            "Disrespectful courtroom behavior",
            "Influencing jurors outside proceedings",
            "Violating gag orders"
        ],
        "good_example": "Respect all courtroom procedures and avoid unauthorized communication with jurors."
    },
    "Rule 3.6 - Trial Publicity": {
        "summary": "A lawyer involved in a case shall not make public statements likely to materially prejudice the proceeding.",
        "common_violations": [
            "Commenting publicly on ongoing trials",
            "Leaking sensitive details to press",
            "Improper statements about evidence or guilt",
            "Violating protective orders"
        ],
        "good_example": "Coordinate with firm policies and avoid extrajudicial statements on pending matters."
    },
    "Rule 3.7 - Lawyer as Witness": {
        "summary": "A lawyer shall not act as advocate at a trial in which they are likely to be a necessary witness, unless exceptions apply.",
        "common_violations": [
            "Acting as counsel and witness in same trial",
            "Failing to withdraw despite testimonial conflict",
            "Not disclosing potential testimony role",
            "Undermining trial fairness by dual role"
        ],
        "good_example": "Assign a different attorney to try the case if you may need to testify."
    },
    "Rule 3.8 - Special Responsibilities of a Prosecutor": {
        "summary": "Prosecutors have heightened responsibilities to seek justice, including disclosure obligations and avoiding prosecuting without probable cause.",
        "common_violations": [
            "Suppressing exculpatory evidence",
            "Pursuing charges with insufficient evidence",
            "Improperly influencing witnesses",
            "Publicly prejudicing the accused"
        ],
        "good_example": "Disclose all relevant evidence to defense, even if harmful to the prosecution’s case."
    },
    "Rule 3.9 - Advocate in Nonadjudicative Proceedings": {
        "summary": "When representing a client before legislative or administrative bodies, a lawyer shall disclose the representation and conform to advocacy standards.",
        "common_violations": [
            "Failing to disclose client representation role",
            "Using deceit in lobbying contexts",
            "Improper influence on public officials",
            "Misstating facts in hearings"
        ],
        "good_example": "Clearly identify client affiliation and remain truthful in all regulatory presentations."
    },
    "Rule 4.1 - Truthfulness in Statements": {
        "summary": "A lawyer shall not knowingly make false statements of material fact to third persons.",
        "common_violations": [
            "Misrepresenting case status",
            "False settlement demands",
            "Deceptive negotiation tactics",
            "Misleading communications"
        ],
        "good_example": "Maintain honest communication while zealously advocating for clients."
    },
    "Rule 4.2 - Communication with Person Represented by Counsel": {
        "summary": "A lawyer shall not communicate about the subject of representation with a person the lawyer knows to be represented by another lawyer unless authorized.",
        "common_violations": [
            "Contacting opposing party directly without permission",
            "Bypassing counsel via email or social media",
            "Improper pre-litigation outreach",
            "Using intermediaries to indirectly communicate"
        ],
        "good_example": "Always obtain opposing counsel's consent before initiating communication with represented individuals."
    },
    "Rule 4.3 - Dealing with Unrepresented Person": {
        "summary": "When dealing with an unrepresented person, a lawyer shall not imply disinterest or give legal advice if the person’s interests conflict with the client’s.",
        "common_violations": [
            "Implying the lawyer is neutral",
            "Giving legal advice to unrepresented parties",
            "Failing to clarify representation role",
            "Using superior legal knowledge to mislead"
        ],
        "good_example": "Clarify you represent your client and suggest they seek independent counsel if interests may conflict."
    },
    "Rule 4.4 - Respect for Rights of Third Persons": {
        "summary": "A lawyer shall not use means that have no substantial purpose other than to embarrass, delay, or burden a third person, or obtain evidence improperly.",
        "common_violations": [
            "Accessing privileged communications inadvertently received",
            "Sending harassing discovery requests",
            "Contacting third parties unethically",
            "Failing to notify sender of misdirected documents"
        ],
        "good_example": "Promptly notify opposing counsel if you receive potentially privileged information by mistake."
    },
    "Rule 5.1 - Supervisory Lawyers": {
        "summary": "Partners and supervisory lawyers shall ensure firm has measures giving reasonable assurance of ethical compliance.",
        "common_violations": [
            "Inadequate oversight of junior lawyers",
            "Poor firm compliance procedures",
            "Failure to address known misconduct",
            "Lack of ethics training"
        ],
        "good_example": "Establish comprehensive ethics compliance program and regular training."
    },
    "Rule 5.2 - Responsibilities of a Subordinate Lawyer": {
        "summary": "A subordinate lawyer is bound by the Rules of Professional Conduct even if acting at the direction of another, but may be protected if acting on a reasonable interpretation of the rules.",
        "common_violations": [
            "Blindly following unethical instructions",
            "Failing to question questionable directives",
            "Participating in misconduct under pressure",
            "Not documenting concerns"
        ],
        "good_example": "Raise concerns to ethics counsel or supervisor and document actions taken."
    },
    "Rule 5.3 - Responsibilities Regarding Nonlawyer Assistance": {
        "summary": "A lawyer shall ensure nonlawyer employees and contractors act in a manner compatible with the lawyer’s professional obligations.",
        "common_violations": [
            "Inadequate supervision of staff",
            "Allowing unauthorized practice of law",
            "Poor training on confidentiality and ethics",
            "Outsourcing work without safeguards"
        ],
        "good_example": "Train staff on confidentiality and supervise all delegated legal tasks."
    },
    "Rule 5.4 - Professional Independence of a Lawyer": {
        "summary": "A lawyer shall not share legal fees or form partnerships with nonlawyers if it compromises professional independence.",
        "common_violations": [
            "Fee-sharing with nonlawyers",
            "Nonlawyer control over legal decisions",
            "Partnering with businesses that direct legal services",
            "Improper alternative business structures"
        ],
        "good_example": "Maintain clear boundaries between legal services and nonlegal business arrangements."
    },
    "Rule 5.5 - Unauthorized Practice of Law; Multijurisdictional Practice": {
        "summary": "A lawyer shall not practice law in a jurisdiction where doing so violates regulations, or assist others in unauthorized practice.",
        "common_violations": [
            "Practicing in another state without admission",
            "Assisting paralegals in giving legal advice",
            "Failing to follow pro hac vice procedures",
            "Ignoring state-specific licensing requirements"
        ],
        "good_example": "Check and comply with all local licensing and pro hac vice requirements before practicing."
    },
    "Rule 5.6 - Restrictions on Right to Practice": {
        "summary": "A lawyer shall not participate in employment or settlement agreements that restrict the lawyer’s right to practice after leaving a firm, except as part of retirement.",
        "common_violations": [
            "Entering into non-compete clauses with law firms",
            "Imposing restrictions in settlement agreements",
            "Using threats to limit lawyer mobility",
            "Restrictive clauses hidden in partnership agreements"
        ],
        "good_example": "Avoid agreements that limit a lawyer’s future ability to represent clients."
    },
    "Rule 5.7 - Responsibilities Regarding Law-related Services": {
        "summary": "Lawyers providing law-related services must take steps to ensure clients understand the protections of the attorney-client relationship may not apply.",
        "common_violations": [
            "Blurring lines between legal and nonlegal services",
            "Failing to disclose lack of privilege",
            "Improper marketing of affiliated services",
            "Using legal authority to influence clients into business deals"
        ],
        "good_example": "Provide clear written disclaimers and keep legal and nonlegal services organizationally separate."
    },
    "Rule 6.1 - Voluntary Pro Bono Publico Service": {
        "summary": "Every lawyer has a professional responsibility to provide legal services to those unable to pay, aiming for at least 50 hours of pro bono service per year.",
        "common_violations": [
            "Ignoring pro bono responsibilities entirely",
            "Failing to track or report pro bono hours when required",
            "Not prioritizing access to justice for underserved groups",
            "Using pro bono for improper self-promotion"
        ],
        "good_example": "Volunteer regularly with legal aid organizations and document service hours."
    },
    "Rule 6.2 - Accepting Appointments": {
        "summary": "A lawyer shall not seek to avoid court appointments except for good cause, such as conflict of interest or unreasonable financial burden.",
        "common_violations": [
            "Refusing court appointments without justification",
            "Citing vague or insincere personal beliefs",
            "Neglecting appointed cases",
            "Failing to notify court of valid conflicts"
        ],
        "good_example": "Accept appointments professionally and seek relief only for clear ethical or practical conflicts."
    },
    "Rule 6.3 - Membership in Legal Services Organization": {
        "summary": "A lawyer may serve in legal services organizations even if interests may conflict, but must not knowingly participate in actions adverse to client interests.",
        "common_violations": [
            "Failing to identify client conflicts",
            "Taking action against a private client through the organization",
            "Improperly disclosing client information",
            "Ignoring dual-role ethical concerns"
        ],
        "good_example": "Screen for conflicts before participating in policy decisions or representation through legal aid groups."
    },
    "Rule 6.4 - Law Reform Activities Affecting Client Interests": {
        "summary": "A lawyer may be involved in law reform activities even if reform may affect client interests, but must disclose material impacts when appropriate.",
        "common_violations": [
            "Failing to disclose when client interests are materially affected",
            "Using reform efforts to benefit specific clients secretly",
            "Not separating personal views from organizational roles",
            "Neglecting fiduciary duties during advocacy"
        ],
        "good_example": "Inform clients if law reform participation could materially impact their interests."
    },
    "Rule 6.5 - Nonprofit and Court-Annexed Limited Legal Services Programs": {
        "summary": "A lawyer providing short-term legal services under these programs is subject to relaxed conflict rules unless they know of a conflict.",
        "common_violations": [
            "Ignoring known conflicts even in short-term settings",
            "Failing to clarify limited scope of service",
            "Providing ongoing representation without proper engagement",
            "Using brief consults to solicit paying clients"
        ],
        "good_example": "Explain scope clearly and avoid representation beyond the program unless formal engagement occurs."
    },
    "Rule 7.1 - Communications About Services": {
        "summary": "A lawyer shall not make false or misleading communications about services.",
        "common_violations": [
            "Exaggerating case results",
            "Misleading advertising claims",
            "False expertise claims",
            "Improper testimonials"
        ],
        "good_example": "Use accurate, factual information in all marketing materials."
    },
    "Rule 7.2 - Communications Concerning a Lawyer's Services: Specific Rules": {
        "summary": "Lawyers may advertise, but must not compensate for recommendations or use misleading claims. Referral arrangements must comply with rule requirements.",
        "common_violations": [
            "Paying for client referrals outside approved systems",
            "Using non-lawyers to solicit clients",
            "Failing to include disclaimers in ads",
            "Posting misleading online reviews or credentials"
        ],
        "good_example": "Use accurate advertisements with proper disclaimers and disclose paid endorsements."
    },
    "Rule 7.3 - Solicitation of Clients": {
        "summary": "A lawyer shall not solicit professional employment by live person-to-person contact unless the recipient is a lawyer, family, or prior client.",
        "common_violations": [
            "Cold-calling accident victims",
            "Soliciting in hospital or courthouse settings",
            "Failing to label communications as advertising",
            "Sending misleading or coercive mailers"
        ],
        "good_example": "Use written solicitations with required notices and avoid live contact unless clearly permitted."
    },
    "Rule 7.6 - Political Contributions to Obtain Legal Engagements or Appointments by Judges": {
        "summary": "A lawyer or firm shall not make political contributions to secure engagements or appointments if the contributions are for the purpose of influencing selection.",
        "common_violations": [
            "Making donations to obtain government legal work",
            "Using political connections to circumvent selection processes",
            "Funneling contributions through third parties",
            "Failing to disclose conflict created by donations"
        ],
        "good_example": "Separate political activity from professional advancement and comply with appointment ethics rules."
    },    "Rule 8.1 - Bar Admission and Disciplinary Matters": {
        "summary": "A lawyer shall not knowingly make false statements or fail to disclose facts in connection with bar admission or disciplinary proceedings.",
        "common_violations": [
            "Lying on bar applications",
            "Omitting criminal or disciplinary history",
            "Failing to correct false character references",
            "Not disclosing material facts in investigations"
        ],
        "good_example": "Fully disclose past misconduct and provide accurate, updated information in all bar-related filings."
    },
    "Rule 8.2 - Judicial and Legal Officials": {
        "summary": "A lawyer shall not make false statements about the qualifications or integrity of judges or public legal officers.",
        "common_violations": [
            "Making baseless public accusations against judges",
            "Spreading rumors about judicial bias",
            "Attacking legal officials for personal gain",
            "Undermining public confidence in legal institutions without basis"
        ],
        "good_example": "Critique judicial decisions respectfully and support concerns with facts and legal reasoning."
    },
    "Rule 8.3 - Reporting Professional Misconduct": {
        "summary": "A lawyer who knows of another lawyer's serious ethical violation must report it to the appropriate authority.",
        "common_violations": [
            "Failing to report known misconduct",
            "Concealing serious ethical breaches",
            "Retaliating against whistleblowers",
            "Ignoring duty to report impaired lawyers"
        ],
        "good_example": "Report significant violations confidentially and document steps taken."
    },
    "Rule 8.4 - Misconduct": {
        "summary": "A lawyer shall not engage in conduct involving dishonesty, fraud, deceit, misrepresentation, or serious interference with justice.",
        "common_violations": [
            "Criminal acts that reflect poorly on fitness to practice",
            "Fraudulent billing practices",
            "Discrimination or harassment in professional conduct",
            "Conduct prejudicial to the administration of justice"
        ],
        "good_example": "Uphold the highest ethical standards in all personal and professional interactions."
    },
    "Rule 8.5 - Disciplinary Authority; Choice of Law": {
        "summary": "A lawyer is subject to the disciplinary authority of the jurisdiction in which they practice, regardless of where conduct occurs.",
        "common_violations": [
            "Claiming immunity due to out-of-state conduct",
            "Violating foreign rules while practicing locally",
            "Failing to account for choice-of-law implications",
            "Ignoring rules of temporary practice jurisdictions"
        ],
        "good_example": "Know and follow applicable ethical rules in all jurisdictions where you provide legal services."
    }

}


def list_law_principles() -> list[str]:
    """Return list of all law principle names."""
    return list(LAW_PRINCIPLES.keys())


def get_law_principle(name: str) -> dict[str, str | list[str]]:
    """Get details for a specific law principle."""
    key = next((k for k in LAW_PRINCIPLES if k.lower() == name.lower()), None)
    if key is None:
        raise KeyError(f"Unknown Law principle: {name}")
    return LAW_PRINCIPLES[key]