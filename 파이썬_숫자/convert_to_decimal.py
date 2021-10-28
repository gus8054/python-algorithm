# * 다른 진법의 숫자를 10진수로 전환한다.(2 <= base <= 10)

def convert_to_decimal(number, base):
    multiplier, result = 1, 0
    while number > 0:
        result += number % 10 * multiplier
        multiplier *= base
        number = number // 10
    return result

def test_convert_to_decimal():
    number, base = 1001, 2
    assert convert_to_decimal(number, base) == 9, "다른 결과가 나옴"
    print("테스트 통과")

if __name__ == "__main__":
    test_convert_to_decimal()