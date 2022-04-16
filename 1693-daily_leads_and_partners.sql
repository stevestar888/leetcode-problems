# https://leetcode.com/problems/daily-leads-and-partners/
SELECT date_id, make_name,
COUNT(DISTINCT lead_id) AS unique_leads, 
COUNT(DISTINCT partner_id) as unique_partners
FROM DailySales 
GROUP BY date_id, make_name
