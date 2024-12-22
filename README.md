# 自動化預約登記結婚

## Purpose

因為要預約特殊日期登記結婚，會有很多人一起在線上進行預約，而且內政部的預約平台會有很多欄位的資料需要填寫，因此寫了一個自動化腳本幫我填寫基本資料，最後再手動輸入驗證碼即可完成預約。

## Prerequisite

1. 安裝 Chrome driver 的套件在專案目錄

    在 [Chrome Driver](https://googlechromelabs.github.io/chrome-for-testing/#stable) 下載對應瀏覽器版本的 chrome driver，並且放在專案目錄

    ```bash
    $ tree -L 1
    .
    ├── README.md
    ├── chromedriver  <---- Here
    ├── main.py
    ├── requirements.txt
    └── venv
    ```

2. 安裝套件

    ```bash
    $ python3 -m venv venv
    $ source ./venv/bin/activate
    $ pip install -r requirements.txt
    ```

## Set up `.env` configuration

```bash
$ cp .env.example .env
```

調整 .env 對應的代碼，相關細節可以從 [內政部網路預約申請](https://www.ris.gov.tw/app/portal/671) 用 F12 去看對應的代碼

```.env
# 城市代碼
# 65000 新北市
# 67000 台南市
# 66000 台中市
CITY_AREA_CODE=65000

# 鄉鎮代碼
# 65000010 板橋區
# 65000020 三重區
SITE_AREA_CODE=65000010

# 身分證字號
PERSON_ID="A123456789"

# 聯絡人姓名
CONTACT_PERSON="王小明"

# 戶籍地城市代碼
CITY_REGISTER=65000

# 戶籍地鄉鎮城市代碼
SITE_REGISTER=65000010

# 聯絡人電話
CONTACT_NUMBER="0912345678"

# 預約登記日期 (YYYMMDD)
REGISTER_DATE="1131231"

# 預約時段 (MM01)
RESERVATION_TIME="1101"

# 生日
YEAR_BIRTHDAY="80" 
MON_BIRTHDAY="01"
DAY_BIRTHDAY="01"
```

## Execution

```bash
$ python main.py
```

**資料確認無誤之後，在畫面中輸入驗證碼，接著確認送出，即可完成登記預約**