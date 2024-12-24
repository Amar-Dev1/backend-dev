# HTTP Methods 
### 💡 in the world of `REST APIs`, one endpoint can perform multiple tasks. It can deliver a resource, create a new resource, update or delete it.

| HTTP Method | Action                                                                                                                                                   |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **GET**     | Returns the requested resource. If not found, returns a `404 Not Found` status code.                                                                    |
| **POST**    | Creates a record. The `POST` request always comes with an HTTP request body containing JSON or Form URL encoded data, which is also called a payload. If the data is valid, the API endpoint will create a new resource based on these data. Although you can create multiple resources with a single `POST` call, it is not considered a best practice to do so. |
| **PUT**     | Instructs the API to replace a resource. Like a `POST` request, the `PUT` request also comes with data. A `PUT` request usually supplies all data for a particular resource so that the API developer can fully replace that resource with the provided data. A `PUT` request deals with a single resource. |
| **PATCH**   | Tells the API to update a part of the resource. Note the difference between a `PUT` and a `PATCH` call: A `PUT` call replaces the complete resource, while the `PATCH` call only updates some parts. A `PATCH` request also deals with a single record. |
| **DELETE**  | Instructs the API to delete a resource.                                                                                                                  |

## Payload
- 💡 The payload is the data sent in the request body to the server. It can be JSON, XML.
