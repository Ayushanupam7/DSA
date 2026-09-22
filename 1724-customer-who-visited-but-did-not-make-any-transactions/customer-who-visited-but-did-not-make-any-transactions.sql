# Write your MySQL query statement below
-- SELECT 
-- V.CUSTOMER_ID,COUNT(*) AS COUNT_NO_TRANS
-- FROM VISITS AS V
-- LEFT JOIN TRANSACTIONS T 
-- ON V.VISIT_ID = T.VISIT_ID
-- WHERE T.VISIT_ID IS NULL
-- GROUP BY V.CUSTOMER_ID;

# Write your MySQL query statement below
SELECT customer_id, COUNT(*) AS count_no_trans
FROM Visits
LEFT JOIN Transactions on Visits.visit_id = Transactions.visit_id
WHERE transaction_id IS NULL
GROUP BY customer_id;
