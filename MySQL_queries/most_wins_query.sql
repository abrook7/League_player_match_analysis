SELECT champion_played as Champion, SUM(win) as 'Total Wins'
FROM MiniSoloCup_match_info
WHERE queue_id = '420'
GROUP BY champion_played
ORDER BY 2 DESC;