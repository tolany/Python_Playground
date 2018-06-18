# 스크립트 목적 : 엑셀형식으로 된 파일에서 자료를 가져오는 스크립트 
# 데이터 형식 : excel 
# 데이터 내용 : UNICEF 아동노동, 아동혼인 데이터

import xlrd
databook = xlrd.open_workbook("SOWC 2014 Stat Tables_Table 9.xlsx")

sheet = databook.sheet_by_name("Table 9 ")

data = {}
for i in xrange(14, sheet.nrows):

    # 14열부터 국가 데이터가 시작하기 때문에 14열부터 시작함. 
    row = sheet.row_values(i)

    country = row[1]

    data[country] = {
        'child_labor': {
            'total': [row[4], row[5]],
            'male': [row[6], row[7]],
            'female': [row[8], row[9]],
        },
        'child_marriage': {
            'married_by_15': [row[10], row[11]],
            'married_by_18': [row[12], row[13]],
        }
    }

    if country == "Zimbabwe":
        break

import pprint
pprint.pprint(data)
