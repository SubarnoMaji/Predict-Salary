
import streamlit as st
import pickle
import numpy as np
import sklearn 




with st.sidebar:
    st.markdown(f"""
                <div style="text-align: center;">
                
                ##  <span style="color:#d9d9d9; ">Explore Subarno Maji's Projects </span>:chart_with_upwards_trend:
             
                <br>              
                <div>
                """, 
               unsafe_allow_html=True)
    st.markdown(f"""
                <div style="text-align: center;  height: 300px; overflow-y: auto;">
              <button style="background-color:#990033; color: white; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 10px; cursor: pointer; border-radius: 4px;width: 250px;">
               <a href="https://www.example1.com" style="color: white; text-decoration: none;"><b>Laptop Price Predictor</b> </a>
                </button> 
                <br>
                
            <button style="background-color: #990033; color: white; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 10px; cursor: pointer; border-radius: 4px;width: 250px;">
                <a href="https://www.example2.com" style="color: white; text-decoration: none;"><b>Salary Predictor</b></a>
             </button>
            </div>
                <hr>
                """, 
               unsafe_allow_html=True)
    st.markdown(f"""
                <div style="text-align: center;">
                
                ##  <span style="color:#d9d9d9; "> Connect with me  </span> :smile:
             
                <br>              
                <div>
                """, 
               unsafe_allow_html=True)
    st.markdown("""



   
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.2/css/all.min.css" integrity="sha512-1sCRPdkRXhBV2PBLUdRb4tMg1w2YPf37qatUFeS7zlBy7jJI8Lf4VHwWfZZfpXtYSLy85pkm9GaYVYMfw5BC1A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

<link rel="stylesheet" href="Style.css">

<div align="center" class="icons" style="display:"flex"; justify-content:"space-between";" >

<a href="mailto:subarnomaji@gmail.com"><i class="fa-solid fa-envelope" style="font-size: 30px; color: #ff4d4d;padding-right: 10px;"></i></a>
<a href="https://www.facebook.com/profile.php?id=100083622261232"><i class="fa-brands fa-facebook" style="font-size: 30px; color:#3b5998;padding-right: 10px;"></i></a>
<a href="#"><i class="fa-brands fa-whatsapp" style="font-size: 30px; color: #075E54;padding-right: 10px;"></i></a>
<a href="https://www.linkedin.com/in/subarno-maji-6076a425b/"><i class="fa-brands fa-linkedin" style="font-size: 30px; color:#3399ff;padding-right: 10px;"></i></a>
<a href="https://github.com/SubarnoMaji"><i class="fa-brands fa-github" style="font-size: 30px; color: white;padding-right: 10px;"></i></a>


   
   </div>
   
   """,unsafe_allow_html=True
       


   )
    



st.markdown(f"""
                # <div align= "center"> <span style="color:#d9d9d9;"> Predict Your Salary </span> :money_with_wings:</div>
               
               """, 
               unsafe_allow_html=True)
pipe1 = pickle.load(open ('pipe1.pkl','rb'))
pipe2 = pickle.load(open ('pipe2.pkl','rb'))
pipe3 = pickle.load(open ('pipe3.pkl','rb'))
df = pickle.load(open ('df.pkl','rb'))

st.markdown("""
    <hr>
    """, unsafe_allow_html=True)



st.markdown(f"""
                ###  <span style="color:#ff6666"> Company Details  </span> :page_facing_up:
            
                <br>
               """, 
               unsafe_allow_html=True)


sector = st.selectbox('Sector',df['Sector'].unique())
ownership = st.selectbox('Type of Ownership',df['Type of ownership'].unique())
state = st.selectbox('State',df['job_state'].unique())
EmSize= st.selectbox('Approx number of Employee in the company',[50,200,500,1000,5000,10000])
    


st.markdown(f"""
                <br>
            
                ###  <span style="color:#ff6666"> Your Details </span> :page_with_curl:
            
                <br>
               """, 
               unsafe_allow_html=True)



job_simp = st.selectbox('JOB ROLE',df['job_simp'].unique())
age = st.number_input('Age' ,10,90, 27,1 )
st.write("Skills")
python = int(st.checkbox("Python"))
r = int(st.checkbox("R"))
spark = int(st.checkbox("Spark"))
aws = int(st.checkbox("AWS"))
excel = int(st.checkbox("Excel"))
seniority 	= st.selectbox('Seniority',df['seniority'].unique())
rating = st.slider("Rating", min_value=0.0, max_value=5.0, value=None, step=0.2)

st.markdown(f"""
            
                <br>
               """, 
               unsafe_allow_html=True)


if st.button("Predict Salary"):
    query = np.array([rating,ownership,sector,state,age,python,r,spark,aws,excel,job_simp,seniority,EmSize])
    
    
    
    
    query = query.reshape(1,13)

    min = str (np.round ( np.exp(pipe1.predict(query)[0])  ,  1 ) )
    max =str (np.round ( np.exp(pipe3.predict(query)[0])  ,  1 ) )
    avg =str (np.round ( np.exp(pipe2.predict(query)[0])  ,  1 ) )
 

    
    st.markdown(f"""
                <div align="Center">
                <br>

                ### Your predicted salary lies in range <span style="color:#32d2dd"> $ {min} K</span> to  <span style="color:#32d2dd">{max} K </span>
                ### With an average salary of      <span style="color:#32ed54"> $ {avg} K</span> :satisfied:
                
                </div>
               """, 
               unsafe_allow_html=True)
    
  