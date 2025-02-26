import json

def process_raw_json_from_gemini(raw_json):
    clean_json = raw_json.replace("```json", "", 1).replace("```", "", 1).strip()
    return json.loads(clean_json)
