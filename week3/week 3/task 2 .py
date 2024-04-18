import urllib.request as req
def getData(url):
    request = req.Request(url,headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    import bs4
    root = bs4.BeautifulSoup(data,"html.parser")
    titles = root.find_all("div",class_="title")
    likes  = root.find_all("div",class_="nrec")
    timelinks = root.find_all("div", class_="title")


    for timelink,title,like in zip(timelinks,titles,likes):
        if title.a != None:
            ArticleTitle=title.a.string

        if like != None:
            like_span = like.find("span")
            if like_span :
                Like_DislikeCount = like_span.string
            else:
                Like_DislikeCount= 0
        if timelink != None:
            link =timelink.a
            if link:
                link2 = link.get("href")
                link3 = "https://www.ptt.cc" + link2



                request2 = req.Request(link3, headers={
                   "cookie": "over18=1",
                   "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36"
                })
                with req.urlopen(request2) as response:
                   data2 = response.read().decode("utf-8")
                root2 = bs4.BeautifulSoup(data2, "html.parser")
                time_span = root2.find_all("span", class_="article-meta-value")
                if len(time_span) >= 4:
                    PublishTime=time_span[3].string

                    file.write(f'{ArticleTitle},{Like_DislikeCount},{PublishTime}\n')
                else:
                   file.write(f'{ArticleTitle},{Like_DislikeCount},No time data found\n')


    nextLink = root.find('a', string='‹ 上頁')
    return nextLink["href"]


with open("article.csv","w",encoding="utf-8") as file:

    Pageurl="https://www.ptt.cc/bbs/Lottery/index.html"
    count = 0
    while count<3:
       Pageurl="https://www.ptt.cc"+getData(Pageurl)
       count+=1





