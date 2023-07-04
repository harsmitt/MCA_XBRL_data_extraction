from pandas import DataFrame as pd
from pandas import concat as ct
import os
from lxml.html import fromstring
from lxml import etree as et
from numpy import array as np
from datetime import datetime as dt
import re


def pps_items(pps):
    items = {"Name of Co.":nm, "CIN" : cin, "Year": pps.find('xbrli:period/xbrli:endDate',ns).text}
    for i in s.xpath('./*[@contextRef="%s"]'%pps.get('id')):
        a = "".join(i.tag.split('}')[1:]).strip()
        b = " ".join(re.sub('([A-Z][a-z])', r' \1', re.sub('([A-Z]+)', r' \1',a)).split())
        items[b] = i.text
    return items

def primary_data(x,y):
    t,u,v = [],[],[]
    for i in x:
        t.append(i.xpath('.//xbrldi:explicitMember[@dimension="in-gaap:EnterprisesPrimaryReportableSegmentsAxis"]/ancestor::xbrli:context',namespaces=ns))
    for i in y:
        u.append(i.xpath('.//xbrldi:explicitMember[@dimension="in-gaap:EnterprisesPrimaryReportableSegmentsAxis"]/ancestor::xbrli:context',namespaces=ns))

    t, u = [i[0] for i in t if len(i)>=1], [i[0] for i in u if len(i)>=1]
    for i in t:
        for j in u:
            if [(k.get('dimension'), k.text) for k in i.findall('.//xbrldi:explicitMember',ns)] == [(k.get('dimension'), k.text) for k in j.findall('.//xbrldi:explicitMember',ns)]:
                v.append((i,j))
    return v

def secondary_data(x,y):
    t,u,v = [],[],[]
    for i in x:
        t.append(i.xpath('.//xbrldi:explicitMember[@dimension="in-gaap:EnterprisesSecondaryReportableSegmentsAxis"]/ancestor::xbrli:context',namespaces=ns))
    for i in y:
        u.append(i.xpath('.//xbrldi:explicitMember[@dimension="in-gaap:EnterprisesSecondaryReportableSegmentsAxis"]/ancestor::xbrli:context',namespaces=ns))

    t, u = [i[0] for i in t if len(i)>=1], [i[0] for i in u if len(i)>=1]
    for i in t:
        for j in u:
            if [(k.get('dimension'), k.text) for k in i.findall('.//xbrldi:explicitMember',ns)] == [(k.get('dimension'), k.text) for k in j.findall('.//xbrldi:explicitMember',ns)]:
                v.append((i,j))
    return v

def entity_data(x,y):
    t,u,v = [],[],[]
    for i in x:
        t.append(i.xpath('.//xbrldi:explicitMember[@dimension="ind-as:EntitySReportableSegmentsAxis"]/ancestor::xbrli:context',namespaces=ns))
    for i in y:
        u.append(i.xpath('.//xbrldi:explicitMember[@dimension="ind-as:EntitySReportableSegmentsAxis"]/ancestor::xbrli:context',namespaces=ns))

    t, u = [i[0] for i in t if len(i)>=1], [i[0] for i in u if len(i)>=1]
    for i in t:
        for j in u:
            if [(k.get('dimension'), k.text) for k in i.findall('.//xbrldi:explicitMember',ns)] == [(k.get('dimension'), k.text) for k in j.findall('.//xbrldi:explicitMember',ns)]:
                v.append((i,j))
    return v

def seg_items(x):
    items = {"Name of Co.":nm, "CIN" : cin, "Year":x[1].find('xbrli:period/xbrli:endDate',ns).text}
    for i in s.xpath('./*[@contextRef="%s"]'%x[1].get('id')):
        a = "".join(i.tag.split('}')[1:]).strip()
        b = " ".join(re.sub('([A-Z][a-z])', r' \1', re.sub('([A-Z]+)', r' \1',a)).split())
        items[b] = i.text
    for j in s.xpath('./*[@contextRef="%s"]'%x[0].get('id')):
        a = "".join(j.tag.split('}')[1:]).strip()
        b = " ".join(re.sub('([A-Z][a-z])', r' \1', re.sub('([A-Z]+)', r' \1',a)).split())
        items[b] = j.text
    return items

filelist = [i for i in os.listdir() if i.endswith('xml')]

main_pps_df = pd()
main_pba_df = pd()
pri_df_main = pd()
sec_df_main = pd()
ent_df_main = pd()

for file in filelist:
    try:
        f = et.parse(file)
        s = f.getroot()
        ns = s.nsmap
        ns.pop('in-gaap') if "in-gaap" in ns and "ind-as" in ns else ns
        ns.pop(None) if None in ns else ns
        nm = s.find('.//in-ca:NameOfCompany',ns).text
        cin = s.find('.//in-ca:CorporateIdentityNumber',ns).text

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

        a = s.findall('xbrli:context', ns)
        one1, two1, three1 = [], [], []
        one2, two2, three2 = [], [], []
        for i in a:
            if i.find('./xbrli:period/xbrli:instant', ns) is not None and str(years_bs[years2_bs[-1]]) in i.find('./xbrli:period/xbrli:instant', ns).text:
                one1.append(i) if len(i.findall('./xbrli:scenario/', ns)) == 1 else None
                two1.append(i) if len(i.findall('./xbrli:scenario/', ns)) == 2 else None
                three1.append(i) if len(i.findall('./xbrli:scenario/', ns)) == 3 else None
            elif i.find('./xbrli:period/xbrli:instant', ns) is not None and str(years_bs[years2_bs[-2]]) in i.find('./xbrli:period/xbrli:instant', ns).text:
                one2.append(i) if len(i.findall('./xbrli:scenario/', ns)) == 1 else None
                two2.append(i) if len(i.findall('./xbrli:scenario/', ns)) == 2 else None
                three2.append(i) if len(i.findall('./xbrli:scenario/', ns)) == 3 else None


        one1_pl, two1_pl, three1_pl = [], [], []
        one2_pl, two2_pl, three2_pl = [], [], []
        for i in a:
            if i.find('./xbrli:period/xbrli:endDate', ns) is not None and str(years_pl[years2_pl[-1]]) in i.find('./xbrli:period/xbrli:endDate', ns).text:
                one1_pl.append(i) if len(
                    i.findall('./xbrli:scenario/', ns)) == 1 else None
                two1_pl.append(i) if len(
                    i.findall('./xbrli:scenario/', ns)) == 2 else None
                three1_pl.append(i) if len(
                    i.findall('./xbrli:scenario/', ns)) == 3 else None
            elif i.find('./xbrli:period/xbrli:endDate', ns) is not None and str(years_pl[years2_pl[-2]]) in i.find('./xbrli:period/xbrli:endDate', ns).text:
                one2_pl.append(i) if len(
                    i.findall('./xbrli:scenario/', ns)) == 1 else None
                two2_pl.append(i) if len(
                    i.findall('./xbrli:scenario/', ns)) == 2 else None
                three2_pl.append(i) if len(
                    i.findall('./xbrli:scenario/', ns)) == 3 else None

        pps = s.xpath('.//xbrldi:typedMember[@dimension="in-ca:TypesOfPrincipalProductOrServicesAxis"]/ancestor::xbrli:context',namespaces=ns)
        p_items = [pps_items(i) for i in pps]
        p_df = pd(p_items,index=list(range(len(p_items))))
        main_pps_df = ct([p_df,main_pps_df],ignore_index=True)

        pba = s.xpath('.//xbrldi:explicitMember[@dimension="in-ca:PrincipalBusinessActivitiesOfCompanyAxis"]/ancestor::xbrli:context',namespaces=ns)
        pba_items = [pps_items(i) for i in pba]
        pba_df = pd(pba_items,index=list(range(len(pba_items))))
        main_pba_df = ct([pba_df,main_pba_df],ignore_index=True)

        if s.find('.//xbrldi:explicitMember[@dimension="in-gaap:EnterprisesPrimaryReportableSegmentsAxis"]',ns) is not None:
            pri_segments1 = primary_data(one1, one1_pl)
            pri_df1 = pd([seg_items(i) for i in pri_segments1])
            pri_df_main = ct([pri_df1,pri_df_main],ignore_index=True)
            if len(years_pl) >= 2:
                pri_segments2 = primary_data(one2, one2_pl)
                pri_df2 = pd([seg_items(i) for i in pri_segments2])
                pri_df_main = ct([pri_df2,pri_df_main],ignore_index=True)

        if s.find('.//xbrldi:explicitMember[@dimension="in-gaap:EnterprisesSecondaryReportableSegmentsAxis"]',ns) is not None:
            sec_segments1 = secondary_data(one1, one1_pl)
            sec_df1 = pd([seg_items(i) for i in sec_segments1])
            sec_df_main = ct([sec_df1,sec_df_main],ignore_index=True)
            if len(years_pl) >= 2:
                sec_segments2 = secondary_data(one2, one2_pl)
                sec_df2 = pd([seg_items(i) for i in sec_segments2])
                sec_df_main = ct([sec_df2,sec_df_main],ignore_index=True)

        if s.find('.//xbrldi:explicitMember[@dimension="ind-as:EntitySReportableSegmentsAxis"]',ns) is not None:
            ent_segments1 = entity_data(one1, one1_pl)
            ent_df1 = pd([seg_items(i) for i in ent_segments1])
            ent_df_main = ct([ent_df1,ent_df_main],ignore_index=True)
            if len(years_pl) >= 2:
                ent_segments2 = entity_data(one2, one2_pl)
                ent_df2 = pd([seg_items(i) for i in ent_segments2])
                ent_df_main = ct([ent_df2,ent_df_main],ignore_index=True)

    except Exception as e:
        print(e + " -in- " + file)
        pass

main_pps_df = main_pps_df.drop_duplicates()
print(main_pps_df)
main_pps_df.to_csv('Principal Product or Service.csv')

main_pba_df = main_pba_df.drop_duplicates()
print(main_pba_df)
main_pba_df.to_csv("Principal Business Activities (Over 10% of Revenue).csv")

print(pri_df_main)
print(sec_df_main)
print(ent_df_main)
pri_df_main.to_csv("Primary Segment.csv")
sec_df_main.to_csv("Secondary Segment.csv")
ent_df_main.to_csv("Entity Segment.csv")