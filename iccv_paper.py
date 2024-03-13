import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
import random

# 目标页面URL
url = 'https://openaccess.thecvf.com/ICCV2023?day=all'

# 用于爬取的关键词
keyword = 'segmentation'

# 发起请求获取页面内容
response = requests.get(url)
response.raise_for_status()  # 确保请求成功

# 解析页面内容
soup = BeautifulSoup(response.text, 'html.parser')

# 定义关键词列表
keywords = ["semi-supervised", "omni-supervised","segment"]

cnt=0

# 初始化列表，用于存储论文的信息
papers_info = []

# 遍历页面中所有的论文标题
for title_element in soup.find_all('dt', class_='ptitle'):
    # 获取<a>标签
    a_tag = title_element.find('a', href=True)
    if a_tag:
        title_text = a_tag.text.strip() if a_tag.text else ''
        # 检查标题是否包含任一关键词
        #if any(keyword.lower() in title_text.lower() for keyword in keywords):
        matched_keyword = next((keyword for keyword in keywords if keyword.lower() in title_text.lower()), None)
        if matched_keyword:
            # 提取链接(href属性)
            cnt=cnt+1
            href = a_tag['href']
            print(f"Title: {title_text}")
            print(f"Link: https://openaccess.thecvf.com{href}")
            full_url =f"https://openaccess.thecvf.com{href}"


            # 访问链接，获取摘要
            paper_response = requests.get(full_url)
            paper_response.raise_for_status()
            paper_soup = BeautifulSoup(paper_response.text, 'html.parser')
            print(matched_keyword)
            # 查找并打印摘要内容
            abstract_div = paper_soup.find('div', id='abstract')
            if abstract_div:
                print("Abstract:", abstract_div.text.strip())
            else:
                print("Abstract not found.")

            # 将论文信息添加到列表
            papers_info.append({
                "Title": title_text,
                "Link": full_url,
                "Abstract": abstract_div.text.strip(),
                "Keyword": matched_keyword
            })

            sleep_time = random.uniform(0.2, 1)

            sleep(sleep_time)  # 在请求之间稍作暂停，以减少服务器负担

print(f"总共爬取了{cnt}项")

# 创建DataFrame
papers_df = pd.DataFrame(papers_info)
# 将DataFrame保存为Excel文件
excel_filename = 'ICCV2023_papers_info_semi-supervised_omni-supervised_segment.xlsx'
papers_df.to_excel(excel_filename, index=False)

print(f"Saved {len(papers_info)} papers information to '{excel_filename}'.")