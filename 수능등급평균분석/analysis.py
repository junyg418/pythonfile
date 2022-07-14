import pandas as pd
from matplotlib import pyplot as plt

what_subject = input('과목명: ')
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['figure.figsize'] = (10,7)
rating_value = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}

for year in range(2017,2022):
    df = pd.read_csv(f'.\수능등급평균분석\csv_file\{year}data.csv', encoding='EUC-KR')
    subject_df = df[df['과목'].str.replace(' ', '')==what_subject]
    for rating in range(1,9):
        grade_list = subject_df[subject_df.등급 == rating].values.tolist()
        grade = grade_list[0][2] # [0] 은 dataframe이 2차원 배열 이기에 작성
        print(grade)
        rating_value[rating].append(int(grade))
        


average_value = []
for num in range(1, 9):
    average_value.append(round(sum(rating_value[num])/5, 2)) # 소수 2째 자리수 까지 나타냄

plt.subplot(2,1,1)
plt.title(what_subject)
x = [year for year in range(2017,2022)]
for rating in range(1,9):
    y = rating_value[rating]
    plt.plot(x, y, 'rs--', label =f'{rating}등급')
plt.xlabel('연도')						#x축 이름 
plt.ylabel('점수')	               #y축 이름

plt.subplot(2,1,2)
x = [f'{i}등급' for i in range(1,9)]
y = average_value
plt.bar(x,y)

plt.show()