---
title: "Python Urllib ⬇📜"
date: 2021-10-26T20:02:07+02:00
draft: false
toc: true
tags:
  - python
  - scraping
  - code
---

I had to pull some meta data from a media data base and since this tends to
be a go to setup when I use urllib with python. I thought I would make a quick
note regarding cookies and making POST/GET requests accordingly.

## Setting up a HTTP session

The urllib python library allows you to get global session parameters directly
by calling the `build_opener` and `install_opener` methods accordingly. Usually
if you make HTTP requests with empty headers or little to no session data
any script will tend to be blocked when robots are not welcome so while setting
these parameters mitigates such an issue it is advised to be a responsible
end-user.

```python
mycookies = http.cookiejar.MozillaCookieJar()
mycookies.load("cookies.txt")
opener = urllib.request.build_opener(
urllib.request.HTTPCookieProcessor(mycookies)
)
opener.addheaders = [
(
    "User-agent",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
    + "(KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
),
(
    "Accept",
    "text/html,application/xhtml+xml,application/xml;q=0.9,"
    + "image/avif,image/webp,image/apng,*/*;q=0.8,"
    + "application/signed-exchange;v=b3;q=0.9",
),
]
urllib.request.install_opener(opener)
```

The above code snippet sets a user agent and what kind of data the session
is willing to accept. This is generic and simply taken from one of my own
browser sessions. Additionally I load in `cookies.txt` which are the session
cookies that I exported to a file for a given domain from my browser.

## HTTP POST request

Web based APIs will have various methods for interacting but POST requests with
JSON type input/output and occasionally XML but given python's native support
for JSON this is generally the way to do things.

``` python
url = f"{host_name}/api.php"
data = json.dumps(post_data).encode()
req = urllib.request.Request(url, data=data)
meta = urllib.request.urlopen(req)
return json.loads(meta.read())
```

The above code snippet prepares a `req` object for particular `host_name` and
`post_data` which is a dictionary that is encoded to a JSON string. Calling
urlopen on this request will perform a POST request accordingly where if
all works as expected should return a JSON string that is mapped to a python
collection.

In the scenario where the data is returned as an XML string / document, there
is a `xmltodict` python library that will return a python collection. The
downside here is the xml has quite a deep hierarchy that is difficult to
appreciate unless the we get into large xml data structures that can be queried.
For reference the xml parsing will look something like this:

```python
xmltodict.parse(meta.read())
```

## HTTP GET request with BeautifulSoup

Performing GET requests is usually much much most simply since you just need
to determine the appropriate url. Here I included an example where the
`BeautifulSoup` python library is used to container the HTTP response and
search through any links within the response that march a regular expression.

```python
query_url = f"{host_name}/?f_search={tag_name}"
resp_data = urllib.request.urlopen(query_url)
resp_soup = BeautifulSoup(resp_data)
return [ link["href"]
    for link in resp_soup.find_all("a", href=True)
    if re.match( f"{host_name}/g/([0-9a-z]+)/([0-9a-z]+)", link["href"] )
]
```

This is probably the most common use case for the `BeautifulSoup` library and
it is very effective instead of sifting through any html data.
