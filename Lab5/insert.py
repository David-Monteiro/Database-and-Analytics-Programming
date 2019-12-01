import csv
import psycopg2

try:
    #establish connection with database
    connection = psycopg2.connect(user="postgres",
                                  password="1234",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="doctors")
    cursor = connection.cursor()

    #Open the csv file
    with open('doctors.csv', newline='') as csvDoctors:
        reader = csv.reader(csvDoctors)
        count = 0
        # For each row we read fromthe csv file we make an insert query to the db
        for row in reader:
            #make sure I don't read the first line
            if count != 0:
                if len(row) > 7:
                    #before I insert I make sure the row hasn't been added
                    clinic_exists_query = "SELECT EXISTS(SELECT 1 FROM clinics WHERE name='" + row[3] + "')"
                    doctor_exists_query = "SELECT EXISTS(SELECT 1 FROM clinics WHERE name='" + row[0] + "')"
                    #Only insert clinic if it doesn't exist
                    if not cursor.execute(clinic_exists_query):
                        clinic_insert_query = """ INSERT INTO clinics (name, address, city) VALUES (%s,%s,%s)"""
                        clinic_to_insert = (row[3], row[4], row[5])
                        cursor.execute(clinic_insert_query, clinic_to_insert)
                        connection.commit()
                    clinic_getID_query = "SELECT clinic_id FROM clinics WHERE name='" + row[3] + "'"
                    cursor.execute(clinic_getID_query)
                    clinicID = cursor.fetchone()[0]
                    print(str(count) + ": " + str(clinicID))
                    # Only insert doctor if it doesn't exist
                    if not cursor.execute(doctor_exists_query):
                        doctor_insert_query = """ INSERT INTO doctors (doctor_id, forename, surname, salary, speciality,
                         clinic_id, joining_date) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
                        doctor_to_insert = (row[0], row[1], row[2], row[7], row[6], clinicID, row[8])
                        cursor.execute(doctor_insert_query, doctor_to_insert)
                        connection.commit()
            count = count + 1
        csvDoctors.close()
    print("Data added successfully in doctors db ")
except IOError:
    print("No data available")
except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to insert record into mobile table", error)
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")