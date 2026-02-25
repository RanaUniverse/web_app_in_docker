My simeple web applicaion in Docker.

How to make this docker and run?
```
docker build -t rana_web_app .
```
Below will run the app in the port of 5001 in my host machine.
```
docker run -p 5001:8001 rana_web_app
```

to pass another folder name i will use 
```
docker build --build-arg APP_DIR=/ranauniverse -t image_tag_name .
```