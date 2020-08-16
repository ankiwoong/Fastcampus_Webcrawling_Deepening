* Scrapy 프레임 워크
  - Scrapy 장점
  - Scrapy 기능 소개
  - Scrapy 설치 방법
    
     ```python
    pip install scrapy
    ```
  
  - 설치 중 에러 발생 해결
    - 셋업 툴 업그레이드
    
    ```python
    pip install --upgrade setuptools
    ```
    
    - Win32 에러 발생 시 -> 윈도우 10
  
    ```python
    pip install pypiwin32
    ```

    - pip upgrade
  
    ```python
    python -m pip install --upgrade pip
    ```

* Scrapy 구조
  - Scrapy 폴더 구조 설명
  - Stratproject

    ```python
    scrapy startproject section01_2
    ```

  - Runspider vs Crawl
    - Runspider(단위 테스트)

    ```python
    scrapy runspider testspider.py
    ```

    - Crawl(운영)

    ```python
    scrapy crawl test1
    ```

  - Genspider

    ```python
    scrapy genspider testspider scrapinghub.com
    ```

  - 기본 값 출력 및 ```--nolog```
    ```python
    scrapy crawl test1 --nolog
    ```