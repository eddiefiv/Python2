import datetime

def get(age: int):
    now_year = datetime.date.today().year
    x = 100 - age
    hundred_year = now_year + x

    return hundred_year

if __name__ == "__main__":
    when = get(int(input('How old are you? ')))

    print(f'You will turn 100 in the year {when}')