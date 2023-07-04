from pandas import DataFrame as pd
from pandas import concat as ct
import os
from lxml.html import fromstring
from lxml import etree as et
from numpy import array as np
from datetime import datetime as dt


filelist = [i for i in os.listdir() if i.endswith('xml')]

def prop_indas(one,two,three):
    hh = {'Name':nm, 'ppe':0, 'ppe_ad':0, 'ppe_own':0, 'ppe_own_ad':0,
    'land':0, 'land_ad':0, 'land_own':0, 'land_own_ad':0,
    'buildings':0, 'buildings_ad':0, 'buildings_own':0, 'buildings_own_ad':0,
    'plant':0, 'plant_ad':0, 'plant_own':0, 'plant_own_ad':0,
    'furniture':0, 'furniture_ad':0, 'furniture_own':0, 'furniture_own_ad':0,
    'vehicle':0, 'vehicle_ad':0, 'vehicle_own':0, 'vehicle_own_ad':0,
    'office':0, 'office_ad':0, 'office_own':0, 'office_own_ad':0,
    'computer':0, 'computer_ad':0, 'computer_own':0, 'computer_own_ad':0,
    'bp':0, 'bp_ad':0, 'bp_own':0, 'bp_own_ad':0,
    'lease':0, 'lease_ad':0, 'lease_own':0, 'lease_own_ad':0,
    'oppe':0, 'oppe_ad':0, 'oppe_own':0, 'oppe_own_ad':0}

    for i in one:
        if i.find('./xbrli:scenario/xbrldi:explicitMember',ns).get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.find('./xbrli:scenario/xbrldi:explicitMember',ns).text == "ind-as:GrossCarryingAmountMember":
            hh['ppe'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
        elif i.find('./xbrli:scenario/xbrldi:explicitMember',ns).get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.find('./xbrli:scenario/xbrldi:explicitMember',ns).text == "ind-as:AccumulatedDepreciationAndImpairmentMember":
            hh['ppe_ad'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

    for i in two:
        if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "ind-as:SubClassesOfPropertyPlantAndEquipmentAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "ind-as:OwnedAssetsMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "ind-as:GrossCarryingAmountMember":
                hh['ppe_own'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
            elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "ind-as:AccumulatedDepreciationAndImpairmentMember":
                hh['ppe_own_ad'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "ind-as:ClassesOfPropertyPlantAndEquipmentAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "ind-as:LandMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "ind-as:GrossCarryingAmountMember":
                hh['land'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
            elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "ind-as:AccumulatedDepreciationAndImpairmentMember":
                hh['land_ad'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "ind-as:ClassesOfPropertyPlantAndEquipmentAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "ind-as:BuildingsMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "ind-as:GrossCarryingAmountMember":
                hh['buildings'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
            elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "ind-as:AccumulatedDepreciationAndImpairmentMember":
                hh['buildings_ad'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "ind-as:ClassesOfPropertyPlantAndEquipmentAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "ind-as:PlantAndEquipmentMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "ind-as:GrossCarryingAmountMember":
                hh['plant'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
            elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "ind-as:AccumulatedDepreciationAndImpairmentMember":
                hh['plant_ad'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "ind-as:ClassesOfPropertyPlantAndEquipmentAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "ind-as:FurnitureAndFixturesMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "ind-as:GrossCarryingAmountMember":
                hh['furniture'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
            elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "ind-as:AccumulatedDepreciationAndImpairmentMember":
                hh['furniture_ad'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "ind-as:ClassesOfPropertyPlantAndEquipmentAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "ind-as:VehiclesMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "ind-as:GrossCarryingAmountMember":
                hh['vehicle'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
            elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "ind-as:AccumulatedDepreciationAndImpairmentMember":
                hh['vehicle_ad'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "ind-as:ClassesOfPropertyPlantAndEquipmentAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "ind-as:OfficeEquipmentMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "ind-as:GrossCarryingAmountMember":
                hh['office'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
            elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "ind-as:AccumulatedDepreciationAndImpairmentMember":
                hh['office_ad'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "ind-as:ClassesOfPropertyPlantAndEquipmentAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "ind-as:ComputerEquipmentsMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "ind-as:GrossCarryingAmountMember":
                hh['computer'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
            elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "ind-as:AccumulatedDepreciationAndImpairmentMember":
                hh['computer_ad'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "ind-as:ClassesOfPropertyPlantAndEquipmentAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "ind-as:BearerPlantsMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "ind-as:GrossCarryingAmountMember":
                hh['bp'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
            elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "ind-as:AccumulatedDepreciationAndImpairmentMember":
                hh['bp_ad'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "ind-as:ClassesOfPropertyPlantAndEquipmentAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "ind-as:LeaseholdImprovementsMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "ind-as:GrossCarryingAmountMember":
                hh['lease'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
            elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "ind-as:AccumulatedDepreciationAndImpairmentMember":
                hh['lease_ad'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "ind-as:ClassesOfPropertyPlantAndEquipmentAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "ind-as:OtherPropertyPlantAndEquipmentMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "ind-as:GrossCarryingAmountMember":
                hh['oppe'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
            elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "ind-as:AccumulatedDepreciationAndImpairmentMember":
                hh['oppe_ad'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

    for i in three:
        if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "ind-as:ClassesOfPropertyPlantAndEquipmentAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "ind-as:LandMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "ind-as:SubClassesOfPropertyPlantAndEquipmentAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "ind-as:OwnedAssetsMember":
                if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "ind-as:GrossCarryingAmountMember":
                    hh['land_own'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
                elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "ind-as:AccumulatedDepreciationAndImpairmentMember":
                    hh['land_own_ad'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "ind-as:ClassesOfPropertyPlantAndEquipmentAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "ind-as:BuildingsMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "ind-as:SubClassesOfPropertyPlantAndEquipmentAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "ind-as:OwnedAssetsMember":
                if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "ind-as:GrossCarryingAmountMember":
                    hh['buildings_own'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
                elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "ind-as:AccumulatedDepreciationAndImpairmentMember":
                    hh['buildings_own_ad'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "ind-as:ClassesOfPropertyPlantAndEquipmentAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "ind-as:PlantAndEquipmentMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "ind-as:SubClassesOfPropertyPlantAndEquipmentAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "ind-as:OwnedAssetsMember":
                if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "ind-as:GrossCarryingAmountMember":
                    hh['plant_own'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
                elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "ind-as:AccumulatedDepreciationAndImpairmentMember":
                    hh['plant_own_ad'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "ind-as:ClassesOfPropertyPlantAndEquipmentAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "ind-as:FurnitureAndFixturesMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "ind-as:SubClassesOfPropertyPlantAndEquipmentAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "ind-as:OwnedAssetsMember":
                if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "ind-as:GrossCarryingAmountMember":
                    hh['furniture_own'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
                elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "ind-as:AccumulatedDepreciationAndImpairmentMember":
                    hh['furniture_own_ad'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "ind-as:ClassesOfPropertyPlantAndEquipmentAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "ind-as:VehiclesMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "ind-as:SubClassesOfPropertyPlantAndEquipmentAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "ind-as:OwnedAssetsMember":
                if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "ind-as:GrossCarryingAmountMember":
                    hh['vehicle_own'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
                elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "ind-as:AccumulatedDepreciationAndImpairmentMember":
                    hh['vehicle_own_ad'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "ind-as:ClassesOfPropertyPlantAndEquipmentAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "ind-as:OfficeEquipmentMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "ind-as:SubClassesOfPropertyPlantAndEquipmentAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "ind-as:OwnedAssetsMember":
                if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "ind-as:GrossCarryingAmountMember":
                    hh['office_own'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
                elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "ind-as:AccumulatedDepreciationAndImpairmentMember":
                    hh['office_own_ad'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "ind-as:ClassesOfPropertyPlantAndEquipmentAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "ind-as:ComputerEquipmentsMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "ind-as:SubClassesOfPropertyPlantAndEquipmentAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "ind-as:OwnedAssetsMember":
                if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "ind-as:GrossCarryingAmountMember":
                    hh['computer_own'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
                elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "ind-as:AccumulatedDepreciationAndImpairmentMember":
                    hh['computer_own_ad'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "ind-as:ClassesOfPropertyPlantAndEquipmentAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "ind-as:BearerPlantsMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "ind-as:SubClassesOfPropertyPlantAndEquipmentAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "ind-as:OwnedAssetsMember":
                if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "ind-as:GrossCarryingAmountMember":
                    hh['bp_own'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
                elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "ind-as:AccumulatedDepreciationAndImpairmentMember":
                    hh['bp_own_ad'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "ind-as:ClassesOfPropertyPlantAndEquipmentAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "ind-as:LeaseholdImprovementsMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "ind-as:SubClassesOfPropertyPlantAndEquipmentAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "ind-as:OwnedAssetsMember":
                if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "ind-as:GrossCarryingAmountMember":
                    hh['lease_own'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
                elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "ind-as:AccumulatedDepreciationAndImpairmentMember":
                    hh['lease_own_ad'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "ind-as:ClassesOfPropertyPlantAndEquipmentAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "ind-as:OtherPropertyPlantAndEquipmentMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "ind-as:SubClassesOfPropertyPlantAndEquipmentAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "ind-as:OwnedAssetsMember":
                if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "ind-as:GrossCarryingAmountMember":
                    hh['oppe_own'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
                elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "ind-as:AccumulatedDepreciationAndImpairmentMember":
                    hh['oppe_own_ad'] = s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./ind-as:PropertyPlantAndEquipment[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

    return hh

def prop_ingaap(one,two,three):
    hh = {'Name':nm, 'ppe':0, 'ppe_ad':0, 'ppe_own':0, 'ppe_own_ad':0,
    'land':0, 'land_ad':0, 'land_own':0, 'land_own_ad':0,
    'buildings':0, 'buildings_ad':0, 'buildings_own':0, 'buildings_own_ad':0,
    'plant':0, 'plant_ad':0, 'plant_own':0, 'plant_own_ad':0,
    'furniture':0, 'furniture_ad':0, 'furniture_own':0, 'furniture_own_ad':0,
    'vehicle':0, 'vehicle_ad':0, 'vehicle_own':0, 'vehicle_own_ad':0,
    'office':0, 'office_ad':0, 'office_own':0, 'office_own_ad':0,
    'computer':0, 'computer_ad':0, 'computer_own':0, 'computer_own_ad':0,
    'bp':0, 'bp_ad':0, 'bp_own':0, 'bp_own_ad':0,
    'lease':0, 'lease_ad':0, 'lease_own':0, 'lease_own_ad':0,
    'oppe':0, 'oppe_ad':0, 'oppe_own':0, 'oppe_own_ad':0}

    for i in one:
        if i.find('./xbrli:scenario/xbrldi:explicitMember',ns).get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.find('./xbrli:scenario/xbrldi:explicitMember',ns).text == "in-gaap:GrossCarryingAmountMember":
            hh['ppe'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
        elif i.find('./xbrli:scenario/xbrldi:explicitMember',ns).get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.find('./xbrli:scenario/xbrldi:explicitMember',ns).text == "in-gaap:AccumulatedDepreciationAndImpairmentMember":
            hh['ppe_ad'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

    for i in two:
        if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "in-gaap:SubClassesOfTangibleAssetsAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "in-gaap:OwnedAssetsMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "in-gaap:GrossCarryingAmountMember":
                hh['ppe_own'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
            elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "in-gaap:AccumulatedDepreciationAndImpairmentMember":
                hh['ppe_own_ad'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "in-gaap:ClassesOfTangibleAssetsAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "in-gaap:LandMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "in-gaap:GrossCarryingAmountMember":
                hh['land'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
            elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "in-gaap:AccumulatedDepreciationAndImpairmentMember":
                hh['land_ad'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "in-gaap:ClassesOfTangibleAssetsAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "in-gaap:BuildingsMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "in-gaap:GrossCarryingAmountMember":
                hh['buildings'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
            elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "in-gaap:AccumulatedDepreciationAndImpairmentMember":
                hh['buildings_ad'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "in-gaap:ClassesOfTangibleAssetsAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "in-gaap:PlantAndEquipmentMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "in-gaap:GrossCarryingAmountMember":
                hh['plant'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
            elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "in-gaap:AccumulatedDepreciationAndImpairmentMember":
                hh['plant_ad'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "in-gaap:ClassesOfTangibleAssetsAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "in-gaap:FurnitureAndFixturesMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "in-gaap:GrossCarryingAmountMember":
                hh['furniture'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
            elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "in-gaap:AccumulatedDepreciationAndImpairmentMember":
                hh['furniture_ad'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "in-gaap:ClassesOfTangibleAssetsAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "in-gaap:VehiclesMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "in-gaap:GrossCarryingAmountMember":
                hh['vehicle'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
            elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "in-gaap:AccumulatedDepreciationAndImpairmentMember":
                hh['vehicle_ad'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "in-gaap:ClassesOfTangibleAssetsAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "in-gaap:OfficeEquipmentMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "in-gaap:GrossCarryingAmountMember":
                hh['office'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
            elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "in-gaap:AccumulatedDepreciationAndImpairmentMember":
                hh['office_ad'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "in-gaap:ClassesOfTangibleAssetsAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "in-gaap:ComputerEquipmentsMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "in-gaap:GrossCarryingAmountMember":
                hh['computer'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
            elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "in-gaap:AccumulatedDepreciationAndImpairmentMember":
                hh['computer_ad'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "in-gaap:ClassesOfTangibleAssetsAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "in-gaap:LeaseholdImprovementsMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "in-gaap:GrossCarryingAmountMember":
                hh['lease'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
            elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "in-gaap:AccumulatedDepreciationAndImpairmentMember":
                hh['lease_ad'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "in-gaap:ClassesOfTangibleAssetsAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "in-gaap:OtherPropertyPlantAndEquipmentMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "in-gaap:GrossCarryingAmountMember":
                hh['oppe'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
            elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "in-gaap:AccumulatedDepreciationAndImpairmentMember":
                hh['oppe_ad'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

    for i in three:
        if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "in-gaap:ClassesOfTangibleAssetsAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "in-gaap:LandMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "in-gaap:SubClassesOfTangibleAssetsAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "in-gaap:OwnedAssetsMember":
                if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "in-gaap:GrossCarryingAmountMember":
                    hh['land_own'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
                elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "in-gaap:AccumulatedDepreciationAndImpairmentMember":
                    hh['land_own_ad'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "in-gaap:ClassesOfTangibleAssetsAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "in-gaap:BuildingsMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "in-gaap:SubClassesOfTangibleAssetsAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "in-gaap:OwnedAssetsMember":
                if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "in-gaap:GrossCarryingAmountMember":
                    hh['buildings_own'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
                elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "in-gaap:AccumulatedDepreciationAndImpairmentMember":
                    hh['buildings_own_ad'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "in-gaap:ClassesOfTangibleAssetsAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "in-gaap:PlantAndEquipmentMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "in-gaap:SubClassesOfTangibleAssetsAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "in-gaap:OwnedAssetsMember":
                if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "in-gaap:GrossCarryingAmountMember":
                    hh['plant_own'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
                elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "in-gaap:AccumulatedDepreciationAndImpairmentMember":
                    hh['plant_own_ad'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "in-gaap:ClassesOfTangibleAssetsAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "in-gaap:FurnitureAndFixturesMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "in-gaap:SubClassesOfTangibleAssetsAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "in-gaap:OwnedAssetsMember":
                if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "in-gaap:GrossCarryingAmountMember":
                    hh['furniture_own'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
                elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "in-gaap:AccumulatedDepreciationAndImpairmentMember":
                    hh['furniture_own_ad'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "in-gaap:ClassesOfTangibleAssetsAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "in-gaap:VehiclesMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "in-gaap:SubClassesOfTangibleAssetsAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "in-gaap:OwnedAssetsMember":
                if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "in-gaap:GrossCarryingAmountMember":
                    hh['vehicle_own'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
                elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "in-gaap:AccumulatedDepreciationAndImpairmentMember":
                    hh['vehicle_own_ad'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "in-gaap:ClassesOfTangibleAssetsAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "in-gaap:OfficeEquipmentMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "in-gaap:SubClassesOfTangibleAssetsAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "in-gaap:OwnedAssetsMember":
                if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "in-gaap:GrossCarryingAmountMember":
                    hh['office_own'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
                elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "in-gaap:AccumulatedDepreciationAndImpairmentMember":
                    hh['office_own_ad'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "in-gaap:ClassesOfTangibleAssetsAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "in-gaap:ComputerEquipmentsMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "in-gaap:SubClassesOfTangibleAssetsAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "in-gaap:OwnedAssetsMember":
                if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "in-gaap:GrossCarryingAmountMember":
                    hh['computer_own'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
                elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "in-gaap:AccumulatedDepreciationAndImpairmentMember":
                    hh['computer_own_ad'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "in-gaap:ClassesOfTangibleAssetsAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "in-gaap:LeaseholdImprovementsMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "in-gaap:SubClassesOfTangibleAssetsAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "in-gaap:OwnedAssetsMember":
                if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "in-gaap:GrossCarryingAmountMember":
                    hh['lease_own'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
                elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "in-gaap:AccumulatedDepreciationAndImpairmentMember":
                    hh['lease_own_ad'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

        elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].get('dimension') == "in-gaap:ClassesOfTangibleAssetsAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[0].text == "in-gaap:OtherPropertyPlantAndEquipmentMember":
            if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].get('dimension') == "in-gaap:SubClassesOfTangibleAssetsAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[1].text == "in-gaap:OwnedAssetsMember":
                if i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "in-gaap:GrossCarryingAmountMember":
                    hh['oppe_own'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0
                elif i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].get('dimension') == "in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)[2].text == "in-gaap:AccumulatedDepreciationAndImpairmentMember":
                    hh['oppe_own_ad'] = s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else 0

    return hh

details = pd()

for i in filelist:

    try:
        f = et.parse(i)
        s = f.getroot()
        ns = s.nsmap
        ns.pop('in-gaap') if "in-gaap" in ns and "ind-as" in ns else ns
        nm = s.find('.//in-ca:NameOfCompany',ns).text

        #Ascertain how many years_bs data is there in file and which year is highest by taking unique Current Assets
        all_y_bs = s.findall('.//in-gaap:CurrentAssets',ns) if 'in-gaap' in ns else s.findall('.//ind-as:CurrentAssets',ns)
        #from above current assets, took contextRef and found out the id of time. Then from datetime converted string into time - year
        years_bs = [dt.strptime(s.xpath('.//*[@id="%s"]' %i.get('contextRef'))[0].find('.//xbrli:period/xbrli:instant',ns).text,
                        "%Y-%m-%d").year for i in all_y_bs]
        # From numpy array converted list in array and sorted on index
        years2_bs = np(years_bs).argsort()

        # If condition for taking two years_bs data or fail safe if there is only one year data
        if len(years_bs) >= 2:
            oneybs = s.xpath('.//*[@contextRef="%s"]' % all_y_bs[years2_bs[-1]].get('contextRef'))
            twoybs = s.xpath('.//*[@contextRef="%s"]' % all_y_bs[years2_bs[-2]].get('contextRef'))

        else:
            oneybs = s.xpath('.//*[@contextRef="%s"]' % all_y_bs[years2_bs[-1]].get('contextRef'))

        #Ascertain how many years_pl data is there in file and which year is highest by taking unique Revenue from Operations
        all_y_pl = s.findall('.//in-gaap:RevenueFromOperations',ns) if 'in-gaap' in ns else s.findall('.//ind-as:RevenueFromOperations',ns)
        #from above revenue, took contextRef and found out the id of time. Then from datetime converted string into time - year
        years_pl = [dt.strptime(s.xpath('.//*[@id="%s"]' %i.get('contextRef'))[0].find('.//xbrli:period/xbrli:endDate',ns).text,
                        "%Y-%m-%d").year for i in all_y_pl]
        # From numpy array converted list in array and sorted on index
        years2_pl = np(years_pl).argsort()

        # If condition for taking two years_pl data or fail safe if there is only one year data
        if len(years_pl) >= 2:
            oneypl = s.xpath('.//*[@contextRef="%s"]' % all_y_pl[years2_pl[-1]].get('contextRef'))
            twoypl = s.xpath('.//*[@contextRef="%s"]' % all_y_pl[years2_pl[-2]].get('contextRef'))

        else:
            oneypl = s.xpath('.//*[@contextRef="%s"]' % all_y_pl[years2_pl[-1]].get('contextRef'))

        a = s.findall('./xbrli:context',ns)
        one1 , two1 , three1 = [], [], []
        one2 , two2 , three2 = [], [], []
        for i in a:
            if i.find('./xbrli:period/xbrli:instant',ns) is not None and str(years_pl[years2_pl[-1]]) in i.find('./xbrli:period/xbrli:instant',ns).text:
                one1.append(i) if len(i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)) == 1 else None
                two1.append(i) if len(i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)) == 2 else None
                three1.append(i) if len(i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)) == 3 else None
            elif i.find('./xbrli:period/xbrli:instant',ns) is not None and str(years_pl[years2_pl[-2]]) in i.find('./xbrli:period/xbrli:instant',ns).text:
                one2.append(i) if len(i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)) == 1 else None
                two2.append(i) if len(i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)) == 2 else None
                three2.append(i) if len(i.findall('./xbrli:scenario/xbrldi:explicitMember',ns)) == 3 else None

        if 'in-gaap' in ns:
            a = prop_ingaap(one1,two1,three1)
            df1 = pd(a,index=[years_pl[years2_pl[-1]]]).T
            if len(years_bs) >= 2:
                b = prop_ingaap(one2,two2,three2)
                df2 = pd(b,index=[years_pl[years2_pl[-2]]]).T
        else:
            a = prop_indas(one1,two1,three1)
            df1 = pd(a,index=[years_pl[years2_pl[-1]]]).T
            if len(years_bs) >= 2:
                b = prop_indas(one2,two2,three2)
                df2 = pd(b,index=[years_pl[years2_pl[-2]]]).T

        df = df1 if len(years_bs) == 1 else ct([df2,df1],axis=1)
        details = ct([details,df],axis=1)
    except:
        pass

for i in details.index:
    try:
        details.loc[i] = details.loc[i].apply(lambda x:float(x)/1000000)
    except:
        details.loc[i] = details.loc[i]

details.to_csv('Asset_Schedule.csv')
print(details)
