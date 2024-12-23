<!-- # JSON 🆚 XML

Notes:
- 💡 When it comes to displaying output, an API developer should always allow the client to request the preferred content type, such as JSON or XML
- 💡 Clients can do this by supplying an additional header called `Accept` in the request header

| Response type | Request header              |
|---------------|-----------------------------|
| JSON          | `Accept: application/json `  |
| XML           | `Accept: application/xml`    |
| XML           | `Accept: text/xml `          |


## Key Defferences 

| JSON | XML             |
|---------------|-----------------------------|
| JSON or JavaScript Object Notation is a lightweight and dependency-free data format.       | XML or Extensible Markup Language is a powerful, tag-based data format. It is similar to HTML. XML data can be fairly complex.  |
| The size of JSON data is smaller than XML. So, it takes less bandwidth.          | XML data is lengthier than JSON and takes up more bandwidth.   |
| JSON data is like keys and values.

{

"author": "Jack London",

"title": "Seawolf"

}           | XML is completely tag-based, it does not have key-value pairs like JSON.

<?xml version="1.0" encoding="UTF-8"?>

<root>

   <author>Jack London</author>

   <title>Seawolf</title>

</root>        | 
|  Generating and parsing JSON data is faster than XML and this conversion process requires less memory and computing power.    |     Generating and parsing XML is a complex process, and it usually takes more processing power and memory than processing JSON.     |
|  There is no way to include comments in JSON data.    |     XML data can include comments.     | -->

# JSON 🆚 XML

### Notes:
- 💡 When displaying output, an API developer should allow the client to request their preferred content type, such as JSON or XML.
- 💡 Clients can specify this preference by including an `Accept` header in the request.

| **Response Type** | **Request Header**           |
|--------------------|------------------------------|
| JSON               | `Accept: application/json`  |
| XML                | `Accept: application/xml`   |
| XML                | `Accept: text/xml`          |

---

## Key Differences Between JSON and XML

| **Feature**                      | **JSON**                                                                                  | **XML**                                                                                  |
|-----------------------------------|------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| **Definition**                    | Lightweight and dependency-free data format.                                             | Tag-based data format, similar to HTML, and can be fairly complex.                      |
| **Size and Bandwidth**            | Smaller in size, requiring less bandwidth.                                               | Lengthier, requiring more bandwidth.                                                    |
| **Data Structure**                | Uses key-value pairs. Example:                                                           | Tag-based structure without key-value pairs. Example:                                    |
|                                   | ```json                                                                                  | ```xml                                                                                   |
|                                   | {                                                                                       | <?xml version="1.0" encoding="UTF-8"?>                                                  |
|                                   |   "author": "Jack London",                                                              | <root>                                                                                  |
|                                   |   "title": "Seawolf"                                                                    |     <author>Jack London</author>                                                        |
|                                   | }                                                                                       |     <title>Seawolf</title>                                                              |
|                                   | ```                                                                                     | </root>                                                                                 |
| **Performance**                   | Faster to generate and parse, requiring less memory and computing power.                 | More complex to generate and parse, requiring more processing power and memory.          |
| **Comments**                      | Does not support comments.                                                              | Supports comments.                                                                      |

---

### JSON Array Example:
```json
{
  "items": [1, 2, 3, 4, 5]
}
```
### XML Array Example:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<root>
  <items>
    <element>1</element>
    <element>2</element>
    <element>3</element>
    <element>4</element>
    <element>5</element>
  </items>
</root>
```