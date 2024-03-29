import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                  password="1234",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="doctors")
    cursor = connection.cursor()

    create_clinic_query = '''CREATE TABLE clinics(
            clinic_id integer GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
            name text NOT NULL,
            address text NOT NULL,
            city text NOT NULL
        ); '''

    create_doctor_query = '''CREATE TABLE doctors(
          doctor_id integer PRIMARY KEY,
          forename text NOT NULL,
          surname text NOT NULL,
          salary numeric NOT NULL,
          speciality text NOT NULL,
          clinic_id integer REFERENCES clinics,
          joining_date DATE NOT NULL 
        ); '''

    cursor.execute(create_clinic_query)
    connection.commit()
    cursor.execute(create_doctor_query)
    connection.commit()
    print("Tables created successfully in doctors db ")


except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to insert record into mobile table", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")