import os
from datetime import datetime as dt
from lxml import etree as et
from numpy import array as np
from pandas import DataFrame as pd
from pandas import concat as ct
from bs4 import BeautifulSoup
import re

auditor = pd()

def auditor_items(aud):
    items = {"Name of Co.":nm, "CIN" : cin}
    for i in s.xpath('./*[@contextRef="%s"]'%aud.get('id')):
        a = "".join(i.tag.split('}')[1:]).strip()
        b = " ".join(re.sub('([A-Z][a-z])', r' \1', re.sub('([A-Z]+)', r' \1',a)).split())
        items[b] = BeautifulSoup(i.text,"html.parser").text
    return items

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

        aud = s.xpath('.//in-ca:AuditorsDomain/ancestor::xbrli:context',namespaces=ns)

        aud_items = [auditor_items(i) for i in aud]

        aud_df = pd(aud_items,index=list(range(len(aud_items))))
        auditor = ct([aud_df,auditor],ignore_index=True)

    except:
        print(file)

auditor = auditor.drop_duplicates()
auditor.to_csv('Auditor.csv',index=False)
print(auditor)