# 문자열
- 문자열
- 패턴 매칭
- 문자열 암호화
- 문자열 압축

### 문자의 표현

#### 발전과정
1. 지역마다의 코드
2. ASCII
3. Unicode

#### 유니코드 인코딩(UTF)
- Unicode를 보여주는 방법
- 파이썬의 경우 UTF-8은 기본적으로 생략 가능
  - UTF-8을 제일 많이 사용, 바이트로 효율적으로 쓰기 좋음
  - -> ASCII가 8bit기 때문에 잘 맞음.
  - ord, chr은 유니코드를 가져다 쓰는 것
    - 하지만 UTF-8이기 때문에 ASCII랑 같게 느낌
- UTF-'8' : 8bit로 표현하겠다.

### python에서의 문자열 처리
#### 문자열
- container > sequence > immutable > iterable
- indexing, **slicing**
- method

#### 문자열 뒤집기
1. 반복문
2. reverse
3. **슬라이싱**

```python
# 1. 반복문을 이용한 문자열 뒤집기

string = 'Hello Algorithm'
reversed_string = ''

for i in range(len(string) - 1, -1, -1):  # 맨 뒤에서부터 시작하여 처음까지
    reversed_string += string[i]

print(reversed_string)


# 2. list()와 .reverse()를 이용한 문자열 뒤집기

string = 'Hello Algorithm'

string_list = list(string)
string_list.reverse()

reversed_string = ''.join(string_list)

print(reversed_string)


# 3. 슬라이싱을 이용한 문자열 뒤집기

string = 'Hello Algorithm'
reversed_string = string[::-1]

print(reversed_string)
```

#### 문자열 숫자를 정수로 변환하기
- atoi : ascii to int
- itoa : int to ascii
- 예시 식이 중요하다기 보단 방식을 다른 곳에 쓸 수 있다는 걸 알면 됨

```python
# 1. ascii to int (문자열을 정수로 변환)

def atoi(number):
    int_number = 0

    for char in number:
        int_number *= 10
        int_number += ord(char) - ord('0')  #<- 기준점 빼는게 중요함!

    return int_number


result = atoi('123')
print(type(result))
print(result)

# 2. int to ascii (정수를 문자열로 변환)

def itoa(number):
    if number == 0:
        return '0'

    is_positive = True  # 음수처리
    if number < 0:
        is_positive = False
        number = -number

    str_number = ''
    while number > 0:
        number, remainder = number // 10, number % 10  # divmod(number, 10)
        str_number = chr(ord('0') + remainder) + str_number  # 기준점 chr(ord('0'))

    if not is_positive:
        str_number = '-' + str_number

    return str_number


result = itoa(123)
print(type(result))
print(result)
```

#### 