# **POST /rent**
--- 
Rent the bicycle with bicycle id and user id

### Header
|**Request Method**|**Content Type**|
|--------------|------------|
|HTTP POST     |application/json|

### Json body parementer
| Name | Type | Description |
|------|------|-------------|
|  id  | String | id of bicycle|

### Example requests
```
curl --request POST 
  --url https://bicycle-rental/rent
  --header 'authorization: Bearer ' 
  --header 'content-type: application/json' 
  --data '{ 
            'bicycle-id': 1 
          }'
```
<!-- tabs:start -->
#### **Success response**
return status code **200**
```
{
  'data': {
    'rented': true
  }
}
```
<!-- tabs:end -->

# **POST /rent/cancel**
---
Cancel renting the bicycle with specific id

### Header
|**Request Method**|**Content Type**|
|--------------|------------|
|HTTP POST     |application/json|

### Json body parementer
| Name | Type | Description |
|------|------|-------------|
|  id  | Integer | id of bicycle|

### Example requests
```
curl --request POST 
  --url https://bicycle-rental/rent/cancel
  --header 'authorization: Bearer ' 
  --header 'content-type: application/json' 
  --data '{ 
            'bicycle-id': 1 
          }'
```
<!-- tabs:start -->
#### **Success response**
return status code **200**
```
{
  'data': {
    'canceled': true
  }
}
```
<!-- tabs:end -->