from typing import List

import auth
import json
import waste_class
from borasem_const import *

class BorasEMAPI:
    """Class to communicate with the Borås Energi och Miljö Garbage API."""

    def __init__(self, auth: auth.Auth):
        """Initialize the API and store the auth so we can make requests."""
        self.auth = auth

    async def async_get_schedule(self) -> List[waste_class.WastePickup]:
        """Return the schedule of the containers."""
        resp = await self.auth.request("get", (WASTE_PATH + "/" + SCHEDULE_PATH + "?" + ADDRESS_PARAM + "=Häglared Lunden 2, Dalsjöfors (44195547)"))
        resp.raise_for_status()
        response = await resp.json()
        return [waste_class.WastePickup(schedule_data, self.auth) for schedule_data in response['RhServices']]
    

    async def async_get_address(self, address: str) -> List[str]:
        """Return any matching addresses."""
        resp = await self.auth.request("post", (WASTE_PATH + "/" + ADDRESSSEARCH_PATH), json={'searchText': address })
        resp.raise_for_status()
        response = await resp.json()
        return response['Buildings']