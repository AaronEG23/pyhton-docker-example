
EXAMPLE OF DOCKER + PYTHON + FLASK + WEB PAGE
=============================================

# CREATING DOCKER IMAGES


Create backend image
```
cd backend/
docker build -t python-example-be .
docker run  -p 5000:5000 python-example-be:latest
docker save python-example-be > ./python-example-be.tar
```

Create frontend image

```
cd frontend/
docker build -t python-example-fe .
docker run  -p 5001:5001 python-example-fe:latest
docker save python-example-fe > ./python-example-fe.tar
```
Enter to http://localhost:5001/ and wait for a moment

# LOADING DOCKER IMAGES

Import the image
```
docker load < ./python-example-be.tar
docker load < ./python-example-fe.tar
```

Run the image
```
docker run  -p 5001:5001 python-example-fe:latest
docker run  -p 5000:5000 python-example-be:latest
```

AUTORS
=======

Aaron Elizondo Gamboa

LICENSE
=======

MIT
