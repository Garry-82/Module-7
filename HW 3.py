Team1 = '"Мастера кода"'
Team2 = '"Волшебники данных"'
team1_num = 6
team2_num = 6
print('В команде %s участников: %d' % (Team1, team1_num))
print('сегодня в командах %s и %s по %d и %d участников соответственно' % (Team1, Team2, team1_num, team2_num))

score_1 = 40
score_2 = 42
print('команда {} решила задач: {} !'.format(Team2, score_2))
print('команда {1} решила задач: {0} !'.format(score_1, Team1))

team1_time = 1552.512
team2_time = 2153.31451
print('команда {} решила задачи за: {} с !'.format(Team2, team2_time))
print('команда {1} решила задачи за: {0} с !'.format(team1_time, Team1))

print(f'Команды {Team1} и {Team2} решили задач: {score_1} и {score_2} соответственно!')

challeng_results = Team1
print(f'Результат битвы: победа команды {challeng_results}!!!')

tasks_total = score_1 + score_2
time_avg = round((team1_time + team2_time) / (score_1 + score_2), 2)
print(f'Сегодня было решено всего: {score_1 + score_2} задач, в среднем по {time_avg} секунды за задачу!!!')
