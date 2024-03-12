import requests
from bs4 import BeautifulSoup
import pyperclip
import datetime

# 요청 URL 및 파라미터 설정
url = "https://open.neis.go.kr/hub/mealServiceDietInfo"

# 오늘 날짜를 YYYYMMDD 형식으로 가져오기
today = datetime.datetime.now().strftime('%Y%m%d')

params = {
    "ATPT_OFCDC_SC_CODE": "(교육청 코드)",#나이스 교육정보개방포털에서 원하는 교육청 코드와 학교 코드를 찾아서 적어주세요
    "SD_SCHUL_CODE": "(학교 코드)",
    "MLSV_YMD": today,
}

# API 요청
response = requests.get(url, params=params)

# BeautifulSoup를 이용해 XML 파싱
soup = BeautifulSoup(response.content, 'lxml')

# 원하는 정보 추출
mlsv_ymd = soup.find('mlsv_ymd')
ddish_nm = soup.find('ddish_nm')
orplc_info = soup.find('orplc_info')
cal_info = soup.find('cal_info')
ntr_info = soup.find('ntr_info')
result = soup.find('result')

# 찾은 태그가 없다면 "(정보없음)"으로 대체
mlsv_ymd = mlsv_ymd.text if mlsv_ymd else "(정보없음)"
ddish_nm = ddish_nm.text if ddish_nm else "(정보없음)"
orplc_info = orplc_info.text if orplc_info else "(정보없음)"
cal_info = cal_info.text if cal_info else "(정보없음)"
ntr_info = ntr_info.text if ntr_info else "(정보없음)"
result = result.text if result else "(정보없음)"

# 정보 조합
info = f"날짜 : {today}\n날짜 : {mlsv_ymd}\n급식 : {ddish_nm}\n정보 : {orplc_info}\n칼로리 : {cal_info}\n상세 : {ntr_info}\n\n{result}"

# 클립보드에 복사
pyperclip.copy(info)
