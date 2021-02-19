import urllib.request
//Imports a library into the python program....will be used to add the way to find online URLs and download it
import os
//Imports the ability to find if a document exists in the current directory

path= './http_access_log.txt'
//gives the relative pathing to solve in the next step
exists = os.path.exists(path)
// runs a scan to check if the file is in the path we gave it

if exists == False:
// if a false is given then the URL is searched out and the program downloads the inforation requested
    print('Starting file download......')

    url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    urllib.request.urlretrieve(url,'./http_access_log.txt')

    print ('Now we will run some analysis')
    file = open("http_access_log.txt")
    data = file.read()
    occurrences = data.count("1994") 
    // counts the data with the set parameters of 1994 and is repeated for 1995 and saves them as two variables
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
