"""Simple password strength checker.

Usage:
    python password_checker.py "MyPassword123!"
"""

from __future__ import annotations

import re
import string
import sys
from dataclasses import dataclass
from typing import List


@dataclass
class CheckResult:
    score: int
    level: str
    suggestions: List[str]


def check_password_strength(password: str) -> CheckResult:
    """Evaluate password strength and return actionable feedback.

    Score range: 0-6
    """

    suggestions: List[str] = []
    score = 0

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 12 characters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    if any(ch in string.punctuation for ch in password):
        score += 1
    else:
        suggestions.append("Add a symbol (e.g., !@#$%).")

    repeated = re.search(r"(.)\1\1", password)
    if repeated:
        score = max(score - 1, 0)
        suggestions.append("Avoid repeating the same character 3+ times in a row.")

    common_patterns = ["password", "qwerty", "123456", "admin"]
    if any(p in password.lower() for p in common_patterns):
        score = max(score - 2, 0)
        suggestions.append("Avoid common words/sequences like 'password' or '123456'.")

    if score >= 6:
        level = "Very Strong"
    elif score >= 4:
        level = "Strong"
    elif score >= 2:
        level = "Moderate"
    else:
        level = "Weak"

    return CheckResult(score=score, level=level, suggestions=suggestions)


def main(argv: List[str]) -> int:
    if len(argv) != 2:
        print("Usage: python password_checker.py '<password>'")
        return 1

    result = check_password_strength(argv[1])
    print(f"Score: {result.score}/6")
    print(f"Strength: {result.level}")
    if result.suggestions:
        print("Suggestions:")
        for item in result.suggestions:
            print(f"- {item}")
    else:
        print("Great password hygiene. No suggestions.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
