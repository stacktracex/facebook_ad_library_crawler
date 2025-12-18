from ads_downloader.downloader import load_results_from_txt, download_images

from config import KEYWORD,DATA_ADS_FETCH_FILE_NAME,DATA_ADS_DOWNLOAD_DIR_NAME
keyword = KEYWORD
data_ads_fetch_results_file_name = DATA_ADS_FETCH_FILE_NAME
data_ads_download_dir_name = DATA_ADS_DOWNLOAD_DIR_NAME

if __name__ == "__main__":
    results = load_results_from_txt(filename=f"data/{data_ads_fetch_results_file_name}")  # 假设存文件也根据关键词命名
    out_dir = f"data/{data_ads_download_dir_name}"  # 根据关键词动态生成文件夹名
    print(f"txt 文件中共 {len(results)} 条广告数据")

    download_images(results, out_dir=out_dir)
    print("处理完成")
