# DRMServerAPIEndpoints Class

The `DRMServerAPIEndpoints` class defines a set of methods representing various functionalities of a Digital Rights Management (DRM) server API. These methods encapsulate operations related to credentials, streams, users, and other common tasks within a DRM system.

## Methods:

### `create_credential`

Creates a new credential and returns a result template using `get_result_template()`.

### `create_stream`

Creates a new stream and returns a result template using `get_result_template()`.

### `create_user`

Creates a new user and returns a result template using `get_result_template()`.

### `delete_credential`

Deletes a credential and returns a result template using `get_result_template()`.

### `delete_stream`

Deletes a stream and returns a result template using `get_result_template()`.

### `delete_user`

Deletes a user and returns a result template using `get_result_template()`.

### `get_credential`

Gets information about a specific credential based on the provided data. If the required parameter 'id' is missing, it returns an error response using `error_response()`; otherwise, it returns a result template using `get_result_template()`.

### `get_stream`

Gets information about a specific stream based on the provided data. If the required parameter 'id' is missing, it returns an error response using `error_response()`; otherwise, it returns a result template using `get_result_template()`.

### `get_user`

Gets information about a specific user based on the provided data. If the required parameter 'id' is missing, it returns an error response using `error_response()`; otherwise, it returns a result template using `get_result_template()`.

### `list_credentials`

Lists all credentials and returns a result template using `get_result_template()`.

### `list_streams`

Lists all streams and returns a result template using `get_result_template()`.

### `list_users`

Lists all users and returns a result template using `get_result_template()`.

### `login`

Performs a login operation and returns a result template using `get_result_template()`.

### `logout`

Performs a logout operation and returns a result template using `get_result_template()`.

### `update_admin_credentials`

Updates admin credentials and returns a result template using `get_result_template()`.

### `update_credential`

Updates a specific credential and returns a result template using `get_result_template()`.

### `update_stream`

Updates a specific stream and returns a result template using `get_result_template()`.

### `update_user`

Updates a specific user and returns a result template using `get_result_template()`.

## Utility Functions:

- `all_keys_set(data, keys)`: A function from `drm_server_common` that checks if all the specified keys are present in the provided data dictionary.
- `error_response(message)`: A function from `drm_server_common` that generates an error response dictionary with the given error message.
- `get_result_template()`: A function from `drm_server_common` that returns a template for a successful response.
- `success_response(data)`: A function from `drm_server_common` (not explicitly used in this code) that generates a success response dictionary with the given data.

Please note that the actual implementation of `all_keys_set`, `error_response`, and `success_response` functions is assumed to be in the `drm_server_common` module, which is not provided in this code snippet.
