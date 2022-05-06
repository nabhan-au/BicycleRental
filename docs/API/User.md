# GET user/:id
---
Get user data by using user id authentication token

### Path parementer
| Name | Type | Description |
|------|------|-------------|
|  id  | String | id of bicycle|

<!-- tabs:start -->
#### **Example request**
```
curl -X GET 'https://bicycle-rental/user/5/
    -H 'Authorization: Bearer $ACCESS_TOKEN'
```

#### **Successful response**
return status code **200**
```
{
    'data': {
        'firstname': 'Kale',
        'lastname': 'Rosales',
        'age': 18
    }
}
```
<!-- tabs:end -->

# POST /user/login
---
Post username and password for login

### Json body parementer
| Name | Type | Description |
|------|------|-------------|
|  username  | String | username of this user|
|  password  | String | password of this user|
<!-- tabs:start -->
#### **Example request**
```
curl -X POST 'https://bicycle-rental/user/5/
    -d '{
        'username': 'Kale123',
        'password': 'test123'
    }'
```
#### **Successful response**
return status code **200**
```
{
    'data': {
        'user_id': 3,
        'tpken': token>
    }
}
```
<!-- tabs:end -->