from faust import App
from agents import get_person_for_prepare_recommendations   # noqa


app = App('my_faust_service', broker='kafka://localhost:9092')

if __name__ == '__main__':
    app.main()