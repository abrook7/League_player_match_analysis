SELECT champion_played as Champion, COUNT(champion_played) as 'Games Played'
FROM MiniSoloCup_match_info
WHERE queue_id = '420'
GROUP BY champion_played
ORDER BY 2 DESC;