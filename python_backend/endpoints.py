from drm_server_common import all_keys_set, error_response, get_result_template, success_response


class DRMServerAPIEndpoints:


    def create_credential(self, data : dict) -> dict:

        result_ = get_result_template()
        return result_


    def create_stream(self, data : dict) -> dict:

        result_ = get_result_template()
        return result_


    def create_user(self, data : dict) -> dict:

        result_ = get_result_template()
        return result_


    def delete_credential(self, data : dict) -> dict:

        result_ = get_result_template()
        return result_


    def delete_stream(self, data : dict) -> dict:

        result_ = get_result_template()
        return result_


    def delete_user(self, data : dict) -> dict:

        result_ = get_result_template()
        return result_


    def get_credential(self, data : dict) -> dict:

        if not all_keys_set(data, ['id']):
            return error_response('Missing required parameter(s).')
        result_ = get_result_template()
        return result_


    def get_stream(self, data : dict) -> dict:

        if not all_keys_set(data, ['id']):
            return error_response('Missing required parameter(s).')
        result_ = get_result_template()
        return result_


    def get_user(self, data : dict) -> dict:

        if not all_keys_set(data, ['id']):
            return error_response('Missing required parameter(s).')
        result_ = get_result_template()
        return result_


    def list_credentials(self, data : dict) -> dict:

        result_ = get_result_template()
        return result_


    def list_streams(self, data : dict) -> dict:

        result_ = get_result_template()
        return result_


    def list_users(self, data : dict) -> dict:

        result_ = get_result_template()
        return result_


    def login(self, data : dict) -> dict:

        result_ = get_result_template()
        return result_


    def logout(self, data : dict) -> dict:

        result_ = get_result_template()
        return result_


    def update_admin_credentials(self, data : dict) -> dict:

        result_ = get_result_template()
        return result_


    def update_credential(self, data : dict) -> dict:

        result_ = get_result_template()
        return result_


    def update_stream(self, data : dict) -> dict:

        result_ = get_result_template()
        return result_


    def update_user(self, data : dict) -> dict:

        result_ = get_result_template()
        return result_
