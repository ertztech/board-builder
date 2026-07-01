import json

from trello import (
    get_board,
    create_trello_list,
    create_trello_card
)

with open("templates/after_the_amen.json", "r", encoding="utf-8") as file:
    project = json.load(file)

board = get_board(project["board"])

if board is None:
    print("Board not found.")
    exit()

print(f'Building "{project["board"]}"')

for list_data in project["lists"]:

    trello_list = create_trello_list(
        board["id"],
        list_data["name"]
    )

    if trello_list is None:
        continue

    for card_name in list_data["cards"]:
        create_trello_card(
            trello_list["id"],
            card_name
        )

print("Done!")