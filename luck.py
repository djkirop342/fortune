import requests
import time

from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError

luck_list = ["쥐띠", "소띠", "호랑이띠", "토끼띠", "용띠", "뱀띠", "말띠", "양띠", "원숭이띠", "닭띠", "개띠", "돼지띠"]
headers = { "user-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36" }

def crawling() :
    for item in luck_list :
        url = f"https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query={item} 운세"
        response = requests.get(url, headers=headers)
        name = ""
        
        if name != item :
            name = item
            print(f"\n- {item}")
        else :
            print(f"- {item}\n")
        
        try :
            if response.status_code == 200 :    
                soup = BeautifulSoup(response.content, "html.parser")
                fortune_list = soup.find_all("dl", "_cs_fortune_list")[0]
                dt_tags = fortune_list.find_all("dt")
                dd_tags = fortune_list.find_all("dd")
            
                for dt, dd in zip(dt_tags, dd_tags) :
                    print(f"{dt.get_text()} : {dd.get_text()}")
                    # print(f"yearOfBirth ===> {value.find("dd").get_text()}")
            else :
                print(f"[ERROR] Failed to fetch data for {item} - Status Code: {response.status_code}")
                
            time.sleep(1)  # 각 요청 사이에 대기 (너무 많은 요청 시 크롤링을 못함)
        except HTTPError as e:
            print(e)
        
if __name__ == "__main__" :
    print("크롤링 시작!")
    
    crawling()
    
    print("\n크롤링 끝!")