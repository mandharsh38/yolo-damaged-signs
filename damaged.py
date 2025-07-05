import os
import json

# Folder with LabelMe JSONs
json_dir = "all/"

for filename in os.listdir(json_dir):
    if filename.endswith(".json"):
        json_path = os.path.join(json_dir, filename)
        try:
            with open(json_path, 'r') as f:
                data = json.load(f)
        except json.JSONDecodeError:
            print(f"Invalid JSON: {filename}")
            continue

        original_count = len(data.get("shapes", []))

        # Keep only DAMAGED_SIGNS shapes
        data["shapes"] = [shape for shape in data.get("shapes", []) if shape.get("label") == "DAMAGED_SIGN"]

        if len(data["shapes"]) != original_count:
            print(f"Updated: {filename} ({original_count} → {len(data['shapes'])} shapes)")

        # Overwrite the file
        with open(json_path, 'w') as f:
            json.dump(data, f, indent=2)
