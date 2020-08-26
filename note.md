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

* Scrapy 블로그 크롤링
  * Scrapy - Request 이해
  * CSS Selector
  * XPath Selector
  * 블로그 Title 수집

  ```python
  scrapy crawl test2 -o result.jl -t jsonlines
  ```

  * Scrapy 블로그 크롤링
    * 페이지 링크 순회
    * 링크 페이지 본문 수집
    * 수집 데이터 다양한 파일 형식 저장
    * Get / Getall / Extract / Extract_first

* Scrapy Shell 활용하기
  * Shell(쉘) 사용 장점
  * 명령어 사용 실습
  * 대상 데이터 수집 실습(CSS, Xpath)
  * Fetch, View, response, request

  ```python
  scrapy shell

  fetch('https://blog.scrapinghub.com')

  response

  response.body

  response.text
  ```

  ```python
  scrapy shell https://blog.scrapinghub.com
  
  response

  fetch('https://www.naver.com')
  
  response.body

  view(response)
  ```

  ```python
  scrapy shell
  
  fetch('https://blog.scrapinghub.com')

  response

  response.url

  response.body

  response.css("div.post-item > div > a::attr('href')").getall()

  response.css("div.post-item > div > a::attr('href')").get()

  response.css("div.post-item > div > a::attr('href')").extract()

  response.css("div.post-item > div > a::attr('href')").extract_first()

  response.xpath('//div[@class="post-item"]/div/a/@href').getall()

  response.headers

  response.meta
  ```

  ```python
  scrapy shell https://www.daum.net --set="ROBOTSTXT_OBEY=False"
  ```

  ```python
  scrapy sehll https://www.daumn.net
  ```