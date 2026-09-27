# 🛡️ Sauti-Pwani AI: Regional Audio Cyber-Forensics Suite

Sauti-Pwani AI is an advanced, lightweight digital forensics and tactical threat intelligence platform designed specifically for national security and digital investigation units operating within **Mombasa County and the Coastal Region of Kenya**.

Traditional security platforms fail to capture local nuances. This engine addresses localized blind spots by parsing raw audio media intercepts to screen for **cryptographic steganography exploits** and **adversarial dialect risk markers** (such as Coastal Sheng, KiMvita, and code-switched Coastal Swahili) commonly deployed by underground regional syndicates and youth gangs (*e.g., Wakali Kwanza*).

---

## 🚀 Core Architectural Features

* **Layer 1: Forensic Chain-of-Custody Verification**  
  Implements a stream-based block reader using `hashlib` to generate an immutable **SHA-256 digital fingerprint** of the target file. This mathematically enforces verbatim file preservation compliant with modern cyber-law standards.
  
* **Layer 2: Structural Tag & Steganography Carving**  
  Leverages the `mutagen` framework to deep-scan file headers and comment blocks, automatically flagging suspicious, high-density data injections often used to mask malicious payloads.

* **Layer 3: Localized Dialect ML Heuristics**  
  Translates phonetic structures into numerical feature arrays via **TF-IDF Vectorization** and screens text patterns using a **Multinomial Naive Bayes** classifier trained on a regional coastal threat intelligence matrix.

* **Layer 4: Zero-Trust Localized Compliance Engine**  
  Built entirely as a local, zero-network-dependency system to prevent sensitive intelligence data leakage. Automatically generates a certified, human-scannable `.txt` evidence report compliant with **Section 106B of the Kenya Evidence Act**. Includes an automated ephemeral data clean-up cycle to ensure post-analysis privacy.

---

## 🛠️ Technology Stack

* **Language:** Python 3.10+
* **Interface UI Framework:** Streamlit
* **Binary Forensics & Tag Carving:** Mutagen
* **Machine Learning / Vectorization:** Scikit-Learn
* **File System Automation:** Built-in Python I/O (`hashlib`, `os`, `datetime`)

---

## 📁 Repository Structure

```text
sauti_pwani_project/
│
├── app.py              # Core Streamlit Web App Interface & Exporter
├── forensic_engine.py  # Binary analyzer, Metadata carver, SHA-256 calculator
├── threat_model.py     # TF-IDF & Multinomial Naive Bayes regional text classifier
└── README.md           # Project system specification documentation
```

---

## ⚙️ Installation & Deployment Guide

Follow these sequential steps to run the framework locally inside your development workspace:

### 1. Clone or Create the Workspace

Clone the repository
```bash
git clone https://github.com/Mwamtindi/sauti-pwani-ai.git
cd sauti-pwani-ai
```

### 2. Set Up a Clean Virtual Environment
Open your terminal window and execute the following commands based on your operating system:

**On Windows (PowerShell):**
```powershell
# Bypass default script execution restrictions for this terminal session
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process

# Initialize and activate the virtual environment
python -m venv venv
.\venv\Scripts\activate
```

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install System Dependencies
With your virtual environment active—indicated by `(venv)` appearing at the start of your terminal prompt—install the required Python packages:
```bash
pip install streamlit mutagen scikit-learn
```

### 4. Launch the Engine
Run the native deployment command to spin up the local web app dashboard session:
```bash
streamlit run app.py
```
The application will automatically spin up and serve the visual dashboard on your local loopback address at: **`http://localhost:8501`**

---

## ⚖️ Legal & Compliance Framework

This project is explicitly structured to support and complement the statutory requirements outlined within the following Kenyan legal architectures:
1. **The Computer Misuse and Cybercrimes Act (2018)** – Governing authorized digital investigation bounds.
2. **The Kenya Evidence Act (Cap 80, Section 106B)** – Admissibility requirements for electronic records via cryptographic chain-of-custody tracking.
3. **The Data Protection Act (2019)** – Maintained through zero-trust local network processing and immediate raw evidence deletion cycles.

---

## Author

**Mwamtindi**

GitHub: https://github.com/Mwamtindi

*Developed as an award-winning Capstone Project for IT/Cybersecurity Regional Innovation.*
