from django.shortcuts import render
from newsapi import NewsApiClient


def Index(request):
    newsapi = NewsApiClient(api_key="3f6bd968728a467d938e457484eccab7")
    topheadlines = newsapi.get_top_headlines( language='en',
                                             country='in'
                                             )

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img)

    return render(request, 'index.html', context={"mylist": mylist})


def bbc(request):
    newsapi = NewsApiClient(api_key="YOUR API KEY")
    topheadlines = newsapi.get_top_headlines(sources='bbc-news')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img)

    return render(request, 'bbc.html', context={"mylist": mylist})