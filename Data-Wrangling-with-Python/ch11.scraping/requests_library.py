import requests

goog = requests.get('http://google.com')

print goog.status_code
print goog.content[:200]
print goog.headers
print goog.cookies.items()
