# 스트림릿 라이브러리 사용하기 위한 임포트
import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# 웹 대시보드 개발 라이브러르 스트림릿은 main 함수가 있어야 한다 

def main():
    col1,col2 = st.columns([2,3])
    # 공간을 2:3 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성합니다.  

    with col1 :
    # column 1 에 담을 내용
        st.title('분할섹션 1')
    with col2 :
    # column 2 에 담을 내용
        st.title('분할섹션 2')
        st.checkbox('분할섹션2의 체크박스1')


    # with 구문 말고 다르게 사용 가능 
    col1.subheader('작은제목! ')
    col2.checkbox('분할섹션2의 체크박스2') 
    #=>위에 with col2: 안의 내용과 같은 기능을합니다


    #st.sidebar는 
    st.sidebar.title('사이드바 제목')
    st.sidebar.checkbox('사이드바의 체크박스 1')
    # 사이드바에 체크박스, 버튼등 추가할 수 있습니다! 
    # 추가적으로 Expander, Container ,Empty가 있습니다

    

    #PIL 패키지에 이미지 모듈을 통해 이미지 열기 
    # Image.open('이미지 경로')
    #logo_img = Image.open('https://github.com/millim1983/bigdata_mr/moldiv_familychair.png')
    st.title("GitHub 이미지 표시 예제")

    # GitHub 리포지토리의 이미지 URL
    url = "https://github.com/user-attachments/assets/57728188-0a49-4204-84dd-0c393d533a7e"


    # try:
    #     # 이미지 URL로부터 이미지 데이터 가져오기
    #     response = requests.get(url)
    #     response.raise_for_status()  # HTTP 오류가 발생하면 예외 발생

    #     # 이미지 데이터를 PIL 이미지로 변환
    #     image = Image.open(BytesIO(response.content))

    #     # Streamlit 앱에서 이미지 표시
    #     st.image(image, caption="GitHub에서 불러온 이미지")

    # except requests.exceptions.RequestException as e:
    #     # HTTP 요청 중 오류가 발생한 경우
    #     st.error(f"이미지를 불러오는 중 오류가 발생했습니다: {e}")
    # #image = image.resize((128, 128), resampling=Image.LANCZOS)
    image = Image.open(url)
    st.image(image)

    # # 컬럼2에 불러온 사진 표시하기
    # col2.image(logo_img)

    

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