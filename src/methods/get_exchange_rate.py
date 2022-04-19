"""
get_exchange_rate function fetches the exchangerate data from the appropriate URL and converts it to a pandas
DataFrame,with columns TIME_PERIOD and OBS_VALUE,corresponding to value of
generic:ObsDimension and generic:ObsValue tags from the XML.OBS_VALUE is converted
to float.
"""

import pandas as pd
from request_handler import request_handler


def get_exchange_rate(source: str, target: str = "EUR") -> pd.DataFrame:
    """

    :param source: str
    :param target: str
    :return: returns a pandas dataframe containing the ObsDimension and ObsValue from the api response xml
    """

    url = "https://sdw-wsrest.ecb.europa.eu/service/data/EXR/M." + source + "." + target + ".SP00.A?detail=dataonly"
    return request_handler(url)


print(get_exchange_rate("GBP", "EUR"))
