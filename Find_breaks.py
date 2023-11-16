import pymorphy2


def find_breaks(plan: list) -> list:
    for i in range(len(plan) - 1, 0, -1):
        for j in range(i - 1, 0, -1):
            start = list(map(lambda x: int(x), plan[j]['stop'].split(':')))
            end = list(map(lambda x: int(x), plan[i]['start'].split(':')))
            if start[0] > end[0] or start[0] == end[0] and start[1] > end[1]:
                plan[i], plan[j] = plan[j], plan[i]
    breaks = []
    morph = pymorphy2.MorphAnalyzer()
    p = morph.parse('перерыв')[0]
    for i in range(len(plan) + 1):
        if i == 0:
            time = list(map(lambda x: int(x), plan[i]['start'].split(':')))
            time = time[0] * 60 + time[1]
            amount = (time - 9 * 60) // 30
            if amount > 0:
                breaks.append(f"между 9:00 и {plan[i]['start']} - {amount} "
                              f"{p.make_agree_with_number(amount).word} по 30 минут")
        elif i == len(plan):
            time = list(map(lambda x: int(x), plan[i - 1]['stop'].split(':')))
            time = time[0] * 60 + time[1]
            amount = (21 * 60 - time) // 30
            if amount > 0:
                breaks.append(f"между {plan[i - 1]['stop']} и 21:00 - {amount} "
                              f"{p.make_agree_with_number(amount).word} по 30 минут")
        else:
            time_1 = list(map(lambda x: int(x), plan[i - 1]['stop'].split(':')))
            time_1 = time_1[0] * 60 + time_1[1]
            time_2 = list(map(lambda x: int(x), plan[i]['start'].split(':')))
            time_2 = time_2[0] * 60 + time_2[1]
            amount = (time_2 - time_1) // 30
            if amount > 0:
                breaks.append(f"между {plan[i - 1]['stop']} и {plan[i]['start']} - {amount} "
                              f"{p.make_agree_with_number(amount).word} по 30 минут")

    return breaks


busy = [
        {'start': '10:30',
         'stop': '10:50'},
        {'start': '18:40',
         'stop': '18:50'},
        {'start': '14:40',
         'stop': '15:50'},
        {'start': '16:40',
         'stop': '17:20'},
        {'start': '20:05',
         'stop': '20:20'}
]

print('\n'.join(find_breaks(busy)))
