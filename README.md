
# Domain Scanner

This Python script automates the process of scanning multiple domains using two tools: **Subdominator** and **HTTPX**. The script allows users to either input a list of domains or specify a file containing the domains. The results are saved in a structured directory, with each domain's scan results stored in a separate folder.

## Requirements

Before running the script, ensure that the following tools are installed on your system:

- **Subdominator**: A tool for subdomain enumeration.
- **HTTPX**: A fast and multi-purpose HTTP toolkit to perform various tests on the domain.

Make sure **Subdominator** and **HTTPX** are properly installed and accessible from the terminal.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/domain-scanner.git
    cd domain-scanner
    ```

2. Install required Python libraries (if needed):
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Input Domains

You can provide domains in two ways:
1. **Enter domains manually** separated by a symbol (e.g., comma or space).
2. **Provide a file path** containing the domains, one domain per line.

### Running the Script

Run the script using the following command:

```bash
python3 scanner.py
```

The script will prompt you to enter domains or a file path containing domains.

### Output

The results for each domain are saved in a directory named `domain_scan_results`. Inside, you'll find folders named after each domain, with a `combined_output.txt` file containing the results of both the **Subdominator** and **HTTPX** scans.

Example output:

```
domain_scan_results/
    example_com/
        combined_output.txt
    anotherdomain_com/
        combined_output.txt
```

## Script Overview

- **run_scan(target)**: Runs the **Subdominator** and **HTTPX** commands for a given domain and returns their outputs.
- **get_domains()**: Prompts the user for domain input and returns a list of domains either from user input or a file.
- **main()**: The main function that processes the domains, runs the scans, and saves the results.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
