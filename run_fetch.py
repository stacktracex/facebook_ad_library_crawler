import os
from ads_fetcher.fetcher import fetch_all_ads, save_results_to_txt
from config import FETCH_AD_LIBRARY_FILE

if __name__ == "__main__":
    results = fetch_all_ads(max_count=30)
    print(f"共抓取 {len(results)} 条广告数据")

    parent_dir = os.path.dirname(FETCH_AD_LIBRARY_FILE)
    if parent_dir:  # 说明路径里带目录
        os.makedirs(parent_dir, exist_ok=True)

    save_results_to_txt(results, filename=FETCH_AD_LIBRARY_FILE)
    print(f"数据已写入 {FETCH_AD_LIBRARY_FILE}")
