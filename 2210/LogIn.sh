#!/bin/bash
read -p "Введите логин: " login
read -p "Введите пароль: " password
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
