import re

PATTERNS_CITY = r'^\*[A-za-zА-я-а-я]+'


def regular_search(patterns, text):
    """Вернет правду если выражение верно, используется в поиске по параметрам"""
    if re.search(patterns, text):
        return True
    else:
        return False
