import requests
api_key = "d4e35dda50b7a4249e6ea6b6c016f5d0"
token = "ATTA98914e607d6011b027f1c7fbc12957edcc16e6c190f9a1eaeb06677521aa8d3c09BCA480"
board_id = "6a4431232a123a5a62c54436"

url = "https://api.trello.com/1/lists"

query = {
    "key": api_key,
    "token": token,
    "idBoard": board_id,
    "name": "📋 Product Backlog"
}

response = requests.post(url, params=query)

print(response.status_code)
print(response.text)