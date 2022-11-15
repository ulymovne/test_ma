import sqlite3

def get_data(database, query):
    try:
        with sqlite3.connect(database) as db:
            cur = db.cursor()
            cur.execute(query)
            data = cur.fetchall()
            return (1, data)
    except Exception as e:
        print(e)
        return (2, e)

def responce(type:int, data):
    if data[0] == 1:
        if type in [1, 2]:
            prod = data[1]
            resp = {}
            for key, value in prod:
                if key in resp:
                    resp[key].append(value)
                else:
                    resp[key] = [value]
            return f"{resp}"
        else:
            prod = data[1]
            prod.sort()
            return f"{[i[0] + ' - ' + i[1] for i in prod]}"
    else:
        return 'Error database'