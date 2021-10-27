import time
import json


def logger(path):

    def decorator(function):

        def wrapper(*args, **kwargs):
            call_date = time.strftime('%H-%M-%S %d-%m-%Y')
            func_return = function(*args, **kwargs)
            log_dict = {
                'func_name': function.__name__,
                'call_date': call_date,
                'func_args': args, **kwargs,
                'func_return': func_return
            }
            with open(path + f'log_{call_date}.json', 'w', encoding='utf-8') as f:
                json.dump(log_dict, f, ensure_ascii=False, indent=4)
                print('Log saved!')

        return wrapper

    return decorator


@logger(path='C:\\log\\')
def max_sales(stats):
    for channel, sale in stats.items():
        if sale == max(stats.values()):
            return channel


data = {
    'facebook': 55,
    'yandex': 120,
    'vk': 115,
    'google': 99,
    'email': 42,
    'ok': 98
}
max_sales(data)
