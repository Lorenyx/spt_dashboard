import socket
import httpx
from contextlib import suppress
from ..constants import SPT_SERVER_HOST, SPT_SERVER_PORT, SPT_PROFILES_URL, FIKA_PLAYERS_URL, SPT_SERVER_TIMEOUT


def is_spt_server_active():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        result = s.connect_ex((SPT_SERVER_HOST, SPT_SERVER_PORT))
        return result == 0


def get_profiles():
    with suppress(httpx._exceptions.HTTPError):
        response = httpx.get(SPT_PROFILES_URL, timeout=SPT_SERVER_TIMEOUT)
        if response.status_code == 200:
            profiles = response.json()
            return profiles
    return []


def get_active_players():
    with suppress(httpx._exceptions.HTTPError):
        response = httpx.get(FIKA_PLAYERS_URL, timeout=SPT_SERVER_TIMEOUT)
        if response.is_success:
            players = response.json()
            return players
    return []
