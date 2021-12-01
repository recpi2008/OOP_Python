import psutil


#  Информация о состоянии памяти
print(psutil.virtual_memory())

# Информация о системном времени
print(psutil.cpu_times())

# Информация об общесистемной загрузке в %
print(psutil.cpu_percent())

# Информация о кол-ве логических процессоров
print(psutil.cpu_count())

# Статистическая информация
print(psutil.cpu_stats())

# Частота процессора
print(psutil.cpu_freq())

