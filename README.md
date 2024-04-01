# Recommendation

---
## About
Сервис для создания персональных рекоммендаций

## Learning

- Запустите jupyter сервер: `./jupyter.sh`
- Используйте [notebooks](./notebooks/) чтобы сгенерировать артифакты

## Inference

- Установите snap и выполните инструкцию ниже по сетапу dvc
- Сетап сервиса базовый [по доке из сервиса api](https://github.com/EDSEDA/api/blob/main/README.md)
- Запустите сервис: `python main.py`


### DVC

В корне проекта

Единожды:
1. (Linux) sudo snap install dvc --classic
1. (MacOS) brew install dvc
2. dvc init
3. dvc remote add --default grifon gdrive://18ZcB-GjivhdO2LkZFKZ4niACshUyTuGu
4. dvc remote modify grifon gdrive_acknowledge_abuse true
5. dvc remote modify grifon gdrive_use_service_account true
6. Получить токен от https://t.me/Vorkov_Nikita
7. dvc remote modify grifon --local gdrive_service_account_json_file_path <путь_к_токену>

Для версионирования новых моделей:
- dvc add <папка с моделями>

Для отправки на гугл диск:
- dvc push

Для скачивания с гугл диска:
- dvc pull
