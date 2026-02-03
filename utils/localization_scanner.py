from configs.localization_config import (
    LOCALIZATION_KEY_REGEX,
    LOCALIZATION_PREFIXES,
    WHITELIST,
)

def find_non_localized_text(text: str) -> set[str]:
    """
    Scans text and returns a set of suspected non-localized strings.
    """
    findings = set()

    for match in LOCALIZATION_KEY_REGEX.findall(text):
        if match in WHITELIST:
            continue

        if match.startswith(LOCALIZATION_PREFIXES):
            findings.add(match)
        else:
            findings.add(match)

    return findings
