import os
from ads_fetcher.fetcher import fetch_all_ads, save_results_to_txt
from config import KEYWORD,DATA_ADS_FETCH_FILE_NAME
keyword = KEYWORD
data_ads_fetch_results_file_name = DATA_ADS_FETCH_FILE_NAME

if __name__ == "__main__":
    results = fetch_all_ads(max_count=6800)
    print(f"共抓取 {len(results)} 条广告数据")

    # 创建保存目录
    data_dir = "data"
    os.makedirs(data_dir, exist_ok=True)

    # 根据关键词生成文件路径
    filename = os.path.join(data_dir, f"{data_ads_fetch_results_file_name}")

    save_results_to_txt(results, filename=filename)
    print(f"数据已写入 {filename}")
