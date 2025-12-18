# config.py
# 关键词
import json
# dreame|Dreame beauty-06|  goodnovel  webnovel   rocnovel
# KEYWORD = "Dreame beauty-06"
# KEYWORD = "goodnovel"
# KEYWORD = "webnovel"
KEYWORD = "rocnovel"
# 投放状态 ACTIVE 表示正在投放
ACTIVE_STATUS="ACTIVE"
# IMAGE_AND_MEME 图片和meme
MEDIATYPE="IMAGE_AND_MEME"
# START_DATE="""{"max":"2025-12-01","min":"2025-12-17"}"""
# START_DATE="""{"max":"2025-11-01","min":"2025-11-28"}"""
# START_DATE="""{"max":"2025-10-01","min":"2025-10-30"}"""
START_DATE="""{"max":"2025-12-17","min":"2025-10-01"}"""

# 解析 START_DATE，提取 min 的 yyyy-MM 部分
start_date_dict = json.loads(START_DATE)
min_date = start_date_dict.get("min", "")
min_yyyymm = min_date[:7] if len(min_date) >= 7 else "unknown"

DATA_ADS_FETCH_FILE_NAME=f"ads_fetch_results_{KEYWORD}_{min_yyyymm}.txt"
DATA_ADS_DOWNLOAD_DIR_NAME=f"ads_download_results_{KEYWORD}_{min_yyyymm}"


