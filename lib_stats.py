#! /usr/bin/env python3

import datetime

try:
    import matplotlib.pyplot as plt
    from matplotlib.cm import get_cmap
    mpl = True
except ModuleNotFoundError as e:
    print('ERROR: matplotlib module not found')
    print('    install it with:')
    print('    pip3 install matplotlib')
    mpl = False

from lib_db import get_items


def stat_run_time():
    tasks = get_items()
    labels = []
    run_times = []
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    map_name = 'Accent'
    cmap = get_cmap(map_name)
    colors = cmap.colors

    for task in tasks:
        try:
            rt = int(task['run_time'])
        except Exception as e:
            rt = 0
        rt_str = str(datetime.timedelta(seconds=rt))
        labels.append(task['name'] + ' | ' + rt_str)
        run_times.append(rt)

    patches, texts = plt.pie(run_times, colors=colors,
                             shadow=True, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.suptitle('Run time per task')
    pic_name = 'imgs/run_times.png'
    plt.savefig(pic_name)
    return pic_name

# stat_run_time()
