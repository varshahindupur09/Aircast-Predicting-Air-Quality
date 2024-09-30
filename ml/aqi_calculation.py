import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from sklearn.metrics import accuracy_score,confusion_matrix

def caluclate_aqi(df):
        def get_PM25_subindex(x):
            if x <= 30:
                return x * 50 / 30
            elif x <= 60:
                return 50 + (x - 30) * 50 / 30
            elif x <= 90:
                return 100 + (x - 60) * 100 / 30
            elif x <= 120:
                return 200 + (x - 90) * 100 / 30
            elif x <= 250:
                return 300 + (x - 120) * 100 / 130
            elif x > 250:
                return 400 + (x - 250) * 100 / 130
            else:
                return 0

        df["PM2.5_SubIndex"] = df["PM2.5_24hr_avg"].apply(lambda x: get_PM25_subindex(x))
        ## PM10 Sub-Index calculation
        def get_PM10_subindex(x):
            if x <= 50:
                return x
            elif x <= 100:
                return x
            elif x <= 250:
                return 100 + (x - 100) * 100 / 150
            elif x <= 350:
                return 200 + (x - 250)
            elif x <= 430:
                return 300 + (x - 350) * 100 / 80
            elif x > 430:
                return 400 + (x - 430) * 100 / 80
            else:
                return 0

        df["PM10_SubIndex"] = df["PM10_24hr_avg"].apply(lambda x: get_PM10_subindex(x))

        ## SO2 Sub-Index calculation
        def get_SO2_subindex(x):
            if x <= 40:
                return x * 50 / 40
            elif x <= 80:
                return 50 + (x - 40) * 50 / 40
            elif x <= 380:
                return 100 + (x - 80) * 100 / 300
            elif x <= 800:
                return 200 + (x - 380) * 100 / 420
            elif x <= 1600:
                return 300 + (x - 800) * 100 / 800
            elif x > 1600:
                return 400 + (x - 1600) * 100 / 800
            else:
                return 0

        df["SO2_SubIndex"] = df["SO2_24hr_avg"].apply(lambda x: get_SO2_subindex(x))

        ## NOx Sub-Index calculation
        def get_NOx_subindex(x):
            if x <= 40:
                return x * 50 / 40
            elif x <= 80:
                return 50 + (x - 40) * 50 / 40
            elif x <= 180:
                return 100 + (x - 80) * 100 / 100
            elif x <= 280:
                return 200 + (x - 180) * 100 / 100
            elif x <= 400:
                return 300 + (x - 280) * 100 / 120
            elif x > 400:
                return 400 + (x - 400) * 100 / 120
            else:
                return 0

        df["NOx_SubIndex"] = df["NOx_24hr_avg"].apply(lambda x: get_NOx_subindex(x))
        ## CO Sub-Index calculation
        def get_CO_subindex(x):
            if x <= 1:
                return x * 50 / 1
            elif x <= 2:
                return 50 + (x - 1) * 50 / 1
            elif x <= 10:
                return 100 + (x - 2) * 100 / 8
            elif x <= 17:
                return 200 + (x - 10) * 100 / 7
            elif x <= 34:
                return 300 + (x - 17) * 100 / 17
            elif x > 34:
                return 400 + (x - 34) * 100 / 17
            else:
                return 0

        df["CO_SubIndex"] = df["CO_8hr_max"].apply(lambda x: get_CO_subindex(x))
        ## O3 Sub-Index calculation
        def get_O3_subindex(x):
            if x <= 50:
                return x * 50 / 50
            elif x <= 100:
                return 50 + (x - 50) * 50 / 50
            elif x <= 168:
                return 100 + (x - 100) * 100 / 68
            elif x <= 208:
                return 200 + (x - 168) * 100 / 40
            elif x <= 748:
                return 300 + (x - 208) * 100 / 539
            elif x > 748:
                return 400 + (x - 400) * 100 / 539
            else:
                return 0

        df["O3_SubIndex"] = df["O3_8hr_max"].apply(lambda x: get_O3_subindex(x))