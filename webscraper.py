from requests import get
from requests.exceptions import RequestException
from contextlib import closing
import re
from bs4 import BeautifulSoup
import requests
import pandas as pd

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException:
        log_error('Error during requests to {0} : {1}'.format(url, str(RequestException)))
        return None

def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

url = input()

raw_html = simple_get(url)
html = BeautifulSoup(raw_html,'html.parser')

data = []
for elt in html.find_all("md-card"):

  data.append([(elt.h4.a.text),elt.div.find_all("div")[1].text[::-1].split(' ',1)[0][::-1],elt.div.find_all("div")[0].text])

df = pd.DataFrame(data,columns = ['Name','Organization','Project'])

df.to_csv('output.csv',index=None)


