def callFunc(*args):
    print(type(args)) #<class 'tuple'>
    result = 0
    #가변 인자 합 구하기
    for i in args:
        result += i
    return result

res = callFunc(10,20,30)
print(res)

def callFunc2(**kwargs):
    print(type(kwargs)) #<class 'dict'>
    tot = 0
    #키워드 인자 합 구하기
    for k in kwargs.keys():
        tot += kwargs[k]
        print(f'{1} = {kwargs[k]}')
    return (tot, tot/len(kwargs))

tot, avg = callFunc2(apple=10, banana=15, blueberry=20)
print(f'합계 = {tot}, 평균 = {avg :.2f}')

grade = {
    'apple' : 11,
    'banana' : 16,
    'blueberry' : 21
}

tot, avg = callFunc2(**grade)
print(f'합계 = {tot}, 평균 = {avg : 2f}')