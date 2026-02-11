import pandas as pd
import csv, json
import re

def validate_regex_patterns(string_list):
    """
    Filter strings that contain underscore (_) or dot (.)
    Drops strings that don't contain either character.
    
    Args:
        string_list: List of strings to validate
        
    Returns:
        List of strings containing _ or .
    """
    pattern = r'[_.]'
    return [item for item in string_list if re.search(pattern, item)]

def list_cleanup(data_list):
    # This keeps the item only if it is NOT an empty string or a dash
    sp_chars = ['', '-', ' ']
    return [item for item in data_list if item not in sp_chars]

def find_loc_codes(ui_strings, source_json_path):
    # 1. Load the Source JSON
    source_json_path = 'output/resources/source.json'
    with open(source_json_path, 'r', encoding='utf-8') as f:
        source_data = json.load(f)

    # 2. Create a set of all valid localized "messages"
    # We use a set for lightning-fast lookups
    valid_messages = {item['message'] for item in source_data}

    leaks = []

    # 3. Compare UI strings against the valid messages
    for string in ui_strings:
        # Check if the UI string is missing from the message whitelist
        if string not in valid_messages:
            leaks.append(string)
        # Else: it exists in 'message', so we skip it (localized)

    return leaks

def write_csv(data, filename):
    # Convert the list to a DataFrame
    df = pd.DataFrame(data, columns=["Locales"])
    
    # Save to CSV
    df.to_csv('output/resources/'+filename, index=False, quoting=csv.QUOTE_ALL , encoding='utf-8')

def write_json(data, filename):
    with open('output/resources/'+filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)