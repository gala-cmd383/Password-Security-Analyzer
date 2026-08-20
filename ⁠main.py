import sys
from getpass import getpass
from password_analyzer.analyzer import PasswordAnalyzer

def main():
    print("=" * 35)
    print("    Password Security Analyzer    ")
    print("=" * 35)
    
    # Prompt the user for input securely without echoing characters
    password = getpass("Enter password to analyze (input hidden): ").strip()
    
    if not password:
        print("[!] Error: Password cannot be empty.")
        sys.exit(1)

    print("\n[+] Analyzing password strength and integrity...")
    
    try:
        analyzer = PasswordAnalyzer(password)

        # 1. Calculate Shannon Entropy
        entropy = analyzer.calculate_entropy()
        print(f"[*] Shannon Entropy : {entropy:.2f} bits")

        # 2. Check for breaches via HIBP API
        breaches = analyzer.check_breach()
        
        if breaches > 0:
            print(f"[!] Alert           : Compromised! Found in breaches {breaches:,} times.")
        elif breaches == 0:
            print("[✓] Status          : Clean (No breaches found in HIBP database).")
        else:
            print("[-] Warning         : Breach check skipped or service unreachable.")

    except Exception as e:
        print(f"[!] An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
