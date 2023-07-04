import os
from datetime import datetime as dt
from lxml import etree as et
from numpy import array as np
from pandas import DataFrame as pd
from pandas import concat as ct
import re

def kmpd_data(x):
    items = {"Name of Co.":nm, "CIN" : cin, "Year":x.find('xbrli:period/xbrli:endDate',ns).text}
    for i in s.xpath('./*[@contextRef="%s"]'%x.get('id')):
        a = "".join(i.tag.split('}')[1:]).strip()
        b = " ".join(re.sub('([A-Z][a-z])', r' \1', re.sub('([A-Z]+)', r' \1',a)).split())
        items[b] = i.text
    return items

kmpd_df_main = pd()

filelist = [i for i in os.listdir() if i.endswith('xml')]

for file in filelist:

    try:
        f = et.parse(file)
        s = f.getroot()
        ns = s.nsmap
        ns.pop('in-gaap') if "in-gaap" in ns and "ind-as" in ns else ns
        ns.pop(None) if None in ns else ns
        nm = s.find('.//in-ca:NameOfCompany',ns).text
        cin = s.find('.//in-ca:CorporateIdentityNumber',ns).text
        
        kmpd = s.xpath('.//xbrldi:typedMember[@dimension="in-ca:KeyManagerialPersonnelsAndDirectorsAxis"]/ancestor::xbrli:context',namespaces=ns)    
        kmpd = [kmpd_data(i) for i in kmpd]
        kmpd_df = pd(kmpd)
        kmpd_df_main = ct([kmpd_df,kmpd_df_main],ignore_index=True)
    except:
        print(file)
        pass

print(kmpd_df_main)
kmpd_df_main.to_csv('KMP & Directors Remuneration.csv', index=False)
