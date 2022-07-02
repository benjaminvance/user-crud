from app.databse import get_db


def output_formatter(results):
    out = []
    for result in results:
        user = {}
        user["first_name"] = result[0]
        user["last_name"] = result[1]
        user["hobbies"] = result[2]
        user["active"] = result[3]
        user["brand"] = result[7]
        user["model"] = result[8]
        user["license_plate"] = result[4]
        user["color"] = result[5]
        user["desription"] = result[6]
        out.append(user)
    return out

    def scan():
        cursor = get_db().execute(
            """SELECT user.last_name,
            user.first_name,
            user.hobbies,
            user.active,
            vehicle.license_plate,
            vehicle.color,
            vehicle_type.description,
            vehicle.brand,
            vehicle.model
            FROM user WHERE active=1""", ())
        results = cursor.fetchall()
        cursor.close()
        return output_formatter(results)
