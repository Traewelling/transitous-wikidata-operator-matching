# Transitous / Motis Operator Mapping

## Overview

This repository collects the mapping of operators used in Motis/Transitous.
The data used cannot be used directly for the purposes of Träwelling, which is why we need a mapping.
In order to have a unique key for each transport company, we use the Wikidata ID.

## Repository Files

- **`mapping.csv`**  
  This CSV file maps Motis/Transitous operator IDs (`motis_id`) and names (`motis_name`) to their corresponding Wikidata
  IDs (`wikidata_id`). A `"null"` value (as a string) indicates that there is currently no mapping for that operator.
  In this case Träwelling will save also null - so no operator.
  There are some weird operators like „Anrufsammeltaxi” or „Bus” which cannot be mapped to a single operator.

- **`operators.csv`**  
  This CSV file contains the operators listed in the database, keyed by their Wikidata IDs along with their official
  names. This file serves as a reference for validating the mappings.

- **`missing.csv`**
  This CSV file is an initial dump of all operators that are not yet mapped to a Wikidata ID.
  Operators can't be in the `mapping.csv` file and `missing.csv` file at the same time.

## How It Works

When a trip is checked in or saved, the system performs the following steps:

1. **Mapping Lookup:**  
   The system references the `mapping.csv` file to obtain the Wikidata ID for a given Motis/Transitous operator. If a
   valid Wikidata ID is provided (i.e., it is not `"null"`), the system uses this ID to identify the operator.

2. **Data Consistency:**  
   The Wikidata ID is cross-checked against the `operators.csv` file. If a match is found, the trip is linked to the
   standardized operator on Wikidata, reducing the risk of duplicate entries.

3. **Fallback Mechanism:**  
   In cases where no mapping is found (i.e., the Motis/Transitous operator ID is not present in `mapping.csv`),
   Träwelling will save the `motis_id` and `motis_name` as-is. This ensures that no data is lost, but it may lead to 
   inconsistencies in the database.

## Contributing

Contributions to improve the CSV mapping or to suggest enhancements for the overall process are welcome. If you have
ideas or improvements, please create an issue or submit a pull request. Community input is essential to keeping the
data consistent and useful for everyone.

## License

CC0 :)
