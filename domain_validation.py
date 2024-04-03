import re
import socket
import os

# ANSI escape codes for colors
RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'

# Regex for basic domain format validation
domain_regex = re.compile(
    r'^(?:http[s]?://)?'
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+'
    r'(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
    r'localhost)'
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

# List of substrings to identify specific company domains
filter_list = ['amazon', 'google', 'facebook', 'netflix', 'yahoo', '1and1']

def is_filtered_domain(domain):
    domain = domain.lower()
    for filter_word in filter_list:
        if filter_word in domain:
            return True
    return False

def validate_domain_format(domain):
    return re.match(domain_regex, domain) is not None

def resolve_domain(domain):
    try:
        domain = re.sub(r'^http[s]?://', '', domain)
        socket.gethostbyname(domain)
        return True
    except socket.error:
        return False

def validate_domain(domain):
    if is_filtered_domain(domain):
        return False, "Filtered"
    if not validate_domain_format(domain):
        return False, "Invalid format"
    if not resolve_domain(domain):
        return False, "Does not resolve"
    return True, "Valid"

def read_domains_from_file(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]

def process_domains(file_path):
    print(f"Processing domains from {file_path}...")
    domains = read_domains_from_file(file_path)
    good_domains = []
    bad_domains = []

    for i, domain in enumerate(domains, start=1):
        is_valid, reason = validate_domain(domain)
        status_message = f"Domain {i}: {domain} - {reason}"
        if is_valid:
            print(GREEN + status_message + RESET)
            good_domains.append(domain)
        else:
            print(RED + status_message + RESET)
            bad_domains.append(domain)

    with open("good_domains.txt", "w") as f:
        for domain in good_domains:
            f.write(f"{domain}\n")

    with open("bad_domains.txt", "w") as f:
        for domain in bad_domains:
            f.write(f"{domain}\n")

    print("Validation complete.")
    print(f"Results: {len(good_domains)} good domains and {len(bad_domains)} bad domains were identified.")

def list_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def select_file(files):
    print("Select a file to process:")
    for index, file in enumerate(files):
        print(f"{index + 1}: {file}")
    choice = int(input("Enter the number of the file: ")) - 1
    return files[choice]

def main():
    print("Listing files...")
    current_directory = os.getcwd()
    files = list_files(current_directory)
    selected_file = select_file(files)
    process_domains(selected_file)

if __name__ == "__main__":
    main()
