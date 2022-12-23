import pickle
import numpy as np
import pandas as pd
import locale


def get_user_input(form: dict) -> dict:
    user_input = dict()
    user_input["CropItem"] = form["CropItem"]
    user_input["Year"] = int(form["Year"])
    user_input["Nutrients(tonnes)"] = float(form["Nutrients(tonnes)"])
    user_input["SyntheticFert(tonnes)"] = float(form["SyntheticFert(tonnes)"])
    user_input["Pesticides(tonnes)"] = float(form["Pesticides(tonnes)"])
    user_input["Temp_ann_degC"] = float(form["Temp_ann_degC"])
    user_input["LandUsed"] = float(form["LandUsed"])
    user_input["LandIrrigated"] = float(form["LandIrrigated"])
    user_input["MarketPrice"] = float(form["MarketPrice"])
    return user_input


def convert_units(user_input: dict) -> dict:
    user_input["Nutrients(tonnes)"] /= 1000
    user_input["SyntheticFert(tonnes)"] /= 1000
    user_input["Pesticides(tonnes)"] /= 1000
    user_input["LandUsed"] /= 2471.052
    user_input["LandIrrigated"] /= 2471.052
    return user_input


def get_df(user_input: dict) -> pd.DataFrame:
    return pd.DataFrame(user_input, columns=list(user_input.keys()), index=[0])


def get_processed_data(user_input: dict) -> np.ndarray:
    user_input = convert_units(user_input)
    user_df = get_df(user_input)
    dpm = pickle.load(open("models/full_pipeline_model.sav", "rb"))
    user_processed = dpm.transform(user_df)
    return user_processed


def get_predicted_yield(processed_data) -> float:
    rfm = pickle.load(open("models/rf_regmodel.sav", "rb"))
    yield_value = rfm.predict(processed_data)
    return yield_value[0] / 24.17


def get_yield(user_input: dict) -> float:
    processed_data = get_processed_data(user_input)
    yield_value = get_predicted_yield(processed_data)
    yield_value = round(yield_value, 3)
    return yield_value


def get_inflation_rate() -> float:
    inflation = pd.read_csv("datasets/InflationRates.csv")
    inflation = inflation[["Year", "Months", "Value"]]
    inflation["Value"].fillna(value=inflation["Value"].median(), inplace=True)
    inflation = inflation.groupby(by=["Year"]).mean()
    inflation.reset_index(inplace=True)
    inflation["Value"] /= 2
    return round(inflation["Value"].median(), 5)


def get_predicted_price(market_price: float) -> float:
    return (100 + get_inflation_rate()) * market_price / 100


def get_income(yield_value: float, predicted_price: float, crop_area: float) -> float:
    income = yield_value * predicted_price * crop_area
    income = round(income, 2)
    locale.setlocale(locale.LC_ALL, 'en_IN')
    return locale.currency(income, grouping=True)


def get_predictions(user_input: dict) -> tuple:

    # remove market price form the dictionary
    market_price = user_input["MarketPrice"]
    del user_input["MarketPrice"]

    # considering the crop area as the land used
    crop_area = user_input["LandUsed"]
    yield_value = get_yield(user_input)
    predicted_price = get_predicted_price(market_price)
    future_income = get_income(yield_value, predicted_price, crop_area)

    return yield_value, future_income
