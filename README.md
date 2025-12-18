# facebook_ad_library_crawler
Crawl Facebook's stock library

facebook_ads_scraper/           # 项目根目录
├── ads_fetcher/                # 抓取模块包
│   ├── __init__.py
│   └── fetcher.py              # 抓取核心代码
├── ads_downloader/             # 下载模块包
│   ├── __init__.py
│   └── downloader.py           # 下载核心代码
├── data/                       # 存放抓取结果文件
│   └── ads_results.txt
├── requirements.txt            # 依赖文件
├── run_fetch.py                # 抓取模块入口脚本
├── run_download.py             # 下载模块入口脚本
└── README.md
