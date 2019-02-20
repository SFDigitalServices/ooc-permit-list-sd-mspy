# SFDS OOC PERMIT LIST SCREENDOOR MICROSERVICE.PY
This microservice returns a list of OOC permits from Screendoor

### Sample Usage
Start WSGI Server
> (ooc-permit-list-sd-mspy)$ gunicorn 'service.microservice:start_service()'

Open with cURL or web browser
> $curl http://127.0.0.1:8000/list/retail

> $curl http://127.0.0.1:8000/list/retail_legacy