import streamlit as st
from PIL import Image
import json
import os

# 设置页面标题和图标
st.set_page_config(page_title="个人介绍 - Yao Ning", page_icon="👨‍💻")

# 加载语言文件
def load_language_file(lang):
    file_path = f"i18n/{lang}.json"
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# 语言选项
languages = {"zh": "中文", "ja": "日本語"}
language = st.sidebar.selectbox("选择语言 / 言語を選択", list(languages.keys()), index=1, format_func=lambda x: languages[x])

# 加载选定语言的内容
info = load_language_file(language)

# 个人头像
image_url = "img/my_pic.PNG"
st.image(image_url, width=150)

# 个人信息展示
st.title(info["title"])
st.subheader(info["role"])

# 显示描述部分
for section in info["description"]:
    if section == "intro":
        for item in info["description"]["intro"]:
            st.markdown(item)
    else:
        st.markdown(f"### {info['description'][section]['title']}")
        for item in info["description"][section]["items"]:
            st.markdown(f"- {item}")

# 技能展示
st.write(info["skills"]["title"])
columns = st.columns(3)
skills_all = []
for category in info["skills"]["categories"].values():
    skills_all.extend(category)
for i, skill in enumerate(skills_all):
    columns[i % 3].button(skill)

# 联系方式
st.write(info["contact"])
st.markdown(
    f"""
    - {info["email"]}
    - {info["linkedin"]}
    - {info["company"]}
    """
)

st.success(info["welcome"])