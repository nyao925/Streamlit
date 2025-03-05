# import streamlit as st
# from PIL import Image

# # 设置页面标题和图标（必须放在第一行）
# st.set_page_config(page_title="个人介绍 - Yao Ning", page_icon="👨‍💻")

# # 语言选项
# languages = {"zh": "中文", "ja": "日本語"}
# language = st.sidebar.selectbox("选择语言 / 言語を選択", list(languages.keys()), index=1, format_func=lambda x: languages[x])

# # 个人信息（多语言支持）
# info = {
#     "zh": {
#         "title": "个人介绍 - Yao Ning",
#         "role": "技术顾问 | AI & 云计算专家",
#         "description": """
#         - 💼 目前在 **DXC Japan** 担任 Associate Manager
#         - 🎯 负责 **ServiceNow** 产品的技术咨询与开发，并领导 6 人开发团队
#         - 🤖 在公司内开发 **DXCJ Chat AI 助手**，提供会议纪要自动生成、邮件回复自动化等功能
#         - 💻 擅长 **Azure、Power Platform、Oracle APEX、Python、Java、JavaScript**
#         - 🚀 过往经验包括 **Microsoft Japan、IBM Japan、FITEC**，专注于云计算与 AI 解决方案
        
#         ### 履历
#         - **2022年12月 - 现在** 日本微软 - 负责PowerPlatform技术支持、讲师和技术支援
#         - **2021年10月 - 2022年11月** 日本IBM - 负责EI-Core的开发，担任开发团队的副负责人
#         - **2017年4月 - 2021年9月** FITEC - 负责AI、云计算及工厂自动化系统开发，曾担任多个项目的副负责人
        
#         ### 项目经历
#         - **智能办公系统开发**：基于云平台开发智能办公系统，整合AI助手，实现语音交互和任务自动化。
#         - **制造业信息系统开发**：参与企业级信息管理系统的开发，优化生产数据管理流程。
#         - **AI 视觉检测系统**：利用深度学习技术开发视觉检测系统，实现产品质量自动化检测。
#         - **跨平台物品管理应用**：基于PaaS/FaaS架构开发跨平台移动应用，支持iOS、Android、Web和桌面端。
        
#         ### 学习经历
#         - **2013年4月 - 2017年3月** 日本某大学 - 计算机科学与技术学士
        
#         ### 职业证书
#         - Microsoft Power Platform Developer Associate
#         - Microsoft Power Platform App Maker Associate
#         - Oracle Java Programmer Silver 认证
#         - Azure Developer Associate
#         - Azure AI Associate
#         - ITIL Foundation Certification
#         - Azure Fundamentals Certification
#         """,
#         "skills": "### 技术栈",
#         "contact": "### 联系方式",
#         "email": "📧 邮箱：yaoning@example.com",
#         "linkedin": "🔗 [LinkedIn](https://www.linkedin.com/in/yaoning)",
#         "company": "🏢 [DXC Japan](https://www.dxc.com)",
#         "welcome": "欢迎访问我的个人介绍页面！"
#     },
#     "ja": {
#         "title": "自己紹介 - Yao Ning",
#         "role": "技術コンサルタント | AI & クラウド専門家",
#         "description": """
#         - 💼 現在 **DXC Japan** の Associate Manager
#         - 🎯 **ServiceNow** 製品の技術コンサルティングと開発を担当し、6人の開発チームをリード
#         - 🤖 社内で **DXCJ Chat AI アシスタント** を開発し、会議メモ自動生成・メール返信自動化を提供
#         - 💻 **Azure、Power Platform、Oracle APEX、Python、Java、JavaScript** に精通
        
#         ### 職務経歴
#         - **2022年12月 - 現在** 日本マイクロソフト - PowerPlatform技術支援、講師、メンター
#         - **2021年10月 - 2022年11月** 日本IBM - EI-Coreの開発、開発チームのサブリーダー
#         - **2017年4月 - 2021年9月** FITEC - AI、クラウド、工場自動化システム開発のリーダー補佐
        
#         ### プロジェクト経験
#         - **スマートオフィスシステム開発**：クラウド基盤を活用し、AIアシスタントを統合したスマートオフィスシステムを開発。
#         - **製造業向け情報管理システム**：企業の生産データ管理を最適化する情報システムを開発。
#         - **AI画像検査システム**：ディープラーニング技術を用いた品質管理の自動化システムを構築。
#         - **マルチプラットフォーム資産管理アプリ**：PaaS/FaaSアーキテクチャを基盤に、iOS、Android、Web、デスクトップ向けのアプリを開発。
        
#         ### 学歴
#         - **2013年4月 - 2017年3月** 日本某大学 - コンピュータサイエンス学士
        
#         ### 資格
#         - Microsoft Power Platform Developer Associate
#         - Microsoft Power Platform App Maker Associate
#         - Oracle Java Programmer Silver 認定
#         - Azure Developer Associate
#         - Azure AI Associate
#         - ITIL Foundation Certification
#         - Azure Fundamentals Certification
#         """,
#         "skills": "### スキルセット",
#         "contact": "### 連絡先",
#         "email": "📧 メール：yaoning@example.com",
#         "linkedin": "🔗 [LinkedIn](https://www.linkedin.com/in/yaoning)",
#         "company": "🏢 [DXC Japan](https://www.dxc.com)",
#         "welcome": "私の自己紹介ページへようこそ！"
#     }
# }

# # 个人头像（请替换为你的图片路径或URL）
# image_url = "img/my_pic.PNG"  # 这里可以放你的头像链接
# st.image(image_url, width=150)

# # 个人信息展示
# st.title("Yao Ning")
# st.subheader(info[language]["role"])
# st.markdown(info[language]["description"])

# # 技能展示
# st.write(info[language]["skills"])
# columns = st.columns(3)
# skills = ["Python", "C#", "JavaScript", "Java", "Spring", "Angular", "Power Platform", "Azure", "TensorFlow"]
# for i, skill in enumerate(skills):
#     columns[i % 3].button(skill)

# # 联系方式
# st.write(info[language]["contact"])
# st.markdown(
#     f"""
#     - {info[language]["email"]}
#     - {info[language]["linkedin"]}
#     - {info[language]["company"]}
#     """
# )

# st.success(info[language]["welcome"])


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