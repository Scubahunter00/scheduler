def get_mock_availability():
    availability_map = [
        {
            'availability_periods': [
                {
                    'period_id': 1,
                    'period_name': 'unnamed',
                    'period_start': '2018-10-22:14:20 UTC',
                    'period_end': '2018-11-22:14:20 UTC',
                    'standard_times': {
                        'start': '08:00 UTC',
                        'end': '14:00 UTC'
                        },

                    'friday_times': {
                        'start': '09:00 UTC',
                        'end': '17:00 UTC'
                    },
                    'saturday_times': {
                        'start': '10:00 UTC',
                        'end': '11:00 UTC'
                    },
                    'unavailable_dow': ['sunday']

                },
                {
                    'period_id': 2,
                    'period_name': 'unnamed',
                    'period_start': '2018-11-22:14:20 UTC',
                    'period_end': '2018-12-22:14:20 UTC',
                    'standard_times': {
                        'start': '10:00 UTC',
                        'end': '11:00 UTC'
                    },
                    'unavailable_dow': ['sunday', 'monday', 'tuesday']
                }

                ],
            'exceptions': [
                {'exception_id': '1', "start_time": "2018-11-22:14:20 UTC",
                 "end_time": "2018-11-22:14:20 UTC", "type": "open"}
            ]
        }
    ]
    return availability_map


MOCK_PROVIDER_TYPE_STRING = 'mock'
DB_PROVIDER_TYPE_STRING = 'db'


class ListingAvailabilityDatabase:

    def __init__(self, provider):
        self.provider_type = provider

    def get_availability_mock (self, listing_id, lookup_window, lookup_start_time):
        return get_mock_availability()

    def get_availability_rdbms (self, listing_id, lookup_window, lookup_start_time):
        raise NotImplementedError

    def get_availability(self, listing_id, lookup_window, lookup_start_time):
        if self.provider_type is MOCK_PROVIDER_TYPE_STRING:
            return self.look_username_mock(listing_id, lookup_window, lookup_start_time)
        else:
            if self.provider_type is DB_PROVIDER_TYPE_STRING:
                return self.look_username_rdbms(listing_id, lookup_window, lookup_start_time)
            else:
                raise NotImplementedError

    def is_avaialble_mock(self,requested_date_time, duration_hours=1):
        return True

    def is_avaialble_rdbms(self,requested_date_time, duration_hours):
        raise NotImplementedError

    def is_available(self, listing_id, requested_date_time, duration_hours):
        if self.provider_type is MOCK_PROVIDER_TYPE_STRING:
            return self.is_avaialble_mock(listing_id, requested_date_time, duration_hours)
        else:
            if self.provider_type is DB_PROVIDER_TYPE_STRING:
                return self.is_avaialble_rdbms(listing_id, requested_date_time, duration_hours)
            else:
                raise NotImplementedError