import re

# Regex for detecting localization keys
LOCALIZATION_KEY_REGEX = re.compile(
    r"\b[A-Z]{2,}_[A-Z0-9_]{2,}\b|\b[A-Z]{2,}\.[A-Z0-9_.]{2,}\b"
)

# Known allowed technical strings (whitelist)
WHITELIST = {
    "API",
    "HTTP",
    "HTTPS",
}

# Prefixes commonly used in DIGIT TL module
LOCALIZATION_PREFIXES = (
    "TL_",
    "TL.",
)
