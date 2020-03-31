'''
lambda : 단일문으로 표현되는 익명 함수
'''

def edit_story(words, func):
    for word in words:
        print(func(word))

stairs = ['thud', 'meow', 'hiss']
edit_story(stairs, lambda word: word.capitalize() + '!')