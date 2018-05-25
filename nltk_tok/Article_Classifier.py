import os
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import operator
from article_data_preprocessor_util import word_count, hit_count
import docx
import pandas as pd

real_estate_keywords = ['house', 'propert', 'properti','property','home', 'mortgag', 'mortgage','estate', 'estat']
retail_keywords = ['retail', 'retai', 'shop', 'amazon' , 'sale', 'supermarket' , 'groceri']
energy_keywords = ['oil','commod', 'gas', 'shale', 'shal', 'solar', 'e-car', 'e-vehicle', 'middle east', 'opec', 'shell', 'bp', 'chevron', 'barrel','energy', 'energi']

xcel = pd.read_excel('C:\\Users\\kartikaya\\Python_Data\\Article_Search_MindTrust\\FUNDS\\Funds-sectors.xlsx')
funds = xcel.iloc[:, 0]
tags = xcel.iloc[:, 1]
isin = xcel.iloc[:, 2]
all_files = os.listdir("C:\\Users\\kartikaya\\Python_Data\\Article_Search_MindTrust\\Articles")    

article_links = {'Are property prices about to feel the chill-Emma-Lou Montgomery.docx' : 'https://www.fidelity.co.uk/markets-insights/daily-insight/property-prices-about-to-feel-the-chill' ,
                 'BlackRock World Mining Trust plc.docx' : 'https://www.fidelity.co.uk/markets-insights/fund-focus/blackrock-world-mining',
                 'Does commercial property still make the grade.docx' : 'https://www.fidelity.co.uk/markets-insights/investors-view/does-commercial-property-still-make-the-grade',
                 'Feast or famine in the retail sector - Emma-Lou Montgomery.docx':'https://www.fidelity.co.uk/markets-insights/daily-insight/feast-or-famine-morrisons',
                 'Four bubbles that are nearest to bursting point - Tom Stevenson.docx' : 'https://www.fidelity.co.uk/markets-insights/viewpoints/four-bubbles',
                 'Get set to put a foot on the property ladder in 2017.docx' : 'https://www.fidelity.co.uk/markets-insights/financial-planning/put-a-foot-on-the-property-ladder',
                 'How to build bricks and mortar into your ISA.docx':'https://www.fidelity.co.uk/markets-insights/financial-planning/how-to-build-bricks-and-mortar',
                 'How to invest in renewable energy.docx' : 'https://www.ig.com/uk/investments/news/investing/2017/09/11/how-to-invest-in-renewable-energy-39764',
                 'Is it too late to invest in commodities.docx' : 'https://www.fidelity.co.uk/markets-insights/investors-view/is-it-too-late',
                 'More change at the tills for UK retailers - Graham Smith.docx' : 'https://www.fidelity.co.uk/markets-insights/investors-view/more-change-at-the-tills',
                 'Opportunities in technology-Aditya Khowala.docx' : 'https://www.fidelity.co.uk/markets-insights/viewpoints/opportunities-in-technology',
                 'Retail disruption-Tom Stevenson.docx' : 'https://www.fidelity.co.uk/markets-insights/viewpoints/retail-disruption',
                 'Retailers floored by new spending pattern - Emma-Lou Montgomery.docx' : 'https://www.fidelity.co.uk/markets-insights/daily-insight/retailers-floored-by-spending-pattern',
                 'Shopping centre owners circle the wagons.docx' : 'https://www.fidelity.co.uk/markets-insights/daily-insight/shopping-centre-owners',
                 'Surprise! House prices rise-Emma-Lou Montgomery.docx' : 'https://www.fidelity.co.uk/markets-insights/daily-insight/surprise-house-prices-rise',
                 'The problem with London property.docx' : 'https://www.fidelity.co.uk/markets-insights/daily-insight/the-problem-with-london-property',
                 'UK property market equipped for a storm - Graham Smith.docx' : 'https://www.fidelity.co.uk/markets-insights/investors-view/uk-property-market-equipped-for-a-storm',
                 'What does 2017 hold for the UK real estate investment market.docx' : 'http://www.propertyreporter.co.uk/property/what-does-2017-hold-for-the-uk-real-estate-investment-market.html',
                 'What does a higher oil price mean for investors.docx' : 'https://www.fidelity.co.uk/markets-insights/viewpoints/what-does-a-higher-oil-price-mean-for-investors',
                 'Where next for oil.docx' : 'https://www.fidelity.co.uk/markets-insights/investors-view/where-next-for-oil',
                 'Which way for house prices.docx' : 'https://www.fidelity.co.uk/markets-insights/daily-insight/which-way-for-house-prices',
                 'You win, you lose - especially when it comes to oil.docx' : 'https://www.fidelity.co.uk/markets-insights/viewpoints/you-win-you-lose',
                 'Government sets out plans to upgrade UK energy infrastructure and increase clean energy investment.docx' : 'https://www.gov.uk/government/news/government-sets-out-plans-to-upgrade-uk-energy-infrastructure-and-increase-clean-energy-investment',
                 'Investing in Property Mutual Funds or Investment Trusts.docx' : 'http://www.morningstar.co.uk/uk/news/110230/investing-in-property-mutual-funds-or-investment-trusts.aspx',
                 'Is this the time for commodities.docx' : 'https://www.fidelity.co.uk/markets-insights/investors-view/is-this-the-time-for-commodities'}
print('Intelli - Insights')
more = 'yes'
while more == 'yes' or more == 'Yes':
    i = 1
    print('\n \n------------------------------------------------------------')
    print('------------------------------------------------------------')
    print('Please select a fund')
    for fund in funds:
        print(str(i)+" - "+str(fund))
        i = i + 1
    fund = input(" ")
    fund = fund.strip()
    index = int(fund) - 1
    fund = funds[index]
    print('You selected : '+fund)
    fund_tags = tags[index]
    fund_isin = isin[index]

    ps = PorterStemmer()
    j = 0
    article_list = []
    for article in all_files:
        file = 'C:\\Users\\kartikaya\\Python_Data\\Article_Search_MindTrust\\Articles\\' + all_files[j]
        j = j + 1
        doc = docx.Document(file)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
            '\n'.join(full_text)
        article_cleaned = ''
        for text in full_text:
            text = re.sub('[^a-zA-Z]',' ',text)
            article_cleaned = article_cleaned + text
        article_cleaned = article_cleaned.lower()
        article_cleaned = article_cleaned.split()
        article_cleaned = [ps.stem(word) for word in article_cleaned if not word in set(stopwords.words('english'))]
        article_cleaned = ' '.join(article_cleaned)
        count = word_count(article_cleaned)
        sorted_x = sorted(count.items(), key=operator.itemgetter(1), reverse = True)
        real_estate_hits = hit_count(sorted_x, real_estate_keywords)
        retail_hits  = hit_count(sorted_x , retail_keywords)
        energy_hits = hit_count(sorted_x, energy_keywords)
        if fund_tags == 'energy' and energy_hits > 10:
            article_list.append(article)
        if fund_tags == 'real_estate' and real_estate_hits > 10:
            article_list.append(article)
    i=1
    print('Relevant Articles : ')
    for article in article_list:
        print(str(i) + '-> '+ article_links[article])
        i = i + 1
    print('------------------------------------------------------------')
    print('------------------------------------------------------------')
    more = input('more insights ? yes/no : ')
