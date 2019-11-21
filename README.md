# click through rate prediction

## Data Description:  https://www.kaggle.com/c/expedia-personalized-sort/data

- srch_id -> The ID of the search
- date_time -> Date and time of the search
- site_id -> ID of the Expedia point of sale (i.e. Expedia.com, Expedia.co.uk, Expedia.co.jp, ..)
- visitor_location_country_id  -> The ID of the country the customer is located
- visitor_hist_starrating -> The mean star rating of hotels the customer has previously purchased; **null signifies there is no purchase history on the customer**
- visitor_hist_adr_usd -> The mean price per night (in US$) of the hotels the customer has previously purchased; **null signifies there is no purchase history** on the customer
- prop_country_id -> The ID of the country the hotel is located in
- prop_id -> The ID of the hotel
- prop_starrating -> The star rating of the hotel, from 1 to 5, **0 = no rating**, **the star rating is not known or cannot be publicized.**
- prop_review_score -> The mean customer review score for the hotel on a scale out of 5, rounded to 0.5 increments. A 0 means there have been no reviews, null that the information is not available
- prop_brand_bool -> **+1 if the hotel is part of a major hotel chain; 0 if it is an independent hotel**
- prop_location_score1 -> A (first) **score outlining the desirability of a hotel’s location**
- prop_location_score2 -> A **(second)** score outlining the desirability of the hotel’s location
