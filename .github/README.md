# SFDS OOC PERMIT LIST SCREENDOOR MICROSERVICE.PY [![CircleCI](https://circleci.com/gh/SFDigitalServices/ooc-permit-list-sd-mspy.svg?style=svg)](https://circleci.com/gh/SFDigitalServices/ooc-permit-list-sd-mspy)
This microservice returns a list of OOC permits from Screendoor

### Sample Usage
Start WSGI Server
> (ooc-permit-list-sd-mspy)$ gunicorn 'service.microservice:start_service()'

Open with cURL or web browser
> $curl http://127.0.0.1:8000/list/retail

> $curl http://127.0.0.1:8000/list/retail_legacy