import math

def calculate_lcm(a, b):
    """
    두 수의 최소공배수 (LCM)를 계산합니다.
    LCM(a, b) = (|a * b|) / GCD(a, b)
    """
    # math.gcd() 함수를 사용하여 최대공약수(GCD)를 구합니다.
    gcd = math.gcd(a, b)
    # 최소공배수를 계산합니다.
    # // 연산자는 정수 나눗셈을 수행하여 정확한 정수 결과를 얻습니다.
    lcm = (a * b) // gcd
    return lcm

def main():
    print("두 수의 공배수를 계산하고 공배수열 공식을 알려드립니다.")
    
    try:
        # 사용자로부터 두 수를 입력받습니다.
        num1 = int(input("첫 번째 양의 정수를 입력하세요: "))
        num2 = int(input("두 번째 양의 정수를 입력하세요: "))

        # 양의 정수 확인
        if num1 <= 0 or num2 <= 0:
            print("두 수는 반드시 양의 정수여야 합니다.")
            return

        # 최소공배수 계산
        lcm = calculate_lcm(num1, num2)
        
        print("\n--- 결과 ---")
        print(f"입력한 두 수 ({num1}과 {num2})의 최소공배수 (LCM)는 {lcm}입니다.")
        
        # 몇 가지 공배수 출력 (LCM의 배수들)
        print("\n몇 가지 공배수 (최소공배수의 배수):")
        for i in range(1, 6): # 첫 5개의 공배수를 보여줍니다.
            common_multiple = lcm * i
            print(f"{i}번째 공배수: {common_multiple}")
            
        print("\n--- 공배수열 공식 ---")
        print("두 수의 공배수는 최소공배수 (LCM)의 배수들로 이루어진 **수열**입니다.")
        
        # 공배수열 공식 설명
        print(f"공배수열은 다음과 같은 **공식**으로 나타낼 수 있습니다:")
        print(f"공배수_n = 최소공배수 * n")
        print(f" (단, n은 1, 2, 3, ... 인 자연수)")
        
        print(f"\n예시: ({num1}과 {num2}의 최소공배수는 {lcm}이므로)")
        print(f"  n=1일 때: {lcm} * 1 = {lcm}")
        print(f"  n=2일 때: {lcm} * 2 = {lcm * 2}")
        print(f"  n=3일 때: {lcm} * 3 = {lcm * 3}")
        
        print(f"\n이 수열은 최소공배수({lcm})를 첫 항으로 하고, 최소공배수({lcm})를 공차로 하는 등차수열의 형태를 가집니다.")

    except ValueError:
        print("입력이 올바르지 않습니다. 정수만 입력해주세요.")

# 스크립트 실행
if __name__ == "__main__":
    main()
