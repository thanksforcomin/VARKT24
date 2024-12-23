# Состав команды
Группа М8О-107БВ-24\
Бахин Андрей Александрович - Тимлид\
Бессонов Тимур Вадимович - Инженер KSP\
Буробин Григорий Ростиславович - Программист\
Кузнецов Артемий Сергеевич - Программист\
Чудов Кирилл Андреевич - Физик, Математик
# Ссылки
[Отчет](https://docs.google.com/document/d/1Ok7q4ElHrTBNracqk8gDPPJ7a3m2rQUgK1zS5FvmIcw)\
[Презентация](https://docs.google.com/presentation/d/1yJuJf3Xnp0loHL7LzINT6v1Ub3VghJbTi7DMQOtDlIA)\
[Видеоотчет](https://disk.yandex.ru/i/mkU6iFH55EBkig)\
[Полет ракеты](https://disk.yandex.ru/i/2NZc9Iy0Ifpncw)
# Установка и настройка
## Моды на KSP
Установите моды для ракеты по [ссылке](./Craft/Dependencies.md)\
Установите мод на автопилот [kRPC](https://github.com/krpc/krpc/releases)\
Поместите моды в папку игры в **GameData**
## Библиотеки Python
У вас должен быть установлен Python 3.12.7
Активируйте виртуальное окружение или установите библиотеки matplotlib и kRPC, прописав в терминал `pip install matplotlib` и `pip install kRPC`.
## Ракета
Скачайте [файл .craft](./Craft) и загрузите его в папку с KSP в /Ships/VAB. Создайте новое сохранение в режиме песочницы и загрузите ракету через вкладку базовые.
## Запуск автопилота
Перейдите на панель запуска, запустите сервер kRPC и запустите скрипт [main1.py](./kRPC)
