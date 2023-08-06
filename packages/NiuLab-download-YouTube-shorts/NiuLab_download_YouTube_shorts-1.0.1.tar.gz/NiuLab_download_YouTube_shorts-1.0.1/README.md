# NiuLab-download-YouTube-shorts


NiuLab-download-YouTube-shorts is a Python library that downloads youtube videos with help of their ID.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install NiuLab-crawl-YouTube-screenshots.

```bash
pip install NiuLab-download-YouTube-shorts
```

## Usage

```python
from NiuLab_download_Youtube_shorts import NiuLab_download_Youtube_shorts

NiuLab_download_Youtube_shorts.youtube_download(XLSX_FILE_LOCATION ,DESTINATION_FOLDER)

```
## Example Usage

```python
from NiuLab_download_Youtube_shorts import NiuLab_download_Youtube_shorts

NiuLab_download_Youtube_shorts.youtube_download(r'C:\Users\testUser\PycharmProjects\python_package_test\test_file.xlsx',r'C:\Users\testUser\PycharmProjects\outputFolder')

```

### Dependencies

To use **NiuLab-download-YouTube-shorts** in your application developments, you must have installed the following dependencies : 
 
 - Pandas
 - Youtube-Dl 
 - OpenPyXl


You can install all the dependencies by running the commands below 

**Pandas**
```bash
pip install pandas
```

**Youtube-Dl**
```bash
pip install youtube-dl
```

**OpenPyXL**
```bash
 pip install openpyxl
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

# NOTE : This package is under process of development.

## Some things to remember:

1. It supports "XLSX" filetype as input
2. Provide raw full pathname for input file and output destination folder
3. First column of excel file should contain all id for videos and it should have title as "video_id"

