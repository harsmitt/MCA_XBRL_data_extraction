import os
from datetime import datetime as dt
from lxml import etree as et
from numpy import array as np
from pandas import DataFrame as pd
from pandas import concat as ct
filelist = [i for i in os.listdir() if i.endswith('xml')]

share = pd()
shareos_final = pd()

def shareholding(two_pl, two, j=1):
    equity = {"Year": two[0].find('./xbrli:period/xbrli:instant', ns).text, "Company": nm, "Class": "Class%s" %
              j, "Type": [], "Name": [], "CIN": [], "PAN": [], "Country": [], "shares": [], "share%": []}
    if "in-gaap" in ns:
        for i in two_pl:
            if i.find('./xbrli:scenario/xbrldi:explicitMember', ns).get('dimension') == "in-gaap:ClassesOfShareCapitalAxis" and i.find('./xbrli:scenario/xbrldi:explicitMember', ns).text == "in-gaap:EquityShares%sMember" % j:
                for k in range(1, 21):
                    if i.findall('./xbrli:scenario/xbrldi:explicitMember', ns)[1].get('dimension') == "in-gaap:NameOfShareholderAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember', ns)[1].text == "in-gaap:Shareholder%sMember" % k:
                        equity['Type'].append(s.find('in-gaap:TypeOfShare[@contextRef="%s"]' % i.get('id'), ns).text) if s.find(
                            'in-gaap:TypeOfShare[@contextRef="%s"]' % i.get('id'), ns) is not None else equity['Type'].append("")
                        equity['Name'].append(s.find('in-gaap:NameOfShareholder[@contextRef="%s"]' % i.get('id'), ns).text) if s.find(
                            'in-gaap:NameOfShareholder[@contextRef="%s"]' % i.get('id'), ns) is not None else equity['Name'].append("")
                        equity['CIN'].append(s.find('in-ca:CINOfShareholder[@contextRef="%s"]' % i.get('id'), ns).text) if s.find(
                            'in-ca:CINOfShareholder[@contextRef="%s"]' % i.get('id'), ns) is not None else equity['CIN'].append("")
                        equity['PAN'].append(s.find('in-ca:PANOfShareholder[@contextRef="%s"]' % i.get('id'), ns).text) if s.find(
                            'in-ca:PANOfShareholder[@contextRef="%s"]' % i.get('id'), ns) is not None else equity['PAN'].append("")
                        equity['Country'].append(s.find('in-ca:CountryOfIncorporationOrResidenceOfShareholder[@contextRef="%s"]' % i.get('id'), ns).text) if s.find(
                            'in-ca:CountryOfIncorporationOrResidenceOfShareholder[@contextRef="%s"]' % i.get('id'), ns) is not None else equity['Country'].append("")
        for i in two:
            if i.find('./xbrli:scenario/xbrldi:explicitMember', ns).get('dimension') == "in-gaap:ClassesOfShareCapitalAxis" and i.find('./xbrli:scenario/xbrldi:explicitMember', ns).text == "in-gaap:EquityShares%sMember" % j:
                for k in range(1, 21):
                    if i.findall('./xbrli:scenario/xbrldi:explicitMember', ns)[1].get('dimension') == "in-gaap:NameOfShareholderAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember', ns)[1].text == "in-gaap:Shareholder%sMember" % k:
                        equity['shares'].append(s.find('in-gaap:NumberOfSharesHeldInCompany[@contextRef="%s"]' % i.get('id'), ns).text) if s.find(
                            'in-gaap:NumberOfSharesHeldInCompany[@contextRef="%s"]' % i.get('id'), ns) is not None else equity['shares'].append("")
                        equity['share%'].append(s.find('in-gaap:PercentageOfShareholdingInCompany[@contextRef="%s"]' % i.get('id'), ns).text) if s.find(
                            'in-gaap:PercentageOfShareholdingInCompany[@contextRef="%s"]' % i.get('id'), ns) is not None else equity['share%'].append("")
        return equity
    else:
        for i in two1_pl:
            if i.find('./xbrli:scenario/xbrldi:explicitMember', ns).get('dimension') == "ind-as:ClassesOfEquityShareCapitalAxis" and i.find('./xbrli:scenario/xbrldi:explicitMember', ns).text == "ind-as:EquityShares%sMember" % j:
                for k in range(1, 21):
                    if i.findall('./xbrli:scenario/xbrldi:explicitMember', ns)[1].get('dimension') == "ind-as:NameOfShareholderAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember', ns)[1].text == "ind-as:Shareholder%sMember" % k:
                        equity['Type'].append(s.find('ind-as:TypeOfShare[@contextRef="%s"]' % i.get('id'), ns).text) if s.find(
                            'ind-as:TypeOfShare[@contextRef="%s"]' % i.get('id'), ns) is not None else equity['Type'].append("")
                        equity['Name'].append(s.find('ind-as:NameOfShareholder[@contextRef="%s"]' % i.get('id'), ns).text) if s.find(
                            'ind-as:NameOfShareholder[@contextRef="%s"]' % i.get('id'), ns) is not None else equity['Name'].append("")
                        equity['CIN'].append(s.find('in-ca:CINOfShareholder[@contextRef="%s"]' % i.get('id'), ns).text) if s.find(
                            'in-ca:CINOfShareholder[@contextRef="%s"]' % i.get('id'), ns) is not None else equity['CIN'].append("")
                        equity['PAN'].append(s.find('in-ca:PANOfShareholder[@contextRef="%s"]' % i.get('id'), ns).text) if s.find(
                            'in-ca:PANOfShareholder[@contextRef="%s"]' % i.get('id'), ns) is not None else equity['PAN'].append("")
                        equity['Country'].append(s.find('in-ca:CountryOfIncorporationOrResidenceOfShareholder[@contextRef="%s"]' % i.get('id'), ns).text) if s.find(
                            'in-ca:CountryOfIncorporationOrResidenceOfShareholder[@contextRef="%s"]' % i.get('id'), ns) is not None else equity['Country'].append("")
        for i in two1:
            if i.find('./xbrli:scenario/xbrldi:explicitMember', ns).get('dimension') == "ind-as:ClassesOfEquityShareCapitalAxis" and i.find('./xbrli:scenario/xbrldi:explicitMember', ns).text == "ind-as:EquityShares%sMember" % j:
                for k in range(1, 21):
                    if i.findall('./xbrli:scenario/xbrldi:explicitMember', ns)[1].get('dimension') == "ind-as:NameOfShareholderAxis" and i.findall('./xbrli:scenario/xbrldi:explicitMember', ns)[1].text == "ind-as:Shareholder%sMember" % k:
                        equity['shares'].append(s.find('ind-as:NumberOfSharesHeldInCompany[@contextRef="%s"]' % i.get('id'), ns).text) if s.find(
                            'ind-as:NumberOfSharesHeldInCompany[@contextRef="%s"]' % i.get('id'), ns) is not None else equity['shares'].append("")
                        equity['share%'].append(s.find('ind-as:PercentageOfShareholdingInCompany[@contextRef="%s"]' % i.get('id'), ns).text) if s.find(
                            'ind-as:PercentageOfShareholdingInCompany[@contextRef="%s"]' % i.get('id'), ns) is not None else equity['share%'].append("")
        return equity

def share_os(oneybs):
    t = {'Year':s.find('.//xbrli:context[@id="%s"]/xbrli:period/xbrli:instant' %oneybs[0].get('contextRef'),ns).text}
    if "in-gaap" in ns:
        for i in oneybs:
            if i.tag == "{%s}NumberOfSharesOutstanding"%ns['in-gaap']:
                t['Shares O/s'] = i.text
            elif i.tag == "{%s}SharesInCompanyHeldByHoldingCompany"%ns['in-gaap']:
                t['Shares in company held by holding company'] = i.text
            elif i.tag == "{%s}SharesInCompanyHeldByUltimateHoldingCompany"%ns['in-gaap']:
                t['Shares in company held by ultimate holding company'] = i.text
            elif i.tag == "{%s}SharesInCompanyHeldBySubsidiariesOfItsHoldingCompany"%ns['in-gaap']:
                t['Shares in company held by subsidiaries of its holding company'] = i.text
            elif i.tag == "{%s}SharesInCompanyHeldBySubsidiariesOfItsUltimateHoldingCompany"%ns['in-gaap']:
                t['Shares in company held by subsidiaries of its ultimate holding company'] = i.text
            elif i.tag == "{%s}SharesInCompanyHeldByAssociatesOfItsHoldingCompany"%ns['in-gaap']:
                t['Shares in company held by associates of its holding company'] = i.text
            elif i.tag == "{%s}SharesInCompanyHeldByAssociatesOfItsUltimateHoldingCompany"%ns['in-gaap']:
                t['Shares in company held by associates of its ultimate holding company'] = i.text
            elif i.tag == "{%s}SharesInCompanyHeldByHoldingCompanyOrUltimateHoldingCompanyOrByItsSubsidiariesOrAssociates"%ns['in-gaap']:
                t['Total shares in company held by holding company or ultimate holding company or by its subsidiaries or associates'] = i.text

    else:
        for i in oneybs:
            if i.tag == "{%s}NumberOfSharesOutstanding"%ns['ind-as']:
                t['Shares O/s'] = i.text
            elif i.tag == "{%s}SharesInCompanyHeldByHoldingCompany"%ns['ind-as']:
                t['Shares in company held by holding company'] = i.text
            elif i.tag == "{%s}SharesInCompanyHeldByUltimateHoldingCompany"%ns['ind-as']:
                t['Shares in company held by ultimate holding company'] = i.text
            elif i.tag == "{%s}SharesInCompanyHeldBySubsidiariesOfItsHoldingCompany"%ns['ind-as']:
                t['Shares in company held by subsidiaries of its holding company'] = i.text
            elif i.tag == "{%s}SharesInCompanyHeldBySubsidiariesOfItsUltimateHoldingCompany"%ns['ind-as']:
                t['Shares in company held by subsidiaries of its ultimate holding company'] = i.text
            elif i.tag == "{%s}SharesInCompanyHeldByAssociatesOfItsHoldingCompany"%ns['ind-as']:
                t['Shares in company held by associates of its holding company'] = i.text
            elif i.tag == "{%s}SharesInCompanyHeldByAssociatesOfItsUltimateHoldingCompany"%ns['ind-as']:
                t['Shares in company held by associates of its ultimate holding company'] = i.text
            elif i.tag == "{%s}SharesInCompanyHeldByHoldingCompanyOrUltimateHoldingCompanyOrByItsSubsidiariesOrAssociates"%ns['ind-as']:
                t['Total shares in company held by holding company or ultimate holding company or by its subsidiaries or associates'] = i.text
    return t

for file in filelist:
    try:
        f = et.parse(file)
        s = f.getroot()
        ns = s.nsmap
        ns.pop('in-gaap') if "in-gaap" in ns and "ind-as" in ns else ns
        nm = s.find('.//in-ca:NameOfCompany', ns).text
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
            if i.find('./xbrli:period/xbrli:instant', ns) is not None and str(years_pl[years2_pl[-1]]) in i.find('./xbrli:period/xbrli:instant', ns).text:
                one1.append(i) if len(
                    i.findall('./xbrli:scenario/', ns)) == 1 else None
                two1.append(i) if len(
                    i.findall('./xbrli:scenario/', ns)) == 2 else None
                three1.append(i) if len(
                    i.findall('./xbrli:scenario/', ns)) == 3 else None
            elif i.find('./xbrli:period/xbrli:instant', ns) is not None and str(years_pl[years2_pl[-2]]) in i.find('./xbrli:period/xbrli:instant', ns).text:
                one2.append(i) if len(
                    i.findall('./xbrli:scenario/', ns)) == 1 else None
                two2.append(i) if len(
                    i.findall('./xbrli:scenario/', ns)) == 2 else None
                three2.append(i) if len(
                    i.findall('./xbrli:scenario/', ns)) == 3 else None
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
        df = pd()
        if "in-gaap" in ns:
            for i in two1:
                if i.find('./xbrli:scenario/xbrldi:explicitMember', ns).get('dimension') == "in-gaap:ClassesOfShareCapitalAxis" and i.find('./xbrli:scenario/xbrldi:explicitMember', ns).text == "in-gaap:EquityShares1Member":
                    df1 = pd(shareholding(two1_pl, two1, j=1))
                    df2 = pd((shareholding(two2_pl, two2, j=1))) if len(years_bs) >=2 and len(years_pl) >=2 else None
                    df = ct([df1, df2, df]) if len(years_bs) >=2 and len(years_pl) >=2 else ct([df1, df])
                elif i.find('./xbrli:scenario/xbrldi:explicitMember', ns).get('dimension') == "in-gaap:ClassesOfShareCapitalAxis" and i.find('./xbrli:scenario/xbrldi:explicitMember', ns).text == "in-gaap:EquityShares2Member":
                    df3 = pd(shareholding(two1_pl, two1, j=2))
                    df4 = pd((shareholding(two2_pl, two2, j=2))) if len(years_bs) >=2 and len(years_pl) >=2 else None
                    df = ct([df3, df4, df]) if len(years_bs) >=2 and len(years_pl) >=2 else ct([df3, df])
                elif i.find('./xbrli:scenario/xbrldi:explicitMember', ns).get('dimension') == "in-gaap:ClassesOfShareCapitalAxis" and i.find('./xbrli:scenario/xbrldi:explicitMember', ns).text == "in-gaap:EquityShares3Member":
                    df5 = pd(shareholding(two1_pl, two1, j=3))
                    df6 = pd((shareholding(two2_pl, two2, j=3))) if len(years_bs) >=2 and len(years_pl) >=2 else None
                    df = ct([df5, df6, df]) if len(years_bs) >=2 and len(years_pl) >=2 else ct([df5, df])
                elif i.find('./xbrli:scenario/xbrldi:explicitMember', ns).get('dimension') == "in-gaap:ClassesOfShareCapitalAxis" and i.find('./xbrli:scenario/xbrldi:explicitMember', ns).text == "in-gaap:EquityShares4Member":
                    df7 = pd(shareholding(two1_pl, two1, j=4))
                    df8 = pd((shareholding(two2_pl, two2, j=4))) if len(years_bs) >=2 and len(years_pl) >=2 else None
                    df = ct([df7, df8, df]) if len(years_bs) >=2 and len(years_pl) >=2 else ct([df7, df])
                elif i.find('./xbrli:scenario/xbrldi:explicitMember', ns).get('dimension') == "in-gaap:ClassesOfShareCapitalAxis" and i.find('./xbrli:scenario/xbrldi:explicitMember', ns).text == "in-gaap:EquityShares5Member":
                    df9 = pd(shareholding(two1_pl, two1, j=5))
                    df10 = pd((shareholding(two2_pl, two2, j=5))) if len(years_bs) >=2 and len(years_pl) >=2 else None
                    df = ct([df9, df10, df]) if len(years_bs) >=2 and len(years_pl) >=2 else ct([df9, df])
            share = ct([df, share])
        else:
            for i in two1:
                if i.find('./xbrli:scenario/xbrldi:explicitMember', ns).get('dimension') == "ind-as:ClassesOfEquityShareCapitalAxis" and i.find('./xbrli:scenario/xbrldi:explicitMember', ns).text == "ind-as:EquityShares1Member":
                    df1 = pd(shareholding(two1_pl, two1, j=1))
                    df2 = pd((shareholding(two2_pl, two2, j=1))) if len(years_bs) >=2 and len(years_pl) >=2 else None
                    df = ct([df1, df2, df]) if len(years_bs) >=2 and len(years_pl) >=2 else ct([df1, df])
                elif i.find('./xbrli:scenario/xbrldi:explicitMember', ns).get('dimension') == "ind-as:ClassesOfEquityShareCapitalAxis" and i.find('./xbrli:scenario/xbrldi:explicitMember', ns).text == "ind-as:EquityShares2Member":
                    df3 = pd(shareholding(two1_pl, two1, j=2))
                    df4 = pd((shareholding(two2_pl, two2, j=2))) if len(years_bs) >=2 and len(years_pl) >=2 else None
                    df = ct([df3, df4, df]) if len(years_bs) >=2 and len(years_pl) >=2 else ct([df3, df])
                elif i.find('./xbrli:scenario/xbrldi:explicitMember', ns).get('dimension') == "ind-as:ClassesOfEquityShareCapitalAxis" and i.find('./xbrli:scenario/xbrldi:explicitMember', ns).text == "ind-as:EquityShares3Member":
                    df5 = pd(shareholding(two1_pl, two1, j=3))
                    df6 = pd((shareholding(two2_pl, two2, j=3))) if len(years_bs) >=2 and len(years_pl) >=2 else None
                    df = ct([df5, df6, df]) if len(years_bs) >=2 and len(years_pl) >=2 else ct([df5, df])
                elif i.find('./xbrli:scenario/xbrldi:explicitMember', ns).get('dimension') == "ind-as:ClassesOfEquityShareCapitalAxis" and i.find('./xbrli:scenario/xbrldi:explicitMember', ns).text == "ind-as:EquityShares4Member":
                    df7 = pd(shareholding(two1_pl, two1, j=4))
                    df8 = pd((shareholding(two2_pl, two2, j=4))) if len(years_bs) >=2 and len(years_pl) >=2 else None
                    df = ct([df7, df8, df]) if len(years_bs) >=2 and len(years_pl) >=2 else ct([df7, df])
                elif i.find('./xbrli:scenario/xbrldi:explicitMember', ns).get('dimension') == "ind-as:ClassesOfEquityShareCapitalAxis" and i.find('./xbrli:scenario/xbrldi:explicitMember', ns).text == "ind-as:EquityShares5Member":
                    df9 = pd(shareholding(two1_pl, two1, j=5))
                    df10 = pd((shareholding(two2_pl, two2, j=5))) if len(years_bs) >=2 and len(years_pl) >=2 else None
                    df = ct([df9, df10, df]) if len(years_bs) >=2 and len(years_pl) >=2 else ct([df9, df])
            share = ct([df, share])
        shareos1 = share_os(oneybs)
        shareos1 = pd(shareos1,index=[nm]).T
        if len(years_bs) >=2 and len(years_pl) >=2:
            shareos2 = share_os(twoybs)
            shareos2 = pd(shareos2,index=[nm]).T
        final_share = ct([shareos2,shareos1],axis=1,sort=False) if len(years_bs) >=2 and len(years_pl) >=2 else shareos1
        shareos_final = ct([shareos_final,final_share],axis=1,sort=False)

    except:
        print(file)
        pass
print(share.drop_duplicates())
print(shareos_final)
shareos_final.to_csv('Share_outstanding.csv')
share.drop_duplicates().to_csv('Shareholding.csv', index=False)
