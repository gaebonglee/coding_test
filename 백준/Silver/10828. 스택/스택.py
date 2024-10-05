import sys

number = int(input())

stack = []
def push(x):
    stack.append(x)

def pop():
    if not empty():
        return stack.pop()
    else:
        return -1

def size():
    return len(stack)

def empty():
    return 1 if len(stack) == 0 else 0

def top():
    if not empty():
        return stack[-1]
    else:
        return -1

for _ in range(number):
    command = sys.stdin.readline().split()  # 명령어와 숫자(있을 경우) 입력받기
    
    if command[0] == "push":
        push(int(command[1]))  # 숫자와 함께 push 실행
    elif command[0] == "pop":
        print(pop())  # pop 결과 출력
    elif command[0] == "size":
        print(size())  # size 결과 출력
    elif command[0] == "empty":
        print(empty())  # empty 결과 출력
    elif command[0] == "top":
        print(top())  # top 결과 출력