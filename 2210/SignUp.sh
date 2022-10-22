read -p "Придумайте логин для своего аккаунта: " login
echo "Login:"$login > TopSecretDontOpen.txt
read -s -p "Введите пароль:" password 
echo "Password:"$password >> TopSecretDontOpen.txt
echo 
echo "Вы успешно зарегистрировались"