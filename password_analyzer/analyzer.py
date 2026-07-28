import hashlib
import math
import requests

class PasswordAnalyzer:
    def __init__(self, password: str):
        self.password = password

    def calculate_entropy(self) -> float:
        length = len(self.password)
        if length == 0:
            return 0.0

        r_size = 0
        if any(c.islower() for c in self.password):
            r_size += 26
        if any(c.isupper() for c in self.password):
            r_size += 26
        if any(c.isdigit() for c in self.password):
            r_size += 10
        if any(not c.isalnum() for c in self.password):
            r_size += 32

        if r_size == 0:
            return 0.0

        entropy = length * math.log2(r_size)
        return round(entropy, 2)

    def check_breach(self) -> int:
        sha1_password = hashlib.sha1(self.password.encode("utf-8")).hexdigest().upper()
        
        prefix = sha1_password[:5]
        suffix = sha1_password[5:]

        url = f"https://api.pwnedpasswords.com/range/{prefix}"

        try:
            response = requests.get(url, timeout=5)
            if response.status_code != 200:
                raise RuntimeError(f"API connection error: {response.status_code}")

            hashes = (line.split(":") for line in response.text.splitlines())
            for h, count in hashes:
                if h == suffix:
                    return int(count) 

            return 0 

        except requests.RequestException as e:
            print(f"Server connection error: {e}")
            return -1
