Tentacles API
=============


A really simple RESTful API used to explore CI and CD.

Docker
------

You can find a Docker image at https://hub.docker.com/r/ddellaquila4beeva/tentacles-api/.

To start a container use:
```
docker run --publish 5000:5000 -d ddellaquila4beeva/tentacles-api
```

API Usage
---------

The only resource exposed by this service is a "tentacle",
which has the following data fields:

    name: name of the "Day of Tentacle" character. String type.
    description: a description of the tentacle. String type.

Available endpoints:

| HTTP Method   | URI                              | Action                      |
| ------------- | -------------------------------- | --------------------------- |
| GET           | http://[hostname]/               | Index page                  |
| GET           | http://[hostname]/tentacles      | Retrieve list of tentacles  |
| GET           | http://[hostname]/tentacles/[id] | Retrieve a tentacle         |
| POST          | http://[hostname]/tentacles      | Create a new tentacle       |
| PUT           | http://[hostname]/tentacles/[id] | Update an existing tentacle |
| DELETE        | http://[hostname]/tentacles/[id] | Delete a tentacle           |

Index page
```
$ curl http://127.0.0.1:5000
Welcome to the Tentacles API.
```

Get a list of tentacles
```
$ curl -i http://127.0.0.1:5000/tentacles
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 421
Server: Werkzeug/0.11.9 Python/2.7.11
Date: Fri, 06 May 2016 08:05:24 GMT

{
    "1": {
        "description": "A mutant monster and lab assistant created by mad scientist Dr. Fred Edison.",
        "name": "Purple Tentacle"
    },
    "2": {
        "description": "Harmless and friendly brother of Purple Tentacle.",
        "name": "Green Tentacle"
    },
    "3": {
        "description": "Green Tentacle's friend, he's a nerd with glasses.",
        "name": "Bernard Bernoulli"
    }
}
```

Get a specific tentacle
```
$ curl -i http://127.0.0.1:5000/tentacles/1
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 134
Server: Werkzeug/0.11.9 Python/2.7.11
Date: Fri, 06 May 2016 08:07:14 GMT

{
    "description": "A mutant monster and lab assistant created by mad scientist Dr. Fred Edison.", 
    "name": "Purple Tentacle"
}
```

Add a new tentacle
```
$ curl -i -X POST -H 'Content-Type: application/json' -d '{"name":"Laverne", "description":"Bernard friend."}' http://127.0.0.1:5000/tentacles
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 65
Server: Werkzeug/0.11.9 Python/2.7.11
Date: Fri, 06 May 2016 08:18:10 GMT

{
    "description": "Bernard friend.",
    "name": "Laverne"
}
```

Edit a tentacle
```
$ curl -i -X PUT -H 'Content-Type: application/json' -d '{"name":"Hoagie", "description":"Bernard friend."}' http://127.0.0.1:5000/tentacles/4
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 64
Server: Werkzeug/0.11.9 Python/2.7.11
Date: Fri, 06 May 2016 08:17:14 GMT

{
    "description": "Bernard friend.",
    "name": "Hoagie"
}
```

Delete a tentacle
```
$ curl -i -X DELETE http://127.0.0.1:5000/tentacles/4
HTTP/1.0 204 NO CONTENT
Content-Type: application/json
Content-Length: 0
Server: Werkzeug/0.11.9 Python/2.7.11
Date: Fri, 06 May 2016 08:25:27 GMT

```
