import urllib.request

def HTTPGET(url):
    return urllib.request.urlopen(url).read()

def urlIsTorNode(url):
    exoneratorOut = str(HTTPGET(url))
    if("Result is positive" in exoneratorOut):
        return True
    else:
        return False

if __name__ == "__main__":
    print(HTTPGET("https://metrics.torproject.org/exonerator.html?ip=86.59.21.38&timestamp=2018-04-23&lang=en"))

    print(urlIsTorNode("https://metrics.torproject.org/exonerator.html?ip=86.59.21.38&timestamp=2018-04-23&lang=en"))

    print(urlIsTorNode("https://metrics.torproject.org/exonerator.html?ip=10.0.0.1&timestamp=2018-04-23&lang=en"))
