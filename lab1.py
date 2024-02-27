import requests

url = input("Give a URL:\n")  # προσδιορισμός του url

if not url.startswith("https://"):
    url = "https://" + url

print("\n")

with requests.get(url) as response:  # το αντικείμενο response

    # Εκτυπώνουμε τις κεφαλίδες της απόκρισης HTTP
    print("Κεφαλίδες της απόκρισης HTTP:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")

    print("\n")

# Πληροφορίες για τον εξυπηρετητή
    print("Λογισμικό εξυπηρετητή:")
    print(f"{response.headers.get('Server', 'Server not found')}")

    print("\n")

