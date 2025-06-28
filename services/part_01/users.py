import requests
<<<<<<< HEAD
=======
API_KEY = "reqres-free-v1"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}"
}

>>>>>>> a827d7aea0c26e0c1897376abcacb4ec6d50c343

def get_user(id):
    url = f"https://reqres.in/api/users/{id}"

    session = requests.session()
<<<<<<< HEAD
    response = session.get(url)
=======
    response = session.get(url,headers=HEADERS)
>>>>>>> a827d7aea0c26e0c1897376abcacb4ec6d50c343

    return response

def get_users_list(page_id):
    url = "https://reqres.in/api/users"

    session = requests.session()
    response = session.get(url, params={'page': page_id})

<<<<<<< HEAD
    return response
=======
    return response
>>>>>>> a827d7aea0c26e0c1897376abcacb4ec6d50c343
