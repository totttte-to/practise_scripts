"""
#-------------------------------------------------------------------
#                                                           
#-------------------------------------------------------------------
#                                                                   
#                   @Project Name : python-scripts                 
#                                                                   
#                   @File Name    : douban_movie_top250.py
#                                                                   
#                   @Programmer   : tongben                          
#                                                                     
#                   @Start Date   : 2020/11/4 8:50 下午               
#                                                                   
#-------------------------------------------------------------------
#                                                                                                                        
#-------------------------------------------------------------------
"""
import requests
import bs4


# 抓取网页
def open_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 "
                      "Safari/537.36 SE 2.X MetaSr 1.0"}
    res = requests.get(url, headers=headers)
    return res


# 解析网页，提取内容
def find_movies(res):
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # 电影名
    names = []
    target = soup.find_all('div', class_='hd')
    for i in target:
        names.append(i.a.span.text)
    # 评分
    ranks = []
    target = soup.find_all('span', class_='rating_num')
    for i in target:
        ranks.append(i.text)
    # 资料
    messages = []
    target = soup.find_all('div', class_='bd')
    for i in target:
        try:
            messages.append(i.p.text.split('\n')[1].strip() + i.p.text.split('\n')[2].strip())
        except:
            continue

    result = []
    length = len(names)
    for i in range(length):
        result.append(names[i] + ',' + ranks[i] + ',' + messages[i] + '\n')

    return result


# 得到总页数
def find_depth(res):
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    depth = soup.find('span', class_='next').previous_sibling.previous_sibling.text

    return int(depth)


def main():
    host = "https://movie.douban.com/top250"
    res = open_url(host)
    depth = find_depth(res)

    result = []
    for i in range(depth):
        url = host + '/?start=' + str(25 * i)
        res = open_url(url)
        result.extend(find_movies(res))

    with open("豆瓣TOP250电影.txt", 'w', encoding='utf-8') as f:
        for each in result:
            f.write(each)


if __name__ == "__main__":
    main()
"""
这是一个入口
Python属于脚本语言，是一行一行执行的
不是像编译语言先将程序编译成二进制再运行，而是动态的从第一行开始逐行执行
if __name__ == "__main__"，可以理解为如果模块是直接被运行的，则代码块被运行；
如果模块是被导入的，则代码块不被运行
就相当于是Python的模拟入口
__name__是内置变量，用于表示当前模块的名字，同时还能反映一个包的结构
python -m：-m参数表示将一个或者包作为脚本运行
__main__.py文件：相当于是一个包的入口程序
"""
