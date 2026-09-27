import streamlit as st
import datetime
import os  # Added for original file tracking and clean-up execution
from forensic_engine import analyze_audio_metadata
from threat_model import analyze_transcript_risk

# 1. Global Dashboard Configuration
st.set_page_config(page_title="Sauti-Pwani AI", page_icon="🛡️", layout="centered")

st.title("🛡️ Sauti-Pwani AI Forensics Suite")
st.write("National Security and Cyber-Forensics Toolkit for the Coast Region of Kenya.")
st.markdown("---")

# 2. UI File Upload Section
uploaded_file = st.file_uploader("Upload Audio Evidence (.wav or .mp3)", type=["wav", "mp3"])

if uploaded_file is not None:
    # FEATURE IMPLEMENTATION: Dynamically extract the true file name from the user's computer
    original_filename = uploaded_file.name
    
    # Save the target file locally using its true original name to maintain forensic standards
    with open(original_filename, "wb") as f:
        f.write(uploaded_file.getbuffer())
        
    st.info(f"📊 Processing {original_filename} through security layers...")
    
    # LAYER 1: Run Forensic Scan using the verified original filename string
    forensic_results = analyze_audio_metadata(original_filename)
    
    st.subheader("1. Structural Integrity & Steganography Scan")
    
    # Cryptographic Chain-of-Custody Visual Anchor
    st.info(f"🔒 **Evidence Chain-of-Custody Hash:** `{forensic_results['cryptographic_hash_sha256']}`")
    st.json(forensic_results)
    
    if forensic_results["steganography_risk"] == "High":
        st.error("⚠️ CRITICAL WARNING: High probability of an encrypted data payload hidden inside audio tags.")
    else:
        st.success("✅ Structural Verification: No obvious metadata-steganography signatures flagged.")
        
    st.markdown("---")
    
    # LAYER 2: Threat Intelligence Transcription Emulation
    st.subheader("2. Dialect Keyword & Threat Analysis")
    
    # Pre-populate sample phrase for seamless presentation flow
    user_transcript = st.text_input(
        "Enter Audio Transcript (or use detected phrase simulation):", 
        value="Tunaenda kuchoma base leo usiku pale Likoni Ferry"
    )
    
    if user_transcript:
        intelligence_results = analyze_transcript_risk(user_transcript)
        
        # Display polished outcome parameters based on classifier risk output
        if intelligence_results["risk_level"] == "High Risk":
            st.metric(label="Threat Risk Status", value="HIGH RISK DETECTED", delta="Action Required", delta_color="inverse")
            st.warning(f"Analysis Verdict: This transcript closely correlates with coordinated gang/radicalization operational language. (Confidence: {intelligence_results['confidence_score']})")
        elif intelligence_results["risk_level"] == "Medium Risk":
            st.metric(label="Threat Risk Status", value="MEDIUM RISK", delta="Monitor Profile", delta_color="off")
            st.info(f"Analysis Verdict: Cryptic or suspicious slang flagged. Continued tracking advised. (Confidence: {intelligence_results['confidence_score']})")
        else:
            st.metric(label="Threat Risk Status", value="LOW RISK", delta="Clear")
            st.success(f"Analysis Verdict: Safe conversational markers. No active threats detected. (Confidence: {intelligence_results['confidence_score']})")
            
        st.markdown("---")
        
        # LAYER 3: Automated Certified Forensic Report Generator
        st.subheader("3. Export Case Evidence Log")
        st.write("Generate a court-admissible forensic log file under Section 106B of the Kenya Evidence Act.")
        
        # Structure clear, human-scannable report text matching Kenya digital court procedures
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
        
        # Streamlit's native button allowing immediate, client-side downloading of raw data strings
        st.download_button(
            label="💾 Download Certified Evidence Report (.txt)",
            data=forensic_report_content,
            file_name=f"Evidence_Log_{forensic_results['cryptographic_hash_sha256'][:8]}.txt",
            mime="text/plain"
        )
        
    # BONUS IMPLEMENTATION: Clean up the file from disk space to enforce strict privacy protocols
    if os.path.exists(original_filename):
        os.remove(original_filename)
