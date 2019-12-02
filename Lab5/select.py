import psycopg2

def getDoctorDetailsByID(doctor_ID):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1234",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="doctors")
        cursor = connection.cursor()

        select_doctor_Query = "SELECT * FROM doctors WHERE doctor_id='" + doctor_ID + "'"

        cursor.execute(select_doctor_Query)
        doctor_records = cursor.fetchone()

        print("Printing Doctor records")
        hospital_Id = str(doctor_records[5])
        print("Doctor Id: ", doctor_records[0])
        print( "Doctor Forename:", doctor_records[1], doctor_records[2])
        print( "Hospital Id:", hospital_Id)
        print( "Joining Date:", doctor_records[6] )
        print( "Speciality:", doctor_records[4] )
        print( "Salary:", doctor_records[3])
#
        select_clinic_Query = "SELECT * FROM clinics WHERE clinic_id='" + hospital_Id + "'"
        cursor.execute(select_clinic_Query)
        clinic_records = cursor.fetchone()

        print("\nPrinting Hospital records")
        print( "Hospital Id:", clinic_records[0])
        print( "Hospital Name:", clinic_records[1] )
        print( "Hospita Address:", clinic_records[2] )
#
    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to get record from  table", error)
#
    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()

getDoctorDetailsByID("52010")
