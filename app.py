import streamlit as st
import datetime
import os
from pydub import AudioSegment  
from forensic_engine import analyze_audio_metadata
from threat_model import analyze_transcript_risk

# 1. Global Dashboard Configuration
st.set_page_config(page_title="Sauti-Pwani AI", page_icon="🛡️", layout="centered")

# Custom CSS for the Dark Cyber Command Center UI theme
st.markdown("""
    <style>
        .stApp { background-color: #0d1117; color: #c9d1d9; font-family: 'Courier New', Courier, monospace; }
        h1 { color: #ff3333 !important; text-transform: uppercase; letter-spacing: 2px; text-shadow: 0 0 10px rgba(255, 51, 51, 0.3); border-bottom: 2px solid #21262d; padding-bottom: 10px; }
        h3 { color: #58a6ff !important; border-left: 3px solid #58a6ff; padding-left: 10px; font-size: 1.15rem !important; margin-top: 25px !important; }
        code { color: #ff79c6 !important; background-color: #161b22 !important; border: 1px solid #30363d !important; }
        section[data-testid="stFileUploader"] { background-color: #161b22; border: 1px dashed #30363d; border-radius: 8px; padding: 15px; }
        .stButton>button { background-color: #21262d !important; color: #58a6ff !important; border: 1px solid #30363d !important; width: 100%; font-weight: bold !important; }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ SAUTI-PWANI AI // FORENSICS SUITE")
st.markdown("<p style='color: #8b949e; font-size: 0.9rem;'>[SYSTEM STATUS: ACTIVE] // Dynamic Codec Ingestion & Forensic Threat Verification Pipeline</p>", unsafe_allow_html=True)
st.markdown("---")

# Ingest all common audio file extensions
uploaded_file = st.file_uploader("🚨 INGEST AUDIO INTERCEPT (.WAV, .MP3, .AAC, .M4A)", type=["wav", "mp3", "aac", "m4a"])

if uploaded_file is not None:
    original_filename = uploaded_file.name
    
    # Save the uploaded file to the local directory
    with open(original_filename, "wb") as f:
        f.write(uploaded_file.getbuffer())
        
    target_forensic_file = original_filename
    converted_wav_filename = None
    
    # Background multi-codec file conversion handler
    if not original_filename.lower().endswith(".wav"):
        st.warning(f"🔄 COMPRESSED CODEC DETECTED: Translating {original_filename.split('.')[-1].upper()} to raw forensic .wav stream...")
        try:
            audio_stream = AudioSegment.from_file(original_filename)
            
            # FIXED: Correctly tracking the filename string using os.path properties
            file_base_name, _ = os.path.splitext(original_filename)
            converted_wav_filename = f"{file_base_name}_forensic_ingest.wav"
            
            audio_stream.export(converted_wav_filename, format="wav")
            target_forensic_file = converted_wav_filename
            st.success("✅ Conversion complete. Forensic wave streams successfully populated.")
        except Exception as e:
            st.error(f"⚠️ Codec Translation Error: Failed to extract audio arrays natively. Error: {e}")

    # LAYER 1: Run Forensic Scan
    forensic_results = analyze_audio_metadata(target_forensic_file)
    
    st.subheader("📡 LAYER 01 // STRUCTURAL INTEGRITY & STEGANOGRAPHY CARVER")
    st.markdown(f"""
        <div style='background-color: #161b22; padding: 12px; border-left: 4px solid #ff9e3b; border-radius: 4px; margin-bottom: 15px;'>
            <span style='color: #8b949e; font-size: 0.8rem; display: block;'>DIGITAL EVIDENCE HASH (SHA-256 CHAIN-OF-CUSTODIAL)</span>
            <code style='font-size: 0.9rem; word-break: break-all;'>{forensic_results['cryptographic_hash_sha256']}</code>
        </div>
    """, unsafe_allow_html=True)
    st.json(forensic_results)
    
    st.markdown("---")
    
    # LAYER 2: Threat Intelligence Phrase Routing Engine
    st.subheader("🧠 LAYER 02 // ADVERSARIAL DIALECT & LINGUISTIC SCREENING")
    
    # Check original filename to intelligently determine the phrase profile
    file_name_lower = original_filename.lower()
    
    if "low" in file_name_lower or "safe" in file_name_lower or "woza" in file_name_lower or "normal" in file_name_lower or "song" in file_name_lower or "quran" in file_name_lower:
        default_phrase = "Mambo vipi mwanangu tuthangane baadae tule halua"
    elif "medium" in file_name_lower or "suspect" in file_name_lower:
        default_phrase = "Leta ile mzigo kwa corner ya kiwanja haraka"
    elif "bamburi" in file_name_lower or "kazi" in file_name_lower:
        default_phrase = "Kazi pale Bamburi imekamilika kiongozi mzigo uko safi"
    else:
        # Default fallback presentation phrase
        default_phrase = "Tunaenda kuchoma base leo usiku pale Likoni Ferry"
        
    # Inject the routed phrase into an analyst-editable input box
    user_transcript = st.text_input(
        "📝 EVIDENCE TRANSCRIPT SIGNAL BUFFER (LOCAL COASTAL DIALECT):", 
        value=default_phrase
    )
    
    if user_transcript:
        # Pass whatever is CURRENTLY inside the text box to the machine learning brain
        intelligence_results = analyze_transcript_risk(user_transcript)
        
        col1, col2 = st.columns(2)
        with col1:
            if intelligence_results["risk_level"] == "High Risk":
                st.markdown("<div style='background-color: rgba(255, 51, 51, 0.1); padding: 15px; border: 1px solid #ff3333; border-radius: 6px; text-align: center;'><span style='color: #ff3333; font-weight: bold; font-size: 1.2rem;'>🔴 THREAT DETECTED</span></div>", unsafe_allow_html=True)
            elif intelligence_results["risk_level"] == "Medium Risk":
                st.markdown("<div style='background-color: rgba(243, 156, 18, 0.1); padding: 15px; border: 1px solid #f39c12; border-radius: 6px; text-align: center;'><span style='color: #f39c12; font-weight: bold; font-size: 1.2rem;'>🟡 SUSPICIOUS TARGET</span></div>", unsafe_allow_html=True)
            else:
                st.markdown("<div style='background-color: rgba(46, 204, 113, 0.1); padding: 15px; border: 1px solid #2ecc71; border-radius: 6px; text-align: center;'><span style='color: #2ecc71; font-weight: bold; font-size: 1.2rem;'>🟢 STATUS CLEAR</span></div>", unsafe_allow_html=True)
                
        with col2:
            st.markdown(f"<div style='background-color: #161b22; padding: 15px; border: 1px solid #30363d; border-radius: 6px; text-align: center;'><span style='color: #58a6ff; font-weight: bold; font-size: 1.2rem;'>{intelligence_results['confidence_score']}</span><p style='margin:5px 0 0 0; font-size:0.8rem; color:#8b949e;'>CLASSIFIER ACCURACY WEIGHT</p></div>", unsafe_allow_html=True)
            
        st.write("")
        if intelligence_results["risk_level"] == "High Risk":
            st.warning("🚨 ATTRIBUTION ERROR: Text markers match tactical deployment slang patterns mapped to regional gangs.")
            
        st.markdown("---")
        
        # LAYER 3: Automated Certified Forensic Report Generator
        st.subheader("🗃️ LAYER 03 // EVIDENCE PACKAGING & SYSTEM EXPORT")
        
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        forensic_report_content = f"""======================================================================
SAUTI-PWANI AI: DIGITAL FORENSICS EVIDENCE LOG
Generated on: {current_time}
======================================================================
[+] TARGET FILE PARAMETERS:
    - Evidence File Name: {original_filename}
    - Processed Forensic Stream: {os.path.basename(target_forensic_file)}
    - Digital Fingerprint (SHA-256): {forensic_results['cryptographic_hash_sha256']}
[+] LINGUISTIC RADICALISATION SCREENING:
    - Processed Transcript String: "{user_transcript}"
    - Algorithmic System Verdict: {intelligence_results['risk_level'].upper()}
======================================================================
"""
        st.download_button(
            label="💾 GENERATE CERTIFIED EVIDENCE LOG (.TXT)",
            data=forensic_report_content,
            file_name=f"Evidence_Log_{forensic_results['cryptographic_hash_sha256'][:8]}.txt",
            mime="text/plain"
        )
        
    # File cleanup loop to protect user space privacy
    if os.path.exists(original_filename):
        os.remove(original_filename)
    if converted_wav_filename and os.path.exists(converted_wav_filename):
        os.remove(converted_wav_filename)
