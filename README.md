# Recommendation

---
## About
App for manage ...

## Dependencies
- RabbitMQ
  - for init run command:
``` bash
sudo docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.12-management`
```

## Quiq start

1 Create venv:
- for Windows:
``` bash
python -m venv venv
```
``` bash
.\venv\Scripts\activate
```
- for Linux:
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
2 Install requirements:
```bash
pip install -r requirements
```
3 Run app:
```bash
python main.py
```
