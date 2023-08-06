## Description

`free-ssl-proxies` is a lightweight Python library that scrapes `ssl` proxies from `https://sslproxies.org/`, 
and provides some convenient objects and caching methods for working with the retrieved proxies. This library 
requires no external Python dependencies to work.


## Usage

### Installation

```commandline
pip3 install .
```

### Importing

```python3
from free_ssl_proxies import proxy_list as pl
```

### First time retrieval

You can iterate through all the proxies currently available on `sslproxies.org` with the following code:
- `profile`: If True, we will attempt to connect through each proxy
- `timeout`: If the timeout is exceeded the proxy object will contain `None` for the `avg_request_time` (relatively slow proxy)

```python3
proxies = pl.ProxyList.from_ssl_proxies_org(profile=True, timeout=1)

for proxy in proxies:
    print(proxy.ip_address, proxy.port, proxy.cc, proxy.country, proxy.google, proxy.avg_request_time)
```


### Caching
`sslproxies.org` refreshes their list every 10 minutes, so it doesn't make sense to constantly hammer their page with 
requests. This package offers a simple caching mechanism that can be used like so:

```python3
proxies = pl.ProxyList.from_ssl_proxies_org(profile=True, timeout=1)

pl.write_proxy_list_to_cache(proxies)
```

To access the cache later:

```python3
proxies = pl.ProxyList.from_cache()
```


### Access

#### By country

You can use either the `country` name `cc` to find proxies.

```python3
for us_proxy in proxies.get_by_country("us"):
    print(us_proxy)
```

#### Fastest

You can get a sorted list of the fastest proxies if profiling has been done.

```python3
for fast_proxy in proxies.get_fastest():
    print(fast_proxy)
```


#### Random

You can get a random proxy selected from the fastest proxies if profiling has been done. If profiling has not been done
then we will pick from the entire pool of available proxies.

```
proxy = proxies.random()
```