from xhs.prompt_template import system_template_text, user_template_text
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate
from xhs.xiaohongshu_model import Xiaohongshu


def generate_xiaohongshu(theme, openai_api_key):
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_template_text),
        ("user", user_template_text)
    ])
    # model = ChatOpenAI(model="gpt-3.5-turbo", api_key=openai_api_key)
    model = ChatOpenAI(
        openai_api_base = "https://api.chatanywhere.org",
        api_key=openai_api_key
    )
    
    output_parser = PydanticOutputParser(pydantic_object=Xiaohongshu)
    chain = prompt | model | output_parser
    result = chain.invoke({
        "parser_instructions": output_parser.get_format_instructions(),
        "theme": theme
    })
    return result

