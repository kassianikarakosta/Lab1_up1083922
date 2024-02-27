import requests

url = input("Give a URL:\n")  # προσδιορισμός του url

if not url.startswith("https://"):
    url = "https://" + url

