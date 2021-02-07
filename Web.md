Q: How would you make an HTTP “GET” request with the HTTP “Pragma” request header set to “nocache”?

Answer:
```curl -X GET -I -H "Pragma:no-cache" https://example.com/index.php```

Another way would be to use the Docker container which we have created in the last excercise :)

```
docker build -t testcurl -f Containers.Dockerfile .
docker run --rm testcurl -i -X GET -H "Pragma: no-cache" https://example.com/index.php
```
