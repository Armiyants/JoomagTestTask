import re

def url_validator(url):
    return True if re.search(r'^(http://www\.|https://www\.|http://|https://)?(([a-z0-9]+([\-.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(/.*)?)|(localhost{1}(:[0-9]{4,5})?(/.*)?))$', url) else False

