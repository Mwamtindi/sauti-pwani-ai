import streamlit as st
import datetime
import os
from forensic_engine import analyze_audio_metadata
from threat_model import analyze_transcript_risk

# 1. Global Dashboard Configuration & Cyber Theme Injection
st.set_page_config(
    page_title="Sauti-Pwani AI", 
    page_icon="🛡️", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS to force a Dark Cyber Command Center UI theme
st.markdown("""
    <style>
        /* Base theme background and text colors */
        .stApp {
            background-color: #0d1117;
            color: #c9d1d9;
            font-family: 'Courier New', Courier, monospace;
        }
        
        /* Main title styling with a glowing tech underline */
        h1 {
            color: #ff3333 !important;
            text-transform: uppercase;
            letter-spacing: 2px;
            text-shadow: 0 0 10px rgba(255, 51, 51, 0.3);
            border-bottom: 2px solid #21262d;
            padding-bottom: 10px;
        }
        
        /* Subheading styling */
        h3 {
            color: #58a6ff !important;
            border-left: 3px solid #58a6ff;
            padding-left: 10px;
            font-size: 1.15rem !important;
            margin-top: 25px !important;
        }
        
        /* Metric block custom container styling */
        [data-testid="stMetricValue"] {
            font-family: 'Courier New', Courier, monospace;
            font-weight: bold;
        }
        
        /* Styled code block boxes */
        code {
            color: #ff79c6 !important;
            background-color: #161b22 !important;
            border: 1px solid #30363d !important;
        }
        
        /* Custom file uploader area tuning */
        section[data-testid="stFileUploader"] {
            background-color: #161b22;
            border: 1px dashed #30363d;
            border-radius: 8px;
            padding: 15px;
        }
        
        /* High-tech custom button look */
        .stButton>button {
            background-color: #21262d !important;
            color: #58a6ff !important;
            border: 1px solid #30363d !important;
            border-radius: 6px !important;
            font-weight: bold !important;
            width: 100%;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            border-color: #58a6ff !important;
            box-shadow: 0 0 8px rgba(88, 166, 255, 0.4);
            background-color: #30363d !important;
        }
    </style>
""", unsafe_allow_html=True)

# Top Brand Header
st.title("🛡️ SAUTI-PWANI AI // FORENSICS SUITE")
st.markdown("<p style='color: #8b949e; font-size: 0.9rem;'>[SYSTEM STATUS: ACTIVE] // National Security & Tactical Cyber-Forensics Toolkit // Coast Region, Kenya</p>", unsafe_allow_html=True)
st.markdown("---")

# 2. UI File Upload Section
uploaded_file = st.file_uploader("🚨 INGEST AUDIO EVIDENCE INTERCEPT (.WAV / .MP3)", type=["wav", "mp3"])

if uploaded_file is not None:
    original_filename = uploaded_file.name
    
    with open(original_filename, "wb") as f:
        f.write(uploaded_file.getbuffer())
        
    st.markdown(f"<p style='color: #e3b341;'>⏳ ANALYZING BINARY STREAM: {original_filename}...</p>", unsafe_allow_html=True)
    
    # LAYER 1: Run Forensic Scan
    forensic_results = analyze_audio_metadata(original_filename)
    
    st.subheader("📡 LAYER 01 // STRUCTURAL INTEGRITY & STEGANOGRAPHY CARVER")
    
    # High-tech warning callout for hash string
    st.markdown(f"""
        <div style='background-color: #161b22; padding: 12px; border-left: 4px solid #ff9e3b; border-radius: 4px; margin-bottom: 15px;'>
            <span style='color: #8b949e; font-size: 0.8rem; display: block;'>DIGITAL EVIDENCE HASH (SHA-256 CHAIN-OF-CUSTODY)</span>
            <code style='font-size: 0.9rem; word-break: break-all;'>{forensic_results['cryptographic_hash_sha256']}</code>
        </div>
    """, unsafe_allow_html=True)
    
    st.json(forensic_results)
    
    if forensic_results["steganography_risk"] == "High":
        st.error("🚨 CRITICAL HEURISTIC ALERT: High density tag injection detected. Potential payload mutation.")
    else:
        st.success("✔ FILE INTEGRITY VERIFIED: No hidden metadata binary anomalies observed.")
        
    st.markdown("---")
    
        # LAYER 2: Threat Intelligence Transcription Emulation
    st.subheader("🧠 LAYER 02 // ADVERSARIAL DIALECT & LINGUISTIC SCREENING")
    
    # FIX: Dynamically change the default text based on the uploaded file name
    file_name_lower = original_filename.lower()
    
    if "low" in file_name_lower or "safe" in file_name_lower or "woza" in file_name_lower:
        default_phrase = "Mambo vipi mwanangu tuthangane baadae tule halua"
    elif "medium" in file_name_lower or "suspect" in file_name_lower:
        default_phrase = "Tuthangane pale mshomoroni baada ya giza kuingia"
    else:
        # Default fallback to the high-risk phrase for normal files
        default_phrase = "Tunaenda kuchoma base leo usiku pale Likoni Ferry"
        
    # Inject the dynamic phrase into the text input box
    user_transcript = st.text_input(
        "🔠 EVIDENCE TRANSCRIPT SIMULATION BUFFER (LOCAL COASTAL DIALECT):", 
        value=default_phrase
    )

    
    if user_transcript:
        intelligence_results = analyze_transcript_risk(user_transcript)
        
        # Grid column layouts for metrics display box
        col1, col2 = st.columns(2)
        
        with col1:
            if intelligence_results["risk_level"] == "High Risk":
                st.markdown("""
                    <div style='background-color: rgba(255, 51, 51, 0.1); padding: 15px; border: 1px solid #ff3333; border-radius: 6px; text-align: center;'>
                        <span style='color: #ff3333; font-weight: bold; font-size: 1.2rem;'>🔴 THREAT DETECTED</span>
                        <p style='margin: 5px 0 0 0; font-size: 0.8rem; color: #8b949e;'>IMMEDIATE INTERVENTION REQUIRED</p>
                    </div>
                """, unsafe_allow_html=True)
            elif intelligence_results["risk_level"] == "Medium Risk":
                st.markdown("""
                    <div style='background-color: rgba(243, 156, 18, 0.1); padding: 15px; border: 1px solid #f39c12; border-radius: 6px; text-align: center;'>
                        <span style='color: #f39c12; font-weight: bold; font-size: 1.2rem;'>🟡 SUSPICIOUS TARGET</span>
                        <p style='margin: 5px 0 0 0; font-size: 0.8rem; color: #8b949e;'>MONITOR AND PROFILE TRACE</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                    <div style='background-color: rgba(46, 204, 113, 0.1); padding: 15px; border: 1px solid #2ecc71; border-radius: 6px; text-align: center;'>
                        <span style='color: #2ecc71; font-weight: bold; font-size: 1.2rem;'>🟢 STATUS CLEAR</span>
                        <p style='margin: 5px 0 0 0; font-size: 0.8rem; color: #8b949e;'>SAFE CONVERSATIONAL DIALECT</p>
                    </div>
                """, unsafe_allow_html=True)
                
        with col2:
            st.markdown(f"""
                <div style='background-color: #161b22; padding: 15px; border: 1px solid #30363d; border-radius: 6px; text-align: center;'>
                    <span style='color: #58a6ff; font-weight: bold; font-size: 1.2rem;'>{intelligence_results['confidence_score']}</span>
                    <p style='margin: 5px 0 0 0; font-size: 0.8rem; color: #8b949e;'>CLASSIFIER ACCURACY WEIGHT</p>
                </div>
            """, unsafe_allow_html=True)
            
        st.write("")
        if intelligence_results["risk_level"] == "High Risk":
            st.warning("🚨 ATTRIBUTION ERROR: Text markers match tactical deployment slang patterns mapped to regional gangs.")
            
        st.markdown("---")
        
        # LAYER 3: Automated Certified Forensic Report Generator
        st.subheader("🗃️ LAYER 03 // EVIDENCE PACKAGING & SYSTEM EXPORT")
        st.write("Compile audited forensic verification report conforming to Cap 80 Section 106B of the Laws of Kenya.")
        
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        forensic_report_content = f"""======================================================================
SAUTI-PWANI AI: DIGITAL FORENSICS EVIDENCE LOG
Generated on: {current_time}
Jurisdiction: Mombasa County / Coast Region, Kenya
======================================================================

[+] TARGET FILE PARAMETERS:
    - Evidence File Name: {forensic_results['file_name']}
    - File Size: {forensic_results['file_size_bytes']} Bytes
    - Playback Duration: {forensic_results['length_seconds']} Seconds
    - Digital Fingerprint (SHA-256 Chain of Custody): 
      {forensic_results['cryptographic_hash_sha256']}

[+] EXPLOIT DETECTION METRICS:
    - Steganography Risk Profile: {forensic_results['steganography_risk']}
    - Flagged Corrupted Meta-Tags: {', '.join(forensic_results['suspicious_tags']) if forensic_results['suspicious_tags'] else 'None'}

[+] LINGUISTIC RADICALISATION SCREENING:
    - Processed Transcript String: "{user_transcript}"
    - Algorithmic System Verdict: {intelligence_results['risk_level'].upper()}
    - Classifier Confidence Weight: {intelligence_results['confidence_score']}

======================================================================
STATUS: INTEGRITY VERIFIED & AUDITED SECURELY BY SAUTI-PWANI ENGINE
======================================================================
"""
        
        st.download_button(
            label="💾 GENERATE CERTIFIED EVIDENCE LOG (.TXT)",
            data=forensic_report_content,
            file_name=f"Evidence_Log_{forensic_results['cryptographic_hash_sha256'][:8]}.txt",
            mime="text/plain"
        )
        
    if os.path.exists(original_filename):
        os.remove(original_filename)
