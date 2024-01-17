# Forecast available bikes of Bikeshare System in Seoul
> 2022-2 Big Data and Knowledge Management Systems1 Project   
> Goal : Build a virtual service using **data management systems**     
<img width="860" alt="스크린샷 2024-01-17 오후 4 23 32" src="https://github.com/sehyunpark99/DDAREUNGI_Project/assets/85481704/478fefa8-da6f-4a77-9b31-a883049e0ab6">

<p> <b> Tech Skills </b></p>
<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"> 
  <img src="https://img.shields.io/badge/Neo4j-4581C3?style=for-the-badge&logo=Neo4j%2B%2B&logoColor=white">
  <img src="https://img.shields.io/badge/GoogleBigQuery-669DF6?style=for-the-badge&logo=googlebigquery&logoColor=white">
</p>

# Team Members
SeHyun Park(Architectural Design, Modeling, Demo), MyungJoo Lee(Model deployment, Simulation), SunYoung Park(Market research, Architectural Design), 
GyuYeol Kim(Neo4j, DBMS(Bigquery), Presenter), ChaiEun Lee(Data preprocessing, EDA, Model Design)       

# 1. Motivation
- **Problem**   
Increase in inefficiency in Seoul bikeshare system due to the relocation of bikes based on the past rental/return data.   
Growing discontent from users, Seoul Bike cumulative deficit also became a problem.     
- **Goal**   
Use real-time remaining bikes count, past rental/return data, weather data, air pollution data, and geographical data for modeling and predict the remaining bikes count
# 2. Scenario
Find correlation between various factors (weather, river accessibility…etc) and remaining bikes number at rental station
Integrate across different DBMS to make prediction on future remaining bikes at selected rental station   

# 3. Architecutural Design
<img width="952" alt="스크린샷 2024-01-17 오후 4 32 15" src="https://github.com/sehyunpark99/DDAREUNGI_Project/assets/85481704/cf8e98ee-3f90-4d02-95af-f48a4cc86406">
<img width="951" alt="스크린샷 2024-01-17 오후 4 36 17" src="https://github.com/sehyunpark99/DDAREUNGI_Project/assets/85481704/8db7f3d2-ba10-458e-92fb-2e825f987dd6">

# 4. Modeling
<img width="950" alt="스크린샷 2024-01-17 오후 4 33 00" src="https://github.com/sehyunpark99/DDAREUNGI_Project/assets/85481704/ea906e8a-8715-4e42-b22f-d929e01c9d87">

# 5. Project results
<img width="952" alt="스크린샷 2024-01-17 오후 4 34 41" src="https://github.com/sehyunpark99/DDAREUNGI_Project/assets/85481704/5b1d06cf-3040-4d12-9959-6029d0950a37">

# DDAREUNGI_Prject
As a part of Data Science Project, our team created an AI model that can predict the rental rate of DDAREUNGI, which is a public bike in Seoul, in each stations. 
In this project, I contributed in constructing an XGBoost ensemble model and creating a web demo using Streamlit. 
This repository comprised of app.py for a web demo and data folder for visual aid of model design and data processing. 


