import pandas

class DataManager:
    #This class is responsible for data storage in csv file.
    FILENAME='prices.csv'

    @classmethod
    def get_prices(cls):
        return pandas.read_csv(cls.FILENAME,keep_default_na=False)

    @classmethod
    def set_prices(cls,data: pandas.DataFrame):
        data.to_csv(cls.FILENAME,index=False)
