import re

PATTERNS_CITY = r'^\*[A-za-zА-я-а-я]+'


def regular_search(text):
    if re.search(PATTERNS_CITY, text):
        return True
    else:
        return False
