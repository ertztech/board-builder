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
            return board

    return None


def create_trello_list(board_id, list_name):
    response = requests.post(
        f"https://api.trello.com/1/boards/{board_id}/lists",
        params={
            "key": api_key,
            "token": token,
            "name": list_name
        }
    )

    return handle_response(response)


def create_trello_card(list_id, card_name):
    response = requests.post(
        "https://api.trello.com/1/cards",
        params={
            "key": api_key,
            "token": token,
            "idList": list_id,
            "name": card_name
        }
    )

    return handle_response(response)