import streamlit as st
import math

# --- 웹페이지 기본 설정 ---
st.set_page_config(page_title="공비수열 계산기", layout="centered")

st.title("공비수열 (등비수열) 계산기")
st.markdown("초항과 공비를 입력하여 공비수열을 계산하고 과정을 확인하세요.")

# --- 사용자 입력 (사이드바) ---
st.sidebar.header("입력 값")

# 사용자로부터 raw 입력값을 받습니다.
raw_first_term = st.sidebar.number_input("초항 (a₁)", value=1.0, step=0.1)
raw_common_ratio = st.sidebar.number_input("공비 (r)", value=2.0, step=0.1)

# --- 수정된 부분: 입력값을 소수점 셋째자리에서 반올림합니다. ---
# 이로써 입력값 표시 오류를 해결합니다.
first_term = round(raw_first_term, 3)
common_ratio = round(raw_common_ratio, 3)

# 계산을 실행할 버튼
calculate_button = st.sidebar.button("수열 계산 시작")

# --- 계산 및 결과 출력 ---
if calculate_button:
    st.header("계산 결과")
    
    # 공비수열 공식 표시 (반올림된 입력값 사용)
    st.subheader("공비수열 공식")
    st.latex(r"a_n = a_1 \cdot r^{(n-1)}")
    st.latex(f"a_n = {first_term} \\cdot {common_ratio}^{{(n-1)}}")
    
    st.markdown("---")
    
    st.subheader("계산 과정 (첫 5항)")
    
    terms = []
    num_terms_to_display = 5 
    
    # 공비수열 계산 및 과정 출력
    for n in range(1, num_terms_to_display + 1):
        
        # 공비수열 공식 적용 (반올림된 입력값 사용)
        term_value = first_term * (common_ratio ** (n - 1))
        
        # 계산된 결과는 소수점 6자리까지 반올림하여 표시 오차를 줄입니다.
        term_value_rounded = round(term_value, 6)
        terms.append(term_value_rounded)
        
        # 계산 과정 상세 출력
        st.write(f"**n = {n}번째 항 계산:**")
        
        # 공비가 음수일 경우 괄호로 표시하여 시각적 명확성을 높입니다.
        ratio_display = f"({common_ratio})" if common_ratio < 0 else f"{common_ratio}"

        if n == 1:
            # 초항 (반올림된 입력값)을 표시합니다.
            st.info(f"  a₁ = {first_term}")
        else:
            # 나머지 항의 계산 과정을 표시합니다.
            st.info(f"  a_{n} = {first_term} * {ratio_display}^{{{n-1}}} = {term_value_rounded}")
        
        st.markdown("---")

    # 최종 결과 요약
    st.success("✅ 공비수열 계산이 완료되었습니다.")
    st.write(f"**계산된 공비수열 (첫 {num_terms_to_display}항):**")
    st.code(f"{terms}")

    # --- 요청하신 최종 메시지 (HTML 스타일링으로 크게 표시) ---
    st.markdown("<h1 style='text-align: center; color: red; font-size: 40px; margin-top: 50px;'>이것도 계산 못하냐 ㅋㅋ</h1>", unsafe_allow_html=True)
