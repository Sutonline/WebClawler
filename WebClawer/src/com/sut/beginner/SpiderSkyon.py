'''
Usage: find all link of skyon and download
Created on 2016年6月28日

@author: Administrator
'''
from idlelib.IOBinding import encoding
import os
import urllib.request

from bs4 import BeautifulSoup


linkList = [];

def get_content(toUrl, count):
    """Return the content of given url
        Args:
            toUrl: aim url
            count: index of this connect

        Return:
            content if success
            'Fail' if fail
    """
    try:
        opener =  urllib.request.urlopen(toUrl);
        mybytes = opener.read();
        mystr = mybytes.decode("utf8")
        opener.close();
        return mystr;
    except Exception as err:
        print(err);
        return 'Fail'
def get_links(myStr):
    soup = BeautifulSoup(myStr, 'html.parser');
    links = [];
    try:
        for link in soup.find_all('a'):
            hrefContent = str(link.get('href'));
            #这里还要屏蔽一个符号#
            if((hrefContent.startswith('#')) | (hrefContent.startswith('http')) | ('/#' in hrefContent)):
                continue;
            else:
                links.append(hrefContent);
    except Exception as err:
        print('get_links exception:' + err)
        return 'Fail';
    else:
        return links;        

def input_file(filepath, filename, content):
    filepath = 'd:\\webClawer\\skyon';
    filename = os.path.basename(filename);
    try:
        if(os.path.exists(filepath) == False):
            print("路径不存在，将创建")
            os.makedirs(filepath);
        destfile = open(filepath +'\\' + filename, 'wt', encoding = 'utf8');
        print('start writting file ' + filepath + '\\' + filename);
        destfile.write(content);
    except Exception as err:
        print('input_file exception:' + str(err));
        destfile.close();
        return 'Fail';
    else:
        destfile.close();
        return 'Success';

def recursive_get(toUrl):
    global linkList;
    print('start getting ' + toUrl + '...');
    WebContent = get_content(toUrl, 1);
    if(str(WebContent) != 'Fail'):
        strUrl = str(toUrl);
        if(strUrl.endswith('com.cn')):
            input_file('', 'skyon.html', WebContent);
        else:
            input_file('',toUrl, WebContent);
        links = get_links(WebContent);
        if(links != 'Fail'):
            if(len(links) > 0):
                for link in links:
                    url = 'http://www.skyon.com.cn' + '/' + link;
                    #这里增加了一个判断，由哪一个链接进来的，不会再重新去get这个链接
                    #但是，还是出现了一个问题，两个链接互相调用,所以我们应该解决的办法是：
                    #建立一个历史访问数组，如果是在里边的话，就不再访问
                    #
                    if(url in linkList):
                        continue;
                    else:
                        linkList.append(url);
                        recursive_get(url);
                        return;
            else:
                #如果已经没有链接，就退出
                #如果名称是已经访问过的，也需要退出
                return;

if __name__ == '__main__':
    try:
        recursive_get('http://www.skyon.com.cn');
    except Exception as err:
        print('读取错误' + str(err))
    else:
        print('done');    