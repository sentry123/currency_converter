"""
get_exchange_rate function fetches the exchangerate data from the appropriate URL and converts it to a pandas
DataFrame,with columns TIME_PERIOD and OBS_VALUE,corresponding to value of
generic:ObsDimension and generic:ObsValue tags from the XML.OBS_VALUE is converted
to float.
"""

import pandas as pd
import requests
import xml.etree.ElementTree as ET


def get_exchange_rate(source: str, target: str = "EUR") -> pd.DataFrame:
    """

    :param source: str
    :param target: str
    :return: returns a pandas dataframe containing the ObsDimension and ObsValue from the api response xml
    """

    url = "https://sdw-wsrest.ecb.europa.eu/service/data/EXR/M." + source + "." + target + ".SP00.A?detail=dataonly"
    response = requests.get(url)
    root = ET.fromstring(response.content)
    exchange_rate_list = []

    for ObsValue, ObsDimension in zip(root.iter('{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic'
                                                '}ObsValue'), root.iter('{http://www.sdmx.org/resources/sdmxml/schemas'
                                                                        '/v2_1/data/generic}ObsDimension')):
        obs_value = ObsValue.attrib.get("value")
        time_period = ObsDimension.attrib.get("value")
        exchange_rate_list.append([time_period, float(obs_value)])

    exchange_rate_list_df = pd.DataFrame(exchange_rate_list, columns=['TIME_PERIOD', 'OBS_VALUE'])
    return exchange_rate_list_df


print(get_exchange_rate("GBP", "EUR"))