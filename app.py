# 스트림릿 라이브러리 사용하기 위한 임포트
import streamlit as st

# 웹 대시보드 개발 라이브러르 스트림릿은 main 함수가 있어야 한다 

def main():
    st.title('내한제분')
    st.title('내가 한번 해보는 제조 데이터 분석')
    st.header('이 영역은 헤더 영역')
    st.subheader('서브헤더 영역')
    st.success('작업이 성공했을때 사용')
    st.warning('경고 문구 보여주고 싶을때 사용')
    st.info('정보를 보여주고 싶을때 사용')
    st.error('문제가 발생했을때 사용')
    st.error('무엇이 문제인지 모르겠다')

    st.help(sum)
    st.help(len)

if __name__ == '__main__':
    main()


