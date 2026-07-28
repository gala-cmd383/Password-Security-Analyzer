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
