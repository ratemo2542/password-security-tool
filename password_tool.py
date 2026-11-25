"""Generate passwords and estimate basic password strength."""
import argparse
import secrets
import string

def generate(length: int = 20, symbols: bool = True) -> str:
    if length < 8 or length > 128:
        raise ValueError("Length must be between 8 and 128.")
    alphabet = string.ascii_letters + string.digits + (string.punctuation if symbols else "")
    # Guarantee character-class coverage, then cryptographically shuffle.
    required = [secrets.choice(string.ascii_lowercase), secrets.choice(string.ascii_uppercase),
                secrets.choice(string.digits)]
    if symbols:
        required.append(secrets.choice(string.punctuation))
    password = required + [secrets.choice(alphabet) for _ in range(length - len(required))]
    secrets.SystemRandom().shuffle(password)
    return "".join(password)

def score(password: str) -> tuple[str, list[str]]:
    tips = []
    if len(password) < 12: tips.append("Use at least 12 characters.")
    if not any(c.islower() for c in password): tips.append("Add lowercase letters.")
    if not any(c.isupper() for c in password): tips.append("Add uppercase letters.")
    if not any(c.isdigit() for c in password): tips.append("Add numbers.")
    if not any(not c.isalnum() for c in password): tips.append("Add symbols.")
    score_value = 5 - len(tips)
    return (["Very weak", "Weak", "Fair", "Good", "Strong", "Excellent"][score_value], tips)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-l", "--length", type=int, default=20)
    parser.add_argument("--no-symbols", action="store_true")
    parser.add_argument("--check", help="Check a password locally (not transmitted)")
    args = parser.parse_args()
    if args.check is not None:
        label, tips = score(args.check)
        print(f"Assessment: {label}")
        for tip in tips: print(f"- {tip}")
    else:
        print(generate(args.length, not args.no_symbols))

if __name__ == "__main__": main()
