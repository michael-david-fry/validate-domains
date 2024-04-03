# Domain Validation Script

This Python script validates a list of domains based on their format, DNS resolution, and checks against a predefined list of domains associated with large organizations or hosting providers (e.g., Google, Amazon, Facebook, Netflix, Yahoo, 1and1). Domains that pass the validation are considered "good," while those that fail any check are classified as "bad." The script provides a user-friendly menu for selecting an input file and displays real-time status updates with color-coded feedback during processing.

## Features

- Validates domains for correct format and DNS resolution.
- Filters out domains associated with specified large companies or hosting providers.
- Interactive file selection menu.
- Real-time, color-coded status updates on domain processing.
- Outputs validated domains into separate files for "good" and "bad" domains.

## Prerequisites

Before running this script, ensure you have Python installed on your system. This script was developed and tested with Python 3.8 and above. No external Python packages are required, as it only uses standard libraries.

## Usage

1. Place your list of domains in a text file within the same directory as the script. Each domain should be on a new line.

2. Run the script using the following command:

    ```
    python domain_validation.py
    ```

3. Follow the on-screen prompts to select the file containing your list of domains.

4. Once processing is complete, check the `good_domains.txt` and `bad_domains.txt` files in the script's directory for the validation results.

## Customization

You can customize the list of filtered domains by modifying the `filter_list` variable in the script:

```python
filter_list = ['amazon', 'google', 'facebook', 'netflix', 'yahoo', '1and1']
