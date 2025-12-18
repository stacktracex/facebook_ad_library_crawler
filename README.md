# facebook_ad_library_crawler

A crawler for Facebook Ad Library that supports:
- Fetching ad metadata
- Downloading ad creatives (images)
- Modular structure for easy extension

---

## 📁 Project Structure

```text
facebook_ad_library/              # Project root
├── ads_fetcher/                   # Fetching module
│   └── fetcher.py                 # Core fetch logic
│
├── ads_downloader/                # Downloading module
│   └── downloader.py              # Core download logic
├── data/                          # Data output directory
│   └── ads_results.txt            # Fetched ad results
├── run_fetch.py                   # Entry script for fetching ads
├── run_download.py                # Entry script for downloading creatives
└── README.md
