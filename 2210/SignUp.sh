read -p "Придумайте логин для своего аккаунта: " login
echo $login > TopSecretDontOpen.txt
read -s -p "Введите пароль:" password 
echo $password >> TopSecretDontOpen.txt
echo 
echo "Вы успешно зарегистрировались"