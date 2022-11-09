###League_player_match_analysis

This repo contains the files I used to conduct my analysis of my league of legends matches by using an ETL to extract data from Riot's API.
There are two Python files which were used extracted data from Riot's API, transformed the JSON into a pandas dataframe, and Loaded the 
information into an Amazon MySQL RDS micro instance. The data was then analyzed and visualized using MySQL to query specific information and 
Tableau to build out a dashboard which can be accessed in the chrome_proxy.exe file or at the link here: 
https://public.tableau.com/app/profile/aidan2791/viz/LeagueofLegendsPlayerRankedMatchHistoryInsights/Champion#1

I also wrote a medium article which is the same as the rest of this README. It can be found here: https://medium.com/p/4d52678b563c/edit

##Data Analysis & ETL - League of Legends Project

These past couple of weeks I have been working on an analytics project focused on drawing insights from my League of Legends games. I enjoy
playing ranked, but I am not always the best player. My goal with this project is to evaluate my current performance in game, determine what
I am doing well, and where I can clean up my execution in order to increase my rank. To do this I will be parsing through my past match 
history. I do want to add a caveat to my work as a lot of good conclusions can be drawn from data, but there are certain parts of the game 
that don't show up in my data such as items purchased, decision making, or poorly playing teammates. Please reference my Github repo if you 
want to follow along with my files, but I have attached pictures to this article showing the steps I took in my analysis as well.

![Minions battling in Mid-lane]([https://myoctocat.com/assets/images/base-octocat.svg](https://nexus.leagueoflegends.com/wp-content/uploads/2018/11/MinionsFighting_e12c7fqpsi0sw8t6hyt0.png))
