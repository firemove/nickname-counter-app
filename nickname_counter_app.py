
import streamlit as st
from PIL import Image
import pytesseract
import re
from collections import Counter
import pandas as pd

st.title("닉네임 등장 횟수 분석기")
st.write("이미지를 업로드하면 닉네임(`***`이 포함된)을 추출하여 횟수를 계산해줍니다.")

uploaded_file = st.file_uploader("이미지를 업로드하세요", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="업로드된 이미지", use_column_width=True)

    text = pytesseract.image_to_string(image, lang="kor+eng")

    # 닉네임 추출
    pattern = re.compile(r'[가-힣a-zA-Z0-9"’‘♡()]+[*]{3}[^,\n\s]*')
    nicknames = pattern.findall(text)

    if nicknames:
        st.subheader("닉네임 목록 및 등장 횟수")
        nickname_counts = Counter(nicknames)
        df = pd.DataFrame(sorted(nickname_counts.items()), columns=["닉네임", "등장 횟수"])
        st.dataframe(df)
    else:
        st.warning("닉네임을 찾을 수 없습니다.")
