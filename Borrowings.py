import os
from datetime import datetime as dt
from lxml import etree as et
from numpy import array as np
from pandas import DataFrame as pd
from pandas import concat as ct
import re

def borrowing_both_items(x,y):
    items = {"Year": x.find('.//xbrli:instant',ns).text,
      "Company": nm,
      "CIN" : cin,
      "Borrowings": "",
      "Nature of security": "",
      "Details of personal security given by promoters, other shareholders or other third parties, though such security does not result in classification of borrowings as secured": "",
      "Aggregate amount of loans guaranteed by directors": "",
      "Aggregate amount of loans guaranteed by others": "",
      "Particulars of any redeemed bonds/debentures which company has power to reissue": "",
      "Terms of repayment of term loans and other loans": "",
      "Beginning date of continuing default for borrowings": "",
      "Outstanding amount of continuing default principal": "",
      "Outstanding amount of continuing default interest": ""}
    try:

        if "in-gaap" in ns:
            items['Borrowings'] = s.find('in-gaap:Borrowings[@contextRef="%s"]'%x.get('id'),ns)
            items['Aggregate amount of loans guaranteed by directors'] = s.find('in-gaap:AggregateAmountOfLoansGuaranteedByDirectors[@contextRef="%s"]'%x.get('id'),ns)
            items['Aggregate amount of loans guaranteed by others'] = s.find('in-gaap:AggregateAmountOfLoansGuaranteedByOthers[@contextRef="%s"]'%x.get('id'),ns)
            items['Outstanding amount of continuing default principal'] = s.find('in-gaap:OutstandingAmountOfContinuingDefaultPrincipal[@contextRef="%s"]'%x.get('id'),ns)
            items['Outstanding amount of continuing default interest'] = s.find('in-gaap:OutstandingAmountOfContinuingDefaultInterest[@contextRef="%s"]'%x.get('id'),ns)

            items['Nature of security'] = s.find('in-gaap:NatureOfSecurity[@contextRef="%s"]'%y.get('id'),ns)
            items['Details of personal security given by promoters, other shareholders or other third parties, though such security does not result in classification of borrowings as secured'] = s.find('in-gaap:DetailsOfPersonalSecurityGivenByPromotersOtherShareholdersOrOtherThirdPartiesThoughSuchSecurityDoesNotResultInClassificationOfBorrowingsAsSecured[@contextRef="%s"]'%y.get('id'),ns)
            items['Particulars of any redeemed bonds/debentures which company has power to reissue'] = s.find('in-gaap:ParticularsOfAnyRedeemedBondsDebenturesWhichCompanyHasPowerToReissue[@contextRef="%s"]'%y.get('id'),ns)
            items['Terms of repayment of term loans and other loans'] = s.find('in-gaap:TermsOfRepaymentOfTermLoansAndOtherLoans[@contextRef="%s"]'%y.get('id'),ns)
            items['Beginning date of continuing default for borrowings'] = s.find('in-gaap:BeginningDateOfContinuingDefaultForBorrowings[@contextRef="%s"]'%y.get('id'),ns)

        else:
            items['Borrowings'] = s.find('ind-as:Borrowings[@contextRef="%s"]'%x.get('id'),ns)
            items['Aggregate amount of loans guaranteed by directors'] = s.find('ind-as:AggregateAmountOfLoansGuaranteedByDirectors[@contextRef="%s"]'%x.get('id'),ns)
            items['Aggregate amount of loans guaranteed by others'] = s.find('ind-as:AggregateAmountOfLoansGuaranteedByOthers[@contextRef="%s"]'%x.get('id'),ns)
            items['Outstanding amount of continuing default principal'] = s.find('ind-as:OutstandingAmountOfContinuingDefaultPrincipal[@contextRef="%s"]'%x.get('id'),ns)
            items['Outstanding amount of continuing default interest'] = s.find('ind-as:OutstandingAmountOfContinuingDefaultInterest[@contextRef="%s"]'%x.get('id'),ns)

            items['Nature of security'] = s.find('ind-as:NatureOfSecurity[@contextRef="%s"]'%y.get('id'),ns)
            items['Details of personal security given by promoters, other shareholders or other third parties, though such security does not result in classification of borrowings as secured'] = s.find('ind-as:DetailsOfPersonalSecurityGivenByPromotersOtherShareholdersOrOtherThirdPartiesThoughSuchSecurityDoesNotResultInClassificationOfBorrowingsAsSecured[@contextRef="%s"]'%y.get('id'),ns)
            items['Particulars of any redeemed bonds/debentures which company has power to reissue'] = s.find('ind-as:ParticularsOfAnyRedeemedBondsDebenturesWhichCompanyHasPowerToReissue[@contextRef="%s"]'%y.get('id'),ns)
            items['Terms of repayment of term loans and other loans'] = s.find('ind-as:TermsOfRepaymentOfTermLoansAndOtherLoans[@contextRef="%s"]'%y.get('id'),ns)
            items['Beginning date of continuing default for borrowings'] = s.find('ind-as:BeginningDateOfContinuingDefaultForBorrowings[@contextRef="%s"]'%y.get('id'),ns)

        for i ,j in items.items():
            try:
                items[i] = j.text
            except:
                items[i] = j
        return items
    except:
        pass

def borrowing_bs_items(x):
    items = {"Year": x.find('.//xbrli:instant',ns).text,
      "Company": nm,
      "CIN" : cin,
      "Borrowings": "",
      "Aggregate amount of loans guaranteed by directors": "",
      "Aggregate amount of loans guaranteed by others": "",
      "Outstanding amount of continuing default principal": "",
      "Outstanding amount of continuing default interest": ""}

    try:
        if "in-gaap" in ns:
            items['Borrowings'] = s.find('in-gaap:Borrowings[@contextRef="%s"]'%x.get('id'),ns)
            items['Aggregate amount of loans guaranteed by directors'] = s.find('in-gaap:AggregateAmountOfLoansGuaranteedByDirectors[@contextRef="%s"]'%x.get('id'),ns)
            items['Aggregate amount of loans guaranteed by others'] = s.find('in-gaap:AggregateAmountOfLoansGuaranteedByOthers[@contextRef="%s"]'%x.get('id'),ns)
            items['Outstanding amount of continuing default principal'] = s.find('in-gaap:OutstandingAmountOfContinuingDefaultPrincipal[@contextRef="%s"]'%x.get('id'),ns)
            items['Outstanding amount of continuing default interest'] = s.find('in-gaap:OutstandingAmountOfContinuingDefaultInterest[@contextRef="%s"]'%x.get('id'),ns)

        else:
            items['Borrowings'] = s.find('ind-as:Borrowings[@contextRef="%s"]'%x.get('id'),ns)
            items['Aggregate amount of loans guaranteed by directors'] = s.find('ind-as:AggregateAmountOfLoansGuaranteedByDirectors[@contextRef="%s"]'%x.get('id'),ns)
            items['Aggregate amount of loans guaranteed by others'] = s.find('ind-as:AggregateAmountOfLoansGuaranteedByOthers[@contextRef="%s"]'%x.get('id'),ns)
            items['Outstanding amount of continuing default principal'] = s.find('ind-as:OutstandingAmountOfContinuingDefaultPrincipal[@contextRef="%s"]'%x.get('id'),ns)
            items['Outstanding amount of continuing default interest'] = s.find('ind-as:OutstandingAmountOfContinuingDefaultInterest[@contextRef="%s"]'%x.get('id'),ns)

        for i ,j in items.items():
            try:
                items[i] = j.text
            except:
                items[i] = j
        return items
    except:
        pass

def data(x,y):
    t,u,v = [],[],[]
    for i in x:
        if 'in-gaap' in ns:
            t.append(i.xpath('.//xbrldi:explicitMember[@dimension="in-gaap:SubclassificationOfBorrowingsAxis"]/ancestor::xbrli:context',namespaces=ns))
        else:
            t.append(i.xpath('.//xbrldi:explicitMember[@dimension="ind-as:SubclassificationOfBorrowingsAxis"]/ancestor::xbrli:context',namespaces=ns))

    for i in y:
        if 'in-gaap' in ns:
            u.append(i.xpath('.//xbrldi:explicitMember[@dimension="in-gaap:SubclassificationOfBorrowingsAxis"]/ancestor::xbrli:context',namespaces=ns))
        else:
            u.append(i.xpath('.//xbrldi:explicitMember[@dimension="ind-as:SubclassificationOfBorrowingsAxis"]/ancestor::xbrli:context',namespaces=ns))

    t, u = [i[0] for i in t if len(i)>=1], [i[0] for i in u if len(i)>=1]
    for i in t:
        for j in u:
            if [(k.get('dimension'), k.text) for k in i.findall('.//xbrldi:explicitMember',ns)] == [(k.get('dimension'), k.text) for k in j.findall('.//xbrldi:explicitMember',ns)]:
                v.append((i,j))
                t.remove(i)
    return t,v

def frame(xx):
    df = pd()
    for i in xx:
        if len(xx) >=1:
            d = {}
            if type(xx[0]) == tuple:
                items = borrowing_both_items(i[0],i[1])
                a = [(l.get('dimension'),l.text) for l in i[0].findall('.//xbrldi:explicitMember',ns)]
            else:
                items = borrowing_bs_items(i)
                a = [(l.get('dimension'),l.text) for l in i.findall('.//xbrldi:explicitMember',ns)]

            if len(a) == 2 :
                b = " ".join(re.sub('([A-Z][a-z])', r' \1', re.sub('([A-Z]+)', r' \1', a[0][0])).split())
                c = " ".join(re.sub('([A-Z][a-z])', r' \1', re.sub('([A-Z]+)', r' \1', a[0][1])).split())
                d["Time Period (Current or Non-Current)"] = "".join(c.split(':')[1:]).strip()
                b = " ".join(re.sub('([A-Z][a-z])', r' \1', re.sub('([A-Z]+)', r' \1', a[1][0])).split())
                c = " ".join(re.sub('([A-Z][a-z])', r' \1', re.sub('([A-Z]+)', r' \1', a[1][1])).split())
                d["Secured or Unsecured"] = "".join(c.split(':')[1:]).strip()
            elif len(a) == 3:
                b = " ".join(re.sub('([A-Z][a-z])', r' \1', re.sub('([A-Z]+)', r' \1', a[0][0])).split())
                c = " ".join(re.sub('([A-Z][a-z])', r' \1', re.sub('([A-Z]+)', r' \1', a[0][1])).split())
                d["Time Period (Current or Non-Current)"] = "".join(c.split(':')[1:]).strip()
                b = " ".join(re.sub('([A-Z][a-z])', r' \1', re.sub('([A-Z]+)', r' \1', a[2][0])).split())
                c = " ".join(re.sub('([A-Z][a-z])', r' \1', re.sub('([A-Z]+)', r' \1', a[2][1])).split())
                if "Subclassification Of Borrowings Axis" in b:
                    d["Secured or Unsecured"] = "".join(c.split(':')[1:]).strip()
                else:
                    d["Class of Borrowings"] = "".join(c.split(':')[1:]).strip()
                b = " ".join(re.sub('([A-Z][a-z])', r' \1', re.sub('([A-Z]+)', r' \1', a[1][0])).split())
                c = " ".join(re.sub('([A-Z][a-z])', r' \1', re.sub('([A-Z]+)', r' \1', a[1][1])).split())
                if "Subclassification Of Borrowings Axis" in b:
                    d["Secured or Unsecured"] = "".join(c.split(':')[1:]).strip()
                else:
                    d["Class of Borrowings"] = "".join(c.split(':')[1:]).strip()

            else:
                pass

            d.update(items)
            df1 = pd(d,index=['a']).T
            df = ct([df1,df],axis=1,ignore_index=True)
    return df

def divide(x):
    """ Returns True is string is a number. """
    try:
        if re.match("^\d+?", x):
            return float(x)/1000000
        elif re.match("^\d+?\.\d+?$", x):
            return float(x)/1000000
        else:
            return x
    except:
        pass

details = pd()

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


        one,two = data(two1,two1_pl)
        three,four = data(two2,two2_pl)
        five,six = data(three1,three1_pl)
        seven,eight = data(three2,three2_pl)

        one = frame(one)
        two = frame(two)
        three = frame(three)
        four = frame(four)
        five = frame(five)
        six = frame(six)
        seven = frame(seven)
        eight = frame(eight)

        details = ct([details,one,two,three,four,five,six,seven,eight],axis=1,ignore_index=True)

    except:
        print(file)
        pass


details = details.T
di = {'Current Member':'Short Term Member','Noncurrent Member':'Long Term Member'}
details["Time Period (Current or Non-Current)"] = details["Time Period (Current or Non-Current)"].replace(di)
details = details.applymap(divide)
details.to_csv('borrow.csv',index=False)
print(details)