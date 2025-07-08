import os
import json

# Semua log di direktori yang sama
LOG_FILES = [
    "battle_log.json",
    "character_log.json",
    "decision_log.json",
    "diplomacy_log.json",
    "economy_log.json",
    "event_log.json",
    "faction_log.json",
    "inventory_log.json",
    "map_log.json",
    "protokol_log.json",
    "research_log.json",
    "status_log.json",
    "story_log.twee",  # bukan JSON, skip
    "timeline_log.json",
    "tracking_log.json",
    "system_protokol.json"
]

def is_json_file(filename):
    return filename.endswith(".json")

def check_json(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            json.load(f)
        return True, None
    except Exception as e:
        return False, str(e)

def run_log_checker():
    print("\n📋 Log Checker Report\n" + "="*30)
    for file in LOG_FILES:
        if not os.path.exists(file):
            print(f"{file:<25} ❌ File not found")
        elif not is_json_file(file):
            print(f"{file:<25} ⚠️ Skipped (non-JSON)")
        else:
            valid, error = check_json(file)
            if valid:
                print(f"{file:<25} ✅ Valid JSON")
            else:
                print(f"{file:<25} ❌ Invalid JSON: {error}")
    print("="*30)

if __name__ == "__main__":
    run_log_checker()
