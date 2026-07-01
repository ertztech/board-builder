import requests
from config import api_key, token


def handle_response(response):
    if response.status_code >= 400:
        print(f"Error {response.status_code}")
        print(response.text)
        return None

    return response.json()


def get_board(board_name):
    response = requests.get(
        "https://api.trello.com/1/members/me/boards",
        params={
            "key": api_key,
            "token": token
        }
    )

    boards = handle_response(response)

    if boards is None:
        return None

    for board in boards:
        if board["name"] == board_name:
            print(f'Board already exists: {board_name}')
            return board

    print(f'Creating board: {board_name}')

    response = requests.post(
        "https://api.trello.com/1/boards",
        params={
            "key": api_key,
            "token": token,
            "name": board_name
        }
    )

    return handle_response(response)

def get_lists(board_id):
    response = requests.get(
        f"https://api.trello.com/1/boards/{board_id}/lists",
        params={
            "key": api_key,
            "token": token
        }
    )

    return handle_response(response)

def get_cards(list_id):
    response = requests.get(
        f"https://api.trello.com/1/lists/{list_id}/cards",
        params={
            "key": api_key,
            "token": token
        }
    )

    return handle_response(response)

def create_trello_list(board_id, list_name):

    lists = get_lists(board_id)

    for trello_list in lists:
        if trello_list["name"] == list_name:
            print(f"List already exists: {list_name}")
            return trello_list

    response = requests.post(
        f"https://api.trello.com/1/boards/{board_id}/lists",
        params={
            "key": api_key,
            "token": token,
            "name": list_name
        }
    )

    print(f"Created list: {list_name}")

    return handle_response(response)


def create_trello_card(list_id, card):

    if isinstance(card, str):
        card_name = card
        card_description = ""
    else:
        card_name = card["name"]
        card_description = card.get("description", "")

    cards = get_cards(list_id)

    for existing_card in cards:
        if existing_card["name"] == card_name:
            print(f"Card already exists: {card_name}")
            return existing_card

    response = requests.post(
        "https://api.trello.com/1/cards",
        params={
            "key": api_key,
            "token": token,
            "idList": list_id,
            "name": card_name,
            "desc": card_description
        }
    )

    print(f"Created card: {card_name}")

    return handle_response(response)