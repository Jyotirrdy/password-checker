# Password Checker Project

A simple Python project that scores password strength and provides practical advice.

## Features
- Scores passwords from **0 to 6**
- Labels strength as **Weak / Moderate / Strong / Very Strong**
- Provides improvement suggestions (length, variety, common patterns, repetition)
- Includes basic tests with `pytest`

## Quick Start

```bash
python password_checker.py "MyP@ssword123"
```

Example output:

```text
Score: 5/6
Strength: Strong
Suggestions:
- Avoid common words/sequences like 'password' or '123456'.
```

## Run tests

```bash
pytest -q
```

## Password advice
- Prefer passphrases of **12+ characters**.
- Mix uppercase, lowercase, numbers, and symbols.
- Avoid reused passwords and common words/sequences.
- Use a password manager to generate and store unique passwords.
- Turn on MFA (multi-factor authentication) for important accounts.
