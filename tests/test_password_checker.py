from password_checker import check_password_strength


def test_very_strong_password():
    result = check_password_strength("Tr0ub4dor&3Long!")
    assert result.level in {"Very Strong", "Strong"}
    assert result.score >= 5


def test_weak_password_common_pattern():
    result = check_password_strength("password123")
    assert result.level == "Weak"
    assert any("common" in suggestion.lower() for suggestion in result.suggestions)


def test_missing_character_classes():
    result = check_password_strength("alllowercase")
    assert any("uppercase" in suggestion.lower() for suggestion in result.suggestions)
    assert any("numbers" in suggestion.lower() for suggestion in result.suggestions)
    assert any("symbol" in suggestion.lower() for suggestion in result.suggestions)
