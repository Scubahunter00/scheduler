def get_mock_user_list(self):
    return [{'id': '1003', 'name': 'larry'}, {'id': '1002', 'name': 'moe'}, {'id': '1004', 'name': 'curly'}]


MOCK_PROVIDER_TYPE_STRING = 'mock'
DB_PROVIDER_TYPE_STRING = 'db'


class UserDatabase:

    provider_type = "none"

    def __init__(self, provider):
        self.provider_type = provider

    def look_username_mock(self, id_num):
        user_map = get_mock_user_list()
        for user in user_map:
            if user['id'] is id_num:
                return user['name']

    def look_username_rdbms(self, id_num):
        # TODO
        raise NotImplementedError

    def lookup_username(self, id_num):
        if self.provider_type is MOCK_PROVIDER_TYPE_STRING:
            return self.look_username_mock(id_num)
        else:
            if self.provider_type is DB_PROVIDER_TYPE_STRING:
                return self.look_username_rdbms(id_num)
            else:
                raise NotImplementedError






