# ascii-coding-challenge

## Usage

In the project directory, launch the Flask application to handle the incoming conversion requests:

```bash
python main.py
```

Then you will be able to call the endpoint to convert ASCII characters in the provided json payload:

```bash
localhost:8888/convert
```

For example, you can curl the endpoint with a provided example payload:
```bash
curl --location --request POST 'localhost:8888/convert' 
--header 'Content-Type: application/json' 
--data-raw '{
    "input": ["@", "g", "h", "i"]
}
'
```
