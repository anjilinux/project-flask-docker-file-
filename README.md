# restapi
REST API Demo Cloud Brothers

#### HTTPS

```
git clone https://github.com/smugford/restapi.git
```
#### SSH

```
git clone git@github.com:smugford/restapi.git
```
#### Docker Commands

```
docker build -t simple-flask-app:latest .
```
```
docker run -d -p 5000:5000 simple-flask-app
```
#### Run a Request

```
curl http://127.0.0.1:5000/
```

##### Example Response:

```
{"message":"Hello World","timestamp":1649623326}
```
