import google.generativeai as genai
import os
genai.configure(api_key="AIzaSyB45quDtyWzRw_ErsU-fxsv_kmytrHLyNM")



model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("hi")
st.write(response)




































































