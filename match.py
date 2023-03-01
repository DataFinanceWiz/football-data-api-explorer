import requests
import csv

endpoint = "https://api.football-data.org/v2/matches"
api_key = "e6e53ebde68d49488baa0187c06c6dab"

headers = {
    "X-Auth-Token": api_key
}

response = requests.get(endpoint, headers=headers)

if response.status_code == 200:
    data = response.json()
    matches = data["matches"]

    with open("matches.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["homeTeam", "awayTeam", "competition", "status", "utcDate"])
        writer.writeheader()
        for match in matches:
            writer.writerow({
                "homeTeam": match["homeTeam"]["name"],
                "awayTeam": match["awayTeam"]["name"],
                "competition": match["competition"]["name"],
                "status": match["status"],
                "utcDate": match["utcDate"],
            })

    print("Data has been successfully written to the CSV file")
else:
    print("Failed to retrieve data from the API. Response code:", response.status_code)
