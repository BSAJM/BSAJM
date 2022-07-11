
from Students import Students
student = Students
from Application import Application
from ApplicationExceptions import ApplicationExceptionsError
from StudentExceptions import *
StringEnd = "or choose QUIT to exit"
userEntry = Application()


def ShowApplicantsIhs():
    ListIhs = 1
    for entry in userEntry.applicants:
        print(f"{ListIhs} {str(entry)}")
        ListIhs += 1

def Display():

    print("IHS Student Data.")
    print("To add a Student to the system, choose ADD")
    print("To remove a Student from the system, choose REMOVE")
    print("To show all students in the system, press SHOW")
    print("To leave datastore, press QUIT")
    print("")

def UserRetrieval():
    string = {"add", "remove", "quit"}
    option = input()
    while not any(str in str for str in option):
        pass
    return option

def DataInput():
    dataEntry = prompt_add_information()
    try:
        userEntry.add_applicant(dataEntry)
    except ApplicationExceptionsError as fail:
        print(f"{str(fail)}")
ELIGIBLE_COUNTRY = ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Republic_of_Cyprus', 'Czech_Republic', 'Denmark',
                         'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy', 'Latvia',
                         'Lithuania', 'Luxembourg', 'Malta', 'Netherlands', 'Poland', 'Portugal', 'Romania', 'Slovakia',
                       'Slovenia', 'Spain', 'Sweden', 'Switzerland']


def prompt_add_information():
    first_name = ''
    last_name = ''
    email = ''
    telephone = ''
    ihs_number = ''
    visa_share_code = ''
    country_of_origin = ''
    length_of_study = ''
    field_of_study = ''
    first_time_applicant = ''
    would_recommend_service = ''
    id_primary_key = ''

    while True:
        try:
            while first_name == "":
                first_name = input(f'Enter the applicants first name {StringEnd}: ').upper()
                if first_name == "QUIT":
                    return


            while last_name == "":
                last_name = input(f'Enter the applicants last name {StringEnd}: ').upper()
                if last_name == "QUIT":
                    return

            while email == "":
                email = input(f'Enter the applicants email address {StringEnd}: ').upper()
                if email == "QUIT":
                    return

            while telephone == "":
                telephone = int(input(f'Enter the applicants telephone number {StringEnd}: '))
                if telephone == "QUIT":
                    return

            while ihs_number == "":
                try:
                    ihs = (input(f'Enter the applicants ihs_number {StringEnd}: '))
                    if ihs == "QUIT":
                        return
                    ihs_number = (f'IHS {ihs}')

                except IhsNumberError:
                    print ('IHS NUMBER can be found on your ihs email correspondence')


            while visa_share_code == "":
                visa_share_code = input(f'Enter the applicants visa share code {StringEnd}: ').upper()
                if visa_share_code == "QUIT":
                    return

            while country_of_origin == "":
                try:
                    origin = (input(f'Enter the applicants country of origin {StringEnd}: '))
                    if origin == "QUIT":
                           return
                    country_of_origin = input(f'Enter the applicants country of origin {StringEnd}: ').upper()

                except EligibleCountryError:
                    print ('It is unlikely you are eligible for a refund')

            while length_of_study == "":
                length_of_study = int(input(f'Enter the applicants study time in this country {StringEnd}: '))
                if length_of_study == "QUIT":
                    return

            while field_of_study == "":
                field_of_study = input(f'Enter the applicants field of study {StringEnd}: ').upper()
                if field_of_study == "QUIT":
                    return

            while first_time_applicant == "":
                first_time_applicant = input(f'Enter yes or no whether this is a first application {StringEnd}; ').upper()
                if first_time_applicant =="QUIT":
                    return

            while would_recommend_service == "":
                would_recommend_service = input(f'Enter the yes or no if the applicant would recommend the service {StringEnd}: ').upper()
                if would_recommend_service == "QUIT":
                    return

            while id_primary_key == "":
                id_primary_key = int(input(f'Enter the applicants unique primary key {StringEnd}: '))
                if id_primary_key == "QUIT":
                    return

            stuDetail = Students(first_name = first_name, last_name = last_name, email = email, telephone = telephone, ihs_number = ihs_number, visa_share_code = visa_share_code, country_of_origin = country_of_origin, length_of_study = length_of_study, field_of_study = field_of_study, first_time_applicant = first_time_applicant, would_recommend_service = would_recommend_service, id_primary_key = id_primary_key)
            return stuDetail

        except IhsNumberError as e:
            print(f'{str(e)}')
            ihs_number = ""

        except VisaShareError as e:
            print(f'{str(e)}')
            visa_share_code = ""

        except LengthOfStudyError as e:
            print(f'{str(e)}')
            length_of_study = ""

def DeleteApplicantIhs():
    try:
        applicant = AccessApplicantIhs('2')
        userEntry.remove_student(applicant)
    except ValueError as e:
            print(f"{str(e)}")
    else:
        print("No applicants stored ")
        print("")

def AccessApplicantIhs(operation):
    ListPosition = IhsApplicantPositionInList(f'{operation} applicant position: ')
    try:
        return userEntry.getStuff(ListPosition - 1)
    except:
        print("")

def IhsApplicantPositionInList(message):
    ListPosition = input(message)
    while not ListPosition.isnumeric() or int(ListPosition) <= 0 or int(ListPosition) >= 11:
        print("There is not such position, value must be between 1 and 10")
        ListPosition = input(message)
    return int(ListPosition)

def GetIhsStudentDetails():
    try:
        applicant = AccessApplicantIhs('SHOW')
        print(applicant)
    except ValueError as e:
        print(f"{str(e)}")
    else:
        print("No applicants stored ")
        print("")


while True:

    ShowApplicantsIhs()
    Display()

    choices = input("Insert your choice here: ")

    if choices == "ADD":
        DataInput()
    elif choices == "REMOVE":
        DeleteApplicantIhs()
    elif choices == "SHOW":
        GetIhsStudentDetails()
    elif choices == "QUIT":
        choices = input("To quit the application, insert YES, otherwise insert anything ").upper()
        if choices == "YES":
            break
    else:
        pass


    print("You have exited the application")

menu()
