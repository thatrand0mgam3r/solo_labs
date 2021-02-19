import urllib.request
import os

path= './http_access_log.txt'

exists = os.path.exists(path)

print(exists)
if exists == False:

    print('Starting file download......')

    url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    urllib.request.urlretrieve(url,'./http_access_log.txt')

    print ('Now we will run some analysis')
    file = open("http_access_log.txt")
    data = file.read()
    occurrences = data.count("1994")
    occurrences2 = data.count("1995")
    print('Times data was accessed last year:', occurrences)
    print('Times data was accessed in both years:', occurrences + occurrences2)



else:
    print("Hello, this program will allow you to analyze some data.")


    answer = input( "Would you like to start the analysis? Yes or No.... ")
    if answer== 'Yes'or answer =="yes":
        print ("One moment let me process this for you")
        file= open ("http_access_log.txt")
        data = file.read()
        occurrences = data.count("1994")
        occurrences2 = data.count("1995")
        print('Times data was accessed last year:', occurrences)
        print('Times data was accessed in both years:', occurrences+occurrences2)
    else:
        print ("You have selected no. Have a nice day")
