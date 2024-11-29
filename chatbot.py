import streamlit as st
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# تحميل بيانات الأسئلة والأجوبة
faq_data = pd.read_csv('faq_first_aid.csv')

# دالة للبحث عن الإجابة الأقرب للسؤال
def find_answer(user_question):
    questions = faq_data['question'].tolist()

    # استخدام fuzzywuzzy للبحث عن السؤال الأقرب
    closest_question, score = process.extractOne(user_question, questions, scorer=fuzz.token_sort_ratio)

    if score > 70:
        answer = faq_data[faq_data['question'] == closest_question]['answer'].values[0]
        return answer
    else:
        return "عذرًا، لا أستطيع العثور على إجابة لهذا السؤال."

# تصميم واجهة البوت
st.set_page_config(page_title="بوت الإسعافات الأولية", page_icon="🩺")

# عنوان الصفحة
st.title("🤖 بوت الإسعافات الأولية")

# تعليمات للمستخدم
st.markdown("""
### مرحبًا بك في بوت الإسعافات الأولية!
#### اسأل أي سؤال متعلق بالإسعافات الأولية وسيقوم البوت بمساعدتك في العثور على الإجابة.
""")

# إدخال السؤال من المستخدم
user_question = st.text_input("💬 **ادخل سؤالك هنا**:")

# عند الضغط على زر الإرسال
if st.button("🚑 إرسال"):
    if user_question:
        answer = find_answer(user_question)
        st.write(f"### 📝 الإجابة: \n {answer}")
    else:
        st.warning("يرجى إدخال سؤال.")

# إضافة تنسيق خلفية أو لون
st.markdown("""
<style>
    body {
        background-color: #f0f2f6;
        font-family: "Arial", sans-serif;
    }
    .stButton>button {
        background-color: #007BFF;
        color: white;
        font-size: 16px;
    }
    .stTextInput>div>div>input {
        font-size: 18px;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #007BFF;
    }
</style>
""", unsafe_allow_html=True)
