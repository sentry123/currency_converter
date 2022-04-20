"""

"""
from typing import Optional
import pandas as pd
from get_raw_data import get_raw_data
from get_exchange_rate import get_exchange_rate


def get_data(identifier: str, target_currency: Optional[str] = None) -> pd.DataFrame:
    """

    :param identifier:
    :param target_currency:
    :return:
    """
    if target_currency is None:
        try:
            identifier = "".join([x for x in identifier if x != '"'])
            return get_raw_data(identifier)
        except ModuleNotFoundError:
            print("Module not found")
    else:
        source_currency = (identifier.split('.'))[12]
        target_currency = "".join([x for x in target_currency if x != '"'])
        return get_exchange_rate(source_currency, target_currency)
