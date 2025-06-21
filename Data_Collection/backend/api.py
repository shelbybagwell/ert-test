import requests as r
import json


class NOAA_SWPC_API:
    def __init__(self) -> None:
        self.base_url = "https://services.swpc.noaa.gov/"
        self.geospace_subpath = "products/geospace/"

    def get_RTSW(self) -> list[dict]:
        response = r.get(
            f"{self.base_url}{self.geospace_subpath}/propagated-solar-wind-1-hour.json"
        )
        if response.status_code != 200:
            print(f"Error {response.status_code}: {response.text}")
            return []
        res = response.json()
        # The way this data returns is a list of lists, where the first element
        # is the keys, and the rest are data.
        keys = res[0]
        data = res[1:]

        rtsw = [dict(zip(keys, datum)) for datum in data]
        return rtsw
