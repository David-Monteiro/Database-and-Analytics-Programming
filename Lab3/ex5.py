###Exercise 5
import xml.etree.ElementTree as ET
import glob
import csv
import json

print(glob.glob("*.xml"))


xmlFile = 'people.xml'
tree = ET.parse(xmlFile)

residents = tree.findall('Resident')

print('People:', len(residents))
print(residents)
csvList = []
with open("csvPeople.json", "w") as jsonfile:
    for res in residents:
        name = res.find('Name').text
        phoneNumber = res.find('PhoneNumber').text
        addresses = []
        resID = res.get("Id")
        print('Name', name)
        print('PhoneNumber', phoneNumber)
        csvList.append(name)
        csvList.append(phoneNumber)

        for address in res.find('Address'):
            address = address.text
            print("\t" + address)
            addresses.append(address)
        print('ID', resID)
        csvList.append(resID)
        csvList.append(addresses)
        json.dump({
            'ID': resID,
            'Name': name,
            'PhoneNumber': phoneNumber,
            'Address': addresses}, jsonfile)
    print("\n")
    print(csvList)

    with open('csvPeople.csv', 'a', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(csvList)
    csvFile.close()
