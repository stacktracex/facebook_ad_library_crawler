import json
import os
import re
import requests
import datetime

# 关键词
from config import KEYWORD
keyword = KEYWORD

def sanitize(text):
    return re.sub(r'[\\/*?:"<>| ]+', '_', text)

def timestamp_to_date(ts):
    if not ts:
        return "unknown_date"
    # 这里假设 ts 是秒级时间戳
    return datetime.datetime.utcfromtimestamp(ts).strftime("%Y-%m-%d")

def load_results_from_txt(filename="data/ads_results.txt"):
    results = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            results.append(json.loads(line))
    return results

def download_images(results, out_dir="images"):
    os.makedirs(out_dir, exist_ok=True)

    total_ads = len(results)
    total_success = 0
    total_skipped = 0


    for ad_idx, ad in enumerate(results, 1):
        try:
            node = ad.get("node")
            if not node:
                raise ValueError("缺少 node")

            collated_list = node.get("collated_results", [])
            if not collated_list:
                raise ValueError("collated_results 为空")

            collated = collated_list[0]
            snapshot = collated.get("snapshot", {})

            ad_id = collated.get("ad_archive_id", "noid")
            page_name = sanitize(snapshot.get("page_name", "noname"))

            start_date = collated.get("start_date")
            end_date = collated.get("end_date")
            start_date_str = timestamp_to_date(start_date)
            end_date_str = timestamp_to_date(end_date)

            images = snapshot.get("images", [])
            img_count = len(images)

            if img_count == 0:
                print(f"[广告 {ad_idx}/{total_ads}] 无图片，跳过")
                continue

            for img_idx, img in enumerate(images, 1):
                url = img.get("original_image_url") or img.get("resized_image_url")
                if not url:
                    continue

                filename = f"{ad_id}_{page_name}_{start_date_str}_{end_date_str}_img{img_idx}.jpg"
                filepath = os.path.join(out_dir, filename)

                # ⭐⭐⭐ 核心新增逻辑：已存在就跳过 ⭐⭐⭐
                if os.path.exists(filepath):
                    total_skipped += 1
                    print(
                        f"[广告 {ad_idx}/{total_ads}] "
                        f"图片 {img_idx}/{img_count} | 已存在，跳过 ({total_skipped})"
                    )
                    continue

                try:
                    resp = requests.get(url, timeout=10)
                    if resp.status_code == 200:
                        with open(filepath, "wb") as f:
                            f.write(resp.content)
                        total_success += 1
                        print(
                            f"[广告 {ad_idx}/{total_ads}] "
                            f"图片 {img_idx}/{img_count} | "
                            f"累计成功 {total_success} -> {filename}"
                        )
                    else:
                        print(
                            f"[广告 {ad_idx}/{total_ads}] "
                            f"图片 {img_idx}/{img_count} | "
                            f"HTTP {resp.status_code}"
                        )
                except Exception as e:
                    print(
                        f"[广告 {ad_idx}/{total_ads}] "
                        f"图片 {img_idx}/{img_count} | 下载异常: {e}"
                    )

        except Exception as e:
            print(f"[广告 {ad_idx}/{total_ads}] 解析广告数据失败: {e}")

    print(
        f"\n🎉 下载完成：成功 {total_success} | 已存在跳过 {total_skipped}"
    )

