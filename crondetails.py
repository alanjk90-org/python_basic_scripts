from crontab import CronTab

user_file = open('/root/pys/userdomains', 'r')
for line in user_file:
    print(line)
    splitted_line = line.split(': ')
    print(splitted_line)
    user_cron = splitted_line[1].split()
    print(user_cron)
    print("crons for", user_cron, "is", CronTab(user=user_cron))
