# 🧪 Log_checker.py
# Validasi otomatis struktur log JSON naratif (by required_fields & relations)

import json
import os
from datetime import datetime

# 📂 Daftar nama file log utama
log_files = [
    "Story_resume.log.json", "System_protokol.json", "battle_log.json",
    "character_log.json", "decision_log.json", "diplomacy_log.json",
    "economy_log.json", "event_log.json", "faction_log.json",
    "inventory_log.json", "map_log.json", "protokol_log.json",
    "research_log.json", "timeline_log.json", "tracking_log.json",
    "Sistem_status_log.json", "Status_karakter.json"
]

# 📋 Required fields minimum
required_fields = ["id", "timestamp", "narrative_time", "type"]

def check_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if not isinstance(data, list):
                print(f"❌ Format error in {filename}: root should be a list")
                return
            for entry in data:
                for field in required_fields:
                    if field not in entry:
                        print(f"❌ Missing '{field}' in {filename} entry: {entry}")
                # Check timestamp format
                try:
                    datetime.fromisoformat(entry['timestamp'].replace('Z', '+00:00'))
                except Exception:
                    print(f"⚠️ Invalid timestamp format in {filename}: {entry.get('timestamp')}")
    except Exception as e:
        print(f"❌ Failed to load {filename}: {str(e)}")

# 🚀 Run checker
if __name__ == "__main__":
    for file in log_files:
        if os.path.exists(file):
            check_file(file)
        else:
            print(f"⚠️ File not found: {file}")
