# port_scanner

## Описание.
     Данная утилита предназначена, для анализа портов. 
     Настоятельно рекомендую ананилизровать только локальные устрйства или если согласовано
     с владельцом устройства, которое ананлизируем.
### Требование
    * python3 3.7 или выше
### Использование
    Перейдите в проект, который установили.
    Введите в cmd/terminal: python3 port_scanner.py [-ip] [-t] [-u] [-p N1 N2] [--ports N1 N2]
    * -ip - ip-адрис, который необходимо проанализировать. 
            Если не будет передан то будем аналезировать локальное устройство.
    * -t - анализ TCP портов. 
    * -г - анализ UDP портов.
    * -p | --ports N1 N2 - диапозон сканирования
    N1 и N2 лежит в диапозоне [0..65534] 
