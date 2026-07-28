# Password Security Analyzer

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A professional Python package designed to evaluate password strength using Shannon Entropy mathematical calculations and perform breach checks via the HaveIBeenPwned API using k-Anonymity.

---

## Features

* **Entropy Calculation:** Measures password randomness using the formula E = L \times \log_2(R).
* **Breach Detection:** Checks if the password has been leaked using the HaveIBeenPwned API.
* **Privacy First:** Implements k-Anonymity (SHA-1 hashing) to keep passwords safe locally without exposing them over the network.

---

## Project Structure

The project is organized to support future distribution via pip:

* `password_analyzer/` 
  * `__init__.py`
  * `analyzer.py`
* `main.py`
* `README.md`

---

## Interactive Usage Example

```python
from password_analyzer.analyzer import PasswordAnalyzer

def main():
    print("=== Password Security Analyzer ===")
    
    # Prompt the user to enter a password
    test_password = input("Enter a password to analyze: ")
    
    analyzer = PasswordAnalyzer(test_password)

    print("\nAnalyzing...")
    entropy = analyzer.calculate_entropy()
    print(f"Entropy: {entropy} bits")

    breaches = analyzer.check_breach()
    
    if breaches > 0:
        print(f"Warning: Password leaked {breaches} times!")
    elif breaches == 0:
        print("Safe: Password not found in leaked databases.")
    else:
        print("Error: Could not complete the breach check.")

if __name__ == "__main__":
    main()

