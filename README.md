# Aplikacja Siłownia
a) Klonowanie repozytorium\
Sklonować repozytorium należy użyć polecenia:

    https://github.com/s24600/Suml_sumy.git

b) Uruchamienie aplikacji lokalnie: \
By uruchomić aplikacje lokalnie nalezy najpierw 
1. Zainstalować biblioteki uruchamiając powyższy kod

       pip install -r requirements.txt
    
3. Uruchomić aplikację:
	
	python3 -m prepare_csv.py
	python3 -m streamlit run app.py 

c) Uruchomienie Aplikacji z Wykorzystaniem Dockera
1. Zbuduj obraz Docker: \
Upewnij się, że jesteś w katalogu głównym repozytorium (gdzie znajduje się Dockerfile).

        docker build -t nazwa-aplikacji .
    
2. Uruchom kontener:

        docker run nazwa-aplikacji

d) Pobranie i Uruchomienie Obrazu z Docker Hub

1. Zaloguj się do Docker Hub:

        docker login

2. Uruchom pobrany obraz:

        docker run -p 8501:8501 kacper24600/sumlprojekt:sumy1.2

3. Wejdź na strone poprzez:
	localhost:8501

d) Uruchomienie poprzez przeglądaekę, wpisz adres:
	83.9.166.247:53106
