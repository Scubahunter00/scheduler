def get_mock_listing(self):
    return [{'listing_id': '100', 'user_id': '1003', 'address': '1002 Bee Tee Lane', 'city': "PleasantView", "state": 'TN',
             "zip": '37146'}, {'listing_id': '101', 'user_id': '1002', 'address': '1032 Peach Lane', 'city': "PleasantView",
            "state": 'TN', "zip": '37146'}, {'listing_id': '102', 'user_id': '1004', 'address': '32 Main Street',
            'city': "PleasantView", "state": 'TN', "zip": '37146'}]


MOCK_PROVIDER_TYPE_STRING = 'mock'
DB_PROVIDER_TYPE_STRING = 'db'


class ListingDatabase:

    provider_type = "none"

    def __init__(self, provider):
        self.provider_type = provider

    def look_listing_mock(self, id_num):
        listing_map = get_mock_listing()
        for listing in listing_map:
            if listing['id'] is id_num:
                return listing['name']

    def look_listing_rdbms(self, id_num):
        # TODO
        raise NotImplementedError

    def lookup_listing(self, id_num):
        if self.provider_type is MOCK_PROVIDER_TYPE_STRING:
            return self.look_username_mock(id_num)
        else:
            if self.provider_type is DB_PROVIDER_TYPE_STRING:
                return self.look_username_rdbms(id_num)
            else:
                raise NotImplementedError






