import requests

def create_incident(title, category, description):
    data = {
        'title': input("Enter Short Details: "), # This will take user input from console but you can hardcode for testing,
        'category': input("Provide Category: "),
        'description': input("Describe the incident: "),
    }
    headers = {'Content-Type': 'application/json'}
    r = requests.post('http://localhost:8000/incidents', json=data, headers=headers) #Update Endpoint details as required)
    if r.status_code == 201: # You can check this in CMD as well if flask is executed locally from Windows machine.
        return 'Incident created'
    else:
        return 'Error creating incident'

print(create_incident('Title', 'Category', 'Description'))
