import json
import sys

from trello import (
    get_board,
    create_trello_list,
    create_trello_card
)

if len(sys.argv) < 2:
    print("Usage:")
    print("python board_builder.py <template.json>")
    exit()

template = sys.argv[1]

with open(template, "r", encoding="utf-8") as file:
    project = json.load(file)

print()
print("=" * 50)
print(f'Building "{project["board"]}"')
print("=" * 50)

board = get_board(project["board"])

if board is None:
    print("❌ Board not found")
    exit()

print("✓ Board found")

list_count = 0
card_count = 0

for list_data in project["lists"]:

    trello_list = create_trello_list(
        board["id"],
        list_data["name"]
    )

    if trello_list is None:
        continue

    list_count += 1

    print(f"\n📋 {list_data['name']}")

    for card_name in list_data["cards"]:

        create_trello_card(
            trello_list["id"],
            card_name
        )

        card_count += 1

print()
print("=" * 50)
print("Build Complete!")
print(f"Lists Processed : {list_count}")
print(f"Cards Processed : {card_count}")
print("=" * 50)