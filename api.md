# AMSHandler - Ant Media Server API Handler

The provided Python script defines a class called `AMSHandler`, which serves as a handler for making HTTP requests to an Ant Media Server (AMS) API. The script utilizes the `requests` library to send HTTP requests and interact with the AMS API.

## Dependencies

- `json` module: Importing the `dumps` function as `json_dumps` for JSON serialization.
- `requests` module: Importing the `request` function for making HTTP requests.
- `time` module: Importing the `sleep` function for handling delays.

## External Module

- `common`: Importing two functions, `error_response` and `success_response`, from the `common` module. These functions are assumed to handle error and success responses but are not provided in the code snippet.

## Constants and Configuration

- **HEADERS**: A dictionary representing the HTTP headers with the key `'accept'` set to `'application/json'`.
- **QUERY_FAIL_SLEEP**: An integer representing the sleep duration (in seconds) when a query fails. Default is set to 30 seconds.
- **QUERY_FAIL_TRIES_COUNT**: An integer representing the maximum number of tries when a query fails. Default is set to 5.

## Class: AMSHandler

### Constructor (`__init__`)

- Initializes the `AMSHandler` object with parameters: `address`, `port`, `application`, `user`, and `password`.
- Performs type checks on the `user` and `password` parameters, raising a `TypeError` if they are not strings or `None`.

### Properties

- `address`, `application`, `password`, and `port`: Getter methods that allow access to the private attributes of the `AMSHandler` instance.

### Method (`get`)

- Sends an HTTP request using the specified method (`GET`, `POST`, `PUT`, or `DELETE`) to the AMS API.
- Parameters:
  - `endpoint`: The API endpoint or a list of endpoint components.
  - `method`: The HTTP method to be used.
  - `data`: Data to be sent in the request body for `POST` requests.
  - `failure_sleep`: Sleep duration (in seconds) in case of a failed request. Default is set to `QUERY_FAIL_SLEEP`.
  - `tries_count`: Maximum number of tries in case of a failed request. Default is set to `QUERY_FAIL_TRIES_COUNT`.
  - `url`: An optional parameter to provide a custom URL for the request.

### Internal Handling

- The method handles retries (`tries_count`) and sleeps (`failure_sleep`) in case of failures.
- The response is parsed as JSON, and successful responses are wrapped in a success response, while failed responses are wrapped in an error response.

### Main Function (`main`)

- A placeholder `main` function with the `pass` statement, indicating no specific functionality.

### Execution Check

- The script checks if it's the main module (`__name__ == '__main__'`) and calls the `main` function if so.
