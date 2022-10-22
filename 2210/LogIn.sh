#!/bin/bash
read -p "Введите логин: " login
login="Login:"$login
read -p "Введите пароль: " password
password="Password:"$password
for i in `cat TopSecretDontOpen.txt`
do
    for j in `cat TopSecretDontOpen.txt`
    do
        if [[ $i = $login ]] && [[ $j = $password ]]
        then
            echo "Вы вошли в аккаунт!"
            break
        fi
    done
done














# read -p "Введите логин: " login
# for i in `cat TopSecretDontOpen.txt`
# do
#     if [[ $i = $login ]]
#     then
#         read -p "Введите пароль: " password
#         for j in `cat TopSecretDontOpen.txt`
#         do
#             if [[ $j = $password ]]
#             then
#                 echo "Вы вошли в аккаунт!"
#                 break
#             fi
#         done
#     fi
# done
