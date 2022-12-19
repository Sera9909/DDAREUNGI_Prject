import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='따릉이 프로젝트'
    #page_icon=''
)

st.title('따릉이 프로젝트')
TASKS = ['따릉이 정보', '대여량 통계', '대여량 예측']
with st.sidebar:
    TASK = st.selectbox('choose task', options=TASKS, key='task')
    #INFERENCE_FREQ = st.select_slider('Inference frequency(IF)', options=[1, 3, 5, 7, 10, 15], value=7, key='inference_freq')
    #ANGLE_THRES = st.slider('Angle Threshold', 1.5, 10.0, value=3.5, step=0.1, key='angle_thres')
    #BOX_PADDING = st.select_slider('Box Padding', options=[15, 30, 45], value=30, key='box_padding')
    #LEFT_ARM = st.checkbox('Left Arm?', value=False, key='left_arm')
    #DO_NOT_CHECKBOX = st.checkbox('Do not start', value=False, key='not_start')

#raw_datasets  = pd.read_csv('data/final_dataset') #1553489 #Row = 1515003, Column = 15 (14 features + 1 label)
data = pd.read_csv('data/statistic.csv')

if TASK == '따릉이 정보':
    st.image('https://mediahub.seoul.go.kr/uploads/mediahub/2021/10/QQrNiCDPdkHNDdUZWHzDFNtUpxsvspKU.png')
    with st.expander("따릉이란?"):
        st.image('data/캡처.PNG')     
        st.write("따릉이는 서울시에서 운영하고 있는 공유 자전거 서비스입니다.  \
            2022년 6월 기준으로 355만여명의 회원과 4만천오백개의 자전거와 2천 6백여개의 대여소가 있고, \
                사용방법은 따릉이 앱을 통해 대여소를 찾은 뒤, 이용권을 구매하고 자전거를 대여한 뒤 반납 시에는 원하는 반납소를 찾아 반납하면 됩니다.")
    with st.expander("서울시 따릉이 대여소"):
        st.image('data/output1.png') 
        st.write('지역구별 따릉이 대여소')
        option = st.selectbox(
            '열람 지역 선택', 
            options = ('영등포구', '마포구', '송파구'))
        if option == '영등포구':
            station_data = data.loc[(data['region'] == '영등포구')]
            station_data = station_data.drop_duplicates(['id'])
            st.table(station_data[:100])
        if option == '마포구':
            station_data = data.loc[(data['region'] == '마포구')]
            station_data = station_data.drop_duplicates(['id'])
            st.table(station_data[:100])
        if option == '송파구':
            station_data = data.loc[(data['region'] == '송파구')]
            station_data = station_data.drop_duplicates(['id'])
            st.table(station_data[:100])

if TASK == '대여량 통계':
    #Raw Data
    if st.checkbox('Show Raw Data'):
        st.subheader('Raw Dataset')
        st.write(data[:500])

    st.subheader('📈 따릉이 대여량')
    tab1, tab2, tab3, tab4 = st.tabs(['따릉이 시간별 대여량', '따릉이 요일별 대여량', '따릉이 월별 대여량', '공휴일 따릉이 대여량'])
    #시간별 대여량
    a = data.groupby('hour')[['rentnum', 'returnnum']].sum()
    chart_data = pd.DataFrame(a['rentnum'], a['returnnum'])
    a['sum'] = a['rentnum']+a['returnnum']
    time_ = pd.DataFrame([[a.iloc[0,0]+a.iloc[1,0]+a.iloc[2,0], a.iloc[0,1]+a.iloc[1,1]+a.iloc[2,1], a.iloc[0,2]+a.iloc[1,2]+a.iloc[2,2]],
                    [a.iloc[3,0]+a.iloc[4,0]+a.iloc[5,0], a.iloc[3,1]+a.iloc[4,1]+a.iloc[5,1], a.iloc[3,2]+a.iloc[4,2]+a.iloc[5,2]],
                    [a.iloc[6,0]+a.iloc[7,0]+a.iloc[8,0], a.iloc[6,1]+a.iloc[7,1]+a.iloc[8,1], a.iloc[6,2]+a.iloc[7,2]+a.iloc[8,2]],
                    [a.iloc[9,0]+a.iloc[10,0]+a.iloc[11,0], a.iloc[9,1]+a.iloc[10,1]+a.iloc[11,1], a.iloc[9,2]+a.iloc[10,2]+a.iloc[11,2]],
                    [a.iloc[12,0]+a.iloc[13,0]+a.iloc[14,0], a.iloc[12,1]+a.iloc[13,1]+a.iloc[14,1], a.iloc[12,2]+a.iloc[13,2]+a.iloc[14,2]],
                    [a.iloc[15,0]+a.iloc[16,0]+a.iloc[17,0], a.iloc[15,1]+a.iloc[16,1]+a.iloc[17,1], a.iloc[15,2]+a.iloc[16,2]+a.iloc[17,2]],
                    [a.iloc[18,0]+a.iloc[19,0]+a.iloc[20,0], a.iloc[18,1]+a.iloc[19,1]+a.iloc[20,1], a.iloc[18,2]+a.iloc[19,2]+a.iloc[20,2]],
                    [a.iloc[21,0]+a.iloc[22,0]+a.iloc[23,0], a.iloc[21,1]+a.iloc[22,1]+a.iloc[23,1], a.iloc[21,2]+a.iloc[22,2]+a.iloc[23,2]]],
                    index=['0~3','3~6','출근 6~9','9~12', '12~15', '15~18', '퇴근 18~21', '21~24'],
                    columns=['대여량','반납량','대여반납량'])
    with tab1:
        st.write("시간별 따릉이 대여량, 반납량, 합계입니다.")
        st.table(time_)
        st.line_chart(a)

    #요일별 대여량
    b = data.groupby('dayofweek')[['rentnum', 'returnnum']].sum()
    b = pd.DataFrame(b, index=['Monday', 'Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    bb = pd.DataFrame([[(b.iloc[0,0]+b.iloc[1,0]+b.iloc[2,0]+b.iloc[3,0]+b.iloc[4,0])/5,(b.iloc[0,1]+b.iloc[1,1]+b.iloc[2,1]+b.iloc[3,1]+b.iloc[4,1])/5],
                    [(b.iloc[5,0]+b.iloc[6,0])/2,(b.iloc[5,1]+b.iloc[6,1])/2]],
                    index=['평일','주말'],columns=['평균 대여량','평균 반납량'])
    with tab2:
        st.write("요일별 따릉이 대여량, 반납량, 합계입니다.")
        st.table(bb)
        st.bar_chart(b)

    #월별 대여량
    c = data.groupby('month')[['rentnum', 'returnnum']].sum()
    c['sum'] = c['rentnum']+c['returnnum']
    cc = pd.DataFrame([[c.iloc[2,0]+c.iloc[3,0]+c.iloc[4,0], c.iloc[2,1]+c.iloc[3,1]+c.iloc[4,1], c.iloc[2,2]+c.iloc[3,2]+c.iloc[4,2]],
                    [c.iloc[5,0]+c.iloc[6,0]+c.iloc[7,0], c.iloc[5,1]+c.iloc[6,1]+c.iloc[7,1], c.iloc[5,2]+c.iloc[6,2]+c.iloc[7,2]],
                    [c.iloc[8,0]+c.iloc[9,0]+c.iloc[10,0], c.iloc[8,1]+c.iloc[9,1]+c.iloc[10,1], c.iloc[8,2]+c.iloc[9,2]+c.iloc[10,2]],
                    [c.iloc[0,0]+c.iloc[1,0]+c.iloc[11,0], c.iloc[0,1]+c.iloc[1,1]+c.iloc[11,1], c.iloc[0,2]+c.iloc[1,2]+c.iloc[11,2]]],       
                    index=['봄','여름','가을','겨울'], columns=['대여량','반납량','대여반납량'])
    with tab3:
        st.write("월별 따릉이 대여량, 반납량, 합계입니다.")
        st.table(cc)
        st.bar_chart(c)

    #Holiday
    holiday = data.groupby('holyday')[['rentnum', 'returnnum']].sum()
    holiday = holiday.rename(index={0: 'No holiday', 1: 'Yes holiday'})
    with tab4:
        st.write("공휴일 따릉이 대여량, 반납량, 합계입니다.")
        st.table(holiday)
        st.bar_chart(holiday)
        
if TASK == '대여량 예측':
    st.write("# To be continued...")
    st.write('Spoiler')
    st.image('data/model.PNG') 
    st.image('data/deploy.PNG') 
