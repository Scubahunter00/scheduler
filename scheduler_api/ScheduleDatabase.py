import scheduler_api.ListingAvailabilityDatabase as AvailabilityDB


def get_mock_schedule(self):
    return [{'id': '1', 'name': 'larry'}, {'id': '2', 'name': 'moe'}, {'id': '3', 'name': 'curly'}]


MOCK_PROVIDER_TYPE_STRING = 'mock'
DB_PROVIDER_TYPE_STRING = 'db'


class ScheduleDatabase:

    def __init__(self, provider):
        self.provider_type = provider
        self.availability = AvailabilityDB()

    def __attempt_to_post_viewing(self,scheduling_user_id, listing_id, request_date_time):
        if self.provider_type is MOCK_PROVIDER_TYPE_STRING:
            return True
        else:
            if self.provider_type is DB_PROVIDER_TYPE_STRING:
                raise NotImplementedError

    def request_viewing(self, scheduling_user_id, listing_id, request_date_time):
        if self.availability.is_available(listing_id,request_date_time):
            return self.__attempt_to_post_viewing(scheduling_user_id, listing_id, request_date_time)
        else:
            return False


