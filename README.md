# Password Security Analyzer

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A professional Python package designed to evaluate password strength using Shannon Entropy mathematical calculations and perform breach checks via the Have I Been Pwned (HIBP) API using k-Anonymity.

---

## Features

* **Entropy Calculation:** Evaluates password complexity and randomness using Shannon Entropy:
  $$E = L \times \log_2(R)$$
  *(where $L$ is the password length and $R$ is the character pool size).*
* **Breach Detection:** Queries the official **Have I Been Pwned** API to identify compromised credentials.
* **Privacy First (k-Anonymity):** Implements client-side SHA-1 hashing. Only the first 5 characters (prefix) of the hash are sent over the network, ensuring the full password never leaves your local environment.

---

## Project Structure

```text
Password-Security-Analyzer/
│
├── password_analyzer/
│   ├── __init__.py
│   └── analyzer.py
├── .gitignore
├── LICENSE
├── main.py
├── README.md
└── requirements.txt
```

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/gala-cmd383/Password-Security-Analyzer.git](https://github.com/gala-cmd383/Password-Security-Analyzer.git)
   cd Password-Security-Analyzer
   ```

2. **Install dependencies:**
   ```bash
   pip install requests
   ```

---

## Usage

### 1. As a Python Library

```python
from password_analyzer.analyzer import PasswordAnalyzer

# Initialize with target password
analyzer = PasswordAnalyzer("SuperSecurePass2026!#")

# 1. Calculate entropy
entropy = analyzer.calculate_entropy()
print(f"Shannon Entropy: {entropy:.2f} bits")

# 2. Check for breaches
breaches = analyzer.check_breach()
if breaches > 0:
    print(f"Alert: Found in leaks {breaches:,} times!")
else:
    print("Safe: No breaches detected.")
```

### 2. Interactive CLI Tool

Run the included interactive script:

```bash
python main.py
```

**Example Output:**

```text
===================================
    Password Security Analyzer    
===================================
Enter password to analyze (input hidden): 

[+] Analyzing password strength and integrity...
[*] Shannon Entropy : 68.42 bits
[✓] Status          : Clean (No breaches found in HIBP database).
```

---

## Security & Ethics

This tool is created for educational, analytical, and defensive security purposes. It strictly adheres to standard security practices by never storing, logging, or transmitting cleartext passwords.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
