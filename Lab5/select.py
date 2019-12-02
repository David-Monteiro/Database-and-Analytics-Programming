import psycopg2

def getDoctorDetailsByID(doctor_ID):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1234",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="doctors")
        cursor = connection.cursor()

        select_Query = "SELECT * FROM doctors WHERE doctor_id='" + doctor_ID + "'"

        cursor.execute(select_Query)
        doctor_records = cursor.fetchall()
        print(doctor_records)

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into  table", error)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

getDoctorDetailsByID("52010")
