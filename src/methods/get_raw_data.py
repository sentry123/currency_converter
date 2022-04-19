"""

"""

import pandas as pd
from request_handler import request_handler


def get_raw_data(identifier: str) -> pd.DataFrame:
    """

    :param identifier: string
    :return: pandas dataframe
    """

    url = "https://sdw-wsrest.ecb.europa.eu/service/data/BP6/" + identifier + "?detail=dataonly"
    return request_handler(url)


print(get_raw_data("M.N.I8.W1.S1.S1.T.N.FA.F.F7.T.EUR._T.T.N"))
