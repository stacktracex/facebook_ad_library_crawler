# config.py
import json
# 关键词
# dreame|Dreame beauty-06|  goodnovel  webnovel   rocnovel
# KEYWORD = "Dreame beauty-06"
# KEYWORD = "goodnovel"
# KEYWORD = "webnovel"
KEYWORD = "rocnovel"
# 投放状态 ACTIVE 表示正在投放
ACTIVE_STATUS="ACTIVE"
# 素材类型 IMAGE_AND_MEME 图片和meme
MEDIATYPE="IMAGE_AND_MEME"
# 日期范围筛选
# START_DATE="""{"max":"2025-12-01","min":"2025-12-17"}"""
# START_DATE="""{"max":"2025-11-01","min":"2025-11-28"}"""
# START_DATE="""{"max":"2025-10-01","min":"2025-10-30"}"""
START_DATE="""{"max":"2025-12-01","min":"2025-12-01"}"""

# 解析 START_DATE日期
start_date_dict=json.loads(START_DATE)
min_date = start_date_dict.get("min","None")
max_date = start_date_dict.get("max","None")
date_range=min_date+"-"+max_date


# 抓取完要放置的目标文件
FETCH_AD_LIBRARY_FILE=f"data/fetch/ads_fetch_results_{KEYWORD}_{date_range}.txt"
DOWNLOAD_AD_LIBRARY_DIR=f"data/download/{KEYWORD}"

if __name__ == '__main__':
    print(FETCH_AD_LIBRARY_FILE)

