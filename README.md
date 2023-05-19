 
## Co to są circuit breakers i do czego służą? Dlaczego to jest ważny element aplikacji Netfixa? 
 
Circuit breakers są mechanizmem stosowanym w systemach rozproszonych, które pozwalają na wykrywanie i ograniczanie awarii usług. Służą do zabezpieczenia systemu przed długotrwałymi i nieudanymi żądaniami do usługi, która nie działa prawidłowo. Głównym celem circuit breakers jest zapewnienie stabilności i odporności systemu, zapobiegając kaskadom błędów, które mogą powstawać w przypadku nieodpowiednich lub nieudanych żądań do usług zewnętrznych. W przypadku aplikacji Netflix, circuit breakers są ważnym elementem, ponieważ ich platforma opiera się na usługach rozproszonych, takich jak usługi strumieniowania wideo. Zapobiegają one nieprawidłowemu przeciążeniu systemu i zapewniają łagodne degradowanie usług w przypadku awarii. 

## Patrząc od strony programisty w Netflixie czy Allegro budującego serwis, dlaczego chcemy uniknąć cascading failures? 

Unikanie cascading failures (kaskadowych awarii) jest ważne dla programistów w Netflixie czy Allegro, którzy budują serwisy, ponieważ kaskadowe awarie mogą prowadzić do całkowitego zepsucia systemu. Jeśli jedna usługa lub komponent nie działa poprawnie i inne usługi zależą od niej, to mogą również zacząć działać nieprawidłowo, co prowadzi do kaskady błędów. Dlatego ważne jest, aby zapewnić odpowiednie zabezpieczenia, takie jak circuit breakers i strategie fallback, aby uniknąć rozprzestrzeniania się awarii w całym systemie.  

## Patrząc od strony programisty w Amazonie budującego serwis, dlaczego graceful degradation jest ważny? 

Dla programistów w Amazonie budujących serwisy, graceful degradation (łagodne degradowanie) jest ważne, ponieważ umożliwia systemowi zachowanie minimalnej funkcjonalności nawet w przypadku problemów. W przypadku wystąpienia problemu z jedną z usług lub komponentów, system będzie nadal działać, ograniczając funkcje, które mogą być zależne od uszkodzonej części. To pozwala na utrzymanie integralności systemu i obsługę żądań, nawet jeśli niektóre funkcje są niedostępne lub działają w ograniczonym zakresie. 


# Użycie curl i jq do wypisania nazw super bohaterów z pliku JSON


#Wywołanie POST na https://httpbin.org/post i wypisanie odpowiedzi bez formatowania

curl -s --fail -X POST \
     -H "Content-Type: application/json" \
     -d '{"name":"natalia"}' https://httpbin.org/post

# Wywołanie POST na https://httpbin.org/post, wypisanie odpowiedzi z formatowaniem za pomocą jq

curl -s --fail -X POST \
     -H "Content-Type: application/json" \
     -d '{"name":"natalia"}' https://httpbin.org/post | jq

#Wywołanie POST na https://httpbin.org/post, wypisanie tylko sekcji "json" odpowiedzi za pomocą jq

curl -s --fail -X POST \
     -H "Content-Type: application/json" \
     -d '{"name":"natalia"}' https://httpbin.org/post | jq '.json'

#Wywołanie GET na https://httpbin.org/get, przekazanie danych w ciele żądania, wypisanie tylko wartości pola "name" za pomocą jq

curl -s --fail -X GET \
    -H "Content-Type: application/json" \
    -d '{"name":"natalia"}' https://httpbin.org/get \
    | jq '.json | .name'

# Użycie jq do wypisania nazw super bohaterów z https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json

# Pobierz dane JSON z podanego URL-a i przekieruj je na wejście jq, wypisz tylko wartości pola "name"

curl -s https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json | jq '.members[].name'

