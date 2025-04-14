import csv
import sys

def main():
    # Load CSV files
    with open("mapping.csv", newline="", encoding="utf-8") as mapping_file:
        mapping_reader = csv.DictReader(mapping_file)
        mapping_rows = list(mapping_reader)

    with open("operators.csv", newline="", encoding="utf-8") as operators_file:
        operators_reader = csv.DictReader(operators_file)
        operator_rows = list(operators_reader)

    # Create a set of Wikidata IDs from operators.csv
    operator_ids = {row["wikidata_id"] for row in operator_rows}

    # Check that each Wikidata ID (except "null") from mapping.csv exists in the operator set
    failed = False
    for row in mapping_rows:
        wd_id = row["wikidata_id"].strip()
        if wd_id.lower() != "null" and wd_id not in operator_ids:
            print(f"Error: Wikidata ID {wd_id} from mapping.csv not found in operators.csv.")
            failed = True

    if failed:
        sys.exit(1)
    else:
        print("All Wikidata IDs from mapping.csv are present in operators.csv.")

if __name__ == "__main__":
    main()
