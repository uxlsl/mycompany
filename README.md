
# 实现实现drf最佳实践里面 类似的url

GET /cars/711/drivers/ Returns a list of drivers for car 711
GET /cars/711/drivers/4 Returns driver #4 for car 711



```

(hello) ➜  mycompany git:(master) http http://127.0.0.1:8000/cars/1/dirvers/   
HTTP/1.1 200 OK
Content-Length: 106
Content-Type: application/json
Date: Fri, 09 Feb 2018 06:11:17 GMT
Server: WSGIServer/0.2 CPython/3.6.2
X-Frame-Options: SAMEORIGIN

[
{
    "id": 1,
        "name": "小明1"
},
{
    "id": 2,
    "name": "小光"
},
{
    "id": 3,
    "name": "小红"
}
]

(hello) ➜  mycompany git:(master) http http://127.0.0.1:8000/cars/1/dirvers/2
HTTP/1.1 200 OK
Content-Length: 33
Content-Type: application/json
Date: Fri, 09 Feb 2018 06:11:21 GMT
Server: WSGIServer/0.2 CPython/3.6.2
X-Frame-Options: SAMEORIGIN

{
    "id": 2,
    "name": "小光"
}




```
