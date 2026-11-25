"""Locally generate high-entropy passwords using secrets."""
import argparse, math, secrets, string

def generate(length=20, symbols=True):
    if length < 12:
        raise ValueError("Choose at least 12 characters.")
    alphabet = string.ascii_letters + string.digits + (string.punctuation if symbols else "")
    # Guarantee at least one character from each enabled class.
    pools = [string.ascii_lowercase, string.ascii_uppercase, string.digits]
    if symbols:
        pools.append(string.punctuation)
    chars = [secrets.choice(pool) for pool in pools]
    chars.extend(secrets.choice(alphabet) for _ in range(length-len(chars)))
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars), len(alphabet)

def main():
    parser = argparse.ArgumentParser(description="Generate a secure password locally.")
    parser.add_argument("--length", type=int, default=20)
    parser.add_argument("--no-symbols", action="store_true")
    args = parser.parse_args()
    try:
        password, alphabet_size = generate(args.length, not args.no_symbols)
    except ValueError as exc:
        parser.error(str(exc))
    entropy = args.length * math.log2(alphabet_size)
    print(password)
    print(f"Estimated search-space entropy: {entropy:.1f} bits")
    print("Store it in a password manager; do not reuse it.")

if __name__ == "__main__":
    main()
