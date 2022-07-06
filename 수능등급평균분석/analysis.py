import pandas as pd
from matplotlib import pyplot as plt

what_subject = input('과목명: ')
rating_value = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}

for year in range(2017,2022):
    df = pd.read_csv(f'.\수능등급평균분석\csv_file\{year}data.csv', encoding='EUC-KR')
    subject_df = df[df['과목']==what_subject]

    for rating in range(1,9):
        grade = subject_df[subject_df.등급 == rating].values.tolist()[0][2] # [0] 은 dataframe이 2차원 배열 이기에 작성
        rating_value[rating].append(int(grade))


average_value = {}
for num in range(1, 9):
    average_value[num] = round(sum(rating_value[num])/5, 2) # 소수 2째 자리수 까지 나타냄

graph_type = input('1. 등급의 변화, 2. 평균 등급')

if graph_type == 1:
    x = [year for year in range(2017,2022)]
    for rating in range(1,9):
        y = rating_value[rating]
        plt.plot(x, y)
    plt.show()
        
