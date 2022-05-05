# GET /bicycle/getall
---
Get all bicycles data in database
<!-- tabs:start -->
#### **Example request**
```
curl "https://bicycle-rental/bicycle/getall"
```
#### **Success response**
return status code **200** with data
```
{
  'data': [{
    'brand' : '6ku',
    'type' : 'fix gear',
    'seat' : 1,
    'user_id' : 3
  },
  {
    'brand' : '3T',
    'type' : 'Mountain Bike',
    'seat' : 2,
    'user_id' : 4
  },
  {
    'brand' : 'AlanBike',
    'type' : 'Mountain Bike',
    'seat' : 1,
    'user_id' : 10
  }]
}
```
<!-- tabs:end -->

# GET /bicycle/get/:id
---
Get bicycle data with specific id
### Path parementer
| Name | Type | Description |
|------|------|-------------|
|  id  | String | id of bicycle|

<!-- tabs:start -->
#### **Example request**
```
curl "https://bicycle-rental/bicycle/get/5"
```
#### **Success response**
return status code **200** with data
```
{
  'data': {
    'brand' : '6ku',
    'type' : 'fix gear',
    'seat' : 1,
    'user_id' : 3
  }
}
```
<!-- tabs:end -->

# PUT /bicycle/edit
---
Edit bicycle data

### Json body parementer
| Name | Type | Description |
|------|------|-------------|
|  id  | Integer | id of bicycle|

<!-- tabs:start -->
#### **Example request**
```
curl -X PUT "https://bicycle-rental/bicycle/edit/
    -H "Authorization: Bearer $ACCESS_TOKEN" 
    -H "Content-type: application/json" 
    -d '{"id": 5}'
```
#### **Success response**
return status code **200**
```
{
  'updated': true
  }
}
```
<!-- tabs:end -->

# DELETE /bicycle/delete
---
Delete bicycle

### Json body parementer
| Name | Type | Description |
|------|------|-------------|
|  id  | Integer | id of bicycle|

<!-- tabs:start -->
#### **Example request**
```
curl -X DELETE "https://bicycle-rental/bicycle/delete 
    -H "Authorization: Bearer $ACCESS_TOKEN" 
    -H "Content-type: application/json" 
    -d '{"id": 5}'
```
#### **Success response**
return status code **200**
```
{
  'deleted': true
  }
}
```
<!-- tabs:end -->
