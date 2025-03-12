import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon
from pyproj import Transformer

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False


class DisasterEvent:
    def __init__(self):
        self.is_above_threshold = False


class HeatWave(DisasterEvent):
    def __init__(self):
        super().__init__()


class ColdWave(DisasterEvent):
    def __init__(self):
        super().__init__()


class Earthquake(DisasterEvent):
    def __init__(self):
        super().__init__()


class Flood(DisasterEvent):
    def __init__(self):
        super().__init__()


class FineDust(DisasterEvent):
    def __init__(self):
        super().__init__()
