"""
request_handler function takes an url :String as an input, parses the xml response from the api call
and returns a pandas dataframe with the columns 'TIME_PERIOD' and 'OBS_VALUE'.
"""

import requests
import pandas as pd
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError


def request_handler(url: str) -> pd.DataFrame:
    """

    :param url: string
    :return: pandas dataframe
    """
    try:
        response = requests.get(url)
        root = ET.fromstring(response.content)
        exchange_rate_list = []

        for ObsValue, ObsDimension in zip(
                root.iter('{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic}ObsValue'),
                root.iter('{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic}ObsDimension')):
            obs_value = ObsValue.attrib.get("value")
            time_period = ObsDimension.attrib.get("value")
            exchange_rate_list.append([time_period, float(obs_value)])

        exchange_rate_list_df = pd.DataFrame(exchange_rate_list, columns=['TIME_PERIOD', 'OBS_VALUE'])
        return exchange_rate_list_df
    except ParseError as PE:
        print(f"Exception Occurred in request_handler => {PE.msg}")
