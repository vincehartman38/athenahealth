test = True
clientId = 'XXX'  #Input Client ID Here
clientSecret = 'XXX' #Input Secret Key Here
version = 'v1'
practiceid = 000000 #UPDATE THIS WITH THE PRACTICE ID OF THE CLIENT

api = APIConnection(version, clientId, clientSecret, practiceid, test)

# GET THE DEPARTMENTS OF THE PRACTICE
depts = api.GET('/departments', {
    'showalldepartments': 'false',
    'providerlist': 'false',
    'hospitalonly': 'false',
    'fullproviderlist': 'false',
    'limit': 5000
})

# GET THE PROVIDERS OF THE PRACTICE
provs = api.GET('/providers')
