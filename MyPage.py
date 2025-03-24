import streamlit as st
from PIL import Image
import json
import os

from xhs.utils import generate_xiaohongshu

# 设置页面配置
st.set_page_config(page_title="个人介绍 - Yao Ning", page_icon="👨‍💻", layout="wide")

# 加载语言文件
def load_language_file(lang):
    file_path = f"i18n/{lang}.json"
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# 创建右上角语言选择器
_, _, last_column = st.columns([6, 6, 2])
with last_column:
    languages = {"zh": "中文", "ja": "日本語"}
    language = st.selectbox("", list(languages.keys()), format_func=lambda x: languages[x])

# 加载选定语言的内容
info = load_language_file(language)

# 侧边栏工具选择
st.sidebar.markdown("### 🛠️ " + info["tools"]["title"])
tool_selection = st.sidebar.radio("", 
    [tool["name"] for tool in info["tools"]["categories"].values()],
    label_visibility="collapsed"
)

# 创建主页面标签页
if tool_selection == info["tools"]["categories"]["mypage"]["name"]:
    # 显示个人介绍内容
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

elif tool_selection == info["tools"]["categories"]["xhs"]["name"]:
    # 小红书生成器
    st.title("📱 小红书文案生成器")
    st.header("爆款小红书AI写作助手 ✏️")
    st.markdown("本页面仅支持中文")

    openai_api_key = st.text_input("请输入OpenAI API密钥：", type="password")
    # st.markdown("[获取OpenAI API密钥](https://platform.openai.com/account/api-keys)")

    theme = st.text_input("主题")
    submit = st.button("开始写作")

    if submit and not openai_api_key:
        st.info("请输入你的OpenAI API密钥")
        st.stop()
    if submit and not theme:
        st.info("请输入生成内容的主题")
        st.stop()
    if submit:
        with st.spinner("AI正在努力创作中，请稍等..."):
            result = generate_xiaohongshu(theme, openai_api_key)
        st.divider()
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown("##### 小红书标题1")
            st.write(result.titles[0])
            st.markdown("##### 小红书标题2")
            st.write(result.titles[1])
            st.markdown("##### 小红书标题3")
            st.write(result.titles[2])
            st.markdown("##### 小红书标题4")
            st.write(result.titles[3])
            st.markdown("##### 小红书标题5")
            st.write(result.titles[4])
        with right_column:
            st.markdown("##### 小红书正文")
            st.write(result.content)


# elif tool_selection == info["tools"]["categories"]["email"]["name"]:
    # 邮件助手
    # st.title("✉️ 邮件助手")
    # 邮件助手相关代码

# elif tool_selection == info["tools"]["categories"]["translator"]["name"]:
    # 多语言翻译器
    # st.title("🌐 多语言翻译器")
    # 翻译器相关代码



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