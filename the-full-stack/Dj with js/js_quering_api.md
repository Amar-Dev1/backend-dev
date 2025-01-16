# 📑 Quering APIs using js (Native)

1. `GET` data from APIs .
```js
fetch('http://127.0.0.1:8000/api/menu-items')
    .then(response => response.json())
    .then(data => {
        console.log(data)
    })

```
2. `POST`, `PUT`, `PATCH` data on APIs
- require to add payload. and convert it to string ❗
- best practice to add headers
```js
const payload = {
    "name": "New Item",
    "price": 10.99,
    }
const endpoint = 'http://127.0.0.1:8000/api/menu-items'
fetch(endpoint, 
    {
        method : 'POST',
        headers : {
            'Accept':'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload)
    }
).then(res=> res.json)
.then(data =>{
    console.log(data)
})
```
3. `DELETE` data from APIs
```js
const endpoint = 'http://127.0.0.1:8000/api/menu-items'
fetch(endpoint,
{
    method : 'DELETE',
    headers : {
        'Accept':'application/json',
        'Content-Type': 'application/json',
        }
        }
        )
        .then(res=> res.json)
        .then(data =>{
            console.log(data)
            })
```
## 📑Making authenticated calls with tokens
- just add `bearer` and token in headers
```js
endpoint = 'blablabla'
token = 'blablabla'
...
headers : {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'authentication':'bearer' + token
}
```