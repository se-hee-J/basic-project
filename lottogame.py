from random import sample

#당첨 번호 저장
winnum = set()

def buyautolotto():
    #정렬 돈 6개의 로또 번호 5개 조합 생성하기
    lotto = [] # 5개의 로또 번호 저장
    for i in range(5):
        num6 = set(sample(list(range(1,46)),6))
        lotto.append(num6)
    return lotto

def printnums(nums):
    for num in sorted(nums):
        print('%02d' % num, end= '')
    print()

def printlotto(lotto):
    #로또 복권 표와 같이 출력
    for i, item in enumerate(lotto):
        print('%c자동' % (ord('A')+i), end= '')
        printnums(item)
    print()

def setwinlotto():
    global winnum
    winnum = set(sample(list(range(1,46)),6))

def getwinner(lotto):
    #5개의 로또 번호에서 각각 당첨 번호 개수와 수를 출력
    for i, item in enumerate(lotto):
        print('%c' % (ord('A')+i),end= '')
        win = winnum.intersection(set(item)) #당첨 번호 구하기
        if win:
            wincnt = len(win)
            print('당첨 번호 개수 %d, '% wincnt, end= '')
            printnums(win)
        else:
            print('꽝')

lotto = buyautolotto() #로또 번호 표 구하기
printlotto(lotto) #로또 번호 출력
setwinlotto() #당첨 번호 선정
print('당첨 번호: ', end= '')
printnums(winnum) #당첨 번호 출력
print()
getwinner(lotto)