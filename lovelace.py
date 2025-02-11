
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='darkgrid')
import plotly.graph_objs as go
import plotly.offline as py

from google.colab import files
uploaded = files.upload()

from zipfile import ZipFile
file_name = "HeartDataCE101.zip"
with ZipFile(file_name, "r") as zip:
  zip.extractall()

import pandas as pd

# Read the CSV file
heart_data = pd.read_csv("heart.csv")
# View the first 5 rows
heart_data.head()

heart_data.columns = ['Age', 'Sex', 'Chest_pain_type', 'Resting_bp',
              'Cholesterol', 'Fasting_bs', 'Resting_ecg',
              'Max_heart_rate', 'Exercise_induced_angina',
              'ST_depression', 'ST_slope', 'Num_major_vessels',
              'Thallium_test', 'Condition']

heart_data.head()

heart_data.describe()

heart_data.isnull().sum()
