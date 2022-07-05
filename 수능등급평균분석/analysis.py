import pandas as pd

what_subject = input('과목명: ')
for year in range(2017,2022):
    df = pd.read_csv(f'.\csv_file\{year}data.csv', encoding='EUC-KR')
    