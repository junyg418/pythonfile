word_list = {'':''}

word_1 = input('처음 시작 단어를 입력해주세요.\n>>')
word_list[1] = word_1
i=2
while True:
    word_list[i] = input('{}로 시작하는 단어를 입력해주세요.\n>>'.format(word_list[i-1][-1]))
    if word_list[i-1][-1] == word_list[i][0]:
        i += 1
    else:
        print('잘못 입력하셨습니다.')