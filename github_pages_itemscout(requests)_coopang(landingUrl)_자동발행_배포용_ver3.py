# -*- coding: utf-8 -*-

import subprocess
import datetime
import platform
import random
import time
from datetime import timedelta
from time import gmtime
from time import sleep
from time import strftime
import chromedriver_autoinstaller
import pyshorteners
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os.path
from bs4 import BeautifulSoup
import time
import requests
import re
import os
import json
import hashlib
import hmac
from time import gmtime, strftime
from pprint import pprint as pp
from urllib.parse import urljoin
from fake_useragent import UserAgent
from urllib import parse
from urllib.parse import urlparse, parse_qs

osName = platform.system()  # window 인지 mac 인지 알아내기 위한
# print(osName)

C_END = "\033[0m"
C_BOLD = "\033[1m"
C_INVERSE = "\033[7m"
C_BLACK = "\033[30m"
C_RED = "\033[31m"
C_GREEN = "\033[32m"
C_YELLOW = "\033[33m"
C_BLUE = "\033[34m"
C_PURPLE = "\033[35m"
C_CYAN = "\033[36m"
C_WHITE = "\033[37m"
C_BGBLACK = "\033[40m"
C_BGRED = "\033[41m"
C_BGGREEN = "\033[42m"
C_BGYELLOW = "\033[43m"
C_BGBLUE = "\033[44m"
C_BGPURPLE = "\033[45m"
C_BGCYAN = "\033[46m"
C_BGWHITE = "\033[47m"

# [사용자 입력 정보] ======================================================================================================== START

# 쿠팡 파트너 API access key와 secret key
coopang_access_key = ""  # access_key 를 입력하세요!
coopang_secret_key = ""  # secret_key 를 입력하세요!

# 링크 변환을 할 수 없는 경우를 위해 fake 쿠팡 링크를 만들어준다.
fake_coopang_link = 'https://link.coupang.com/a/bawvXk'  # 간편 링크를 통해 만든 본인 링크

# 쿠팡 파트너스 본인 AF 코드
AFCODE = 'AF4962993'

# 본인들이 만든 쿠팡 채널 아이디 default를 쓰고 있다면 빈공란
CHANNELID = 'github1moneydory'

# pause time 정보
PAUSE_TIME = 0.5
LOADING_WAIT_TIME = 3
LOGIN_WAIT_TIME = 180
GENERAL_REQUEST_WAIT_TIME = 0.3  # 일반적인 requests의 속도

# # fake-useragent / user-agent
# # https://domdom.tistory.com/329
# # ua = UserAgent(use_cache_server=True)
# ua = UserAgent(verify_ssl=False)
# user_agent = ua.random
# print(f'User-Agent : {user_agent}')
fixed_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Whale/3.19.166.16 Safari/537.36'

# itemscout category 및 파라미터 선택
# 1차분류: 선택안함,
#        패션의류(1)(여성의류, 여성언더웨어/잠옷, 남성의류, 남성언더웨어/잠옷),
#        패션잡화(2)(양말, 여성신발, 남성신발, 신발용품, 여성가방, 남성가방, 여행용가방/소품, 지갑, 벨트, 모자, 장갑, 선글라스/안경태, 헤어액세서리, 패션소품, 시계, 순금, 주얼리),
#        화장품/미용(3)(스킨케어, 선케어, 클렌징, 마스크/팩, 베이스메이크업, 색조메이크업, 네일케어, 바디케어, 헤어케어, 헤어스타일링, 향수, 뷰티소품, 남성화장품),
#        디이털/가전(4)(학습기기, 게임기/타이틀, PC, PC액세서리, 노트북액세서리, 태블릿PC액세서리, 모니터주변기기, 주변기기, 멀티미디어장비, 저장장치, PC부품, 네트워크장비, 소프트웨어, 노트북, 태블릿PC, 모니터, 휴대폰, 휴대폰악세서리, 카메라/캠코더용품, 광학기기/용품, 영상가전, 음향가전, 이미용가전, 계절가전, 주방가전, 자동차기기),
#        가구/인테리어(5)(침실가구, 거실가구, 주방가구, 수납가구, 아동/주니어가구, 서재/사무용가구, 아웃도어가구, DIY자재/용품, 인테리어소품, 침구단품, 침구세트, 솜류, 카페트/러그, 커큰/블라인드, 수예, 홈데코),
#        출산/육아(6)(분유, 기저귀, 물티슈, 이유식, 아기간식, 수유용품, 유모차, 카시트, 외출용품, 목용용품, 스킨/바디용품, 위생/건강용품, 구강철결용품, 유아세제, 소독/살균용품, 안전용품, 유아가구, 이유식용품, 임부복, 임산부용품, 유아침구, 출산/돌기념품, 신생아의류, 유아동의류, 유아동잡화, 수영복/용품, 유아발육용품, 완구/매트, 인형, 교구, 유아동 주얼리, 유아동언더웨어/잠옷),
#        식품(7)(건강식품, 다이어트식품, 냉동/간편조리식품, 축산물, 반찬, 김치, 음료, 과자/베이커리, 유가공품, 수산물, 농산물, 밀키트, 가루/분말류, 라면/면류, 소스/드레싱, 식용유/오일, 장류, 잼/시럽, 제과/제빵재료, 조미료, 통조림/캔, 주류),
#        스포츠/레저(8)(마라톤용품, 당구용품, 기타스포츠용품, 등산, 캠핑, 골프, 헬스, 요가/필라테스, 인라인스케이트, 스케이트/보드/롤러, 오토바이/스쿠터, 축구, 야구, 농구, 배구, 탁구, 배드민턴, 테니스, 스쿼시, 족구, 볼링, 스킨스쿠버, 검도, 댄스, 권투, 보호용품, 수련용품, 스포츠액세서리, 자전거, 스키/보드, 낚시, 수영),
#        생활/건강(9)(화방용품, 자동차용품, 수집품, 관상어용품, 음반, DVD, 종교, 주방용품, 세탁용품, 건강측정용품, 건강관리용품, 당뇨관리용품, 의료용품, 실버용, 재활운동용품, 물리치료/저주파용품, 좌욕/좌훈용품, 냉온/찜질용품, 구강위생용품, 눈건강용품, 발건강용품, 안마용품, 수납/정리용품, 청소용품, 생활용춤, 원예/식물, 정원/원예용품, 블루레이, 반려동물, 악기, 욕실용품, 문구/사무용품, 공구),
#        여가/생활편의(10)(원데이클래스, 국내여행/체험, 해외여행, 렌터카, 생활편의, 예체능레슨, 자기계발/취미레슨, 홈케어서비스),
#        면세점(11)(화장품, 향수, 시계/기프트, 주얼리, 패션/잡화, 전자제품, 식품/건강),
#        도서(45830)(소설, 시/에세이, 인문, 가정/요리, 경제/경영, 자기계발, 사회/정치, 역사, 종교, 예술/대중문화, 국어/외국어, 자연/과학, 수험서/자격증, 여행, 컴퓨터/IT, 잡지, 청소년, 유아, 어린이, 만화, 외국도서, 건가/취미, 중학교참고서, 고등학교참고서, 초등학교참고서, 중고도서)
# 기간: 최근 30일, 과거선택(날짜선택) (duration 30d 또는 날짜 설정, duration: 2023-03,2023-04 3월부터 4월)
# 성별: 전체, 남성, 여성 (sample. 남성과 여성이면 f,m)
# 연령대: 10, 20, 30, 40, 50, 60 (sample. 20,60 이면 20대부터 60대까지)

# 아이템스카우트 카테고리 (1차 분류만 있을때)
random_itemscout_category_lists = ['패션의류', '패션잡화', '화장품/미용', '디이털/가전', '가구/인테리어',
                                   '출산/육아', '식품', '스포츠/레저', '생활/건강', '여가/생활편의', '면세점', '도서']
random_itemscout_cid_lists = ['1', '2', '3', '4', '5',
                              '6', '7', '8', '9', '10', '11', '45830']

# 추출하고자 하는 각 카테고리별 keyword 수 (네이버 max:500, 아이템스카우트 max: "아이템발굴"을 통한 500)
wanted_item_num = 500

# github pages 를 위한 post md 파일이 저장될 위치
post_md_location = r"C:\Users\sundo\Desktop\workspace\moneydory.github.io\_posts"

# [사용자 입력 정보] ======================================================================================================== END

# [시스템 공통 입력 정보] ======================================================================================================== START

# partner product info
product_name_lists = []  # 상품명
product_discount_rate_lists = []  # 할인률과 원래가격
product_price_lists = []  # 상품가격
product_arrival_time_lists = []  # 도착예정
product_rating_star_lists = []  # star 평가: ex.3.5
product_review_lists = []  # 상품리뷰 수
product_link_lists = []  # 상품 구매 링크
product_image_lists = []  # 상품 이미지
product_short_url_lists = []  # 쿠팡 숏 링크 리스트
shorten_url_lists = []  # 숏링크 생성기로 만든 링크 리스트

##-------------------------------------------------------------------------------------------------------

# itemscout 에서 아이템들 대한 정보 리스트
keyword_id_lists = []  # keyword 아이디
rank_lists = []  # 랭킹
keyword_name_lists = []  # 키워드
no_of_search_total_lists = []  # 검색수
prdCnt_lists = []  # 상품수

# itemscout 에서 각 keyword 에 따른 전반적인 분석을 위한 리스트
competitionIntensity_lists = []  # 경쟁강도 수치
competitionIntensityDesc_lists = []  # 경쟁강도 등급
adClickRateTotal_lists = []  # 광고클릭률 수치
adClickRateTotalDesc_lists = []  # 광고클릭률 등급

# itemscout 에서 각 keyword 에 따른 블로그 카페 분석 리스트
blogCompetitionRatio_lists = []  # 블로그 경쟁강도 수치
blogCompetitionDesc_lists = []  # 블로그 경쟁강도 등급
cafeCompetitionRatio = []  # 카페 경쟁강도 수치
cafeCompetitionDesc_lists = []  # 카페 경쟁강도 등급

# itemscout 에서 각 keyword 에 따른 쿠팡 분석 리스트
coupangCompetitionRatio_lists = []  # 쿠팡 경쟁강도 수치
coupangCompetitionDesc_lists = []  # 쿠팡 경쟁강도 등급

# 랜덤 생성 리스트
itemscout_cid_category_lists = []
itemscout_duration_lists = []
itemscout_age_lists = []
itemscout_gender_list = []

# 랜덤 수 생성 이미 나온 랜덤 번호는 안나오도록 (겹치지 않는 카테고리를 선택하기 위해)
random_number_list = []


# [시스템 공통 입력 정보] ======================================================================================================== END


def init_driver():
    # try :
    #     shutil.rmtree(r"C:\chrometemp")  #쿠키 / 캐쉬파일 삭제(캐쉬파일 삭제시 로그인 정보 사라짐)
    # except FileNotFoundError :
    #     pass

    # if osName not in "Windows":
    #     try:
    #         subprocess.Popen([
    #             '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="~/Desktop/crawling/chromeTemp22"'],
    #             shell=True, stdout=subprocess.PIPE)  # 디버거 크롬 구동
    #     except FileNotFoundError:
    #         subprocess.Popen([
    #             '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="~/Desktop/crawling/chromeTemp22"'],
    #             shell=True, stdout=subprocess.PIPE)
    # else:
    #     try:
    #         subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 '
    #                          r'--user-data-dir="C:\chrometemp22"')  # 디버거 크롬 구동
    #     except FileNotFoundError:
    #         subprocess.Popen(
    #             r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 '
    #             r'--user-data-dir="C:\chrometemp22"')

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    # if osName not in "Windows":
    #     chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]  # 크롬드라이버 버전 확인
    #     try:
    #         driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver', options=chrome_options)
    #     except:
    #         chromedriver_autoinstaller.install(True)
    #         driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver', options=chrome_options)
    # else:
    #     chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]  # 크롬드라이버 버전 확인
    #     try:
    #         driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=chrome_options)
    #     except:
    #         chromedriver_autoinstaller.install(True)
    #         driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=chrome_options)

    # driver = webdriver.Chrome('./chromedriver.exe', options=chrome_options)
    driver = webdriver.Chrome(f'/Users/taesub/Desktop/crawling/chromedriver', options=chrome_options)
    driver.implicitly_wait(LOADING_WAIT_TIME)
    return driver


def itemscout_login(driver):
    driver.get('https://login.aliexpress.com/')
    sleep(LOADING_WAIT_TIME)

    print(f'\n{C_BOLD}{C_RED}{C_BGBLACK}[주의: 3분안에 로그인을 완료해주세요!!!]{C_END}')
    pbar = tqdm(total=LOGIN_WAIT_TIME)
    for x in range(LOGIN_WAIT_TIME):
        sleep(1)
        try:
            driver.find_element(By.CLASS_NAME, 'ng-account-icon')
            break
        except:
            pass
        pbar.update(1)
    pbar.close()


def get_cookies_session(driver, url):
    driver.get(url)
    sleep(LOADING_WAIT_TIME)

    _cookies = driver.get_cookies()
    cookie_dict = {}
    for cookie in _cookies:
        cookie_dict[cookie['name']] = cookie['value']
        print(f"{cookie['name']} | {cookie['value']}")
    # print(cookie_dict)

    _session = requests.Session()
    headers = {
        'User-Agent': fixed_user_agent,
    }
    # print(f'\n{_session.headers}')
    # print(f'\n{_session.cookies}')

    _session.headers.update(headers)  # User-Agent 변경
    print(f'\n{_session.headers}')

    _session.cookies.update(cookie_dict)  # 응답받은 cookies로  변경
    print(f'\n{_session.cookies}')

    # # 셀레니움 웹 드라이버를 종료(drivet.quit())
    # print(f'\n세션 정보를 얻어왔습니다. 셀레니움 웹 드리이버를 종료하겠습니다.')
    #
    # if url == 'https://ch.kakao.com/channels/@issuehouse':  # 이슈 하우스 채널에 대한 페이지일때만 close
    #     driver.close()
    #     driver.quit()

    return _session


def recursive_random_int_no_again(_count):
    if _count == 0:  # 카운트가 0이 되면 작동 종료
        print(random_number_list)
        return
    a = random.randint(1, 12)  # 아쉽지만 수동으로 _count 수를 넣어줌
    while a in random_number_list:
        a = random.randint(1, 12)  # 아쉽지만 수동으로 _count 수를 넣어줌
    random_number_list.append(a)
    _count -= 1  # 카운트를 - 1하고, 함수를 다시 호출 한다.
    recursive_random_int_no_again(_count)


def get_items_for_itemscout(cid, category, duration, ages, gender):
    # itemscout 랜덤 생성 리스트
    global itemscout_cid_category_lists
    itemscout_cid_category_lists = []
    global itemscout_duration_lists
    itemscout_duration_lists = []
    global itemscout_age_lists
    itemscout_age_lists = []
    global itemscout_gender_list
    itemscout_gender_list = []

    global keyword_id_lists
    keyword_id_lists = []  # keyword 아이디
    global rank_lists
    rank_lists = []  # 랭킹
    global keyword_name_lists
    keyword_name_lists = []  # 키워드
    global no_of_search_total_lists
    no_of_search_total_lists = []  # 검색수
    global prdCnt_lists
    prdCnt_lists = []  # 상품수

    headers = {
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://itemscout.io',
        'referer': 'https://itemscout.io/',
        'user-agent': fixed_user_agent,
    }

    data = {
        'duration': parse.quote(duration, encoding="utf-8"),  # url encoding 후 넣어줌
        'genders': parse.quote(gender, encoding="utf-8"),
        'ages': parse.quote(ages, encoding="utf-8")
    }

    response = requests.post(f'https://api.itemscout.io/api/category/{cid}/data', headers=headers, data=data).json()
    # pp(response)

    for idx, item in enumerate(response['data']['data'].items()):
        if idx == wanted_item_num:
            break
        # print(f'{item}')
        # print(f"keywordID(keyword ID): {item[0]}")  # keyword 아이디
        # print(f"rank(랭킹): {item[1]['rank']}")  # 랭킹
        # print(f"keyword(키워드): {item[1]['keyword']}")  # 키워드
        # print(f"total(검색수): {item[1]['monthly']['total']}")  # 검색수
        # print(f"prdCnt(상품수): {item[1]['prdCnt']}")  # 상품수
        print(
            f"{idx + 1}. ID {item[0]} | keyword {item[1]['keyword']} | 랭킹 {item[1]['rank']} | 검색수 {item[1]['monthly']['total']} | 상품수 {item[1]['prdCnt']}")
        itemscout_cid_category_lists.append(category)
        itemscout_duration_lists.append(duration)
        itemscout_age_lists.append(ages)
        itemscout_gender_list.append(gender)
        keyword_id_lists.append(item[0])
        rank_lists.append(item[1]['rank'])
        keyword_name_lists.append(item[1]['keyword'])
        no_of_search_total_lists.append(item[1]['monthly']['total'])
        prdCnt_lists.append(item[1]['prdCnt'])


def get_keyword_stats_for_itemscout():
    global competitionIntensity_lists
    competitionIntensity_lists = []  # 경쟁강도 수치
    global competitionIntensityDesc_lists
    competitionIntensityDesc_lists = []  # 경쟁강도 등급
    global adClickRateTotal_lists
    adClickRateTotal_lists = []  # 광고클릭률 수치
    global adClickRateTotalDesc_lists
    adClickRateTotalDesc_lists = []  # 광고클릭률 등급

    headers = {
        'accept': 'application/json, text/plain, */*',
        'origin': 'https://itemscout.io',
        'referer': 'https://itemscout.io/',
        'user-agent': fixed_user_agent,
    }

    for idx, keyword_id in enumerate(keyword_id_lists):
        response = requests.get(f'https://api.itemscout.io/api/v2/keyword/stats/{keyword_id}', headers=headers).json()
        # pp(response)
        # print(response['data']['competitionIntensity'])  # 경쟁강도 수치
        # print(response['data']['competitionIntensityDesc'])  # 경쟁강도 등급
        # print(response['data']['adClickRateStats']['adClickRateTotal'])  # 광고클릭률 수치
        # print(response['data']['adClickRateStats']['adClickRateTotalDesc'])  # 광고클릭률 등급
        print(
            f"{idx + 1}. 경쟁강도({response['data']['competitionIntensityDesc']}) | 광고클릭률({response['data']['adClickRateStats']['adClickRateTotalDesc']})")
        competitionIntensity_lists.append(response['data']['competitionIntensity'])
        competitionIntensityDesc_lists.append(response['data']['competitionIntensityDesc'])
        adClickRateTotal_lists.append(response['data']['adClickRateStats']['adClickRateTotal'])
        adClickRateTotalDesc_lists.append(response['data']['adClickRateStats']['adClickRateTotalDesc'])
        sleep(GENERAL_REQUEST_WAIT_TIME)


def get_keyword_contents_competition_stats_for_itemscout():
    global blogCompetitionRatio_lists
    blogCompetitionRatio_lists = []  # 블로그 경쟁강도 수치
    global blogCompetitionDesc_lists
    blogCompetitionDesc_lists = []  # 블로그 경쟁강도 등급
    global cafeCompetitionRatio
    cafeCompetitionRatio = []  # 카페 경쟁강도 수치
    global cafeCompetitionDesc_lists
    cafeCompetitionDesc_lists = []  # 카페 경쟁강도 등급

    headers = {
        'accept': 'application/json, text/plain, */*',
        'origin': 'https://itemscout.io',
        'referer': 'https://itemscout.io/',
        'user-agent': fixed_user_agent,
    }

    for idx, keyword_id in enumerate(keyword_id_lists):
        response = requests.get(f'https://api.itemscout.io/api/v2/keyword/contents_competition_stats/{keyword_id}',
                                headers=headers).json()
        # pp(response)
        # print(response['data']['blogCompetitionRatio'])  # 블로그 경쟁강도 수치
        # print(response['data']['blogCompetitionDesc'])  # 블로그 경쟁강도 등급
        # print(response['data']['cafeCompetitionRatio'])  # 카페 경쟁강도 수치
        # print(response['data']['cafeCompetitionDesc'])  # 카페 경쟁강도 등급
        print(
            f"{idx + 1}. 블로그 경쟁강도({response['data']['blogCompetitionDesc']}) | 카페 경쟁강도({response['data']['cafeCompetitionDesc']})")
        blogCompetitionRatio_lists.append(response['data']['blogCompetitionRatio'])
        blogCompetitionDesc_lists.append(response['data']['blogCompetitionDesc'])
        cafeCompetitionRatio.append(response['data']['cafeCompetitionRatio'])
        cafeCompetitionDesc_lists.append(response['data']['cafeCompetitionDesc'])
        sleep(GENERAL_REQUEST_WAIT_TIME)


def get_keyword_coupang_stats_for_itemscout():
    global coupangCompetitionRatio_lists
    coupangCompetitionRatio_lists = []  # 쿠팡 경쟁강도 수치
    global coupangCompetitionDesc_lists
    coupangCompetitionDesc_lists = []  # 쿠팡 경쟁강도 등급

    headers = {
        'accept': 'application/json, text/plain, */*',
        'origin': 'https://itemscout.io',
        'referer': 'https://itemscout.io/',
        'user-agent': fixed_user_agent,
    }

    for idx, keyword_id in enumerate(keyword_id_lists):
        response = requests.get(f'https://api.itemscout.io/api/v2/keyword/coupang_stats/{keyword_id}',
                                headers=headers).json()
        # pp(response)
        # print(response['data']['coupangCompetitionRatio'])  # 쿠팡 경쟁강도 수치
        # print(response['data']['coupangCompetitionDesc'])  # 쿠팡 경쟁강도 등급
        print(f"{idx + 1}. 쿠팡 경쟁강도({response['data']['coupangCompetitionDesc']})")
        coupangCompetitionRatio_lists.append(response['data']['coupangCompetitionRatio'])
        coupangCompetitionDesc_lists.append(response['data']['coupangCompetitionDesc'])
        sleep(GENERAL_REQUEST_WAIT_TIME)


# def shorten_url(link_url):
#     shortener = pyshorteners.Shortener()

#     try:
#         shorten_url = shortener.isgd.short(link_url)  # https://is.gd
#         if shorten_url:
#             print(shorten_url)
#             shorten_url_lists.append(shorten_url)
#             return
#     except Exception as e:
#         print(f'Error: {e}')
#         pass

#     try:
#         shorten_url = shortener.tinyurl.short(link_url)  # https://tinyurl.com
#         if shorten_url:
#             print(shorten_url)
#             shorten_url_lists.append(shorten_url)
#             return
#     except Exception as e:
#         print(f'Error: {e}')
#         pass

#     try:
#         shorten_url = shortener.clckru.short(link_url)  # https://clck.ru
#         if shorten_url:
#             print(shorten_url)
#             shorten_url_lists.append(shorten_url)
#             return
#     except Exception as e:
#         print(f'Error: {e}')
#         pass

#     try:
#         shorten_url = shortener.dagd.short(link_url)  # https://da.gd
#         if shorten_url:
#             print(shorten_url)
#             shorten_url_lists.append(shorten_url)
#             return
#     except Exception as e:
#         print(f'Error: {e}')
#         pass

#     try:
#         shorten_url = shortener.osdb.short(link_url)  # http://osdb.link
#         if shorten_url:
#             print(shorten_url)
#             shorten_url_lists.append(shorten_url)
#             return
#     except Exception as e:
#         print(f'Error: {e}')
#         pass

#     try:
#         shorten_url = shortener.chilpit.short(link_url)  # http://chilp.it
#         if shorten_url:
#             print(shorten_url)
#             shorten_url_lists.append(shorten_url)
#             return
#     except Exception as e:
#         print(f'Error: {e}')
#         pass


def partner_coupang(keyword, _input_num=1):
    # if _input_num == '2':  # 키워드 검색이 아닐때
    #     print('\n' + C_BOLD + C_YELLOW + C_BGBLACK + '[파트너 링크 생성 시작]', C_END)

    global check_random_time

    target_url = 'https://www.coupang.com/np/search?component=&q=' + \
                 str(keyword) + '&channel=user'  # URL

    headers = {'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6,zh;q=0.5',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
               'Accept-Encoding': 'gzip'
               }

    res = requests.get(url=target_url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    descriptions_inner_lists = soup.select('div.descriptions-inner')
    image_lists = soup.select('dt.image')

    if len(descriptions_inner_lists) < 10:
        print('검색된 결과가 없거나 10개 이하입니다. 다시금 시도하세요')
        check_random_time = 1
        return 0
    else:
        print('검색된 상품 수량 : ', len(descriptions_inner_lists))

    # # Top 10개만 리스트에 담기 (사용되는 리스트 설명)
    # product_name_lists = []  # 상품명
    # product_discount_rate_lists = []  # 할인률과 원래가격
    # product_price_lists = []  # 상품가격
    # product_arrival_time_lists = []  # 도착예정
    # product_rating_star_lists = []  # star 평가: ex.3.5
    # product_review_lists = []  # 상품리뷰 수
    # product_link_lists = []  # 상품 구매 링크
    # product_image_lists = []  # 상품 이미지

    for inner in descriptions_inner_lists[:10]:
        product_name = inner.select_one('div > div.name')  # 상품명
        if product_name is not None:
            # print(product_name.text)
            product_name_lists.append(product_name.text)
        else:
            product_name_lists.append('No data')
        product_discount_rate = inner.select_one('div.price-wrap > div.price > span.price-info')  # 할인률과 원래가격
        if product_discount_rate is not None:
            # print(product_discount_rate.text.lstrip())
            product_discount_rate_lists.append(f'{product_discount_rate.text.lstrip()}원')
        else:
            product_discount_rate_lists.append('')
        product_price = inner.select_one('div.price-wrap > div.price > em > strong')  # 상품가격
        if product_price is not None:
            # print(product_price.text.replace(",", ""))
            product_price_lists.append(f"{product_price.text}원")
        else:
            product_price_lists.append('No data')
        product_arrival_time = inner.select_one('div.price-wrap > div.delivery > span.arrival-info')  # 도착예정
        if product_arrival_time is not None:
           # print(product_arrival_time.text)
            product_arrival_time_lists.append("상품페이지 참조") #
        else:
            product_arrival_time_lists.append('No data')
        product_rating_star = inner.select_one(
            'div.other-info > div.rating-star > span.star > em.rating')  # star 평가: ex.3.5
        if product_rating_star is not None:
            # print(product_rating_star.text)
            product_rating_star_lists.append(product_rating_star.text)
        else:
            product_rating_star_lists.append('No data')
        product_review = inner.select_one('div.other-info > div > span.rating-total-count')  # 상품리뷰 수
        if product_review is not None:
            # print(re.sub("[()]", "", product_review.text))
            product_review_lists.append(re.sub("[()]", "", product_review.text))
        else:
            product_review_lists.append('0')

    product_links = soup.select('a.search-product-link')  # 상품 구매 링크
    for link in product_links[:10]:  # 상품 구매 링크 리스트에 넣기
        p_link = "https://www.coupang.com" + link['href']
        product_link_lists.append(p_link)

    for image in image_lists[:10]:
        product_image = image.select_one('img.search-product-wrap-img')  # 상품 이미지
        # print(product_image)

        p_image = product_image.get('data-img-src')

        if p_image is None:
            p_image = product_image.get('src')
            p_image = f'https:{p_image}'
            # print(p_image)
            product_image_lists.append(p_image)
        else:
            p_image = f'https:{p_image}'
            # print(p_image)
            product_image_lists.append(p_image)


    # 출력
    count = 1
    for product_name, product_discount_rate, product_price, product_arrival_time, product_rating_star, product_review, product_link, product_image in zip \
                (product_name_lists, product_discount_rate_lists, product_price_lists, product_arrival_time_lists,
                 product_rating_star_lists,
                 product_review_lists, product_link_lists, product_image_lists):
        print(
            f'{count}. {product_name} | {product_discount_rate} | {product_price} | {product_arrival_time} | {product_rating_star} | {product_review} | \n{product_link} | \n{product_image}\n')
        count = count + 1

    # -----------------------------------------------------------------------
    # 쿠팡 API 가 없는 사람들을 위한 쿠팡 링크 생성
    # -----------------------------------------------------------------------

    def getPageKey(coupangurl):
        # URL에서 숫자 부분을 추출하는 정규표현식
        pattern = r"/products/(\d+)"

        # 정규표현식에 맞는 부분 찾기
        match = re.search(pattern, coupangurl)

        pagekey = ''
        # 숫자를 추출한 결과 출력
        if match:
            extracted_number = match.group(1)
            pagekey = extracted_number
        else:
            pagekey = 0

        return pagekey

    def getProductType(coupangurl):
        product_type = 'AFFTDP'
        if '/vp/' in coupangurl:
            product_type = 'AFFSDP'

        return product_type

    def getQueryText(str, coupangurl):
        parsed_url = urlparse(coupangurl)
        query_params = parse_qs(parsed_url.query)

        value = query_params.get(str, [None])[0]
        return value

    def makeDirectPartnersLink(coupangurl):
        traceid = 'V0-153'
        coupang_product_type = getProductType(coupangurl)
        pagekey = getPageKey(coupangurl)

        itemId = getQueryText('itemId', coupangurl)
        vendorItemId = getQueryText('vendorItemId', coupangurl)

        channelid = CHANNELID

        p_url = f"https://link.coupang.com/re/{coupang_product_type}?lptag={AFCODE}&subid={channelid}&pageKey={pagekey}&traceid={traceid}&itemId={itemId}&vendorItemId={vendorItemId}"

        return p_url

    for original_link in product_link_lists[:10]:
        print(makeDirectPartnersLink(original_link))
        product_short_url_lists.append(makeDirectPartnersLink(original_link))

    # -----------------------------------------------------------------------
    # 쿠팡파트너스 API 를 사용한 링크 생성 방법
    # -----------------------------------------------------------------------

    # REQUEST_METHOD = "POST"
    # DOMAIN = "https://api-gateway.coupang.com"
    # URL = "/v2/providers/affiliate_open_api/apis/openapi/v1/deeplink"
    #
    # # Replace with your own ACCESS_KEY and SECRET_KEY
    # COOPANG_ACCESS_KEY = coopang_access_key
    # COOPANG_SECRET_KEY = coopang_secret_key
    #
    # print('쿠팡 파트너스 API 한도(제한) 때문에 쿠팡 링크의 변환은 다소 시간이 걸릴 수 있습니다. 현재는 10초 간격으로 요청을 합니다.')
    # for idx, i in enumerate(product_link_lists[:10]):
    #     coupang_link = i  # 쿠팡링크
    #     REQUEST = {"coupangUrls": [coupang_link]}  # 해당 쿠팡링크 받기
    #
    #     def generateHmac(method, url, api_secret_key, api_access_key):
    #         path, *query = url.split('?')
    #         os.environ['TZ'] = 'GMT+0'
    #         dt_datetime = strftime('%y%m%d', gmtime()) + 'T' + \
    #                       strftime('%H%M%S', gmtime()) + 'Z'  # GMT+0
    #         msg = dt_datetime + method + path + (query[0] if query else '')
    #         signature = hmac.new(bytes(api_secret_key, 'utf-8'),
    #                              msg.encode('utf-8'), hashlib.sha256).hexdigest()
    #
    #         return 'CEA algorithm=HmacSHA256, access-key={}, signed-date={}, signature={}'.format(api_access_key,
    #                                                                                               dt_datetime,
    #                                                                                               signature)
    #
    #     authorization = generateHmac(
    #         REQUEST_METHOD, URL, COOPANG_SECRET_KEY, COOPANG_ACCESS_KEY)
    #     url = "{}{}".format(DOMAIN, URL)
    #     response = requests.request(method=REQUEST_METHOD, url=url,
    #                                 headers={
    #                                     "Authorization": authorization,
    #                                     "Content-Type": "application/json"
    #                                 },
    #                                 data=json.dumps(REQUEST)
    #                                 )
    #
    #     # print(response.json())  #확인
    #     if idx != 0:
    #         time.sleep(5)  # 10초마다 한번씩 (쿠팡 제약 때문)
    #         # - 검색 API: 1시간당 10회
    #         # - 리포트 API: 1시간당 50회
    #         # - 모든 API: 1분당 100회
    #         # - 파트너스 웹의 링크생성 기능: 1분당 50회44
    #
    #     text = response.json()
    #     # print(text)
    #     try:
    #         text_2 = text['data']
    #         print(f'{idx + 1}. {text_2}')
    #     except:
    #         # 없을시 가짜 리스트 생성
    #         text_2 = ['https://www.coupang.com/np/coupangglobal']
    #         # print('except(1) - 가짜 링크 생성')
    #     for i in text_2:
    #         try:
    #             product_short_url = i['shortenUrl']
    #         except:
    #             product_short_url = fake_coopang_link  # 가짜 링크 집어넣기
    #             # print('except(2) - 가짜 링크 생성')
    #         print(product_short_url)  # 확인
    #         product_short_url_lists.append(product_short_url)
    #
    # print("\n최종 쿠팡 파트너스 숏 링크가 생성 되었습니다.")  # 최종 확인

    if len(product_image_lists) < 10:
        check_random_time = 1
        print('product_image_lists, out of range')
        return 0


def make_md_file(input_num, keyword, age='10,10', gender='f,m'):
    # 글 제목 구성
    if input_num == '1':  # 검색을 통한 발행이라면,
        post_title = product_name_lists[0][:69]
    else:  # 검색을 통한 발행이 아니라 datalab 에 의한 랜덤한 내용이라면,
        if gender == 'f,m':
            if age == '10,10':
                post_title = '[10대][전연령] ' + product_name_lists[0][:69]
            elif age == '20,20':
                post_title = '[20대][전연령] ' + product_name_lists[0][:69]
            elif age == '30,30':
                post_title = '[30대][전연령] ' + product_name_lists[0][:69]
            elif age == '40,40':
                post_title = '[40대][전연령] ' + product_name_lists[0][:69]
            elif age == '50,50':
                post_title = '[50대][전연령] ' + product_name_lists[0][:69]
            elif age == '60,60':
                post_title = '[60대][전연령] ' + product_name_lists[0][:69]
            else:
                post_title = f'[{str(age.split(",")[0])}~{str(age.split(",")[1])}대] ' + \
                             product_name_lists[0][:69]
        elif gender == 'f':
            if age == '10,10':
                post_title = '[10대][여성] ' + product_name_lists[0][:69]
            elif age == '20,20':
                post_title = '[20대][여성] ' + product_name_lists[0][:69]
            elif age == '30,30':
                post_title = '[30대][여성] ' + product_name_lists[0][:69]
            elif age == '40,40':
                post_title = '[40대][여성] ' + product_name_lists[0][:69]
            elif age == '50,50':
                post_title = '[50대][여성] ' + product_name_lists[0][:69]
            elif age == '60,60':
                post_title = '[60대][여성] ' + product_name_lists[0][:69]
            else:
                post_title = f'[{str(age.split(",")[0])}~{str(age.split(",")[1])}대][여성] ' + \
                             product_name_lists[0][:69]
        else:
            if age == '10,10':
                post_title = '[10대][남성] ' + product_name_lists[0][:69]
            elif age == '20,20':
                post_title = '[20대][남성] ' + product_name_lists[0][:69]
            elif age == '30,30':
                post_title = '[30대][남성] ' + product_name_lists[0][:69]
            elif age == '40,40':
                post_title = '[40대][남성] ' + product_name_lists[0][:69]
            elif age == '50,50':
                post_title = '[50대][남성] ' + product_name_lists[0][:69]
            elif age == '60,60':
                post_title = '[60대][남성] ' + product_name_lists[0][:69]
            else:
                post_title = f'[{str(age.split(",")[0])}~{str(age.split(",")[1])}대][남성] ' + \
                             product_name_lists[0][:69]

    # HTML content
    partner_announcement = 'https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fb8pNGP%2FbtrH0SmcF5j%2FoLshlkyBZGVAOxyYqnEvOK%2Fimg.jpg'
    naver_datalab_url = 'https://itemscout.io/'

    post_head = f'''---
title: "{keyword} TOP10 추천 - {post_title}"
author: Jirm Shin
categories: shopping
tags: [Top10, shopping]
pin: true
---

해당 게시물에서는 [**분석도구**]({naver_datalab_url})를 이용하여 성별, 연령별 등의 데이터를 바탕으로 [**상품**]({fake_coopang_link})들을 추천해드리고 있습니다.
'''

    post_body = ''
    for item_index in range(len(product_short_url_lists)):
        if (item_index + 1) % 2 == 1:
            align1 = 'left'
            align2 = 'right'
        else:
            align1 = 'right'
            align2 = 'left'
        if product_rating_star_lists[item_index] == 'No data':
            star = '1'
            star_image_link = 'https://user-images.githubusercontent.com/78655692/151471925-e5f35751-d4b9-416b-b41d-a059267a09e3.png'
        else:
            if int(float(product_rating_star_lists[item_index])) <= 2:
                star = '1'
                star_image_link = 'https://user-images.githubusercontent.com/78655692/151471925-e5f35751-d4b9-416b-b41d-a059267a09e3.png'
            elif int(float(product_rating_star_lists[item_index])) <= 4:
                star = '2'
                star_image_link = 'https://user-images.githubusercontent.com/78655692/151471960-29c5febe-c509-4c6d-99f4-a2203eb193c5.png'
            else:
                star = '3'
                star_image_link = 'https://user-images.githubusercontent.com/78655692/151471989-9e21d7a8-a7b6-44b0-b598-2bb204b56b00.png'
        post_body = post_body + f"""
### [{item_index + 1}] {keyword} 판매 순위 <img width="81" alt="star{star}" src="{star_image_link}">

![{keyword} TOP01]({product_image_lists[item_index]}){{: width="300" height="300" .w-50 .{align1}}}


[{product_name_lists[item_index]}]({product_short_url_lists[item_index]})
<br>
- 할인율과 원래가격: {product_discount_rate_lists[item_index]}
- 가격: {product_price_lists[item_index]}
- 도착예정: {product_arrival_time_lists[item_index]}
- star 평가: {product_rating_star_lists[item_index]}
- 리뷰수: {product_review_lists[item_index]}
<br>
<br>
[**[CLICK]**]({product_short_url_lists[item_index]}){{: .{align2}}}
<br>
<br>

---
"""

    post_partner_content = f"<br><br><br><br><br> [💦 💦 💦 파트너스 활동을 통해 일정액의 수수료를 제공받을 수 있습니다]({fake_coopang_link}){{: .right}}"

    post_content = post_head + post_body + post_partner_content

    # 현재 날짜를 이용해 파일명 생성
    yesterday = datetime.datetime.now() - timedelta(days=1)
    timestring = yesterday.strftime('%Y-%m-%d')
    # yesterday = datetime.now() - timedelta(days=1)
    # timestring = yesterday.strftime('%Y-%m-%d')

    # 파일명 생성
    product_name_result = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", product_name_lists[0])  # 특수문자 제거
    filename = f"{timestring}-{keyword}-{product_name_result.replace(' ', '-')}.md"

    # 파일 경로 설정
    blog_directory = post_md_location
    filepath = os.path.join(blog_directory, filename)

    # 파일에 블로그 내용 작성
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(post_content)
        f.close()


# main start
if __name__ == '__main__':
    try:
        start_time = time.time()  # 시작 시간 체크
        now = datetime.datetime.now()
        print("START TIME : ", now.strftime('%Y-%m-%d %H:%M:%S'))
        print("\nSTART...")

        # print('\n' + C_BOLD + C_YELLOW + C_BGBLACK + '[크롬 드라이버 초기화 시작]', C_END)
        # driver = init_driver()
        # sleep(PAUSE_TIME)
        # print('\n' + C_BOLD + C_YELLOW + C_BGBLACK + '[크롬 드라이버 초기화 완료]', C_END)
        #
        # print('\n' + C_BOLD + C_YELLOW + C_BGBLACK + '[아이템 스카우트 로그인 시작(3분안에 로그인을 해주세요)]', C_END)
        # itemscout_login(driver)
        # sleep(PAUSE_TIME)
        # print('\n' + C_BOLD + C_YELLOW + C_BGBLACK + '[아이템 스카우트 로그인 완료]', C_END)
        #
        # print('\n' + C_BOLD + C_YELLOW + C_BGBLACK + '[아이템 스카우트 로그인 후 쿠키값 저장 및 세션 리턴 시작]', C_END)
        # itemscout_session = get_cookies_session(driver, 'https://portals.aliexpress.com/affiportals/web/link_generator.htm')
        # sleep(PAUSE_TIME)
        # print('\n' + C_BOLD + C_YELLOW + C_BGBLACK + '[아이템 스카우트 로그인 후 쿠키값 저장 및 세션 리턴 완료]', C_END)

        while True:
            # partner info
            product_link_lists = []
            product_image_lists = []
            product_name_lists = []
            product_price_lists = []
            product_short_url_lists = []
            shorten_url_lists = []

            print('검색을 통해 파트너 url얻기 원하시면' + C_BOLD +
                  C_RED + '(1)' + C_END + '를 눌러주시고,')
            print('아이템스카우트에서 추천하는 상품에 대한 파트너 url을 얻기 원하신다면' +
                  C_BOLD + C_RED + '(2)' + C_END + '를 눌러주세요')
            print('프로그램을 종료하고 싶으면' + C_BOLD +
                  C_RED + '(q)' + C_END + '를 눌러주세요')
            input_num = input('원하는 번호를 입력하세요 : ')

            # input_num = '2'

            if input_num == 'q':
                break

            if input_num == '1':
                print('입력하신 키는 1 입니다...\n')
                sleep(3)
                query = input('검색 키워드를 입력하세요 : ')
                query = query.replace(' ', '+')

                print('\n' + C_BOLD + C_YELLOW +
                      C_BGBLACK + '[파트너 링크 생성 시작]', C_END)
                ret = partner_coupang(query, input_num)
                if ret == 0:
                    continue
                print('\n' + C_BOLD + C_YELLOW +
                      C_BGBLACK + '[파트너 링크 생성 완료]', C_END)

                # print('\n' + C_BOLD + C_YELLOW + C_BGBLACK +
                #       '[파트너 단축 url 생성 시작]', C_END)
                # for i in range(0, len(product_short_url_lists)):
                #     shorten_url(product_short_url_lists[i])
                # print('\n' + C_BOLD + C_YELLOW + C_BGBLACK +
                #       '[파트너 단축 url 생성 완료]', C_END)

                print('\n' + C_BOLD + C_YELLOW + C_BGBLACK +
                      '[md(mark down) 파일 생성 시작]', C_END)
                make_md_file(input_num, query)
                print('\n' + C_BOLD + C_YELLOW + C_BGBLACK +
                      '[md(mark down) 파일 생성 완료]', C_END)

            elif input_num == '2':
                print('입력하신 키는 2 입니다...\n')
                sleep(2)

                # global random_itemscout_category_lists
                # global random_itemscout_cid_lists

                # 아이템스카우트 카테고리 (1차 분류만 있을때)
                random_itemscout_cid_lists = ['1', '2', '3', '4', '5',
                                              '6', '7', '8', '9', '10', '11', '45830']

                random_number_list = []
                recursive_random_int_no_again(len(random_itemscout_cid_lists))
                print(f'random_number_list >> {random_number_list}')
                count = 1
                for number in random_number_list:
                    print('\n' + C_BOLD + C_YELLOW +
                          C_BGBLACK + 'count : ', count, C_END)
                    print('number of al_list = [' + str(number) + ']')
                    cid = random_itemscout_cid_lists[number - 1]
                    # 아이템스카우트 기간
                    itemscout_duration = '30d'  # (duration 30d 또는 날짜 설정, duration: 2023-03,2023-04 3월부터 4월)
                    # 아이템스카우트 나이
                    random_age_lists = ['10,10', '20,20', '30,30', '40,40', '50,50', '60,60', '10,20', '10,30', '10,40',
                                        '10,50', '10,60', '20,30', '20,40', '20,50', '20,60'
                                        , '30,40', '30,50', '30,60', '40,50', '40,60', '50,60']
                    x = random.randint(0, len(random_age_lists) - 1)
                    itemscout_ages = random_age_lists[x]
                    # 아이템스카우트 성별
                    random_gender_lists = ['f,m', 'f', 'm']  # 전체, 여성, 남성
                    x = random.randint(0, len(random_gender_lists) - 1)
                    itemscout_gender = random_gender_lists[x]

                    # 수동으로 알아보려면 아래의 코드 활용
                    # # 아이템스카우트 성별
                    # itemscout_gender = 'f,m'  # (sample. 남성과 여성이면 f,m)
                    # # 아이템스카우트 나이
                    # itemscout_ages = '10,60'  # (sample. 20,60 이면 20대부터 60대까지)

                    print(
                        f'{C_BOLD}{C_YELLOW}{C_BGBLACK}RANDOM info >>> cid {cid} | duration {itemscout_duration} | age {itemscout_ages} | gender {itemscout_gender} {C_END}')

                    print(f'\n{C_BOLD}{C_YELLOW}{C_BGBLACK}[itemscout 에서 아이템들 리스트를 전체 받기 시작]{C_END}')
                    get_items_for_itemscout(cid, random_itemscout_category_lists[number - 1], itemscout_duration,
                                            itemscout_ages, itemscout_gender)
                    sleep(PAUSE_TIME)
                    print(f'\n{C_BOLD}{C_YELLOW}{C_BGBLACK}[itemscout 에서 아이템들 리스트를 전체 받기 완료]{C_END}')

                    # print(f'\n{C_BOLD}{C_YELLOW}{C_BGBLACK}[itemscout 에서 각 keyword 에 따른 전반적인 분석 시작]{C_END}')
                    # get_keyword_stats_for_itemscout()
                    # sleep(PAUSE_TIME)
                    # print(f'\n{C_BOLD}{C_YELLOW}{C_BGBLACK}[itemscout 에서 각 keyword 에 따른 전반적인 분석 완료]{C_END}')
                    # #
                    # print(f'\n{C_BOLD}{C_YELLOW}{C_BGBLACK}[itemscout 에서 각 keyword 에 따른 블로그 카페 분석 시작]{C_END}')
                    # get_keyword_contents_competition_stats_for_itemscout()
                    # sleep(PAUSE_TIME)
                    # print(f'\n{C_BOLD}{C_YELLOW}{C_BGBLACK}[itemscout 에서 각 keyword 에 따른 블로그 카페 분석 완료]{C_END}')

                    # print(f'\n{C_BOLD}{C_YELLOW}{C_BGBLACK}[itemscout 에서 각 keyword 에 따른 쿠팡 분석 시작]{C_END}')
                    # get_keyword_coupang_stats_for_itemscout()
                    # sleep(PAUSE_TIME)
                    # print(f'\n{C_BOLD}{C_YELLOW}{C_BGBLACK}[itemscout 에서 각 keyword 에 따른 쿠팡 분석 완료]{C_END}')

                    # count = 0  # 처음에는 대기 시간을 가지지 않도록 함
                    print("키워드 데이터 >>> ", keyword_name_lists)
                    for j in range(0, len(keyword_name_lists)):
                        product_link_lists = []
                        product_image_lists = []
                        product_name_lists = []
                        product_price_lists = []
                        product_short_url_lists = []
                        shorten_url_lists = []
                        # sleep(LONG_PAUSE_TIME)
                        if j == 0 or check_random_time == 1:
                            now = datetime.datetime.now()
                            current_hour = now.strftime('%H')
                            today_date = str(datetime.datetime.now())
                            today_date = today_date[:today_date.rfind(
                                ':')].replace('-', '.')
                            print('\n')
                            print(today_date)
                            check_random_time = 0
                            pass
                        else:
                            # random_start_time = random.randint(5400, 7200)  # 각 발행을 random 하게 시작 (90분~120분 사이)
                            # random_start_time = random.randint(3600, 3800)  # 각 발행을 random 하게 시작 (90분~120분 사이)
                            # random_start_time = random.randint(300, 400)
                            random_start_time = random.randint(120, 300)
                            now = datetime.datetime.now()
                            current_hour = now.strftime('%H')
                            today_date = str(datetime.datetime.now())
                            today_date = today_date[:today_date.rfind(
                                ':')].replace('-', '.')
                            print('\n')
                            print('현재 시간: ', today_date)
                            print('다음 시작 시간: ', strftime(
                                "%H:%M:%S", gmtime(random_start_time)))
                            # print('random start time = ', random_start_time)
                            sleep(random_start_time)

                            check_random_time = 0

                        print('\n' + C_BOLD + C_YELLOW +
                              C_BGBLACK + '[파트너 링크 생성 시작]', C_END)
                        print(
                            f'{C_BOLD} {C_YELLOW} {C_BGBLACK} 파트너 검색 상품 : [{x}] {keyword_name_lists[x - 1]} {C_END}')
                        ret = partner_coupang(keyword_name_lists[j], input_num)
                        if ret == 0:
                            continue
                        print('\n' + C_BOLD + C_YELLOW +
                              C_BGBLACK + '[파트너 링크 생성 완료]', C_END)

                        # print('\n' + C_BOLD + C_YELLOW +
                        #       C_BGBLACK + '[단축 url 생성 시작]', C_END)
                        # for t in range(0, len(product_short_url_lists)):
                        #     shorten_url(product_short_url_lists[t])
                        # print('\n' + C_BOLD + C_YELLOW +
                        #       C_BGBLACK + '[단축 url 생성 완료]', C_END)

                        print('\n' + C_BOLD + C_YELLOW + C_BGBLACK +
                              '[md(mark down) 파일 생성 시작]', C_END)
                        make_md_file(input_num, keyword_name_lists[j], itemscout_ages, itemscout_gender)
                        print('\n' + C_BOLD + C_YELLOW + C_BGBLACK +
                              '[md(mark down) 파일 생성 완료]', C_END)

                count = count + 1

            else:
                print("잘못 입력 하였습니다. 1, 2, q 중에서 선택하시기 바랍니다.")
                continue

    finally:
        # driver.close() # 마지막 창을 닫기 위해서는 해당 주석 제거
        # driver.quit()
        end_time = time.time()  # 종료 시간 체크
        ctime = end_time - start_time
        time_list = str(datetime.timedelta(seconds=ctime)).split(".")
        print("\n실행시간(초)", ctime)
        print("실행시간 (시:분:초)", time_list)
        now = datetime.datetime.now()
        print("END TIME : ", now.strftime('%Y-%m-%d %H:%M:%S'))
        print("\nEND...")
