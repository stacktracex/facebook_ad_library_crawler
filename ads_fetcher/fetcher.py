import requests
import json
import time
from requests.exceptions import SSLError, RequestException

# ads_fetcher/fetcher.py

# 关键词
from config import KEYWORD,ACTIVE_STATUS,MEDIATYPE,START_DATE
keyword = KEYWORD
activeStatus=ACTIVE_STATUS
mediatype=MEDIATYPE
start_date=START_DATE

url = "https://www.facebook.com/api/graphql/"
headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://www.facebook.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&is_targeted_country=false&media_type=all&q=%22rocnovel%22&search_type=keyword_exact_phrase&source=nav-panel",
    "sec-ch-prefers-color-scheme": "light",
    "sec-ch-ua": "\"Chromium\";v=\"142\", \"Google Chrome\";v=\"142\", \"Not_A Brand\";v=\"99\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"142.0.7444.163\", \"Google Chrome\";v=\"142.0.7444.163\", \"Not_A Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "\"\"",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "x-asbd-id": "359341",
    "x-fb-friendly-name": "AdLibrarySearchPaginationQuery",
    "x-fb-lsd": "AdG_59VtGNg"
}
cookies = {
    "datr": "327baAh6gx4MyaZW6FjPMb3a",
    "sb": "4m7baHWP_Twe1m7e_cMCGHGO",
    "ps_l": "1",
    "ps_n": "1",
    "wd": "1920x953",
    "fr": "0T3g6APHoxzwqwMPr..BpLre2..AAA.0.0.BpLrgR.AWc0feuO686HPEE0YLFlkWwXOLs"
}
variables = {
    "activeStatus": f"{activeStatus}",
    "adType": "ALL",
    "bylines": [],
    # 分页标识
    "collationToken": None,
    "contentLanguages": [],
    "countries": ["ALL"],#地区，ALL表示所有国家
    "cursor": None,    # 分页用 cursor，第一页为 None
    "excludedIDs": None, # 排除的广告ID，空表示不过滤
    "first": 10,# 每次请求数量
    "isTargetedCountry": False,
    "location": None,
    "mediaType": f"{mediatype}",#  素材类型筛选
    "multiCountryFilterMode": None,
    "pageIDs": [],
    "potentialReachInput": None,
    "publisherPlatforms": [],
    "queryString": f"{keyword}",# 搜索关键字
    "regions": None,
    "searchType": "keyword_exact_phrase",# 搜索类型，基于关键词
    "sessionID": "767ece17-4041-454d-b3b4-22cab47141d8",
    "sortData": None,
    "source": "NAV_PANEL",
    "startDate": f"{start_date}",# # 开始日期，null表示不限
    "v": "f01af3",
    "viewAllPageID": "0"
}

data_template = {
    "av": "0",
    "__aaid": "0",
    "__user": "0",
    "__a": "1",
    "__req": "5",
    "__hs": "20424.HYP:comet_plat_default_pkg.2.1...0",
    "dpr": "1",
    "__ccg": "EXCELLENT",
    "__rev": "1030476050",
    "__s": "39pn30:znt5dx:k8fd9q",
    "__hsi": "7579197878147677389",
    "__dyn": "7xeUmwlECdwn8K2Wmh0no6u5U4e1Fx-ewSAwHwNw9G2S2q0_EtxG4o0B-qbwgE1EEb87C1xwEwgo9oO0n24oaEd86a3a1YwBgao6C0Mo6i588Etw8WfK1LwPxe2GewbCXwJwmE2eUlwhE2Lw6OyES0gq0K-1LwqobU3Cwr86C1nwf6Eb87u1rwea1ww",
    "__csr": "ghhknirh24AmahnCShHkyiCQlukBQdx54y8uKFra5oW8DgyEpG588oeFoO3qax6eGawkE8Hzo4V2ofo521vwt85ObwTwsU3Wzoiwv9Hweu3e391i04vE09bU6CE1NE0stw2s80sCw08hKfw0ema00Uko05rR5w5dw29U1T80gMw",
    "__hsdp": "l2sO48gO0QxEDoCCgzKbBDrKoxkkH4mAFbZ5Fa2e8zRyEpg5W2jBlwDNF2aJ4pQmAi781FE5u1ww24Ugwraw9K1szU7twgU-bzowx6m02gu02Ai01B4w0iH804JG",
    "__hblp": "00BmwXw1oC0e4w6BBw3WU0wq0aBw0jPU24w5qw3B8nw863-0acw1Eq02bW097xq02-u04AU0_u1Pw47wmo0qPw1wK034-0caw5dw5fU",
    "__sjsp": "l2sO48gO0QxEDoCCgzKbBDrKoxkkH4mAFbZ5Fa2e8zRyEpg5W2jBlwDNF5Gh4pQmAi781FE5u1ww24Ugwraw9K1szU7twkUKdy24po",
    "__comet_req": "94",
    "lsd": "AdG_59VtGNg",
    "jazoest": "2895",
    "__spin_r": "1030476050",
    "__spin_b": "trunk",
    "__spin_t": "1764669520",
    "__jssesw": "1",
    "fb_api_caller_class": "RelayModern",
    "fb_api_req_friendly_name": "AdLibrarySearchPaginationQuery",
    "server_timestamps": "true",
    "variables": None,  # 动态赋值
    "doc_id": "25593754380216290"
}  # 你的 data_template，略去

def get_next_cursor(response_json):
    try:
        page_info = response_json['data']['ad_library_main']['search_results_connection']['page_info']
        if page_info['has_next_page']:
            return page_info['end_cursor']
    except Exception:
        pass
    return None
def fetch_all_ads(max_count=30):
    cursor = None
    all_results = []
    page_num = 1

    while True:
        try:
            variables["cursor"] = cursor
            data = data_template.copy()
            data["variables"] = json.dumps(variables)

            response = requests.post(
                url,
                headers=headers,
                cookies=cookies,
                data=data,
                # timeout=15  # ⭐ 必须
            )

            response.raise_for_status()# 如果 HTTP 状态码不是 2xx（成功），立刻抛异常
            response_json = response.json()

            edges = response_json.get('data', {}) \
                .get('ad_library_main', {}) \
                .get('search_results_connection', {}) \
                .get('edges', [])

            all_results.extend(edges)

            print(f"⭐ 第 {page_num} 页 -> {len(edges)} 条 | 总计 {len(all_results)}")

            if len(all_results) >= max_count:
                print("🎉 达到最大数量，停止")
                break

            cursor = get_next_cursor(response_json)
            if not cursor:
                print("📌 无更多分页")
                break

            page_num += 1
            # time.sleep(2.5)  # ⭐ 极其重要：减速

        except (SSLError, RequestException) as e:
            print("❌ 请求异常，停止采集:", e)

            # 1️⃣ 先把已经抓到的写盘
            save_results_to_txt(
                all_results,
                "data/ads_partial_results.txt"
            )

            # 2️⃣ 错误单独记录
            save_error(e)

            # 3️⃣ 立刻停止
            break

        except Exception as e:
            print("❌ 未知异常:", e)
            save_error(e)
            break

    return all_results

def save_results_to_txt(results, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for item in results:
            if isinstance(item, str):
                # item 已经是 JSON 字符串，直接写
                f.write(item.strip() + "\n")
            else:
                # item 是 dict / list，序列化
                f.write(json.dumps(item, ensure_ascii=False) + "\n")


def save_error(err, filename="data/error.log"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(str(err) + "\n")
