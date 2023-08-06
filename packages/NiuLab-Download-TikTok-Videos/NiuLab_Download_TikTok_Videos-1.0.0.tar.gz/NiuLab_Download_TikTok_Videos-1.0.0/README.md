# NiuLab-download-TikTok-videos


NiuLab-download-TikTok-videos is a Python library that downloads tiktok videos with help of their ID.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install NiuLab-download-TikTok-videos.

```bash
pip install NiuLab_download_TikTok_videos
```

## Usage

```python
from NiuLab_download_TikTok_videos import NiuLab_download_TikTok_videos

NiuLab_download_TikTok_videos.tiktok_download(XLSX_FILE_LOCATION ,DESTINATION_FOLDER)

```
## Example Usage

```python
from NiuLab_download_TikTok_videos import NiuLab_download_TikTok_videos

NiuLab_download_TikTok_videos.tiktok_download(r'C:\Users\testUser\PycharmProjects\python_package_test\test_file.xlsx',r'C:\Users\testUser\PycharmProjects\outputFolder')

```

### Dependencies

To use **NiuLab_download_TikTok_videos** in your application developments, you must have installed the following dependencies : 
 
 - Pandas
 - OpenPyXl
 - TikTokApi


You can install all the dependencies by running the commands below 

**Pandas**
```bash
pip install pandas
```

**OpenPyXL**
```bash
 pip install openpyxl
```

**TikTokApi**
```bash
pip install TikTokApi
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

# NOTE : This package is under process of development.

## Some things to remember:

1. It supports "XLSX" filetype as input
2. Provide raw full pathname for input file and output destination folder
3. First column of excel file should contain all id for videos and it should have title as "video_id"

