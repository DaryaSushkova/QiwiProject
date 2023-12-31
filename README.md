# QiwiProject
### Решение ТЗ в рамках отбора на стажировку #FRESHQIWI.

В репозитории представлен проект на Python 3.11, IDE PyCharm 2023.1.4.   
В каталоге $/code$ располагается основной код проекта, включающий парсинг данных с сайта ЦБ и саму реализацию консольной утилиты.   
Важно отметить, что в решении используется интеграция модуля $click$ с $setuptools$, поэтому для установки утилиты в виртуальном окружении нужно установить соответствующий пакет с помощью команды:   
```
pip install --e .
```
После этого в терминале должно появится следующее сообщение об успешной установке:   
![image](https://github.com/DaryaSushkova/QiwiProject/assets/89806836/3a22a9f2-7ea2-4fc2-9efc-2b191c15f9e3)   
   
Ура-ура, можно использовать нашу утилиту в терминале!    
![image](https://github.com/DaryaSushkova/QiwiProject/assets/89806836/78ccb011-bc93-498b-8c67-9ebcfbee56a1)   
   
Учтены некорректные входные данные для даты (дата не существует/ формат даты невалиден/ данные для указанной даты отсутствуют) и кода валюты. При этом ошибки, связанные с неверным написанием команды (например, добавление лишнего значения/ параметра) автор не учитывал - об этом терминал уведомляет самостоятельно с просьбой обратиться к функции $--help$. Например, как в ниже приведенном случае:   
![image](https://github.com/DaryaSushkova/QiwiProject/assets/89806836/9f178524-7ace-44ab-880c-ee65b40864c8)
   
Автор решил, что в текущей версии передавать в качестве кода можно только одно значение, а в качестве даты - только конкретное число, без учета диапазонов и прочего. Все эти оговорки - как мысли на будущее, что можно было бы добавить в функционал.   
