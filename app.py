# 스트림릿 라이브러리 사용하기 위한 임포트
import streamlit as st
from PIL import Image

# 웹 대시보드 개발 라이브러르 스트림릿은 main 함수가 있어야 한다 

def main():
    col1,col2 = st.columns([2,3])
    # 공간을 2:3 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성합니다.  

    with col1 :
    # column 1 에 담을 내용
        st.title('here is column1')
    with col2 :
    # column 2 에 담을 내용
        st.title('here is column2')
        st.checkbox('this is checkbox1 in col2 ')


    # with 구문 말고 다르게 사용 가능 
    col1.subheader(' i am column1  subheader !! ')
    col2.checkbox('this is checkbox2 in col2 ') 
    #=>위에 with col2: 안의 내용과 같은 기능을합니다


    #st.sidebar는 
    st.sidebar.title('this is sidebar')
    st.sidebar.checkbox('체크박스에 표시될 문구')
    # 사이드바에 체크박스, 버튼등 추가할 수 있습니다! 
    # 추가적으로 Expander, Container ,Empty가 있습니다

    

    #PIL 패키지에 이미지 모듈을 통해 이미지 열기 
    # Image.open('이미지 경로')
    img = 'https://github.com/user-attachments/assets/8ae84f11-c6e9-482e-b55a-3e01d4a283e6'
    logo_img = Image.open(img)

    col1,col2 = st.columns([2,3])

    with col1 :
    # column 1 에 담을 내용
        st.title('here is column1')
    with col2 :
    # column 2 에 담을 내용
        st.title('here is column2')
        st.checkbox('this is checkbox1 in col2 ')


    # 컬럼2에 불러온 사진 표시하기
    col2.image(logo_img)

    

if __name__ == '__main__':
    main()


    # st.title('vscode -> github ->streamlit')
    # st.header('데이타 전문가가 되자')
    # st.subheader('어여 나으세요')
    # st.success('겸둥이 동영이를 사랑해')
    # st.warning('술 마시면 경고')
    # st.info('오늘은 늦는다')
    # st.error('비가많이온다')
    # st.error('재미따 껄껄')
    # st.title('연결된건가')