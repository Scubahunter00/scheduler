User Table

| user_id | user_name | first_name | last_name | middle_initial | user_type    |
| ------- | --------- | ---------- | --------- | -------------- | ------------ |
|         |           |            |           |                | buyer,seller |

Seller Preference Table

| seller_id | preferred_contact |      |      |      |      |
| --------- | ----------------- | ---- | ---- | ---- | ---- |
|           |                   |      |      |      |      |

Listings Table

| Name             | Description | type   |
| ---------------- | ----------- | ------ |
| listing_id       |             |        |
| seller_id        |             |        |
| post_date        |             |        |
| price            |             |        |
| street address   |             |        |
| city             |             |        |
| state            |             | CHAR   |
| zip              |             | number |
| square_feet      |             |        |
| num_of_bedrooms  |             |        |
| num_of_bathrooms |             |        |

Listing Details Table

| Name                    | Description    | type |
| ----------------------- | -------------- | ---- |
| mls_num                 |                |      |
| Description             | formatted text |      |
| home_type               |                |      |
| year_built              |                |      |
| style                   |                |      |
| heating                 |                |      |
| cooling                 |                |      |
| parking                 |                |      |
| lot_size                |                |      |
| roof_type               |                |      |
| exterior_materials      |                |      |
| room_count              |                |      |
| flooring                |                |      |
| master_bath_type        |                |      |
| master_bath_description |                |      |
| county                  |                |      |
| elementary_school       |                |      |
| middle_school           |                |      |
| high_school             |                |      |
| num_of_stories          |                |      |

Interior Features Table

| Name       | Description | type |
| ---------- | ----------- | ---- |
| listing_id |             |      |
| feature_id |             |      |



Interior Features List

| Name         | Description                           | type |
| ------------ | ------------------------------------- | ---- |
| feature_id   |                                       |      |
| feature_type | other,spaces,amenities,exterior,green |      |
| feature_name |                                       |      |

Listing Appliances Table

| Name         | Description | type |
| ------------ | ----------- | ---- |
| listing_id   |             |      |
| appliance_id |             |      |

Appliances Table

| Name           | Description | type |
| -------------- | ----------- | ---- |
| appliance_id   |             |      |
| appliance_type |             |      |
| appliance_name |             |      |

