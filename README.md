# Simple demo application for `Hello World` written in Flask to run in a Production environment.

## Docker

Build Image
```
docker build -t flask_docker .
```

Run Image
```
docker run -p 80:80 flask_docker
```

*OR*

Run named container
```
docker run --name flask_docker_container -p 80:80 flask_docker
```

Open
```
http://localhost:80
```

*Note*
Adding new package to requirements.txt needs to rebuild Docker image as well.