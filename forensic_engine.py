import os
import hashlib
from mutagen import File

def generate_sha256(file_path):
    """Generates a cryptographic SHA-256 fingerprint for absolute data integrity verification."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        # Read the file in small byte blocks to keep memory footprint tiny
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def analyze_audio_metadata(file_path):
    """Carves audio metadata to look for anomalies or hidden payloads."""
    audio = File(file_path)
    
    # Generate cryptographic signature
    file_fingerprint = generate_sha256(file_path)
    
    report = {
        "file_name": os.path.basename(file_path),
        "cryptographic_hash_sha256": file_fingerprint,
        "file_size_bytes": os.path.getsize(file_path),
        "mime_type": getattr(audio, 'mime', ["Unknown"]) if getattr(audio, 'mime', None) else "Unknown",
        "bitrate": getattr(audio.info, 'bitrate', 'Unknown') if audio else 'Unknown',
        "length_seconds": round(getattr(audio.info, 'length', 0), 2) if audio else 0,
        "suspicious_tags": [],
        "steganography_risk": "Low"
    }
    
    if audio:
        for tag in audio.keys():
            if "comment" in tag.lower() or "description" in tag.lower():
                tag_content = str(audio[tag])
                if len(tag_content) > 100:  
                    report["suspicious_tags"].append(f"{tag} (Excessive string size)")
                    report["steganography_risk"] = "High"
                    
    return report
