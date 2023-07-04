from pandas import DataFrame as pd
from pandas import concat as ct
import os
from lxml import etree as et
from numpy import array as np
from datetime import datetime as dt

filelist = [i for i in os.listdir() if i.endswith('xml')]

def balance_sheet_gaap(oneybs, one):
    bs = {'co' : [],
    'tsti' : [],
     'arg' : [],
     'bd': [],
     'or': [],
     'inv': [],
     'pe': [],
     'mca': [],
     'oppe': [],
     'ppeg':[],
     'ad':[],
     'ius' : [],
     'oi' : [],
     'ng': [],
     'noi': [],
     'dta': [],
     'toa': [],
     'std': [],
     'ltdm': [],
     'ap': [],
     'itp': [],
     'dp': [],
     'acp' : [],
     'mcl' : [],
     'ltd' : [],
     'pfrc' : [],
     'dtl' : [],
     'ol': [],
     'di' : [],
     'csv': [],
     'apic': [],
     're' :[],
     'ur': [],
     'ami': [],
    }
    for i in oneybs:
        bs['co'].append(i.text) if i.tag == "{%s}CashAndBankBalances" %ns['in-gaap'] else None
        bs['tsti'].append(i.text) if i.tag == "{%s}CurrentInvestments" %ns['in-gaap'] else None
        bs['arg'].append(i.text) if i.tag == "{%s}TradeReceivablesGross" %ns['in-gaap'] else None
        bs['bd'].append(i.text) if i.tag == "{%s}AllowanceForBadAndDoubtfulDebts" %ns['in-gaap'] else None
        bs['or'].append(i.text) if i.tag == "{%s}ShortTermLoansAndAdvances" %ns['in-gaap'] else None
        bs['inv'].append(i.text) if i.tag == "{%s}Inventories" %ns['in-gaap'] else None
        #bs['pe'].append(i.text) if i.tag == "{%s}CurrentAdvances" %ns['in-gaap'] else None
        #bs['pe'].append(i.text) if i.tag == "{%s}OtherUnamortisedExpenses" %ns['in-gaap'] else None
        bs['mca'].append(i.text) if i.tag == "{%s}OtherCurrentAssets" %ns['in-gaap'] else None
        bs['oppe'].append(i.text) if i.tag == "{%s}TangibleAssets" %ns['in-gaap'] else None
        bs['oppe'].append(i.text) if i.tag == "{%s}ProducingProperties" %ns['in-gaap'] else None
        bs['oppe'].append(i.text) if i.tag == "{%s}PreproducingProperties" %ns['in-gaap'] else None
        bs['oppe'].append(i.text) if i.tag == "{%s}TangibleAssetsCapitalWorkInProgress" %ns['in-gaap'] else None
        #bs['ius'].append(i.text) if i.tag == "{%s}InvestmentProperty" %ns['in-gaap'] else None
        #bs['ius'].append(i.text) if i.tag == "{%s}InvestmentsAccountedForUsingEquityMethod" %ns['in-gaap'] else None
        bs['oi'].append(i.text) if i.tag == "{%s}NoncurrentInvestments" %ns['in-gaap'] else None
        bs['oi'].append(i.text) if i.tag == "{%s}ForeignCurrencyMonetaryItemTranslationDifferenceAssetAccount" %ns['in-gaap'] else None
        bs['oi'].append(i.text) if i.tag == "{%s}LongTermLoansAndAdvances" %ns['in-gaap'] else None
        #ng
        bs['noi'].append(i.text) if i.tag == "{%s}IntangibleAssets" %ns['in-gaap'] else None
        bs['noi'].append(i.text) if i.tag == "{%s}IntangibleAssetsUnderDevelopmentOrWorkInProgress" %ns['in-gaap'] else None
        bs['dta'].append(i.text) if i.tag == "{%s}DeferredTaxAssetsNet" %ns['in-gaap'] else None
        bs['toa'].append(i.text) if i.tag == "{%s}OtherNoncurrentAssets" %ns['in-gaap'] else None
        bs['std'].append(i.text) if i.tag == "{%s}ShortTermBorrowings" %ns['in-gaap'] else None
        bs['ltdm'].append(i.text) if i.tag == "{%s}CurrentMaturitiesOfLongTermDebt" %ns['in-gaap'] else None
        bs['ltdm'].append(i.text) if i.tag == "{%s}CurrentMaturitiesOfFinanceLeaseObligations" %ns['in-gaap'] else None
        bs['ap'].append(i.text) if i.tag == "{%s}TradePayables" %ns['in-gaap'] else None
        #bs['itp'].append(i.text) if i.tag == "{%s}TradeReceivablesGross" %ns['in-gaap'] else None
        bs['dp'].append(i.text) if i.tag == "{%s}UnpaidDividends" %ns['in-gaap'] else None
        bs['acp'].append(i.text) if i.tag == "{%s}AccruedSalaryPayable" %ns['in-gaap'] else None
        bs['acp'].append(i.text) if i.tag == "{%s}AccruedPayrollLiabilitiesOther" %ns['in-gaap'] else None
        bs['acp'].append(i.text) if i.tag == "{%s}ShortTermEmployeeRelatedLiabilities" %ns['in-gaap'] else None
        bs['acp'].append(i.text) if i.tag == "{%s}ContributionToProvidentFundScheme" %ns['in-gaap'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}ShortTermProvisions" %ns['in-gaap'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}InterestAccruedButNotDueOnBorrowings" %ns['in-gaap'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}InterestAccruedAndDueOnBorrowings" %ns['in-gaap'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}InterestAccruedButNotDueOnPublicDeposits" %ns['in-gaap'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}InterestAccruedAndDueOnPublicDeposits" %ns['in-gaap'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}DebenturesClaimedButNotPaid" %ns['in-gaap'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}IncomeReceivedInAdvance" %ns['in-gaap'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}ApplicationMoneyReceivedForAllotmentOfSecuritiesAndDueForRefundAndInterestAccruedThereon" %ns['in-gaap'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}UnpaidMaturedDepositsAndInterestAccruedThereon" %ns['in-gaap'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}UnpaidMaturedDebenturesAndInterestAccruedThereon" %ns['in-gaap'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}OtherPayablesCurrent" %ns['in-gaap'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}DerivativeLiabilities" %ns['in-gaap'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}AdvanceReceivedAgainstContracts" %ns['in-gaap'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}AdvanceReceivedFromCustomers" %ns['in-gaap'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}OtherAdvanceReceived" %ns['in-gaap'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}BillsPayableAcceptances" %ns['in-gaap'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}RetentionMoneyPayable" %ns['in-gaap'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}CurrentLiabilitiesPortionOfShareApplicationMoneyPendingAllotment" %ns['in-gaap'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}OtherCurrentLiabilitiesOthers" %ns['in-gaap'] else None

        bs['ltd'].append(i.text) if i.tag == "{%s}LongTermBorrowings" %ns['in-gaap'] else None
        bs['pfrc'].append(i.text) if i.tag == "{%s}LongTermProvisions" %ns['in-gaap'] else None
        bs['dtl'].append(i.text) if i.tag == "{%s}DeferredTaxLiabilitiesNet" %ns['in-gaap'] else None
        bs['ol'].append(i.text) if i.tag == "{%s}DeferredGovernmentGrants" %ns['in-gaap'] else None
        bs['ol'].append(i.text) if i.tag == "{%s}ForeignCurrencyMonetaryItemTranslationDifferenceLiabilityAccount" %ns['in-gaap'] else None
        bs['ol'].append(i.text) if i.tag == "{%s}TradePayablesLongTerm" %ns['in-gaap'] else None
        bs['ol'].append(i.text) if i.tag == "{%s}OthersLongTermOthers" %ns['in-gaap'] else None
        bs['di'].append(i.text) if i.tag == "{%s}GrossAmountDueToCustomersForContractWorkNoncurrent" %ns['in-gaap'] else None
        bs['csv'].append(i.text) if i.tag == "{%s}ShareCapital" %ns['in-gaap'] else None
        bs['apic'].append(i.text) if i.tag == "{%s}MoneyReceivedAgainstShareWarrants" %ns['in-gaap'] else None
        bs['re'].append(i.text) if i.tag == "{%s}ReservesAndSurplus" %ns['in-gaap'] else None
        bs['ur'].append(i.text) if i.tag == "{%s}ShareApplicationMoneyPendingAllotment" %ns['in-gaap'] else None
        bs['ami'].append(i.text) if i.tag == "{%s}MinorityInterest" %ns['in-gaap'] else None

    for i in one:
        a = i.find('./xbrli:scenario/xbrldi:explicitMember[@dimension="in-gaap:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis"]',ns)
        if a is not None and a.text == "in-gaap:GrossCarryingAmountMember":
            bs['ppeg'].append(s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text) if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else bs['ppeg'].append(0)
        elif a is not None and a.text == "in-gaap:AccumulatedDepreciationAndImpairmentMember":
            bs['ad'].append(s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text) if s.find('./in-gaap:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else bs['ad'].append(0)

    for i in bs:
        bs[i] = sum([float(k) for k in bs[i]])
    return bs

def profit_loss_gaap(oneypl):
    pl = {'sale' : [],
    'cogs' : [],
     'dep' : [],
     'amort1': [],
     'amort2': [],
     'rnd': [],
     'osga': [],
     'ooe': [],
     'noii': [],
     'eea' : [],
     'oie' : [],
     'gie': [],
     'fixai': [],
     'finai': [],
     'exprov': [],
     'oiai': [],
     'invgain': [],
     'oue': [],
     'taxcur': [],
     'taxdef': [],
     'ofta' : [],
     'mie' : [],
     'dividend' : []
     }
    for i in oneypl:
        pl['sale'].append(i.text) if i.tag == "{%s}RevenueFromOperations" %ns['in-gaap'] else None
        pl['cogs'].append(i.text) if i.tag == "{%s}PurchasesOfStockInTrade" %ns['in-gaap'] else None
        pl['cogs'].append(i.text) if i.tag == "{%s}ExpenditureOnProductionTransportationAndOtherExpenditurePertainingToExplorationAndProductionActivities" %ns['in-gaap'] else None
        pl['cogs'].append(i.text) if i.tag == "{%s}CostOfMaterialsConsumed" %ns['in-gaap'] else None
        pl['cogs'].append(i.text) if i.tag == "{%s}ChangesInInventoriesOfFinishedGoodsWorkInProgressAndStockInTrade" %ns['in-gaap'] else None
        pl['cogs'].append(i.text) if i.tag == "{%s}SalariesAndWages" %ns['in-gaap'] else None
        pl['cogs'].append(i.text) if i.tag == "{%s}ConsumptionOfStoresAndSpareParts" %ns['in-gaap'] else None
        pl['cogs'].append(i.text) if i.tag == "{%s}PowerAndFuel" %ns['in-gaap'] else None
        pl['dep'].append(i.text) if i.tag == "{%s}DepreciationExpense" %ns['in-gaap'] else None
        pl['amort1'].append(i.text) if i.tag == "{%s}AmortisationExpense" %ns['in-gaap'] else None
        pl['amort2'].append(i.text) if i.tag == "{%s}DepletionExpense" %ns['in-gaap'] else None
        pl['rnd'].append(i.text) if i.tag == "{%s}ResearchDevelopmentExpenditure" %ns['in-gaap'] else None

        pl['osga'].append(i.text) if i.tag == "{%s}CSRExpenditure" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}ManagerialRemuneration" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}ContributionToProvidentAndOtherFunds" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}ExpenseOnEmployeeStockOptionSchemeAndEmployeeStockPurchasePlan" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CommissionEmployees" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}EmployeeMedicalInsuranceExpenses" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}LeaveEncashmentExpenses" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}Gratuity" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}PensionSchemes" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}VoluntaryRetirementCompensation" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}OtherRetirementBenefits" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}StaffWelfareExpense" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}OtherEmployeeRelatedExpenses" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}Rent" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}RepairsToBuilding" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}RepairsToMachinery" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}Insurance" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}RatesAndTaxesExcludingTaxesOnIncome" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}SubscriptionsMembershipFees" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}ElectricityExpenses" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}TelephonePostage" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}PrintingStationery" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}InformationTechnologyExpenses" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}TravellingConveyance" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CateringCanteenExpenses" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}EntertainmentExpenses" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}LegalProfessionalCharges" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}TrainingRecruitmentExpenses" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}VehicleRunningExpenses" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}SafetySecurityExpenses" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}DirectorsSittingFees" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CommissionToDirectorsOtherThanWholeTimeDirectorOrManagingDirectorOrManager" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}DonationsSubscriptions" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}BooksPeriodicals" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}SeminarsConferenceExpenses" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}RegistrationFilingFees" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CustodialFees" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}BankCharges" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}GuestHouseExpenses" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}AdvertisingPromotionalExpenses" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}AfterSalesServiceExpenses" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}WarrantyClaimExpenses" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CommissionPaidSoleSellingAgents" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CommissionPaidOtherSellingAgents" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CommissionPaidSoleBuyingAgents" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}TransportationDistributionExpenses" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}SecondaryPackingExpenses" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}DiscountingCharges" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}GuaranteeCommission" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CostRepairsMaintenanceOtherAssets" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CostTransportation" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CostLeaseRentals" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CostEffluentDisposal" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}ProvisionForCostOfRestoration" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CostWarehousing" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CostWaterCharges" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CostTechnicalServices" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CostRoyalty" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}ProvisionBadDoubtfulDebtsCreated" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}ProvisionBadDoubtfulLoansAdvancesCreated" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}ContractCost" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CostDryWells" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}OperatingAndMaintenanceCostOfEmissionAndOtherPollutionReductionEquipments" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}PaymentsToAuditor" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}PaymentsToCostAuditor" %ns['in-ca'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CostInformationTechnology" %ns['in-gaap'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CostReimbursableExpenses" %ns['in-gaap'] else None

        pl['ooe'].append(i.text) if i.tag == "{%s}MiscellaneousExpenses" %ns['in-gaap'] else None
        pl['noii'].append(i.text) if i.tag == "{%s}InterestIncome" %ns['in-gaap'] else None
        pl['eea'].append(i.text) if i.tag == "{%s}ShareOfProfitLossOfAssociates" %ns['in-gaap'] else None

        pl['oie'].append(i.text) if i.tag == "{%s}DividendIncome" %ns['in-gaap'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}NetGainLossOnSaleOfInvestments" %ns['in-gaap'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}RentalIncomeOnInvestmentProperty" %ns['in-gaap'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}NetGainLossOnForeignCurrencyFluctuationsTreatedAsOtherIncome" %ns['in-gaap'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}SurplusOnDisposalDiscardDemolishmentAndDestructionOfDepreciableTangibleAsset" %ns['in-gaap'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}GainOnDisposalOfIntangibleAsset" %ns['in-gaap'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}AmountCreditedToProfitAndLossAsTransferFromRevaluationReserveOnAccountOfAdditionalDepreciationChargedOnRevaluedTangibleAssets" %ns['in-gaap'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}ExcessProvisionDiminutionInValueInvestmentWrittenBack" %ns['in-gaap'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}ExcessProvisionsBadDoubtfulDebtsAdvancesWrittenBack" %ns['in-gaap'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}IncomeGovernmentGrantsSubsidies" %ns['in-gaap'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}IncomeExportIncentives" %ns['in-gaap'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}IncomeImportEntitlements" %ns['in-gaap'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}IncomeInsuranceClaims" %ns['in-gaap'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}IncomeFromSubsidiaries" %ns['in-gaap'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}InterestOnIncomeTaxRefund" %ns['in-gaap'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}IncomeOnBrokerageCommission" %ns['in-gaap'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}IncomeOnSalesTaxBenefit" %ns['in-gaap'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}ExcessProvisionsWrittenBack" %ns['in-gaap'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}OtherAllowancesDeductionOtherIncome" %ns['in-gaap'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}MiscellaneousOtherNonoperatingIncome" %ns['in-gaap'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}IncomeFromPipelineTransportation" %ns['in-gaap'] else None

        pl['gie'].append(i.text) if i.tag == "{%s}FinanceCosts" %ns['in-gaap'] else None

        pl['fixai'].append(i.text) if i.tag == "{%s}LiabilitiesWrittenOff" %ns['in-gaap'] else None
        pl['fixai'].append(i.text) if i.tag == "{%s}FixedAssetsWrittenOff" %ns['in-gaap'] else None
        pl['fixai'].append(i.text) if i.tag == "{%s}InventoriesWrittenOff" %ns['in-gaap'] else None
        pl['fixai'].append(i.text) if i.tag == "{%s}BadDebtsWrittenOff" %ns['in-gaap'] else None
        pl['fixai'].append(i.text) if i.tag == "{%s}BadDebtsAdvancesWrittenOff" %ns['in-gaap'] else None
        pl['fixai'].append(i.text) if i.tag == "{%s}OtherAssetsWrittenOff" %ns['in-gaap'] else None

        pl['finai'].append(i.text) if i.tag == "{%s}InvestmentsWrittenOff" %ns['in-gaap'] else None
        pl['exprov'].append(i.text) if i.tag == "{%s}NetProvisionsCharged" %ns['in-gaap'] else None
        pl['oiai'].append(i.text) if i.tag == "{%s}LossOnDisposalOfIntangibleAsset" %ns['in-gaap'] else None
        pl['invgain'].append(i.text) if i.tag == "{%s}AdjustmentsToCarryingAmountsOfInvestments" %ns['in-gaap'] else None

        pl['oue'].append(i.text) if i.tag == "{%s}PriorPeriodItemsBeforeTax" %ns['in-gaap'] else None
        pl['oue'].append(i.text) if i.tag == "{%s}ExceptionalItemsBeforeTax" %ns['in-gaap'] else None
        pl['oue'].append(i.text) if i.tag == "{%s}ExtraordinaryItemsBeforeTax" %ns['in-gaap'] else None
        pl['oue'].append(i.text) if i.tag == "{%s}DiscountIssueSharesDebenturesWrittenOff" %ns['in-gaap'] else None
        pl['oue'].append(i.text) if i.tag == "{%s}MiscellaneousExpenditureWrittenOff" %ns['in-gaap'] else None
        pl['oue'].append(i.text) if i.tag == "{%s}LossOnDisposalDiscardDemolishmentAndDestructionOfDepreciableTangibleAsset" %ns['in-gaap'] else None

        pl['taxcur'].append(i.text) if i.tag == "{%s}CurrentTax" %ns['in-gaap'] else None
        pl['taxdef'].append(i.text) if i.tag == "{%s}DeferredTax" %ns['in-gaap'] else None
        pl['ofta'].append(i.text) if i.tag == "{%s}ProfitLossFromDiscontinuingOperationAfterTax" %ns['in-gaap'] else None
        pl['mie'].append(i.text) if i.tag == "{%s}ProfitLossOfMinorityInterest" %ns['in-gaap'] else None
        pl['dividend'].append(i.text) if i.tag == "{%s}DividendsPaidClassifiedAsFinancingActivities" %ns['in-gaap'] else None
    for i in pl:
        pl[i] = sum([float(k) for k in pl[i]])
    return pl

def balance_sheet_indas(oneybs, one):
    bs = {'co' : [],
    'tsti' : [],
     'arg' : [],
     'bd': [],
     'or': [],
     'inv': [],
     'pe': [],
     'mca': [],
     'oppe': [],
     'ppeg':[],
     'ad':[],
     'ius' : [],
     'oi' : [],
     'ng': [],
     'noi': [],
     'dta': [],
     'toa': [],
     'std': [],
     'ltdm': [],
     'ap': [],
     'itp': [],
     'dp': [],
     'acp' : [],
     'mcl' : [],
     'ltd' : [],
     'pfrc' : [],
     'dtl' : [],
     'ol': [],
     'di' : [],
     'csv': [],
     'apic': [],
     're' :[],
     'ur': [],
     'ami': [],
    }
    for i in oneybs:
        bs['co'].append(i.text) if i.tag == "{%s}CashAndCashEquivalents" %ns['ind-as'] else None
        bs['tsti'].append(i.text) if i.tag == "{%s}CurrentInvestments" %ns['ind-as'] else None
        bs['tsti'].append(i.text) if i.tag == "{%s}BankBalanceOtherThanCashAndCashEquivalents" %ns['ind-as'] else None
        bs['tsti'].append(i.text) if i.tag == "{%s}OtherCurrentFinancialAssetsOthers" %ns['ind-as'] else None
        bs['arg'].append(i.text) if i.tag == "{%s}TradeReceivablesCurrent" %ns['ind-as'] else None
        #bs['bd'].append(i.text) if i.tag == "{%s}AllowanceForBadAndDoubtfulDebts" %ns['ind-as'] else None
        bs['or'].append(i.text) if i.tag == "{%s}LoansCurrent" %ns['ind-as'] else None
        bs['or'].append(i.text) if i.tag == "{%s}UnbilledRevenue" %ns['ind-as'] else None
        bs['or'].append(i.text) if i.tag == "{%s}SecurityDeposits" %ns['ind-as'] else None
        bs['inv'].append(i.text) if i.tag == "{%s}Inventories" %ns['ind-as'] else None
        bs['pe'].append(i.text) if i.tag == "{%s}CurrentAdvances" %ns['ind-as'] else None
        bs['pe'].append(i.text) if i.tag == "{%s}OtherUnamortisedExpenses" %ns['ind-as'] else None
        bs['mca'].append(i.text) if i.tag == "{%s}NoncurrentAssetsClassifiedAsHeldForSale" %ns['ind-as'] else None
        bs['mca'].append(i.text) if i.tag == "{%s}RegulatoryDeferralAccountDebitBalancesAndRelatedDeferredTaxAssets" %ns['ind-as'] else None
        bs['mca'].append(i.text) if i.tag == "{%s}DerivativeFinancialInstruments" %ns['ind-as'] else None
        bs['mca'].append(i.text) if i.tag == "{%s}PropertyPlantAndEquipmentHeldForSale" %ns['ind-as'] else None
        bs['mca'].append(i.text) if i.tag == "{%s}CurrentTaxAssets" %ns['ind-as'] else None
        bs['mca'].append(i.text) if i.tag == "{%s}OtherCurrentAssetsOthers" %ns['ind-as'] else None

        bs['oppe'].append(i.text) if i.tag == "{%s}PropertyPlantAndEquipment" %ns['ind-as'] else None
        bs['oppe'].append(i.text) if i.tag == "{%s}CapitalWorkInProgress" %ns['ind-as'] else None
        bs['oppe'].append(i.text) if i.tag == "{%s}BiologicalAssetsOtherThanBearerPlants" %ns['ind-as'] else None

        bs['ius'].append(i.text) if i.tag == "{%s}InvestmentProperty" %ns['ind-as'] else None
        bs['ius'].append(i.text) if i.tag == "{%s}InvestmentsAccountedForUsingEquityMethod" %ns['ind-as'] else None
        bs['oi'].append(i.text) if i.tag == "{%s}TradeReceivablesNoncurrent" %ns['ind-as'] else None
        bs['oi'].append(i.text) if i.tag == "{%s}OtherNoncurrentFinancialAssets" %ns['ind-as'] else None
        bs['oi'].append(i.text) if i.tag == "{%s}LoansNoncurrent" %ns['ind-as'] else None
        bs['oi'].append(i.text) if i.tag == "{%s}OtherNoncurrentAssets" %ns['ind-as'] else None
        bs['oi'].append(i.text) if i.tag == "{%s}NoncurrentInvestments" %ns['ind-as'] else None
        bs['ng'].append(i.text) if i.tag == "{%s}Goodwill" %ns['ind-as'] else None
        bs['noi'].append(i.text) if i.tag == "{%s}IntangibleAssetsUnderDevelopment" %ns['ind-as'] else None
        bs['noi'].append(i.text) if i.tag == "{%s}OtherIntangibleAssets" %ns['ind-as'] else None
        bs['dta'].append(i.text) if i.tag == "{%s}DeferredTaxAssetsNet" %ns['ind-as'] else None
        #bs['toa'].append(i.text) if i.tag == "{%s}OtherNoncurrentAssets" %ns['ind-as'] else None
        bs['std'].append(i.text) if i.tag == "{%s}BorrowingsCurrent" %ns['ind-as'] else None
        bs['ltdm'].append(i.text) if i.tag == "{%s}CurrentMaturitiesOfLongTermDebt" %ns['ind-as'] else None
        bs['ltdm'].append(i.text) if i.tag == "{%s}CurrentMaturitiesOfFinanceLeaseObligations" %ns['ind-as'] else None
        bs['ap'].append(i.text) if i.tag == "{%s}TradePayablesCurrent" %ns['ind-as'] else None
        bs['itp'].append(i.text) if i.tag == "{%s}CurrentTaxLiabilities" %ns['ind-as'] else None
        #bs['dp'].append(i.text) if i.tag == "{%s}UnpaidDividends" %ns['ind-as'] else None
        bs['acp'].append(i.text) if i.tag == "{%s}ProvisionsCurrent" %ns['ind-as'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}DeferredGovernmentGrantsCurrent" %ns['ind-as'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}LiabilitiesDirectlyAssociatedWithAssetsInDisposalGroupClassifiedAsHeldForSale" %ns['ind-as'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}OtherCurrentLiabilities" %ns['ind-as'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}RegulatoryDeferralAccountCreditBalancesAndRelatedDeferredTaxLiability" %ns['ind-as'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}InterestAccruedOnBorrowings" %ns['ind-as'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}InterestAccruedOnPublicDeposits" %ns['ind-as'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}InterestAccruedOthers" %ns['ind-as'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}UnpaidDividends" %ns['ind-as'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}RetentionMoneyPayable" %ns['ind-as'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}ApplicationMoneyReceivedForAllotmentOfSecuritiesAndDueForRefundAndInterestAccruedThereon" %ns['ind-as'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}UnpaidMaturedDepositsAndInterestAccruedThereon" %ns['ind-as'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}UnpaidMaturedDebenturesAndInterestAccruedThereon" %ns['ind-as'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}DebenturesClaimedButNotPaid" %ns['ind-as'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}PublicDepositPayableCurrent" %ns['ind-as'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}DerivativeLiabilities" %ns['ind-as'] else None
        bs['mcl'].append(i.text) if i.tag == "{%s}OtherCurrentFinancialLiabilitiesOthers" %ns['ind-as'] else None
        bs['ltd'].append(i.text) if i.tag == "{%s}BorrowingsNoncurrent" %ns['ind-as'] else None
        bs['pfrc'].append(i.text) if i.tag == "{%s}ProvisionsNoncurrent" %ns['ind-as'] else None
        bs['dtl'].append(i.text) if i.tag == "{%s}DeferredTaxLiabilitiesNet" %ns['ind-as'] else None
        bs['ol'].append(i.text) if i.tag == "{%s}TradePayablesNoncurrent" %ns['ind-as'] else None
        bs['ol'].append(i.text) if i.tag == "{%s}OtherNoncurrentFinancialLiabilities" %ns['ind-as'] else None
        bs['ol'].append(i.text) if i.tag == "{%s}DeferredGovernmentGrantsNoncurrent" %ns['ind-as'] else None
        bs['ol'].append(i.text) if i.tag == "{%s}OtherNoncurrentLiabilitiesOthers" %ns['ind-as'] else None
        bs['di'].append(i.text) if i.tag == "{%s}AdvancesReceivedNoncurrentLiabilities" %ns['ind-as'] else None
        bs['csv'].append(i.text) if i.tag == "{%s}EquityShareCapital" %ns['ind-as'] else None
        #bs['apic'].append(i.text) if i.tag == "{%s}MoneyReceivedAgainstShareWarrants" %ns['ind-as'] else None
        bs['re'].append(i.text) if i.tag == "{%s}OtherEquity" %ns['ind-as'] else None
        #bs['ur'].append(i.text) if i.tag == "{%s}ShareApplicationMoneyPendingAllotment" %ns['ind-as'] else None
        bs['ami'].append(i.text) if i.tag == "{%s}NonControllingInterest" %ns['ind-as'] else None

    for i in one:
        a = i.find('./xbrli:scenario/xbrldi:explicitMember[@dimension="ind-as:CarryingAmountAccumulatedDepreciationAndGrossCarryingAmountAxis"]',ns)
        if a is not None and a.text == "ind-as:GrossCarryingAmountMember":
            bs['ppeg'].append(s.find('./ind-as:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text) if s.find('./ind-as:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else bs['ppeg'].append(0)
        elif a is not None and a.text == "ind-as:AccumulatedDepreciationAndImpairmentMember":
            bs['ad'].append(s.find('./ind-as:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns).text) if s.find('./ind-as:TangibleAssets[@contextRef="%s"]'%i.get('id'),ns) is not None else bs['ad'].append(0)

    for i in bs:
        bs[i] = sum([float(k) for k in bs[i]])
    return bs

def profit_loss_indas(oneypl):
    pl = {'sale' : [],
    'cogs' : [],
     'dep' : [],
     'amort1': [],
     'amort2': [],
     'rnd': [],
     'osga': [],
     'ooe': [],
     'noii': [],
     'eea' : [],
     'oie' : [],
     'gie': [],
     'fixai': [],
     'finai': [],
     'exprov': [],
     'oiai': [],
     'invgain': [],
     'oue': [],
     'taxcur': [],
     'taxdef': [],
     'ofta' : [],
     'mie' : [],
     'dividend' : []
     }
    for i in oneypl:
        pl['sale'].append(i.text) if i.tag == "{%s}RevenueFromOperations" %ns['ind-as'] else None
        pl['cogs'].append(i.text) if i.tag == "{%s}ChangesInInventoriesOfFinishedGoodsWorkInProgressAndStockInTrade" %ns['ind-as'] else None
        pl['cogs'].append(i.text) if i.tag == "{%s}SalariesAndWages" %ns['ind-as'] else None
        pl['cogs'].append(i.text) if i.tag == "{%s}ConsumptionOfStoresAndSpareParts" %ns['ind-as'] else None
        pl['cogs'].append(i.text) if i.tag == "{%s}PowerAndFuel" %ns['ind-as'] else None
        pl['cogs'].append(i.text) if i.tag == "{%s}ExpenditureOnProductionTransportationAndOtherExpenditurePertainingToExplorationAndProductionActivities" %ns['ind-as'] else None
        pl['cogs'].append(i.text) if i.tag == "{%s}CostOfMaterialsConsumed" %ns['ind-as'] else None
        pl['cogs'].append(i.text) if i.tag == "{%s}PurchasesOfStockInTrade" %ns['ind-as'] else None
        pl['dep'].append(i.text) if i.tag == "{%s}DepreciationExpense" %ns['ind-as'] else None
        pl['amort1'].append(i.text) if i.tag == "{%s}AmortisationExpense" %ns['ind-as'] else None
        pl['amort2'].append(i.text) if i.tag == "{%s}DepletionExpense" %ns['ind-as'] else None
        pl['rnd'].append(i.text) if i.tag == "{%s}ResearchDevelopmentExpenditure" %ns['ind-as'] else None

        pl['osga'].append(i.text) if i.tag == "{%s}CSRExpenditure" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}ManagerialRemuneration" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}ContributionToProvidentAndOtherFunds" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}EmployeeShareBasedPayment" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CommissionEmployees" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}EmployeeMedicalInsuranceExpenses" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}LeaveEncashmentExpenses" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}Gratuity" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}PensionSchemes" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}VoluntaryRetirementCompensation" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}OtherRetirementBenefits" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}StaffWelfareExpense" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}OtherEmployeeRelatedExpenses" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}Rent" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}RepairsToBuilding" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}RepairsToMachinery" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}Insurance" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}RatesAndTaxesExcludingTaxesOnIncome" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}SubscriptionsMembershipFees" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}ElectricityExpenses" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}TelephonePostage" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}PrintingStationery" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}InformationTechnologyExpenses" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}TravellingConveyance" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CateringCanteenExpenses" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}EntertainmentExpenses" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}LegalProfessionalCharges" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}TrainingRecruitmentExpenses" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}VehicleRunningExpenses" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}SafetySecurityExpenses" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}DirectorsSittingFees" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CommissionToDirectorsOtherThanWholeTimeDirectorOrManagingDirectorOrManager" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}DonationsSubscriptions" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}BooksPeriodicals" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}SeminarsConferenceExpenses" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}RegistrationFilingFees" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CustodialFees" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}BankCharges" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}GuestHouseExpenses" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}AdvertisingPromotionalExpenses" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}AfterSalesServiceExpenses" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}WarrantyClaimExpenses" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CommissionPaidSoleSellingAgents" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CommissionPaidOtherSellingAgents" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CommissionPaidSoleBuyingAgents" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}TransportationDistributionExpenses" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}SecondaryPackingExpenses" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}DiscountingCharges" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}GuaranteeCommission" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CostRepairsMaintenanceOtherAssets" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CostTransportation" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CostLeaseRentals" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CostEffluentDisposal" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}ProvisionForCostOfRestoration" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CostWarehousing" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CostWaterCharges" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CostTechnicalServices" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CostRoyalty" %ns['ind-as'] else None
        #pl['osga'].append(i.text) if i.tag == "{%s}ProvisionBadDoubtfulDebtsCreated" %ns['ind-as'] else None
        #pl['osga'].append(i.text) if i.tag == "{%s}ProvisionBadDoubtfulLoansAdvancesCreated" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}ContractCost" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}CostDryWells" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}OperatingAndMaintenanceCostOfEmissionAndOtherPollutionReductionEquipments" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}PaymentsToAuditor" %ns['ind-as'] else None
        pl['osga'].append(i.text) if i.tag == "{%s}PaymentsToCostAuditor" %ns['in-ca'] else None
        #pl['osga'].append(i.text) if i.tag == "{%s}CostInformationTechnology" %ns['ind-as'] else None
        #pl['osga'].append(i.text) if i.tag == "{%s}CostReimbursableExpenses" %ns['ind-as'] else None

        pl['ooe'].append(i.text) if i.tag == "{%s}MiscellaneousExpenses" %ns['ind-as'] else None
        pl['noii'].append(i.text) if i.tag == "{%s}InterestIncome" %ns['ind-as'] else None
        pl['eea'].append(i.text) if i.tag == "{%s}ShareOfProfitLossOfAssociates" %ns['ind-as'] else None
        pl['eea'].append(i.text) if i.tag == "{%s}DividendIncomeCurrentInvestmentsFromSubsidiaries" %ns['ind-as'] else None
        pl['eea'].append(i.text) if i.tag == "{%s}DividendIncomeNoncurrentInvestmentsFromSubsidiaries" %ns['ind-as'] else None

        pl['oie'].append(i.text) if i.tag == "{%s}DividendIncomeCurrentEquitySecurities" %ns['ind-as'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}DividendIncomeCurrentMutualFunds" %ns['ind-as'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}DividendIncomeCurrentInvestmentsFromOthers" %ns['ind-as'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}DividendIncomeNoncurrentEquitySecurities" %ns['ind-as'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}DividendIncomeNoncurrentMutualFunds" %ns['ind-as'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}DividendIncomeNoncurrentInvestmentsFromOthers" %ns['ind-as'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}NetGainLossOnSaleOfInvestments" %ns['ind-as'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}RentalIncomeOnInvestmentProperty" %ns['ind-as'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}NetGainLossOnForeignCurrencyFluctuationsTreatedAsOtherIncome" %ns['ind-as'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}SurplusOnDisposalDiscardDemolishmentAndDestructionOfDepreciablePropertyPlantAndEquipment" %ns['ind-as'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}GainOnDisposalOfIntangibleAssets" %ns['ind-as'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}AmountCreditedToProfitAndLossAsTransferFromRevaluationReserveOnAccountOfAdditionalDepreciationChargedOnRevaluedTangibleAssets" %ns['ind-as'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}ExcessProvisionDiminutionInValueInvestmentWrittenBack" %ns['ind-as'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}ExcessProvisionsBadDoubtfulDebtsAdvancesWrittenBack" %ns['ind-as'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}IncomeGovernmentGrantsSubsidies" %ns['ind-as'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}IncomeExportIncentives" %ns['ind-as'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}IncomeImportEntitlements" %ns['ind-as'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}IncomeInsuranceClaims" %ns['ind-as'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}IncomeFromSubsidiaries" %ns['ind-as'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}InterestOnIncomeTaxRefund" %ns['ind-as'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}IncomeOnBrokerageCommission" %ns['ind-as'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}IncomeOnSalesTaxBenefit" %ns['ind-as'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}ExcessProvisionsWrittenBack" %ns['ind-as'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}OtherAllowancesDeductionOtherIncome" %ns['ind-as'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}MiscellaneousOtherNonoperatingIncome" %ns['ind-as'] else None
        pl['oie'].append(i.text) if i.tag == "{%s}LiabilitiesWrittenOff" %ns['ind-as'] else None

        pl['gie'].append(i.text) if i.tag == "{%s}FinanceCosts" %ns['ind-as'] else None

        pl['fixai'].append(i.text) if i.tag == "{%s}ImpairmentLossOnNonFinancialAssets" %ns['ind-as'] else None

        pl['finai'].append(i.text) if i.tag == "{%s}ImpairmentLossOnFinancialAssets" %ns['ind-as'] else None
        pl['exprov'].append(i.text) if i.tag == "{%s}NetProvisionsCharged" %ns['ind-as'] else None
        pl['oiai'].append(i.text) if i.tag == "{%s}LossOnDisposalOfIntangibleAssets" %ns['ind-as'] else None
        #pl['invgain'].append(i.text) if i.tag == "{%s}AdjustmentsToCarryingAmountsOfInvestments" %ns['ind-as'] else None

        #pl['oue'].append(i.text) if i.tag == "{%s}PriorPeriodItemsBeforeTax" %ns['ind-as'] else None
        #pl['oue'].append(i.text) if i.tag == "{%s}ExceptionalItemsBeforeTax" %ns['ind-as'] else None
        #pl['oue'].append(i.text) if i.tag == "{%s}ExtraordinaryItemsBeforeTax" %ns['ind-as'] else None
        pl['oue'].append(i.text) if i.tag == "{%s}DiscountIssueSharesDebenturesWrittenOff" %ns['ind-as'] else None
        #pl['oue'].append(i.text) if i.tag == "{%s}MiscellaneousExpenditureWrittenOff" %ns['ind-as'] else None
        pl['oue'].append(i.text) if i.tag == "{%s}LossOnDisposalDiscardDemolishmentAndDestructionOfDepreciablePropertyPlantAndEquipment" %ns['ind-as'] else None

        pl['taxcur'].append(i.text) if i.tag == "{%s}CurrentTax" %ns['ind-as'] else None
        pl['taxdef'].append(i.text) if i.tag == "{%s}DeferredTax" %ns['ind-as'] else None
        pl['ofta'].append(i.text) if i.tag == "{%s}ProfitLossFromDiscontinuedOperationsAfterTax" %ns['ind-as'] else None
        pl['mie'].append(i.text) if i.tag == "{%s}ProfitOrLossAttributableToNonControllingInterests" %ns['ind-as'] else None
        pl['dividend'].append(i.text) if i.tag == "{%s}DividendsPaidClassifiedAsFinancingActivities" %ns['ind-as'] else None
    for i in pl:
        pl[i] = sum([float(k) for k in pl[i]])
    return pl

bs_df = pd()
pl_df = pd()

for file in filelist:
    try:

        f = et.parse(file)
        s = f.getroot()
        ns = s.nsmap
        ns.pop('in-gaap') if "in-gaap" in ns and "ind-as" in ns else ns
        nm = s.find('.//in-ca:NameOfCompany',ns).text
        cin = s.find('.//in-ca:CorporateIdentityNumber',ns).text

        #Ascertain how many years_bs data is there in file and which year is highest by taking unique Current Assets
        all_y_bs = s.findall('.//in-gaap:CurrentAssets',ns) if 'in-gaap' in ns else s.findall('.//ind-as:CurrentAssets',ns)

        #from above current assets, took contextRef and found out the id of time. Then from datetime converted string into time - year
        years_bs = [dt.strptime(s.xpath('.//*[@id="%s"]' %i.get('contextRef'))[0].find('.//xbrli:period/xbrli:instant',ns).text,
                        "%Y-%m-%d").year for i in all_y_bs]
        # From numpy array converted list in array and sorted on index
        years2_bs = np(years_bs).argsort()

        #Ascertain how many years_pl data is there in file and which year is highest by taking unique Revenue from Operations
        all_y_pl = s.findall('.//in-gaap:RevenueFromOperations',ns) if 'in-gaap' in ns else s.findall('.//ind-as:RevenueFromOperations',ns)
        #from above revenue, took contextRef and found out the id of time. Then from datetime converted string into time - year
        years_pl = [dt.strptime(s.xpath('.//*[@id="%s"]' %i.get('contextRef'))[0].find('.//xbrli:period/xbrli:endDate',ns).text,
                        "%Y-%m-%d").year for i in all_y_pl]
        # From numpy array converted list in array and sorted on index
        years2_pl = np(years_pl).argsort()

        context = s.findall('./xbrli:context',ns)
        one1 , two1 , three1 = [], [], []
        one2 , two2 , three2 = [], [], []
        for i in context:
            if i.find('./xbrli:period/xbrli:instant',ns) is not None and str(years_pl[years2_pl[-1]]) in i.find('./xbrli:period/xbrli:instant',ns).text:
                one1.append(i) if len(i.findall('./xbrli:scenario/',ns)) == 1 else None
                two1.append(i) if len(i.findall('./xbrli:scenario/',ns)) == 2 else None
                three1.append(i) if len(i.findall('./xbrli:scenario/',ns)) == 3 else None
            elif i.find('./xbrli:period/xbrli:instant',ns) is not None and str(years_pl[years2_pl[-2]]) in i.find('./xbrli:period/xbrli:instant',ns).text:
                one2.append(i) if len(i.findall('./xbrli:scenario/',ns)) == 1 else None
                two2.append(i) if len(i.findall('./xbrli:scenario/',ns)) == 2 else None
                three2.append(i) if len(i.findall('./xbrli:scenario/',ns)) == 3 else None

        # If condition for taking two years_bs data or fail safe if there is only one year data
        if len(years_bs) >= 2:
            oneybs = s.xpath('.//*[@contextRef="%s"]' % all_y_bs[years2_bs[-1]].get('contextRef'))
            twoybs = s.xpath('.//*[@contextRef="%s"]' % all_y_bs[years2_bs[-2]].get('contextRef'))
            bs1 = balance_sheet_gaap(oneybs, one1) if 'in-gaap' in ns else balance_sheet_indas(oneybs, one1)
            bs2 = balance_sheet_gaap(twoybs, one2) if 'in-gaap' in ns else balance_sheet_indas(twoybs, one2)
            df1 = pd(bs1,index=[years_bs[years2_bs[-1]]]).T
            df2 = pd(bs2,index=[years_bs[years2_bs[-2]]]).T
            df3 = df2.join(df1)
        else:
            oneybs = s.xpath('.//*[@contextRef="%s"]' % all_y_bs[years2_bs[-1]].get('contextRef'))
            bs1 = balance_sheet_gaap(oneybs, one1) if 'in-gaap' in ns else balance_sheet_indas(oneybs, one1)
            df1 = pd(bs1,index=[years_bs[years2_bs[-1]]]).T

        # If condition for taking two years_pl data or fail safe if there is only one year data
        if len(years_pl) >= 2:
            oneypl = s.xpath('.//*[@contextRef="%s"]' % all_y_pl[years2_pl[-1]].get('contextRef'))
            twoypl = s.xpath('.//*[@contextRef="%s"]' % all_y_pl[years2_pl[-2]].get('contextRef'))
            pl1 = profit_loss_gaap(oneypl) if 'in-gaap' in ns else profit_loss_indas(oneypl)
            pl2 = profit_loss_gaap(twoypl) if 'in-gaap' in ns else profit_loss_indas(twoypl)
            df4 = pd(pl1,index=[years_pl[years2_pl[-1]]]).T
            df4.loc['co_name'] = nm
            df4.loc['cin'] = cin
            df5 = pd(pl2,index=[years_pl[years2_pl[-2]]]).T
            df5.loc['co_name'] = nm
            df5.loc['cin'] = cin
            df6 = df5.join(df4)
        else:
            oneypl = s.xpath('.//*[@contextRef="%s"]' % all_y_pl[years2_pl[-1]].get('contextRef'))
            pl1 = profit_loss_gaap(oneypl) if 'in-gaap' in ns else profit_loss_indas(oneypl)
            df4 = pd(pl1,index=[years_pl[years2_pl[-1]]]).T
            df4.loc['co_name'] = nm
            df4.loc['cin'] = cin

        pl_df = ct([pl_df,df6],axis=1) if len(years_pl) >=2 else ct([pl_df,df4],axis=1)
        bs_df = ct([bs_df,df3],axis=1) if len(years_bs) >=2 else ct([bs_df,df1],axis=1)
    except:
        print(file)
        pass


pl_df.loc['dna'] = pl_df.loc['dep'] + pl_df.loc['amort1'] + pl_df.loc['amort2']
pl_df.loc['cogida'] = pl_df.loc['cogs'] + pl_df.loc['dna']
pl_df.loc['gi'] = pl_df.loc['sale'] - pl_df.loc['cogida']
pl_df.loc['sgna'] = pl_df.loc['rnd'] + pl_df.loc['osga']
pl_df.loc['ebit'] = pl_df.loc['gi'] - pl_df.loc['sgna'] - pl_df.loc['ooe']
pl_df.loc['ebitda'] = pl_df.loc['ebit'] + pl_df.loc['dna']
pl_df.loc['noie'] = pl_df.loc['noii'] + pl_df.loc['eea'] + pl_df.loc['oie']
pl_df.loc['ie'] = pl_df.loc['gie']
pl_df.loc['ic'] = 0
pl_df.loc['imp'] = pl_df.loc['fixai'] + pl_df.loc['finai'] + pl_df.loc['oiai']
pl_df.loc['ue'] = pl_df.loc['imp'] + pl_df.loc['exprov'] + pl_df.loc['invgain'] + pl_df.loc['oue']
pl_df.loc['lce'] = 0
pl_df.loc['pi'] = pl_df.loc['ebit'] + pl_df.loc['noie'] - pl_df.loc['ie'] - pl_df.loc['ue']
pl_df.loc['tax'] = pl_df.loc['taxcur'] + pl_df.loc['taxdef']
pl_df.loc['tcf'] = 0
pl_df.loc['tdf'] = 0
pl_df.loc['itc'] = 0
pl_df.loc['cni'] = pl_df.loc['pi'] - pl_df.loc['tax'] + pl_df.loc['ofta']
pl_df.loc['pd'] = 0
pl_df.loc['ni'] = pl_df.loc['cni'] + pl_df.loc['mie']
pl_df.loc['nia'] = pl_df.loc['ni']
pl_df.loc[""] = ""

bs_df.loc["csti"] = bs_df.loc["co"] + bs_df.loc["tsti"]
bs_df.loc["arn"] = bs_df.loc["arg"] - bs_df.loc["bd"]
bs_df.loc["tar"] = bs_df.loc["arn"] + bs_df.loc["or"]
bs_df.loc["invt"] = bs_df.loc["inv"]
bs_df.loc["wip"] = 0
bs_df.loc["raw"] = 0
bs_df.loc["ppa"] = 0
bs_df.loc["oca"] = bs_df.loc["pe"] + bs_df.loc["mca"]
bs_df.loc["tca"] = bs_df.loc["csti"] + bs_df.loc["tar"] + bs_df.loc["invt"] + bs_df.loc["oca"]
bs_df.loc["ppe"] = bs_df.loc["oppe"]
bs_df.loc["ppeg"] = bs_df.loc["oppe"] + bs_df.loc["ad"]
bs_df.loc["oppe"] = bs_df.loc["ppeg"]
bs_df.loc["buil"] = 0
bs_df.loc["land"] = 0
bs_df.loc["mach"] = 0
bs_df.loc["cons"] = 0
bs_df.loc["lease"] = 0
bs_df.loc["cs"] = 0
bs_df.loc["lp"] = 0
bs_df.loc["tre"] = 0
bs_df.loc["abuil"] = 0
bs_df.loc["aland"] = 0
bs_df.loc["amach"] = 0
bs_df.loc["acons"] = 0
bs_df.loc["alease"] = 0
bs_df.loc["acs"] = 0
bs_df.loc["alp"] = 0
bs_df.loc["atre"] = 0
bs_df.loc["aoppe"] = bs_df.loc["ad"]
bs_df.loc["tia"] = bs_df.loc["ius"] + bs_df.loc["oi"]
bs_df.loc["ltnm"] = 0
bs_df.loc["ia"] = bs_df.loc["ng"] + bs_df.loc["noi"]
bs_df.loc["dc"] = 0
bs_df.loc["tgoa"] = bs_df.loc["dc"] + bs_df.loc["toa"]
bs_df.loc["tnca"] = bs_df.loc["ppe"] + bs_df.loc["tia"] + bs_df.loc["ltnm"] + bs_df.loc["ia"] + bs_df.loc["dta"] + bs_df.loc["tgoa"]
bs_df.loc["ta"] = bs_df.loc["tca"] + bs_df.loc["tnca"]
bs_df.loc["std"] = bs_df.loc["std"] + bs_df.loc["ltdm"]
bs_df.loc["ocl"] = bs_df.loc["dp"] + bs_df.loc["acp"] + bs_df.loc["mcl"]
bs_df.loc["tcl"] = bs_df.loc["std"] + bs_df.loc["ap"] + bs_df.loc["itp"] + bs_df.loc["ocl"]
bs_df.loc["ols"] = bs_df.loc["ol"] + bs_df.loc["di"]
bs_df.loc["untax"] = 0
bs_df.loc["tncl"] = bs_df.loc["ltd"] + bs_df.loc["pfrc"] + bs_df.loc["dtl"] + bs_df.loc["ols"]
bs_df.loc["tl"] = bs_df.loc["tncl"] + bs_df.loc["tcl"]
bs_df.loc["ner"] = 0
bs_df.loc["ps"] = 0
bs_df.loc["rps"] = 0
bs_df.loc["nrps"] = 0
bs_df.loc["esop"] = 0
bs_df.loc["esopg"] = 0
bs_df.loc["cet"] = bs_df.loc["csv"] + bs_df.loc["apic"] + bs_df.loc["re"] + bs_df.loc["ur"]
bs_df.loc["edg"] = 0
bs_df.loc["cta"] = 0
bs_df.loc["ugl"] = 0
bs_df.loc["rr"] = 0
bs_df.loc["oar"] = 0
bs_df.loc["tsc"] = 0
bs_df.loc["tse"] = bs_df.loc["cet"]
bs_df.loc["te"] = bs_df.loc["tse"] + bs_df.loc["ami"]
bs_df.loc["lset"] = bs_df.loc["te"] + bs_df.loc["tl"]

pl_df.index = pl_df.index.map({'cin': '0.CIN',
'co_name' : '0.Name',
'sale' : '1.Total Sales/Revenue',
'cogida' :'2.Cost of Goods Sold (COGS) incl D&A',
'cogs' :'3.COGS excluding D&A',
'dna' :'4.Depreciation & Amortization',
'dep' :'5.Depreciation',
'amort1' :'6.Amortization of Intangibles',
'amort2' :'7.Amortization of Deferred Charges',
'gi' :'8.Gross Income',
'sgna' :'9.Selling, General & Administrative Expense',
'rnd' :'10.Research & Development',
'osga' :'11.Other Selling, General & Administrative Expense',
'ooe' :'12.Other Operating Expense',
'ebitda' :'13.EBITDA (Operating Income)',
'ebit' :'14.EBIT (Operating Income)',
'noie' :'15.Non-Operating Income (Expense)',
'noii' :'16.Non-Operating Interest Income',
'eea' :'17.Equity in Earnings of Affiliates',
'oie' :'18.Other Income (Expense)',
'ie' :'19.Interest Expense',
'gie' :'20.Gross Interest Expense',
'ic' :'21.Interest Capitalized',
'ue' :'22.Unusual Expense',
'imp' :'23.Impairment',
'exprov' :'24.Exceptional Provisions',
'lce' :'25.Legal Claim Expense',
'oue' :'26.Other Unusual Expense',
'pi' :'27.Pretax Income',
'tax' :'28.Income Taxes',
'taxcur' :'29.Income Tax - Current - Domestic',
'tcf' :'30.Income Tax - Current - Foreign',
'taxdef' :'31.Income Tax - Deferred - Domestic (incl. local)',
'tdf' :'32.Income Tax - Deferred - Foreign',
'itc' :'33.Income Tax Credits',
'ofta' :'34.Other After Tax Adjustments',
'cni' :'35.Consolidated Net Income',
'pd' :'36.Preferred Dividends',
'ni' :'37.Net Income',
'mie' :'38.Minority Interest Expense',
'nia' :'39.Net Income Avail to Common - Basic',
'dividend' :'40.Common Dividend Paid (Cash Payment)',
"" : "41.Balance Sheet"})

bs_df.index = bs_df.index.map({'csti' : '1.Cash & Short Term Investments',
'co' : '2.Cash Only',
'tsti' : '3.Total Short Term Investments',
'tar' : '4.Total Accounts Receivable',
'arn' : '5.Accounts Receivables, Net',
'arg' : '6.Accounts Receivables, Gross',
'bd' : '7.Bad Debt / Doubtful Accounts',
'or' : '8.Other Receivables',
'invt' : '9.Inventories',
'inv' : '10.Inventories - Finished Goods',
'wip' : '11.Inventories - Work In Progress',
'raw' : '12.Inventories - Raw Materials',
'ppo' : '13.Inventories - Progress Payments & Other',
'oca' : '14.Other Current Assets',
'pe' : '15.Prepaid Expenses',
'mca' : '16.Miscellaneous Current Assets',
'tca' : '17.Total Current Assets',
'ppe' : '18.Net Property, Plant & Equipment',
'ppeg' : '19.Property, Plant, & Equipment - Gross',
'buil' : '20.Property, Plant, & Equipment - Buildings',
'land' : '21.Property, Plant, & Equipment - Land & Improvements',
'mach' : '22.Property, Plant, & Equipment - Machinery & Equipment',
'cons' : '23.Property, Plant, & Equipment - Construction in Progress',
'lease' : '24.Property, Plant, & Equipment - Leases',
'cs' : '25.Property, Plant, & Equipment - Computer Software and Equipment',
'lp' : '26.Property, Plant, & Equipment - Leased Property',
'tre' : '27.Property, Plant, & Equipment - Transportation Equipment',
'oppe' : '28.Other Property, Plant & Equipment',
'ad' : '29.Accumulated Depreciation',
'abuil' : '30.Accumulated Depreciation - Buildings',
'aland' : '31.Accumulated Depreciation - Land & Improvements',
'amach' : '32.Accumulated Depreciation - Machinery & Equipment',
'acons' : '33.Accumulated Depreciation - Construction in Progress',
'alease' : '34.Accumulated Depreciation - Leased Property',
'acs' : '35.Accumulated Depreciation - Computer Software and Equipment',
'alp' : '36.Accumulated Depreciation - Leases',
'atre' : '37.Accumulated Depreciation - Transportation Equipment',
'aoppe' : '38.Accumulated Depreciation - Other Property, Plant, & Equip',
'tia' : '39.Total Investments and Advances',
'ius' : '40.Investment in Unconsolidated Subs.',
'oi' : '41.Other Investments',
'ltnm' : '42.Long-Term Note Receivable',
'ia' : '43.Intangible Assets',
'ng' : '44.Net Goodwill',
'noi' : '45.Net Other Intangibles',
'dta' : '46.Deferred Tax Assets',
'tgoa' : '47.Tangible Other Assets',
'dc' : '48.Deferred Charges',
'toa' : '49.Tangible Other Assets',
'tnca' : '50.Total Non-Current Assets',
'ta' : '51.Total Assets',
'std' : '52.Short-Term Debt (incl. Current Portion of LTD)',
'ltdm' : '53.Long Term Debt Maturities',
'ap' : '54.Accounts Payable',
'itp' : '55.Income Tax Payable',
'ocl' : '56.Other Current Liabilities',
'dp' : '57.Dividends Payable',
'acp' : '58.Accrued Payroll',
'mcl' : '59.Miscellaneous Current Liabilities',
'tcl' : '60.Total Current Liabilities',
'ltd' : '61.Long Term Debt',
'pfrc' : '62.Provision for Risks & Charges',
'dtl' : '63.Deferred Tax Liabilities',
'ols' : '64.Other Liabilities',
'untax' : '65.Deferred Tax Liability-Untaxed Reserves',
'ol' : '66.Other Liabilities (excluding Deferred Revenue)',
'di' : '67.Deferred Income',
'tncl' : '68.Total Non-Current Liabilities',
'tl' : '69.Total Liabilities',
'ner' : '70.Non-Equity Reserves',
'ps' : '71.Preferred Stock - Carrying Value',
'rps' : '72.Redeemable Preferred Stock',
'nrps' : '73.Non Redeemable Preferred Stock',
'esop' : '74.Preferred Stock Issues for ESOP',
'esopg' : '75.ESOP Guarantees - Preferred Stock',
'cet' : '76.Common Equity (Total)',
'csv' : '77.Common Stock Par/Carry Value',
'apic' : '78.Additional Paid-In Capital / Capital Surplus (incl. Deferred Compensation)',
're' : '79.Retained Earnings',
'edg' : '80.ESOP Debt Guarantee',
'cta' : '81.Cumulative Translation Adjustment',
'ugl' : '82.Unrealized Gain/Loss Marketable Securities',
'rr' : '83.Revaluation Reserves',
'oar' : '84.Other Appropriated Reserves',
'ur' : '85.Unappropriated (Free) Reserves',
'tsc' : '86.Treasury Stock - Common (incl. ESOP)',
'tse' : "87.Total Shareholders' Equity",
'ami' : '88.Accumulated Minority Interest - Total',
'te' : '89.Total Equity',
'lset' : "90.Liabilities & Stockholders' Equity - Total"})

pl_df = pl_df.loc[pl_df.index.dropna()]
bs_df = bs_df.loc[bs_df.index.dropna()]

pl_df.reset_index(inplace=True)
bs_df.reset_index(inplace=True)
pl_df['serial'] = pl_df['index'].str.extract(r'(\d+)')
pl_df['serial'] = pl_df['serial'].map(int)
bs_df['serial'] = bs_df['index'].str.extract(r'(\d+)')
bs_df['serial'] = bs_df['serial'].map(int)
pl_df.sort_values(by=['serial'], inplace=True)
bs_df.sort_values(by=['serial'], inplace=True)

final = ct([pl_df, bs_df], axis=0, sort=False)

final.drop('serial',axis=1,inplace=True)
final.rename(columns={'index':'Particulars'},inplace=True)
final['Particulars'] = final['Particulars'].str.extract(r'\.(.*)')
final.set_index('Particulars',inplace=True)

for i in final.index:
    try:
        final.loc[i] = final.loc[i].apply(lambda x:float(x)/1000000)
    except:
        final.loc[i] = final.loc[i]

print(final)
final.to_csv('Financials.csv')