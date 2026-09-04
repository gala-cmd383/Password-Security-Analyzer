# Password Security Analyzer

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

# Password Security Analyzer 🔐

A modular, defensive Python tool and package designed to evaluate password strength using theoretical **Shannon Entropy** and check for compromised credentials via the **Have I Been Pwned (HIBP) API** using the **k-Anonymity** model.

---

## 🌟 Key Features

* **Shannon Entropy Analysis:** Evaluates theoretical randomness and complexity using:
  $$E = L \times \log_2(R)$$
  *(where $L$ is password length and $R$ is character pool size).*
* **Real-World Breach Detection:** Queries the official Have I Been Pwned (HIBP) database to detect if credentials appeared in known data breaches.
* **Privacy-Preserving (k-Anonymity):** Generates client-side SHA-1 hashes and transmits only the first 5 characters (prefix) over the network. Plaintext passwords never leave the local environment.
* **Modular Interface:** Usable as a standalone CLI tool or imported directly into Python applications.

---

## 📁 Project Structure

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

---
🚀 Installation
Clone the repository:

Bash
git clone [https://github.com/gala-cmd383/Password-Security-Analyzer.git](https://github.com/gala-cmd383/Password-Security-Analyzer.git)
cd Password-Security-Analyzer
Install dependencies:

Bash
pip install -r requirements.txt

---

## Usage

### 1. As a Python Library

```python
from password_analyzer.analyzer import PasswordAnalyzer

# Initialize with target password
analyzer = PasswordAnalyzer("SuperSecurePass2026!#")

# 1. Calculate theoretical entropy
entropy = analyzer.calculate_entropy()
print(f"Shannon Entropy: {entropy:.2f} bits")

# 2. Check for known data breaches
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

This tool is created for educational, analytical, and defensive security workflows. It strictly adheres to privacy standards:

No plaintext passwords are stored, logged, or transmitted.

API interactions strictly follow k-Anonymity protocols.

---


📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
