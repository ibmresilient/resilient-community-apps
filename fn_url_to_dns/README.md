# URL to DNS 

This very simple function just chops a URL down to just the DNS name, this is very useful for instances where a domain might have threat intelligence or be listed in another incident but not the full URL (such as a phishing use case). 

The integration comes with an example workflow but contains no app.config content. 

It is installed via the usual method:

```
pip install fn_url_to_dns-1.0.0.tar.gz
```

```
resilient-circuits customize
```