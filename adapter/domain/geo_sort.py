from pydantic import BaseModel
from typing import List

class Properties(BaseModel):
    url: str
    var: str
    project: str
    Device: str
    Device_id: str
    IFOV: str
    MFOV: str
    ACC: str
    Date: str
    Time: str
    tag: str
    x: float
    y: float
    xmax: float
    ymax: float
    hotspot_type: str
    priority: int
    maxTemperature: float
    minTemperature: float
    maxIndex: List[int]
    minIndex: List[int]
    pv_brand: str
    normal_temp: float
    pv_min: str
    cell_size: str

class Geometry(BaseModel):
    type: str
    coordinates: List[str]

class Feature(BaseModel):
    type: str
    properties: Properties
    geometry: Geometry

class FeatureCollection(BaseModel):
    type: str
    features: List[Feature]

def Data01(data):
    results = []

    for feature in data['features']:
        # project = feature['properties']['project']
        max_Temperature = feature['properties']['maxTemperature']
        hotspot_type = feature['properties']['hotspot_type']
        priority = feature['properties']['priority']
        string_tag = feature['properties']['tag']

        result = {
            # "Project": project,
            "Max Temperature": max_Temperature,
            "hotspot_type": hotspot_type,
            "priority": priority,
            "string_tag": string_tag
        }

        results.append(result)

    return results

