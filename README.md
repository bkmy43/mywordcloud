# MYWORDCLOUD

## ReDI School project at distruptberlin2017 Hackaton by Tech Crunch

### Backend

to build and run backend run following:

```bash
cd mywordcloud/backend/python-flask-server
docker build -t swagger_server .
docker run -p 8080:8080 swagger_server
```
 or use helper script:
 ```bash
 ./build_and_run.sh
 ```
