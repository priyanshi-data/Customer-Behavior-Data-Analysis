-- QUESTION 1: How much money did we make from Male vs Female customers?
-- Helps marketing see which group spends more.
SELECT gender, SUM(purchase_amount) AS total_revenue 
FROM customer 
GROUP BY gender;

-- QUESTION 2: Which products have the best reviews?
-- Identifies the top 5 items for promotion.
SELECT item_purchased, AVG(review_rating) AS average_rating 
FROM customer 
GROUP BY item_purchased 
ORDER BY average_rating DESC 
LIMIT 5;

-- QUESTION 3: How many customers have shopped with us before?
-- Groups by previous purchase count to understand customer loyalty.
SELECT previous_purchases, COUNT(customer_id) AS number_of_customers
FROM customer
GROUP BY previous_purchases
ORDER BY previous_purchases DESC;

-- QUESTION 4: Do subscribers spend more than non-subscribers?
-- Checks if the subscription plan actually drives higher spending.
SELECT subscription_status, AVG(purchase_amount) AS average_spend
FROM customer
GROUP BY subscription_status;

-- QUESTION 5: Does shipping method affect how much people spend?
-- Compares spending between Express, Standard, and Next Day shipping.
SELECT shipping_type, AVG(purchase_amount) AS average_spend
FROM customer
GROUP BY shipping_type;