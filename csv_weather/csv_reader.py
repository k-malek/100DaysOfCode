import csv

with open('weather_data.csv','r',encoding='utf-8') as csv_file:
    data = csv.reader(csv_file)
    headers=[]
    for i,row in enumerate(data):
        if i==0:
            headers=row
        else:
            str_row=''
            for j,header in enumerate(headers):
                str_row+=f'{header:^5s}: {row[j]:^11s}'
                if j!=len(headers)-1:
                    str_row+=' | '
            print(str_row)