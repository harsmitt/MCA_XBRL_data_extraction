import os
from datetime import datetime as dt
from lxml import etree as et
from numpy import array as np
from pandas import DataFrame as pd
from pandas import concat as ct
import re

def rp_data_indas(x,y):
    t,u,v = [],[],[]
    for i in x:
        t.append(i.xpath('.//xbrldi:explicitMember[@dimension="ind-as:CategoriesOfRelatedPartiesAxis"]/ancestor::xbrli:context',namespaces=ns))
    for i in y:
        u.append(i.xpath('.//xbrldi:explicitMember[@dimension="ind-as:CategoriesOfRelatedPartiesAxis"]/ancestor::xbrli:context',namespaces=ns))

    t, u = [i[0] for i in t if len(i)>=1], [i[0] for i in u if len(i)>=1]
    for i in t:
        for j in u:
            if i.find('.//xbrli:scenario/xbrldi:typedMember/ind-as:RelatedPartyDomain',ns).text == j.find('.//xbrli:scenario/xbrldi:typedMember/ind-as:RelatedPartyDomain',ns).text:
                v.append((i,j))

    for i in v:
        l = i[0].find('.//xbrli:scenario/xbrldi:typedMember/ind-as:RelatedPartyDomain',ns).text
        m = [i.find('.//xbrli:scenario/xbrldi:typedMember/ind-as:RelatedPartyDomain',ns).text for i in t]
        if l in m:
            t.pop(m.index(l))
    return t,v

def rp_data_ingaap(x,y):
    t,u,v = [],[],[]
    for i in x:
        t.append(i.xpath('.//xbrldi:typedMember[@dimension="in-gaap:CategoriesOfRelatedPartiesAxis"]/ancestor::xbrli:context',namespaces=ns))
    for i in y:
        u.append(i.xpath('.//xbrldi:typedMember[@dimension="in-gaap:CategoriesOfRelatedPartiesAxis"]/ancestor::xbrli:context',namespaces=ns))

    t, u = [i[0] for i in t if len(i)>=1], [i[0] for i in u if len(i)>=1]
    for i in t:
        for j in u:
            if i.find('.//xbrli:scenario/xbrldi:typedMember/in-gaap:RelatedPartiesDomain',ns).text == j.find('.//xbrli:scenario/xbrldi:typedMember/in-gaap:RelatedPartiesDomain',ns).text:
                v.append((i,j))

    for i in v:
        l = i[0].find('.//xbrli:scenario/xbrldi:typedMember/in-gaap:RelatedPartiesDomain',ns).text
        m = [i.find('.//xbrli:scenario/xbrldi:typedMember/in-gaap:RelatedPartiesDomain',ns).text for i in t]
        if l in m:
            t.pop(m.index(l))
    return t,v

def rp_items_pl(x):
    items = {"Name of Co.":nm, "CIN" : cin, "Year":x.find('xbrli:period/xbrli:endDate',ns).text}
    for i in s.xpath('./*[@contextRef="%s"]'%x.get('id')):
        a = "".join(i.tag.split('}')[1:]).strip()
        b = " ".join(re.sub('([A-Z][a-z])', r' \1', re.sub('([A-Z]+)', r' \1',a)).split())
        items[b] = i.text
    return items

def rp_items_both(x):
    items = {"Name of Co.":nm, "CIN" : cin, "Year":x[0].find('xbrli:period/xbrli:endDate',ns).text}
    for i in s.xpath('./*[@contextRef="%s"]'%x[0].get('id')):
        a = "".join(i.tag.split('}')[1:]).strip()
        b = " ".join(re.sub('([A-Z][a-z])', r' \1', re.sub('([A-Z]+)', r' \1',a)).split())
        items[b] = i.text
    for j in s.xpath('./*[@contextRef="%s"]'%x[1].get('id')):
        a = "".join(j.tag.split('}')[1:]).strip()
        b = " ".join(re.sub('([A-Z][a-z])', r' \1', re.sub('([A-Z]+)', r' \1',a)).split())
        items[b] = j.text
    return items

rp_df_main = pd()

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


        # Ascertain how many years_bs data is there in file and which year is highest by taking unique Current Assets
        all_y_bs = s.findall('.//in-gaap:CurrentAssets',
                            ns) if 'in-gaap' in ns else s.findall('.//ind-as:CurrentAssets', ns)
        # from above current assets, took contextRef and found out the id of time. Then from datetime converted string into time - year
        years_bs = [dt.strptime(s.xpath('.//*[@id="%s"]' % i.get('contextRef'))[0].find('.//xbrli:period/xbrli:instant', ns).text,
                                "%Y-%m-%d").year for i in all_y_bs]
        # From numpy array converted list in array and sorted on index
        years2_bs = np(years_bs).argsort()
        # If condition for taking two years_bs data or fail safe if there is only one year data
        if len(years_bs) >= 2:
            oneybs = s.xpath('.//*[@contextRef="%s"]' %
                            all_y_bs[years2_bs[-1]].get('contextRef'))
            twoybs = s.xpath('.//*[@contextRef="%s"]' %
                            all_y_bs[years2_bs[-2]].get('contextRef'))
        else:
            oneybs = s.xpath('.//*[@contextRef="%s"]' %
                            all_y_bs[years2_bs[-1]].get('contextRef'))


        # Ascertain how many years_pl data is there in file and which year is highest by taking unique Revenue from Operations
        all_y_pl = s.findall('.//in-gaap:RevenueFromOperations',
                            ns) if 'in-gaap' in ns else s.findall('.//ind-as:RevenueFromOperations', ns)
        # from above revenue, took contextRef and found out the id of time. Then from datetime converted string into time - year
        years_pl = [dt.strptime(s.xpath('.//*[@id="%s"]' % i.get('contextRef'))[0].find('.//xbrli:period/xbrli:endDate', ns).text,
                                "%Y-%m-%d").year for i in all_y_pl]
        # From numpy array converted list in array and sorted on index
        years2_pl = np(years_pl).argsort()
        # If condition for taking two years_pl data or fail safe if there is only one year data
        if len(years_pl) >= 2:
            oneypl = s.xpath('.//*[@contextRef="%s"]' %
                            all_y_pl[years2_pl[-1]].get('contextRef'))
            twoypl = s.xpath('.//*[@contextRef="%s"]' %
                            all_y_pl[years2_pl[-2]].get('contextRef'))
        else:
            oneypl = s.xpath('.//*[@contextRef="%s"]' %
                            all_y_pl[years2_pl[-1]].get('contextRef'))

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

        if 'ind-as' in ns:
            rp1,rp2 = rp_data_indas(two1_pl, two1)
            rp_df1 = pd([rp_items_pl(i) for i in rp1])
            rp_df2 = pd([rp_items_both(i) for i in rp2])
            rp_df_main = ct([rp_df1,rp_df2,rp_df_main],ignore_index=True)
            if len(years_pl) >= 2:
                rp1,rp2 = rp_data_indas(two2_pl, two2)
                rp_df1 = pd([rp_items_pl(i) for i in rp1])
                rp_df2 = pd([rp_items_both(i) for i in rp2])
                rp_df_main = ct([rp_df1,rp_df2,rp_df_main],ignore_index=True)

        else:
            rp1,rp2 = rp_data_ingaap(one1_pl, one1)
            rp_df1 = pd([rp_items_pl(i) for i in rp1])
            rp_df2 = pd([rp_items_both(i) for i in rp2])
            rp_df_main = ct([rp_df1,rp_df2,rp_df_main],ignore_index=True)
            if len(years_pl) >= 2:
                rp1,rp2 = rp_data_ingaap(one2_pl, one2)
                rp_df1 = pd([rp_items_pl(i) for i in rp1])
                rp_df2 = pd([rp_items_both(i) for i in rp2])
                rp_df_main = ct([rp_df1,rp_df2,rp_df_main],ignore_index=True)

    except:
        print(file)
        pass

print(rp_df_main)
rp_df_main.to_csv('Related Party Transactions.csv')
