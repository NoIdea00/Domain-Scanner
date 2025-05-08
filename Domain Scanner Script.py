#!/usr/bin/env python3

import subprocess
import os

def run_scan(target):
    # Run subdominator and httpx commands
    subdominator_cmd = f"subdominator -d {target}"
    httpx_cmd = f"~/go/bin/httpx -silent -title -tech-detect -status-code"

    try:
        subdominator_output = subprocess.check_output(subdominator_cmd, shell=True).decode()
        httpx_output = subprocess.check_output(f"{subdominator_cmd} | {httpx_cmd}", shell=True).decode()
    except subprocess.CalledProcessError as e:
        subdominator_output = f"Error running subdominator: {e.output.decode()}"
        httpx_output = f"Error running httpx: {e.output.decode()}"
    
    return subdominator_output, httpx_output

def get_domains():
    # Prompt user for domain input
    print("Enter domains separated by a symbol (e.g., comma, space) or provide a file path:")
    input_data = input().strip()
    
    if os.path.isfile(input_data):
        # Read domains from file
        with open(input_data, 'r') as file:
            domains = [line.strip() for line in file if line.strip()]
    else:
        # Split domains by symbol
        domains = [domain.strip() for domain in input_data.replace(',', ' ').split() if domain.strip()]
    
    return domains

def main():
    # Get user input
    domains = get_domains()
    
    # Ensure at least one domain is provided
    if not domains:
        print("No domains provided. Exiting.")
        return
    
    # Create directory for results
    results_dir = "domain_scan_results"
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
    
    for target in domains:
        print(f"Processing {target}...")
        
        # Create a directory for each domain
        domain_dir = os.path.join(results_dir, target.replace('.', '_'))
        if not os.path.exists(domain_dir):
            os.makedirs(domain_dir)
        
        # Run commands and get their outputs
        print("Running scan...")
        subdominator_output, httpx_output = run_scan(target)
        
        # Combine outputs and save to a file
        combined_output = f"Subdominator Output:\n{subdominator_output}\n\nHTTPX Output:\n{httpx_output}"
        
        file_path = os.path.join(domain_dir, 'combined_output.txt')
        with open(file_path, 'w') as f:
            f.write(combined_output)
        
        print(f"Results for {target} saved to '{file_path}'.")

if __name__ == "__main__":
    main()
