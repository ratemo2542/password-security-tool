# Password Security Tool

Generate random passwords using Python's cryptographically secure `secrets` module. Passwords are generated locally and are never saved or transmitted.

## Requirements
- Python 3.10+
- No third-party packages

## Run
```bash
python main.py --length 20
python main.py --length 24 --no-symbols
```

The tool prints a generated password once. Copy it into a trusted password manager. Do not reuse passwords across accounts.

## Security note
The strength estimate is a rough entropy calculation, not a guarantee that a password is safe against every attack. Avoid sharing terminal screenshots containing generated passwords.
