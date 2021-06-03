import re

PATTERNS_CITY = r'^\*[A-za-zА-я-а-я]+'


def regular_search(patterns, text):
    if re.search(patterns, text):
        return True
    else:
        return False
