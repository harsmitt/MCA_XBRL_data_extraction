from pandas import DataFrame as pd
from pandas import concat as ct
import os
from lxml.html import fromstring
from lxml import etree as et
from numpy import array as np
from datetime import datetime as dt
from bs4 import BeautifulSoup
import re

def auditor_items(aud):
    items = {"Name of Co.":nm, "CIN" : cin}
    for i in s.xpath('./*[@contextRef="%s"]'%aud.get('id')):
        a = "".join(i.tag.split('}')[1:]).strip()
        b = " ".join(re.sub('([A-Z][a-z])', r' \1', re.sub('([A-Z]+)', r' \1',a)).split())
        items[b] = BeautifulSoup(i.text,"html.parser").text
    return items

details = pd()
auditor = pd()

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

        pan = s.find('./in-ca:PermanentAccountNumberOfEntity',ns)
        pan = pan.text if pan is not None else None
        address = s.find('./in-ca:AddressOfRegisteredOfficeOfCompany',ns)
        address = fromstring(address.text).text_content() if address is not None else None
        listed = s.find('./in-ca:WhetherCompanyIsListedCompany',ns)
        listed = listed.text if listed is not None else None
        category = s.find('./in-ca:CategoryOrSubcategoryOfCompany',ns) if not None else None
        category = category.text if category is not None else None
        parent = s.find('./ind-as:NameOfUltimateParentOfGroup',ns) if 'ind-as' in ns else None
        parent = parent.text if parent is not None else None
        startdate0 = s.findall('./in-ca:DateOfStartOfReportingPeriod',ns)
        startdate = [i.text for i in startdate0 if len(years_pl) >=2 and i.get('contextRef')==all_y_pl[years2_pl[-2]].get('contextRef')]
        startdate.append([i.text for i in startdate0 if i.get('contextRef')==all_y_pl[years2_pl[-1]].get('contextRef')][0])
        enddate0 = s.findall('./in-ca:DateOfEndOfReportingPeriod',ns)
        enddate = [i.text for i in enddate0 if len(years_pl)>= 2 and i.get('contextRef')==all_y_pl[years2_pl[-2]].get('contextRef')]
        enddate.append([i.text for i in enddate0 if i.get('contextRef')==all_y_pl[years2_pl[-1]].get('contextRef')][0])

        nature = s.find('./in-ca:NatureOfReportStandaloneConsolidated',ns)
        nature = nature.text if nature is not None else None
        content = s.find('./in-ca:ContentOfReport',ns)
        content = content.text if content is not None else None
        currency = s.find('./in-ca:DescriptionOfPresentationCurrency',ns)
        currency = currency.text if currency is not None else None
        is_qualified = s.find("./in-ca:WhetherAuditorsReportHasBeenQualifiedOrHasAnyReservationsOrContainsAdverseRemarks",ns)
        is_qualified = is_qualified.text if is_qualified is not None else None
        if 'ind-as' in ns:
            claims1 = [i.text for i in oneybs if i.tag == "{%s}ClaimsAgainstCompanyNotAcknowledgedAsDebt" %ns['ind-as']]
            claims1 = claims1[-1] if len(claims1) >=1 else 0
            guarantees1 = [i.text for i in oneybs if i.tag == "{%s}Guarantees"%ns['ind-as']]
            guarantees1 = guarantees1[-1] if len(guarantees1) >=1 else 0
            other_money1 = [i.text for i in oneybs if i.tag == "{%s}OtherMoneyForWhichCompanyIsContingentlyLiable"%ns['ind-as']]
            other_money1 = other_money1[-1] if len(other_money1) >=1 else 0
            contract1 = [i.text for i in oneybs if i.tag == "{%s}EstimatedAmountOfContractsRemainingToBeExecutedOnCapitalAccountAndNotProvidedFor"%ns['ind-as']]
            contract1 = contract1[-1] if len(contract1) >=1 else 0
            uncalled1 = [i.text for i in oneybs if i.tag == "{%s}UncalledLiabilityOnSharesAndOtherInvestmentsPartlyPaid"%ns['ind-as']]
            uncalled1 = uncalled1[-1] if len(uncalled1) >=1 else 0
            other_commit1 = [i.text for i in oneybs if i.tag == "{%s}OtherCommitments"%ns['ind-as']]
            other_commit1 = other_commit1[-1] if len(other_commit1) >=1 else 0
            tcl1 = [i.text for i in oneybs if i.tag == "{%s}ContingentLiabilities"%ns['ind-as']]
            tcl1 = tcl1[-1] if len(tcl1) >=1 else 0
            if len(all_y_bs) >= 2:
                claims2 = [i.text for i in twoybs if i.tag == "{%s}ClaimsAgainstCompanyNotAcknowledgedAsDebt" %ns['ind-as']]
                claims2 = claims2[-1] if len(claims2) >=1 else 0
                guarantees2 = [i.text for i in twoybs if i.tag == "{%s}Guarantees"%ns['ind-as']]
                guarantees2 = guarantees2[-1] if len(guarantees2) >=1 else 0
                other_money2 = [i.text for i in twoybs if i.tag == "{%s}OtherMoneyForWhichCompanyIsContingentlyLiable"%ns['ind-as']]
                other_money2 = other_money2[-1] if len(other_money2) >=1 else 0
                contract2 = [i.text for i in twoybs if i.tag == "{%s}EstimatedAmountOfContractsRemainingToBeExecutedOnCapitalAccountAndNotProvidedFor"%ns['ind-as']]
                contract2 = contract2[-1] if len(contract2) >=1 else 0
                uncalled2 = [i.text for i in twoybs if i.tag == "{%s}UncalledLiabilityOnSharesAndOtherInvestmentsPartlyPaid"%ns['ind-as']]
                uncalled2 = uncalled2[-1] if len(uncalled2) >=1 else 0
                other_commit2 = [i.text for i in twoybs if i.tag == "{%s}OtherCommitments"%ns['ind-as']]
                other_commit2 = other_commit2[-1] if len(other_commit2) >=1 else 0
                tcl2 = [i.text for i in twoybs if i.tag == "{%s}ContingentLiabilities"%ns['ind-as']]
                tcl2 = tcl2[-1] if len(tcl2) >=1 else 0

        else:
            claims1 = [i.text for i in oneybs if i.tag == "{%s}ClaimsAgainstCompanyNotAcknowledgedAsDebt" %ns['in-gaap']]
            claims1 = claims1[-1] if len(claims1) >=1 else 0
            guarantees1 = [i.text for i in oneybs if i.tag == "{%s}Guarantees"%ns['in-gaap']]
            guarantees1 = guarantees1[-1] if len(guarantees1) >=1 else 0
            other_money1 = [i.text for i in oneybs if i.tag == "{%s}OtherMoneyForWhichCompanyIsContingentlyLiable"%ns['in-gaap']]
            other_money1 = other_money1[-1] if len(other_money1) >=1 else 0
            contract1 = [i.text for i in oneybs if i.tag == "{%s}EstimatedAmountOfContractsRemainingToBeExecutedOnCapitalAccountAndNotProvidedFor"%ns['in-gaap']]
            contract1 = contract1[-1] if len(contract1) >=1 else 0
            uncalled1 = [i.text for i in oneybs if i.tag == "{%s}UncalledLiabilityOnSharesAndOtherInvestmentsPartlyPaid"%ns['in-gaap']]
            uncalled1 = uncalled1[-1] if len(uncalled1) >=1 else 0
            other_commit1 = [i.text for i in oneybs if i.tag == "{%s}OtherCommitments"%ns['in-gaap']]
            other_commit1 = other_commit1[-1] if len(other_commit1) >=1 else 0
            tcl1 = [i.text for i in oneybs if i.tag == "{%s}ContingentLiabilities"%ns['in-gaap']]
            tcl1 = tcl1[-1] if len(tcl1) >=1 else 0
            if len(all_y_bs) >= 2:
                claims2 = [i.text for i in twoybs if i.tag == "{%s}ClaimsAgainstCompanyNotAcknowledgedAsDebt" %ns['in-gaap']]
                claims2 = claims2[-1] if len(claims2) >=1 else 0
                guarantees2 = [i.text for i in twoybs if i.tag == "{%s}Guarantees"%ns['in-gaap']]
                guarantees2 = guarantees2[-1] if len(guarantees2) >=1 else 0
                other_money2 = [i.text for i in twoybs if i.tag == "{%s}OtherMoneyForWhichCompanyIsContingentlyLiable"%ns['in-gaap']]
                other_money2 = other_money2[-1] if len(other_money2) >=1 else 0
                contract2 = [i.text for i in twoybs if i.tag == "{%s}EstimatedAmountOfContractsRemainingToBeExecutedOnCapitalAccountAndNotProvidedFor"%ns['in-gaap']]
                contract2 = contract2[-1] if len(contract2) >=1 else 0
                uncalled2 = [i.text for i in twoybs if i.tag == "{%s}UncalledLiabilityOnSharesAndOtherInvestmentsPartlyPaid"%ns['in-gaap']]
                uncalled2 = uncalled2[-1] if len(uncalled2) >=1 else 0
                other_commit2 = [i.text for i in twoybs if i.tag == "{%s}OtherCommitments"%ns['in-gaap']]
                other_commit2 = other_commit2[-1] if len(other_commit2) >=1 else 0
                tcl2 = [i.text for i in twoybs if i.tag == "{%s}ContingentLiabilities"%ns['in-gaap']]
                tcl2 = tcl2[-1] if len(tcl2) >=1 else 0

        domestic1 = [i.text for i in oneypl if i.tag == "{%s}DomesticTurnoverGoodsGross" %ns['in-ca']]
        domestic1 = domestic1[-1] if len(domestic1) >=1 else 0
        export1 = [i.text for i in oneypl if i.tag == "{%s}ExportTurnoverGoodsGross" %ns['in-ca']]
        export1 = export1[-1] if len(export1) >=1 else 0
        dom_service1 = [i.text for i in oneypl if i.tag == "{%s}DomesticRevenueServices" %ns['in-ca']]
        dom_service1 = dom_service1[-1] if len(dom_service1) >=1 else 0
        exp_service1 = [i.text for i in oneypl if i.tag == "{%s}ExportRevenueServices" %ns['in-ca']]
        exp_service1 = exp_service1[-1] if len(exp_service1) >=1 else 0
        tcom1 = sum([float(contract1), float(uncalled1), float(other_commit1)])
        sale_dom1 = sum([float(domestic1), float(dom_service1)])
        sale_exp1 = sum([float(export1), float(exp_service1)])
        if len(all_y_pl) >=2:
            dom_service2 = [i.text for i in twoypl if i.tag == "{%s}DomesticRevenueServices" %ns['in-ca']]
            dom_service2 = dom_service2[-1] if len(dom_service2) >=1 else 0
            export2 = [i.text for i in twoypl if i.tag == "{%s}ExportTurnoverGoodsGross" %ns['in-ca']]
            export2 = export2[-1] if len(export2) >=1 else 0
            domestic2 = [i.text for i in twoypl if i.tag == "{%s}DomesticTurnoverGoodsGross" %ns['in-ca']]
            domestic2 = domestic2[-1] if len(domestic2) >=1 else 0
            exp_service2 = [i.text for i in twoypl if i.tag == "{%s}ExportRevenueServices" %ns['in-ca']]
            exp_service2 = exp_service2[-1] if len(exp_service2) >=1 else 0
            sale_exp2 = sum([float(export2), float(exp_service2)])
            sale_dom2 = sum([float(domestic2), float(dom_service2)])
            tcom2 = sum([float(contract2), float(uncalled2), float(other_commit2)])


        gg = {'Name':nm,
            'CIN':cin,
            'PAN':pan,
            'Regd. Address':address,
            'Listed':listed,
            'Category':category,
            'Parent':parent,
            'Startdate':startdate,
            'Enddate':enddate,
            'Nature':nature,
            'Content':content,
            'Currency':currency,
            'Qualified Opinon':is_qualified,
            'Claims against company not acknowledged as debt':[claims2, claims1] if len(all_y_bs) >= 2 else claims1,
            'Guarantees':[guarantees2 ,guarantees1] if len(all_y_bs) >= 2 else guarantees1,
            'Other Contingent Liabilities':[other_money2, other_money1] if len(all_y_bs) >= 2 else other_money1,
            'Total Contingent Liabilities' : [tcl2, tcl1] if len(all_y_bs) >= 2 else tcl1,
            'Capital Commitments (Unprovided)':[contract2,contract1] if len(all_y_bs) >= 2 else contract1,
            'Uncalled Liability':[uncalled2,uncalled1] if len(all_y_bs) >= 2 else uncalled1,
            'Other Commitments':[other_commit2,other_commit1] if len(all_y_bs) >= 2 else other_commit1,
            'Total Commitments' : [tcom2,tcom1] if len(all_y_bs) >= 2 else tcom1,
            'Domestic Sale Goods':[domestic2,domestic1] if len(all_y_pl) >= 2 else domestic1,
            'Export Sale Goods':[export2,export1] if len(all_y_pl) >= 2 else export1,
            'Domestic Sale Service':[dom_service2,dom_service1] if len(all_y_pl) >= 2 else dom_service1,
            'Export Sale Service':[exp_service2,exp_service1] if len(all_y_pl) >= 2 else exp_service1,
            'Total Domestic Sale' : [sale_dom2,sale_dom1] if len(all_y_pl) >= 2 else sale_dom1,
            'Total Export Sale' : [sale_exp2,sale_exp1] if len(all_y_pl) >= 2 else sale_exp1
            }

        gh = pd(gg,index=enddate).T
        details = ct([details,gh],ignore_index=True,axis=1,sort=False)

    except Exception as e:
        print(e)
        print(file)
        pass

details.columns = details.loc['Enddate']

for i in details.index:
    try:
        details.loc[i] = details.loc[i].apply(lambda x:float(x)/1000000)
    except:
        details.loc[i] = details.loc[i]

print(details)
details.to_csv('Extras.csv')
auditor = auditor.drop_duplicates()
auditor.to_csv('Auditor.csv',index=False)
print(auditor)