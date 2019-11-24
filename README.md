# click through rate prediction

### Objective : 
To find how likely the user clicks the search result based on these properties

## Data Description:  https://www.kaggle.com/c/expedia-personalized-sort/data

### General search info

- srch_id -> The ID of the search
- date_time -> Date and time of the search
- site_id -> ID of the Expedia point of sale (i.e. Expedia.com, Expedia.co.uk, Expedia.co.jp, ..)

### Visitor's features

- visitor_location_country_id  -> The ID of the country the customer is located
- visitor_hist_starrating -> The mean star rating of hotels the customer has previously purchased; **null signifies there is no purchase history on the customer** (So we expect to have lots of null values here.)
- visitor_hist_adr_usd -> The mean price per night (in US$) of the hotels the customer has previously purchased; **null signifies there is no purchase history** on the customer. (So we expect to have lots of null values here.)

### Hotel or property features

- prop_country_id -> The ID of the country the hotel is located in
- prop_id -> The ID of the hotel
- **prop_starrating** -> The star rating of the hotel, from 1 to 5, **0 = no rating**, **the star rating is not known or cannot be publicized.**
- **prop_review_score** -> The mean customer review score for the hotel on a scale out of 5, rounded to 0.5 increments. A 0 means there have been no reviews, null that the information is not available
- **prop_brand_bool** -> **+1 if the hotel is part of a major hotel chain; 0 if it is an independent hotel**
- prop_location_score1 -> A (first) **score outlining the desirability of a hotel’s location**
- prop_location_score2 -> A **(second)** score outlining the desirability of the hotel’s location. (So we expect to have lots of null values here because this is **Second desirability**.)
- prop_log_historical_price -> The logarithm of the mean price of the hotel over the last trading period. A **0 will occur if the hotel was not sold** in that period.

- **position** (Important feature I guess) -> Hotel position on Expedia's search results page
- **price_usd** -> **Displayed price of the hotel** for the given search.
- promotion_flag -> +1 if the **hotel had a sale price promotion** specifically displayed

- gross_booking_usd -> Total value of the transaction

### Searching 

- **srch_destination_id** -> the **search ID of the destination** where the hotel search was performed
- srch_length_of_stay ->  Number of nights stay that was searched
- srch_booking_window -> Number of days in the future the hotel stay started from the search date
- srch_adults_count -> The number of adults specified in the hotel room
- srch_children_count -> The number of (extra occupancy) children specified in the hotel room
- **srch_room_count** -> Number of hotel rooms specified in the search
- srch_saturday_night_bool -> +1 if the stay includes a Saturday night, starts from Thursday with a length of stay is less than or equal to 4 nights (i.e. weekend); otherwise 0
- srch_query_affinity_score -> The log of the **probability a hotel will be clicked on in Internet searches** (hence the values are negative)  A null signifies there are no data (i.e. hotel did not register in any searches)
- orig_destination_distance -> **Physical distance between the hotel and the customer at the time of search**. A null means the distance could not be calculated.(Can have lots of null values)
- random_bool -> +1 when the displayed sort was random, 0 when the normal sort order was displayed

### Comparison between Expedia and other competitor, This is individual comparison among the competitor (lots of null values)


- **comp1_rate** -> **+1** if Expedia **has a lower price** than competitor 1 for the hotel;    **0 if the same**;     **-1** if Expedia’s **price is higher** than competitor 1; **null signifies there is no competitive data** (Lots and lots of null values expected)
- comp1_inv -> +1 if competitor 1 does not have availability in the hotel; 0 if both Expedia and competitor 1 have availability; null signifies there is no competitive data (Not understood)
- comp1_rate_percent_diff -> The absolute **percentage difference in price** (if one exists) between Expedia and competitor 1’s price (Expedia’s price the denominator); **null signifies there is no competitive data**

-comp2_rate ....... same 
