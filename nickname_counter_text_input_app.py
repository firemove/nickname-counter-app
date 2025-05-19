
import streamlit as st
import re
from collections import Counter
import pandas as pd

st.title("닉네임 등장 횟수 분석기 (텍스트 입력용)")
st.write("닉네임 텍스트를 입력하면 `***`이 포함된 닉네임만 추출하여 등장 횟수를 세어줍니다.")

sample = '"청***탕.", "이***미", "부자***34", "쭈야***마♡", "이선***16"'
text_input = st.text_area("닉네임 텍스트 입력 (예:)", value=sample, height=200)

if st.button("분석하기"):
    pattern = re.compile(r'[가-힣a-zA-Z0-9"’‘♡()]+[*]{3}[^,\n\s]*')
    nicknames = pattern.findall(text_input)

    if nicknames:
        nickname_counts = Counter(nicknames)
        df = pd.DataFrame(sorted(nickname_counts.items()), columns=["닉네임", "등장 횟수"])
        st.success(f"{len(nicknames)}개의 닉네임을 추출했습니다.")
        st.dataframe(df)
    else:
        st.warning("닉네임을 찾을 수 없습니다. `***`이 포함된 항목만 인식됩니다.")
