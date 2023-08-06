# MisskeyAPI
Python wrapper for Miskkey API (WIP)

Sample usage:  

```
from misskey.misskeyapi import MisskeyAPI

misskey = MisskeyAPI("https://your.misskey.instance")  

app_secret = misskey.app_create(
    app_name,
    description,
    permission,
    callbackUrl
    )  

response = misskey.auth_session_generate(app_secret)

if response.ok:

    token = response.json()['token']
    url = response.json()['url']
    input(f'open this url in your browser: {url} and accept it. Then press enter')

else:

    print(response)  

response = misskey.auth_session_userkey(app_secret, token)

if response.ok:

    token = response.json()['accessToken']

else:

    print(response.text) 
```

Store or write down in a safe place this last obtained `token` to further usage with any of the API endpoints that require it (param `i(token)`). 

| **description**       | **Misskey API endpoint**           | **method**            | **params**                                          |
|-----------------------|----------------------------|-----------------------|-----------------------------------------------------|
| i                     | /api/i                     | account_i             | i(token)                                            |
| create app            | /api/app/create            | app_create            | name, description, permission, callbackUrl, session |
| show app              | /api/app/show              | app_show              | app_id, session                                     |
| generate auth session | /api/auth/session/generate | auth_session_generate | app_secret                                          |
| show auth session     | /api/auth/session/show     | auth_session_show     | token                                               |
| auth session userkey  | /api/auth/session/userkey  | auth_session_userkey  | app_secret, token                                   |
| create note           | /api/notes/create          | notes_create          | i(token), visibility, text, local_only              |
| create group          | /api/users/groups/create   | users_groups_create   | i(token), groupId                                   |
| delete group          | /api/users/groups/delete   | users_groups_delete   | i(token), groupId                                   |
