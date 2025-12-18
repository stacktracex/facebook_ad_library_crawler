from ads_downloader.downloader import load_results_from_txt, download_images

from config import FETCH_AD_LIBRARY_FILE,DOWNLOAD_AD_LIBRARY_DIR

if __name__ == "__main__":
    # 读取文件
    results = load_results_from_txt(filename=f"{FETCH_AD_LIBRARY_FILE}")
    print(f"txt 文件中共 {len(results)} 条广告数据")

    download_images(results, out_dir=DOWNLOAD_AD_LIBRARY_DIR)
    print("处理完成")
