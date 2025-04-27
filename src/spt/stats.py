import httpx
from ..constants import SPT_SERVER, CONNECT_TIMEOUT


async def is_spt_server_active():
    async with httpx.AsyncClient(verify=False, timeout=CONNECT_TIMEOUT) as client:
        try:
            r = await client.get(SPT_SERVER)
            return r.is_success
        except httpx.HTTPError:
            return False
