from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Regional threat-intel data matrix (Sheng/Coastal Swahili operational keywords)
# Refined Regional Threat-Intel Data Matrix
# Categories: High Risk (Operational/Coordination), Medium Risk (Suspicious), Low Risk (Safe/Daily life)
TRAINING_DATA = [
    # --- HIGH RISK: Operational & Localized Coordination ---
    ("tunaenda kuchoma base leo usiku pale likoni ferry", "High Risk"),
    ("vijana wote wajae mtwapa base kuchukua chuma zetu", "High Risk"),
    ("kazi pale bamburi imekamilika kiongozi mzigo uko safi", "High Risk"),
    ("kuja na panga na sime tukutane corner ya changamwe", "High Risk"),
    ("tunavamia ile duka kisauni polisi wakilala", "High Risk"),
    ("piga doria kule nyali uangalie kama kuna makarao wa mtaa", "High Risk"),
    ("kundi la vijana lazima liingie barabarani kupiga fujo leo", "High Risk"),

    # --- MEDIUM RISK: Suspicious Activity & Cryptic Slang ---
    ("leta ile mzigo kwa corner ya kiwanja haraka", "Medium Risk"),
    ("wazee wa kazi wako macho usiongee kwa simu kabisa", "Medium Risk"),
    ("tuthangane pale mshomoroni baada ya giza kuingia", "Medium Risk"),
    ("mambo iko tayari hakikisha kila mtu ako rada", "Medium Risk"),
    ("mzigo mpya umeingia kutoka mpakani luku iko sawa", "Medium Risk"),
    ("fanya mambo chini ya maji asijue mtu yeyote", "Medium Risk"),

    # --- LOW RISK: Safe Conversational Baseline (Mombasa Context) ---
    ("habari yako kaka sasa hivi unakuja lini ferry", "Low Risk"),
    ("nataka kununua samaki freshness sokoni mwananyamala", "Low Risk"),
    ("mambo vipi mwanangu tuthangane baadae tule halua", "Low Risk"),
    ("leo jua ni kali sana hapa pwani twende tukaketi chini ya mwembe", "Low Risk"),
    ("mashua ya wavuvi imeingia salama malindi asubuhi hii", "Low Risk"),
    ("naenda kutoa pesa kwa mpesa pale duka ya jirani", "Low Risk"),
    ("kazi yangu ya mchana ni kuendesha tuktuk hapa mombasa county", "Low Risk")
]


def analyze_transcript_risk(text_input):
    """Vectorizes and classifies incoming transcripts based on local threat matrices."""
    texts, labels = zip(*TRAINING_DATA)
    
    # Initialize basic TF-IDF Vectorizer and Naive Bayes Classifier
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)
    
    clf = MultinomialNB()
    clf.fit(X, labels)
    
    # Process the live input string
    input_vector = vectorizer.transform([text_input.lower()])
    prediction = clf.predict(input_vector)[0]
    probabilities = clf.predict_proba(input_vector)[0]
    
    confidence = max(probabilities) * 100
    
    return {
        "risk_level": prediction,
        "confidence_score": f"{round(confidence, 2)}%"
    }
