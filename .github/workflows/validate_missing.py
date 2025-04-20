import csv
import sys

def main():
    # Load mapping of motis_id to motis_name from mapping.csv
    try:
        with open("mapping.csv", newline="", encoding="utf-8") as mapping_file:
            mapping_reader = csv.DictReader(mapping_file)
            mapping_dict = {}
            for row in mapping_reader:
                mid = row.get("motis_id", "").strip()
                mname = row.get("motis_name", "").strip()
                if mid and mname:
                    mapping_dict[mid] = mname
    except FileNotFoundError:
        print("Error: mapping.csv file not found.")
        sys.exit(1)

    # Load missing entries as a list of (motis_id, name) tuples from missing.csv
    try:
        with open("missing.csv", newline="", encoding="utf-8") as missing_file:
            missing_reader = csv.DictReader(missing_file)
            missing_list = []
            for row in missing_reader:
                mid = row.get("motis_id", "").strip()
                name = row.get("name", "").strip()
                if mid and name:
                    missing_list.append((mid, name))
    except FileNotFoundError:
        print("Error: missing.csv file not found.")
        sys.exit(1)

    # Check: if (motis_id, name) from missing.csv exists AND the same motis_id with this motis_name
    # is in mapping.csv, report an error
    failed = False
    for mid, name in missing_list:
        mapped_name = mapping_dict.get(mid)
        if mapped_name and mapped_name == name:
            print(f"Error: Combination motis_id='{mid}' and name='{name}' is listed in missing.csv, "
                  f"but also present in mapping.csv (motis_name='{mapped_name}').")
            failed = True

    if failed:
        sys.exit(1)
    else:
        print("All clear: No matching motis_id,name combinations found in both files.")

if __name__ == "__main__":
    main()
