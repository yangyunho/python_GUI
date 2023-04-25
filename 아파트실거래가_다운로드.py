from tkinter import *
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import requests
from bs4 import BeautifulSoup
from tkinter import filedialog
import pandas as pd

win = Tk()
win.geometry("800x800")
win.title("부동산빅데이터땅짚고 아파트실거래 다운로더")

frame0 = tk.LabelFrame(win, text="서비스키입력", padx=5, pady=5)  # padx / pady 내부여백
frame0.pack(fill="both", padx=10, pady=10)  # padx / pady 외부여백
# lbl = Label(frame0, text="공공데이터포털 서비스키", anchor="w").grid(row=0, column=0, sticky="W")
ent1 = ttk.Entry(frame0, width=108)
ent1.grid(row=0, column=1, padx=(0, 5), pady=(5, 5))

value = ent1.get()
print(value)

frame거래종류 = tk.LabelFrame(win, text="거래종류선택", padx=5, pady=5)  # padx / pady 내부여백
frame거래종류.pack(fill="both", padx=10, pady=10)  # padx / pady 외부여백
combo1 = tk.StringVar()
combo_chosen1 = ttk.Combobox(
    frame거래종류, width=15, textvariable=combo1, state="readonly", justify="left"
)
combo_chosen1["values"] = ("매매", "전월세")
combo_chosen1.grid(column=1, row=1, sticky="W", padx=(0, 5), pady=(0, 5))
combo_chosen1.current(0)


frame = tk.LabelFrame(win, text="기간설정", padx=5, pady=5)  # padx / pady 내부여백
frame.pack(fill="both", padx=10, pady=10)  # padx / pady 외부여백


# frame = win.LabelFrame(win, text='1번 프레임', padx=15, pady=15) # padx / pady 내부여백
# frame.pack(padx=10, pady=10) # padx / pady 외부여백

# # win.option_add("*Font","궁서 20")


# lb2 = Label(frame, text="거래 종류", justify='left').grid(row=1, column=0, sticky="W")
# combo1 = tk.StringVar()
# combo_chosen1 = ttk.Combobox(frame, width=15, textvariable=combo1, state='readonly', justify='left')
# combo_chosen1['values'] = ("매매","전월세")
# combo_chosen1.grid(column=1, row=1, sticky="W", padx=(0, 5),pady=(0, 5))
# combo_chosen1.current(0)


def DEAL_YMD_list(s_ym, e_ym):
    date = pd.date_range(str(s_ym) + "01", str(e_ym) + "01", freq="MS").strftime("%Y%m")
    return list(date)


# lb3 = Label(frame, text="기간 설정", justify='left').grid(row=2, column=0, sticky="W")

button_select = Label(frame, text="시작년월")
button_select.grid(row=1, column=0, sticky="W", padx=(0, 5), pady=(0, 5))

combo2 = tk.StringVar()
combo_chosen2 = ttk.Combobox(
    frame, width=15, textvariable=combo2, state="readonly", justify="left"
)
combo_chosen2["values"] = DEAL_YMD_list(200601, 202302)
combo_chosen2.grid(row=1, column=1, sticky="W", padx=(0, 5), pady=(0, 5))
combo_chosen2.current(0)
value2 = combo2.get()

button_select = Label(frame, text="종료년월")
button_select.grid(row=1, column=2, sticky="W", padx=(0, 5), pady=(0, 5))

combo3 = tk.StringVar()
combo_chosen3 = ttk.Combobox(
    frame, width=15, textvariable=combo3, state="readonly", justify="left"
)
combo_chosen3["values"] = DEAL_YMD_list(200601, 202302)
combo_chosen3.grid(row=1, column=3, sticky="W", padx=(0, 5), pady=(0, 5))
combo_chosen3.current(0)
value3 = combo3.get()


# lb2 = Label(win, text="기간 선택")
# lb2.grid(row=1, column=0)
# ent2 = Entry(win, width=100)
# ent2.grid(row=1, column=1)

# # win.option_add("*Font","궁서 20")
# lb4 = Label(frame, text="파일저장폴더", justify='left').grid(row=3, column=0, sticky="W")
# # lbl.grid(row=0, column=0)
# ent4 = Entry(frame, width=50, justify='left', borderwidth=1, relief='solid').grid(row=3, column=1, sticky="W", padx=(0, 5),pady=(0, 5))
# # ent4.grid(row=3, column=1)


def select_folder():
    folder_path = filedialog.askdirectory()
    entry_path.delete(0, tk.END)
    entry_path.insert(0, folder_path)
    #     value = ent1.get()
    print(value, value2, value3)


frame폴더선택 = tk.LabelFrame(win, text="폴더지정", padx=5, pady=5)  # padx / pady 내부여백
frame폴더선택.pack(fill="both", padx=10, pady=10)  # padx / pady 외부여백
# label = tk.Label(frame폴더선택, text="폴더 경로", justify='left').grid(row=3, column=0, sticky="W")
# label.grid(row=3, column=0, padx=5, pady=5)

entry_path = ttk.Entry(frame폴더선택, width=99)
entry_path.grid(row=3, column=1, sticky="W", padx=(0, 5), pady=(0, 5))

button_select = Button(frame폴더선택, text="폴더 선택", command=select_folder)
button_select.grid(row=3, column=2, sticky="W", padx=(0, 5), pady=(0, 5))


# ent.pack()
def lotto_p():
    ##################################
    import selenium
    from selenium import webdriver
    import json
    import pandas as pd
    import openpyxl
    from datetime import datetime
    import requests
    from bs4 import BeautifulSoup as bs
    import time
    import random
    from tqdm import tqdm
    import os

    ##################################
    import pandas as pd

    date = pd.date_range("20060101", "20230201", freq="MS").strftime("%Y%m")

    # print(list(date))

    def DEAL_YMD_list(s_ym, e_ym):
        date = pd.date_range(str(s_ym) + "01", str(e_ym) + "01", freq="MS").strftime(
            "%Y%m"
        )
        return list(date)

    print(len(DEAL_YMD_list(200601, 202302)))

    ##################################

    ##################################
    import requests
    import json
    import xmltodict

    global value, value2, value3
    print(value, value2, value3)
    #     service_key = os.environ.get('service_key')
    #     n = ent.get()
    #     service_key='6huNFddtUv7Ztnc%2B%2BuXOXO6MD%2F5q%2BISl4%2Fw7qzulYBlMFBt8pknpuKs2fibErcqXFmtKtWiFiD6EoJtNTnHHlg%3D%3D'
    service_key = value
    print("service_key", service_key)
    # lawd_cd = '48170'
    # deal_ymd = '202204'

    # f-string

    def get_data_trade(지역코드, 년월):
        base_url = "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade?"
        base_url += f"serviceKey={service_key}"  #'servicekey=' + service_key
        #     base_url = base_url+ f'serviceKey={service_key}'
        base_url += f"&LAWD_CD={지역코드}"
        base_url += f"&DEAL_YMD={년월}"

        # print(base_url)

        res = requests.get(base_url)
        # print(xmltodict.parse(res.text))
        data = json.loads(json.dumps(xmltodict.parse(res.text)))
        # print(data['response']['body']['items']['item'])
        #     print(data)
        #     print('/n')
        try:
            df = pd.DataFrame(data["response"]["body"]["items"]["item"])
            df["거래금액"] = df["거래금액"].str.replace(",", "")
            # print(지역코드,"/",년월,"실거래가를 df로 테이블을 만들었습니다!!")
            return df
        #         df.to_excel(str(지역코드)+'_'+str(년월)+'.xlsx', encoding='euc_kr', index=False)
        #         print(지역코드,"/",년월,"실거래가를 excel파일로 담았습니다!!")
        except:
            print(str(지역코드) + "/" + str(년월) + "/실거래가 신고내역이 없습니다.")
            pass

    # get_data_trade(48170, 202302)
    ##################################

    ##################################
    def get_silga_mama(년월):

        #         global sigun_code_list,codelist_b
        #################################
        print("지역명_API테이블 가져오기")
        file_path = "C:/Users/Administrator/Downloads/지역명_API.xlsx"
        region_api = pd.read_excel(
            file_path, sheet_name="R1_지역명"
        )  # for구문으로 csv파일들을 읽어 들인다
        region_api

        region_api.columns
        columns = list(region_api.columns)
        print(columns)

        region_api = region_api[
            (region_api["gubun"] == 1) | (region_api["gubun"] == 13)
        ]
        region_api

        region_api = region_api.astype({"area_code5": "int64"})
        region_api = region_api.astype({"area_code5": "str"})

        region_api.info()

        region_api_dict = region_api.to_dict()
        # print(region_api_dict)
        dic_val = region_api_dict["area_code5"].values()
        sigun_code_list = list(dic_val)
        print(sigun_code_list)
        #################################

        result = pd.DataFrame()
        for 지역코드 in sigun_code_list:
            temp = get_data_trade(지역코드, 년월)
            result = pd.concat([result, temp])
            # print(지역코드,"/",년월,"실거래가를 result 데이터프레임에 추가하였습니다.")
        result.to_csv(
            "C:/Users/Administrator/Downloads/" + str(년월) + ".csv",
            encoding="utf-8-sig",
            index=False,
        )
        #     result.to_excel('C:/Users/Administrator/Documents/pmp202204/repository/trade/'s+tr(년월)+'.xlsx', encoding='euc_kr', index=False)
        print("176개지역 " + str(년월) + " 실거래가를 csv파일로 저장하였습니다")

    ##################################
    for y in DEAL_YMD_list(combo2.get(), combo3.get()):
        print(y, "실거래가 가져오기 시작")
        try:
            get_silga_mama(y)
        except Exception as e:
            print(e)
            get_silga_mama(y)
        print(y, "실거래가 가져오기 종료")


btn = Button(frame폴더선택)
btn.config(text="실거래가가져오기")
btn.config(command=lotto_p)
# btn.pack()
btn.grid(column=1, row=5)


###### 2번째 Frame ######
frame2 = tk.LabelFrame(
    win, text="아파트 실거래가 다운로더 사용방법", padx=15, pady=15
)  # padx / pady 내부여백
frame2.pack(fill="both", expand=True, padx=10, pady=10)  # padx / pady 외부여백
Label(frame2, text="1. 공공데이터포털에 회원가입 후 OPEN API 사용신청을 하세요").place(x=0, y=5)
Label(frame2, text="2. 설정을 하세요").place(x=0, y=25)

# name_entered.focus()

win.mainloop()

# [출처] [초보자를 위한 파이썬 GUI 프로그래밍 with tkinter] 3. 로또 회차 입력 받아 당첨 번호 확인하기|작성자 초보코딩
