import requests
from jobspider.util.db import *
from sqlalchemy.sql import text


def notify(token, msg):
    headers = {"Authorization": "Bearer " + token}
    params = {"message": msg}
    requests.post(
        "https://notify-api.line.me/api/notify", headers=headers, params=params
    )


def message(job):
    return "職缺提醒\n「" + job["name"] + "」\n－" + job["company"] + job["url"]


def alert():
    print("notify started")
    metadata = MetaData()
    engine = db_connect()
    create_forum_table(engine)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        alert_query = session.query(Alert)
        alerts = [alert.__dict__ for alert in alert_query.all()]

        for alert in alerts:
            print("alert:", alert)
            title = alert["title"]
            keyword = alert["keyword"]
            area = alert["area"]
            cat = alert["cat"]
            period = alert["period"]
            user_id = alert["user_id"]

            result = (
                session.query(Job.id)
                .filter(
                    Job.name.like("%" + keyword + "%")
                    if keyword is not None
                    else text(""),
                    Job.area.like("%" + area + "%") if area is not None else text(""),
                    Job.alerted == False,
                )
                .count()
            )

            if result:
                print("result:", result)
                user = session.query(Users).get(user_id)

                token = user.__dict__["notify_token"]
                id = alert["id"]
                url = (
                    "https://liff.line.me/1656495409-YPJpOrV4/alertredirect/{}".format(
                        id
                    )
                )
                notify(token, "\n符合{}設定條件的職缺\n今日抓取到了{}個\n{}".format(title, result, url))

        session.query(Job).update({Job.alerted: True})
        # session.query(Job).update({Job.alerted: False})
        session.commit()
        print("notify ended")


if __name__ == "__main__":
    alert()
    # metadata = MetaData()

    # engine = db_connect()
    # create_forum_table(engine)
    # Session = sessionmaker(bind=engine)

    # with Session() as session:
    #     alert_query = session.query(Alert)
    #     alerts = [alert.__dict__ for alert in alert_query.all()]

    #     for alert in alerts:
    #         title = alert['title']
    #         keyword = alert['keyword']
    #         area = alert['area']
    #         cat = alert['cat']
    #         period = alert['period']
    #         user_id = alert['user_id']

    #         result = session.query(Job.id).filter(
    #             Job.name.like("%" + keyword + "%") if keyword is not None else text(""),
    #             Job.area.like("%" + area + "%") if area is not None else text(""),
    #             Job.alerted == False
    #         ).count()

    #         # result = session.query(Job.id).filter(
    #         #     Job.name.like("{}".format(keyword)),
    #         #     Job.area.like("{}".format(area)),
    #         # ).count()

    #         print(alert['title'],result)
