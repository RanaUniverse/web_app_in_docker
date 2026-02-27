My simeple web applicaion in Docker.

How to make this docker and run?
```
docker build -t rana_web_app .
```
Below will run the app in the port of 5001 in my host machine.
```
docker run -p 5001:8001 rana_web_app
```

to pass another folder name i will use in the container i will want to have.
```
docker build --build-arg APP_DIR=/ranauniverse -t rana_web_app .
```

Now i will try to keep the caddy here in this project.
First i will run the gunicorn server
then i will run the caddy server which will use https and it will connect with reverse proxy.

The below should start the server goodly.
```
docker compose up --build
```