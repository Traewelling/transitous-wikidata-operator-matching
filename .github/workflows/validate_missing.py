import csv
import sys

def main():
    # Load IDs from mapping.csv
    try:
        with open("mapping.csv", newline="", encoding="utf-8") as mapping_file:
            mapping_reader = csv.DictReader(mapping_file)
            mapping_ids = {row["motis_id"].strip() for row in mapping_reader if row.get("motis_id")}
    except FileNotFoundError:
        print("Error: mapping.csv file not found.")
        sys.exit(1)

    # Load IDs from missing.csv
    try:
        with open("missing.csv", newline="", encoding="utf-8") as missing_file:
            missing_reader = csv.DictReader(missing_file)
            missing_ids = [row["motis_id"].strip() for row in missing_reader if row.get("motis_id")]
    except FileNotFoundError:
        print("Error: missing.csv file not found.")
        sys.exit(1)

    # Check each ID from missing.csv to see if it is also in mapping.csv
    failed = False
    for missing_id in missing_ids:
        if missing_id in mapping_ids:
            print(f"Error: ID '{missing_id}' found in both mapping.csv and missing.csv. It's obviously not missing, so should be removed from missing.csv.")
            failed = True

    if failed:
        sys.exit(1)
    else:
        print("All IDs in missing.csv are not present in mapping.csv.")

if __name__ == "__main__":
    main()
