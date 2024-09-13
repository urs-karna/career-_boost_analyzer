from dotenv import load_dotenv

load_dotenv()
import base64
import streamlit as st 
#from streamlit.web.cli import main 
import streamlit.components.v1 as com
import os
import io
from PIL import Image                  
import pdf2image
import google.generativeai as genai
 #import csv

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_content,prompt):
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_files):
    if uploaded_files is not None:
        ## Convert the PDF to image
        images=pdf2image.convert_from_bytes(uploaded_files.read())

        first_page=images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

## Streamlit App


# Streamlit App Configuration
st.set_page_config(page_title="Career Boost Analyzer", page_icon="📄", layout="wide")
#css 
with open("style.css") as source:
    st.markdown ( f" <style> {source.read()} </style>",unsafe_allow_html=True)


   

st.markdown('<h1 class="title" style=" background-color:#4a2b7a; color:#FFFF9E; border-radius:10px;" >CAREER BOOST ANALYZER<h1>',unsafe_allow_html=True)
#st.markdown('<img src="RoboChecking.jpeg" alt="image of a robo" width="500" height="200"' />,unsafe_allow_html=True)
com.iframe("https://lottie.host/embed/dc2478c0-452f-447b-aa01-93a123bb8301/AzpnSbHPvm.json",height=300)

# Input Section
st.markdown('<div class="input-section">', unsafe_allow_html=True)
input_text = st.text_area("Enter The Job Description Of Your Desired Job:", key="input", height=150)
st.markdown('</div>', unsafe_allow_html=True)



# input_text=st.text_area("Enter The Job Description Of Your Desired Job: ",key="input")
#
# Upload Section
st.markdown('<div class="upload-section">', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
com.iframe("https://lottie.host/embed/9c67f2c6-ef0c-4d30-93fc-fa3d48b7efec/hmUBefkLQE.json",height=200)
uploaded_files = st.file_uploader("Upload your resume (PDF):", type=["pdf"], accept_multiple_files=True)
st.markdown('<div style="margin-top: 20px" class="upload-section">',unsafe_allow_html=True)

st.markdown('</div > ',unsafe_allow_html=True)
#uploaded_files=st.file_uploader("Upload your resume(PDF)...",type=["pdf"] , accept_multiple_files=True)
st.markdown("<h3>Click the Buttons Below & Wait for the Amazing Result of Your Resume</h3>",unsafe_allow_html=True)
st.markdown("___")
#if uploaded_files is not None:
  #  st.write("PDF Uploaded Successfully")
com.iframe("https://lottie.host/embed/2c94fbf2-b141-4d33-afa7-fc0dcc8ec1d8/D7nHn6herj.json",height=180)
st.header("Employee")
 
submit1 = st.button("Tell Me About My Resume")

submit2 = st.button("Skill Gap Analysis and Learning Resources")

submit3 = st.button("Percentage match")

submit5= st.button("Interview question's ")
submit6= st.button("Job suggestions based on your skills")
 
st.header("RECRUITER")
com.iframe("https://lottie.host/embed/a3bb4e33-6cdd-44e3-935c-1e3484ebcced/O2ALFHhCMi.json",height=200)

submit4=st.button("ATS score for each candidate")

submit_suggestions = st.button("suggestion")


input_prompt1 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
 Please share your professional evaluation on whether the candidate's profile aligns with the role.  
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""
 
input_prompt2= """ You are a experinced  career mentor, First the output should come as candidate name highlight     it  and  identify the skills that are missing in the resume based on job discription.
and suggest how can the candidate improve missing  skills along with some platforms,popular options along with links  with some small discription
"""

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as candidate name and percentage and last final thoughts .
"""
input_prompt0=  """You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as candidate name and percentage and last profile summary. 
"""
input_prompt5="""You are an experienced Technical Human Resource Manager, your task is to generate interview questions for a candidate based on this job description and resume and make sure that provide answers for each at the end """

input_prompt6= """ You are a experinced  career mentor adn recruitment consultant, your task is to identify the skills in the resume and provide job suggestion that he is suitable for that and the output should be job role, company name and link for applying if that company is recruiting """
 #You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
# Evaluate the resume against the provided job description and percentage of match if the resume matches
# the job description.
#  your task is I want the response in one single string having the structure
# {{"Candidate name":"" ,,"missing skills in resume based on JD":"","Profile Summary":" " }}




if submit1:
    if uploaded_files is not None:
        for file in uploaded_files:
            pdf_content=input_pdf_setup(file)
            response=get_gemini_response(input_prompt1,pdf_content,input_text)
            st.subheader("The Repsonse of")
            st.write(response)
    else:
        st.write("Please uplaod the resume")

if submit2:
    if uploaded_files is not None:
        for file in uploaded_files:
            pdf_content=input_pdf_setup(file)
            response=get_gemini_response(input_prompt2,pdf_content,input_text)
            st.subheader("The Repsonse of")
            st.write(response)
    else:
        st.write("Please uplaod the resume")


if submit4:
    if uploaded_files is not None:
            for file in uploaded_files :
             pdf_content=input_pdf_setup(file)
             res=get_gemini_response(input_prompt0,pdf_content,input_text)
             st.subheader("The Repsonse of")
             st.write(res)
        
         
 

 
if submit3:
    if uploaded_files is not None:
        for file in uploaded_files :
         
         pdf_content=input_pdf_setup(file)
         response=get_gemini_response(input_prompt3,pdf_content,input_text)
         st.subheader("The Repsonse of")
         st.write(response)
    else:
        st.write("Please uplaod the resume")

if submit5:
    if uploaded_files is not None:
        for file in uploaded_files :
         
         pdf_content=input_pdf_setup(file)
         response=get_gemini_response(input_prompt5,pdf_content,input_text)
         st.subheader("The Repsonse of")
         st.write(response)
    else:
        st.write("Please uplaod the resume")
if submit6:
    if uploaded_files is not None:
        for file in uploaded_files :
         
         pdf_content=input_pdf_setup(file)
         response=get_gemini_response(input_prompt6,pdf_content,input_text)
         st.subheader("The Repsonse of")
         st.write(response)
    else:
        st.write("Please uplaod the resume")

   




