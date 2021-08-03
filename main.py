import face_recognition
import pandas as pd
import cv2
import numpy as np
from sklearn import neighbors

database = pd.read_csv("data.csv")
database.head(15)

#Need for describing the data as it is recieved
database['Ethnicity'] = pd.to_numeric(database['Ethnicity'],errors='coerce')
database.describe()

