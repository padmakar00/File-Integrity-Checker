import os
import hashlib
import json

HASH_DB = "hashes.json"

def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except:
        return None

def scan_directory(directory):
    hashes = {}
    for root, _, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            hash_value = calculate_hash(path)
            if hash_value:
                hashes[path] = hash_value
    return hashes

def load_old_hashes():  
    if not os.path.exists(HASH_DB):
        return {}
    with open(HASH_DB, "r") as f:
        return json.load(f)

def save_hashes(hashes):
    with open(HASH_DB, "w") as f:
        json.dump(hashes, f, indent=4)

def integrity_check(directory):
    old = load_old_hashes()   
    new = scan_directory(directory)

    result = {
        "MODIFIED": [],
        "DELETED": [],
        "ADDED": [],
        "NO CHANGE": []
    }

    for file in old:
        if file not in new:
            result["DELETED"].append(file)
        elif old[file] != new[file]:
            result["MODIFIED"].append(file)
        else:
            result["NO CHANGE"].append(file)

    for file in new:
        if file not in old:
            result["ADDED"].append(file)

    save_hashes(new)
    return result
