# task_elephants
task_elephants
W Bajtockim Zoo ma się za chwilę odbyć parada, w której uczestniczyć będą wszystkie
znajdujące się w nim słonie. Pracownicy zoo zachęcili już zwierzęta do ustawienia się w jednym
rzędzie, gdyż zgodnie z zarządzeniem dyrektora zoo taka powinna być początkowa figura parady.
Niestety, na miejsce przybył sam dyrektor i zupełnie nie spodobała mu się wybrana
przez pracowników kolejność słoni. Dyrektor zaproponował kolejność, w której według niego
zwierzęta będą się najlepiej prezentować, i wydał pracownikom polecenie poprzestawiania słoni
zgodnie z tą propozycją.
Aby uniknąć nadmiernego chaosu tuż przed paradą, pracownicy postanowili przestawiać
słonie, zamieniając miejscami kolejno pewne pary słoni. Przestawiane zwierzęta nie muszą
sąsiadować ze sobą w rzędzie. Wysiłek potrzebny do nakłonienia słonia do ruszenia się z miej-
sca jest wprost proporcjonalny do jego masy, a zatem wysiłek związany z zamianą miejscami
dwóch słoni o masach m 1 oraz m 2 można oszacować przez m 1 + m 2 . Jakim minimalnym wy-
siłkiem pracownicy mogą poprzestawiać słonie tak, aby usatysfakcjonować dyrektora?
Napisz program, który:
• wczyta ze standardowego wejścia masy wszystkich słoni z zoo oraz aktualną i docelową
kolejność słoni w rzędzie,
• wyznaczy taki sposób poprzestawiania słoni, który prowadzi od kolejności początkowej
do docelowej i minimalizuje sumę wysiłków związanych ze wszystkimi wykonanymi
zamianami pozycji słoni,
• wypisze sumę wartości tych wysiłków na standardowe wyjście.
Wejście
Pierwszy wiersz wejścia zawiera jedną liczbę całkowitą n (2 6 n 6 1 000 000 ), oznaczającą
liczbę słoni w Bajtockim Zoo. Dla uproszczenia zakładamy, że słonie są ponumerowane od
1 do n. Drugi wiersz zawiera n liczb całkowitych m i (100 6 m i 6 6 500 dla 1 6 i 6 n),
pooddzielanych pojedynczymi odstępami i oznaczających masy poszczególnych słoni (wyrażone
w kilogramach).
Trzeci wiersz wejścia zawiera n różnych liczb całkowitych a i (1 6 a i 6 n), pooddzielanych
pojedynczymi odstępami i oznaczających numery kolejnych słoni w aktualnym ustawieniu.
Czwarty wiersz zawiera n różnych liczb całkowitych b i (1 6 b i 6 n), pooddzielanych pojedyn-
czymi odstępami i oznaczających numery kolejnych słoni w ustawieniu proponowanym przez
dyrektora zoo. Możesz założyć, że ustawienia reprezentowane przez ciągi ( a i ) oraz ( b i ) są
różne.72
Słonie
Wyjście
Pierwszy i jedyny wiersz wyjścia powinien zawierać jedną liczbę całkowitą, oznaczającą
minimalny łączny wysiłek związany z poprzestawianiem słoni, w wyniku którego z ustawienia
reprezentowanego przez ( a i ) uzyskuje się ustawienie ( b i ).
Przykład
Dla danych
6
2400 2000
1 4 5 3 6
5 3 2 4 6
poprawnym
11200
wejściowych:
1200 2400 1600 4000
2
1
wynikiem jest:
Jeden z najlepszych sposobów poprzestawiania słoni uzyskujemy, zamieniając miejscami
kolejno pary słoni:
• 2 i 5 — wysiłek związany z zamianą to 2 000 + 1 600 = 3 600 , a uzyskane ustawienie to
1 4 2 3 6 5,
• 3 i 4 — wysiłek to 1 200 + 2 400 = 3 600 , a uzyskane ustawienie to 1 3 2 4 6 5,
• 1 i 5 — wysiłek to 2 400 + 1 600 = 4 000 , a uzyskane ustawienie to 5 3 2 4 6 1, czyli
ustawienie docelowe.
Rozwiązanie
Wstęp
Aby łatwiej wyobrazić sobie zadanie, jakie przed pracownikami zoo postawił dy-
rektor, spróbujemy przedstawić je graficznie.
W tym celu zdefiniujemy funkcj ̨e
p : {1, 2, . . . , n} → {1, 2, . . . , n} w nast ̨epuj acy
 ̨ sposób:
p(b 1 ) = a 1 ,
p(b 2 ) = a 2 ,
...,
p(b n ) = a n .
Zauważmy, że wówczas p(x) = y b ̨edzie oznaczało, że słoń o numerze x powinien znaleźć si ̨e
w końcowym ustawieniu w miejscu, które jest aktualnie zajmowane przez słonia o numerze
y. Wszystkie liczby b i s a  ̨ różne, zatem p jest poprawnie zdefiniowan a  ̨ funkcj a,  ̨ a ponieważ
wszystkie liczby a i s a  ̨ różne, p jest permutacj a  ̨ zbioru {1, 2, . . . , n}. Sytuacj ̨e z zadania
możemy zatem przedstawić w postaci grafu skierowanego, w którym wierzchołkami s a  ̨
numery 1, 2, . . . , n słoni, kraw ̨edziami natomiast wartości funkcji p (patrz rys. 1).
Dalej, jak każd a  ̨ permutacj ̨e, funkcj ̨e p można rozłożyć na tak zwane cykle proste
C 1 ,C 2 , . . . ,C c . W tym celu należy wystartować z dowolnego wierzchołka grafu i pod a  ̨ żać
po kraw ̨edziach, aż dojdzie si ̨e z powrotem do tego wierzchołka (dlaczego zawsze trafiaSłonie
si ̨e w końcu w wierzchołek pocz atkowy
 ̨
trasy?), po czym usun ać
 ̨ znaleziony cykl z grafu
i kontynuować proces aż do wyczerpania wszystkich wierzchołków — patrz rys. 2.
1
Rys. 1:
3
2
5
4
6
Graf wyznaczony przez funkcj ̨e p dla przykładu z treści zadania. Wierzchołki grafu
reprezentuj a  ̨ numery słoni, natomiast strzałka z x do y obrazuje relacj ̨e „słoń x
powinien zaj ać
 ̨ miejsce słonia y”.
1
2
3
4
6
5
Rys. 2:
Rozkład grafu z rys. 1 na cykle proste: trójelementowy, dwuelementowy i jednoe-
lementowy.
Zastanówmy si ̨e teraz, jak na tle opisanego rozkładu na cykle proste wygl ada
 ̨ operacja
zamiany miejscami słoni o numerach e oraz f . Koszt takiej zamiany to m e + m f . Jeżeli słonie
e oraz f znajduj a  ̨ si ̨e w tym samym cyklu, to nast ̨epuje wówczas podział tego cyklu na dwa
rozł aczne,
 ̨
z których jeden zawiera jednego z tych słoni, a drugi drugiego — patrz rys. 3.
2
2
1 3 1 6
6 4 3 4
5
Rys. 3:
5
Zamiana miejscami trzeciego i szóstego słonia w cyklu prowadzi do powstania
dwóch cykli trójelementowych.
W szczególności, w wyniku zamiany miejscami dwóch słoni, które s asiaduj
 ̨
a  ̨ na cyklu, jeden
z powstałych cykli jest jednoelementowy, co oznacza dokładnie tyle, że po tej zamianie jeden
ze słoni znajduje si ̨e na swojej pozycji docelowej (rys. 4).
1
2
1 3 2 3
6 4 6 4
5
Rys. 4:
5
Zamiana miejscami pierwszego i drugiego słonia w cyklu powoduje, że pierwszy
słoń trafia na właściw a  ̨ pozycj ̨e.
7374
Słonie
Z kolei jeżeli słonie e oraz f należ a  ̨ do różnych cykli, to zamiana ich miejscami powoduje
sklejenie tych cykli w jeden (rys. 5).
5
5
1
2
3
Rys. 5:
1
4
6
4
2
3
6
Zamiana miejscami słoni należ acych
 ̨
do różnych cykli.
Rozwiązanie wzorcowe 1
Przyjmijmy nast ̨epuj ace
 ̨ oznaczenia:
• |C| — długość cyklu C, czyli liczba wierzchołków grafu w nim zawartych
• suma(C) — suma mas słoni należ acych
 ̨
do cyklu C
• min(C) — masa najlżejszego słonia na cyklu C
• min — masa najlżejszego słonia w ogóle.
Naszym celem jest sprowadzenie układu cykli reprezentowanego przez permutacj ̨e p do
takiego, który b ̨edzie złożony wył acznie
 ̨
z cykli jednoelementowych. W rozwi azaniu
 ̨
wzorco-
wym każdy cykl C rozpatrujemy osobno, a wspomniane przekształcenie realizujemy, stosuj ac
 ̨
do C jedn a  ̨ z nast ̨epuj acych
 ̨
metod przestawiania słoni.
Metoda 1. Porz adkujemy
 ̨
cały cykl pojedynczymi zamianami s asiednich
 ̨
słoni (jak na
rys. 4). Za każdym razem zamieniamy najlżejszego słonia z całego cyklu (min(C)) z jego
poprzednikiem na cyklu, w wyniku czego poprzednik ten trafia na właściwe miejsce (patrz
rys. 6). W ten sposób najlżejszego słonia przemieszczamy ł acznie
 ̨
|C| − 1 razy, natomiast
każdego z pozostałych słoni z cyklu — dokładnie raz. Ł aczny
 ̨
koszt porz adkowania
 ̨
cyklu t a  ̨
metod a  ̨ wynosi zatem:

metoda 1 (C) = suma(C) + |C| − 2 · min(C).
(1)
Metoda 2. Tym razem post ̨epujemy bardzo podobnie, jednakże do obsłużenia całego
cyklu wykorzystujemy globalnie najlżejszego słonia (min). W tym celu zamieniamy go
z najlżejszym słoniem cyklu (min(C)), a nast ̨epnie za jego pomoc a  ̨ przestawiamy kolejno
wszystkie słonie z cyklu C (poza min(C)) jak poprzednio, po czym z powrotem zamieniamy
min z min(C). Na ten ci ag
 ̨ zamian można też spojrzeć jak na sklejenie C z cyklem zawiera-
j acym
 ̨
min, po którym nast ̨epuje ustawienie wszystkich słoni z C na właściwych miejscach
za pomoc a  ̨ pojedynczych zamian ze słoniem min. W ten sposób najlżejszy słoń w całym zoo
zostaje przemieszczony |C| + 1 razy, najlżejszy w cyklu — 2 razy, a każdy z pozostałych
słoni tego cyklu — dokładnie raz. Ł aczny
 ̨
koszt wszystkich przestawień to wówczas:

metoda 2 (C) = suma(C) + min(C) + |C| + 1 · min.
(2)
1 Duża
cz ̨eść opisu rozwi azania
 ̨
wzorcowego została zaczerpni ̨eta z pracy [37].Słonie
1
4
4
2
1
3 3
4 4
3
1
3
2
Rys. 6:
2
2
1
Porz adkowanie
 ̨
czteroelementowego cyklu za pomoc a  ̨ pierwszej metody. Zakła-
damy, że najlżejszy słoń ma numer 1.
Okazuje si ̨e, że w całym rozwi azaniu
 ̨
wystarczy wzi ać
 ̨ pod uwag ̨e jedynie dwie opisane
metody i dla każdego cyklu w rozkładzie do uporz adkowania
 ̨
użyć korzystniejszej z nich 2 .
Ostatecznie otrzymujemy nast ̨epuj acy
 ̨ minimalny koszt poprzestawiania słoni:
c
∑ min(metoda 1 (C i ), metoda 2 (C i )).
(3)
i=1
Implementacja
Jako podsumowanie słownego opisu rozwi azania
 ̨
wzorcowego umieszczamy poniższy jego
pseudokod. Łatwo sprawdzić, że cały algorytm ma złożoność czasow a  ̨ O(n). Konkretne
implementacje tego algorytmu można znaleźć w plikach slo.cpp, slo1.java oraz
slo2.pas.
1:
2:
{ Konstrukcja permutacji p. }
for i := 1 to n do p[b i ] := a i ;
3:
4:
5:
6:
7:
8:
9:
{ Rozkład p na cykle proste. }
odw : array[1. .n] := (false, false, . . . , false);
c := 0;
for i := 1 to n do
if not odw[i] then begin
c := c + 1; x := i;
2 Dodajmy tylko, że dla niektórych cykli zachodzi min(C) = min, i wówczas druga metoda traci sens, jednakże
nie trzeba si ̨e tym faktem przejmować, gdyż wówczas i tak metoda 2 (C) > metoda 1 (C).
7576
Słonie
10:
11:
12:
13:
14:
15:
while not odw[x] do begin
odw[x] := true;
C c := C c ∪ {x};
x := p[x];
end
end
16:
17:
18:
19:
20:
21:
22:
23:
24:
25:
26:
{ Wyznaczenie parametrów cykli. }
min := ∞;
for i := 1 to c do begin
suma(C i ) := 0; min(C i ) := ∞;
forall e ∈ C i do begin
suma(C i ) := suma(C i ) + m e ;
min(C i ) := min(min(C i ), m e );
end
min := min(min, min(C i ));
end
27:
28:
29:
30:
31:
32:
33:
34:
35:
{ Obliczenie wyniku. }
w := 0;
for i := 1 to c do begin

metoda 1 (C i ) := suma(C i ) + |C i | − 2 · min(C i ); 
metoda 2 (C i ) := suma(C i ) + min(C i ) + |C i | + 1 · min;
w := w + min(metoda 1 (C i ), metoda 2 (C i ));
end
return w;
Uzasadnienie poprawności
Na sam koniec opisu rozwi azania
 ̨
wzorcowego pozostawiliśmy jego dowód poprawności.
Jest on, niestety, troch ̨e skomplikowany, jednakże jest to jedyna niezawodna metoda
sprawdzenia tego, czy w rozwi azaniu
 ̨
nie zapomnieliśmy o żadnym z przypadków.
Jeżeli C jest cyklem, to przez
koszt(C) = min(metoda 1 (C), metoda 2 (C))
oznaczmy koszt uporz adkowania
 ̨
tego cyklu w rozwi azaniu
 ̨
wzorcowym. Niech dalej
OPT (p) oznacza najmniejszy możliwy koszt poprzestawiania wszystkich słoni zgodnie
z zarz adzeniem
 ̨
dyrektora. Aby wykazać poprawność rozwi azania
 ̨
wzorcowego, wystarczy
udowodnić, że
c
OPT (p) > ∑ koszt(C i ).
(4)
i=1
Nierówność (4) udowodnimy przez indukcj ̨e wzgl ̨edem liczby zamian wykonywanych
w rozwi azaniu
 ̨
optymalnym. Przypadek zerowej liczby zamian jest trywialny. ZałóżmySłonie
wi ̨ec, że (4) zachodzi dla wszystkich permutacji, dla których algorytm optymalny wykonuje
k − 1 zamian, i niech p b ̨edzie dowoln a  ̨ permutacj a,  ̨ do której uporz adkowania
 ̨
algorytm ten
potrzebuje k zamian. Musimy udowodnić, że (4) zachodzi także dla p.
Przyjrzyjmy si ̨e pierwszemu krokowi rozwi azania
 ̨
optymalnego „OPT” uruchomionego
dla p. Załóżmy, że s a  ̨ w nim zamieniane słonie e oraz f . Permutacj ̨e po ich zamianie
oznaczmy przez p ′ — uporz adkowanie
 ̨
jej przez algorytm optymalny wymaga k − 1 zamian,
wi ̨ec wiadomo, że nierówność (4) zachodzi dla p ′ . W zależności od wzajemnego położenia e
oraz f wyróżniamy teraz kilka przypadków.
Przypadek 1: e i f należ a  ̨ do tego samego cyklu w p. Dla ustalenia uwagi niech e, f ∈ C 1 .
Po zamianie słoni cykl C 1 rozpada si ̨e na dwa mniejsze cykle (patrz rys. 3). Oznaczmy te
cykle przez A i B oraz niech e ∈ A i f ∈ B. Wówczas rozkład p ′ na cykle proste wygl ada
 ̨ tak:
{A, B,C 2 ,C 3 , . . . ,C c }, a st ad
 ̨ i z (4) dla p ′ mamy:
c
OPT (p) = OPT (p ′ ) + m e + m f > koszt(A) + koszt(B) + ∑ koszt(C i ) + m e + m f .
i=2
Aby pokazać (4) dla p, wystarczy zatem udowodnić, że:
koszt(A) + koszt(B) + m e + m f > koszt(C 1 ).
(5)
Dalsze uzasadnienie możemy podzielić na trzy podprzypadki:
Przypadek 1.1: koszt(A) = metoda 1 (A) i koszt(B) = metoda 1 (B). Korzystaj ac
 ̨ z faktu, że
zbiór słoni zawartych w cyklu C 1 jest sum a  ̨ zbiorów słoni odpowiadaj acych
 ̨
A oraz B, oraz
z tego, że każda z wartości min(A), min(B), m e , m f jest nie mniejsza niż min(C 1 ), mamy:
metoda 1 (A) + metoda 1 (B) + m e + m f =


= suma(A) + |A| − 2 · min(A) + suma(B) + |B| − 2 · min(B) + m e + m f >

> suma(C 1 ) + |C 1 | − 2 · min(C 1 ) = metoda 1 (C 1 ) > koszt(C 1 ).
Intuicyjnie, pokazaliśmy, że zamiast rozbijać cykl C 1 na cykle A i B (za pomoc a  ̨ zamiany e
z f ) i każdy z nich porz adkować
 ̨
za pomoc a  ̨ pierwszej metody, można równie dobrze od razu
uporz adkować
 ̨
cały cykl C 1 za pomoc a  ̨ tej metody.
Przypadek 1.2: koszt(A) = metoda 1 (A) i koszt(B) = metoda 2 (B) (lub odwrotnie). Po-
dobnie jak poprzednio, w poniższej nierówności liczba składników nie zmienia si ̨e, a jedynie
zast ̨epujemy ci ̨eższe słonie przez min(C 1 ) lub min:
metoda 1 (A) + metoda 2 (B) + m e + m f =


= suma(A) + |A| − 2 · min(A) + suma(B) + min(B) + |B| + 1 · min + m e + m f >

> suma(C 1 ) + min(C 1 ) + |C 1 | + 1 · min = metoda 2 (C 1 ) > koszt(C 1 ).
Tym razem intuicja stoj aca
 ̨ za powyższym ci agiem
 ̨
przekształceń jest taka, że zamiast
wprowadzać najlżejszego słonia tylko do cyklu B, można go wprowadzić od razu do całego
C 1 , co nie przynosi żadnej straty, a może si ̨e dodatkowo opłacić przy porz adkowaniu
 ̨
fragmentu C 1 odpowiadaj acego
 ̨
cyklowi A.
7778
Słonie
Przypadek 1.3: koszt(A) = metoda 2 (A) i koszt(B) = metoda 2 (B). I tym razem do wy-
prowadzenia (5) wykorzystujemy te same spostrzeżenia. W tym przypadku strata wynikła
z rozbicia cyklu C 1 jest ewidentna: intuicyjnie, zamiast wprowadzać słonia min osobno do
każdego z cykli A, B, można na samym pocz atku
 ̨ wprowadzić go do całego C 1 :
metoda 2 (A) + metoda 2 (B) + m e + m f =


= suma(A) + min(A) + |A| + 1 · min + suma(B) + min(B) + |B| + 1 · min + m e + m f >

> suma(C 1 ) + min(C 1 ) + |C 1 | + 1 · min = metoda 2 (C 1 ) > koszt(C 1 ).
Przypadek 2: e i f należ a  ̨ do różnych cykli. Dla ustalenia uwagi niech tym razem
e ∈ C 1 , f ∈ C 2 . Po zamianie słoni cykle C 1 i C 2 ł acz
 ̨ a  ̨ si ̨e w jeden cykl A (patrz rys. 5),
st ad
 ̨ rozkład p ′ na cykle to: {A,C 3 ,C 4 , . . . ,C c }. St ad
 ̨ i z (4) dla p ′ otrzymujemy:
c
OPT (p) = OPT (p ′ ) + m e + m f > koszt(A) + ∑ koszt(C i ) + m e + m f .
i=3
Aby pokazać (4) dla p, wystarczy udowodnić, że:
koszt(A) + m e + m f > koszt(C 1 ) + koszt(C 2 ).
(6)
Bez straty ogólności załóżmy, że min(C 1 ) 6 min(C 2 ), czyli min(A) = min(C 1 ). Tym razem
mamy dwa podprzypadki:
Przypadek 2.1: koszt(A) = metoda 1 (A). Korzystaj ac
 ̨ z tego, że cykl A jest sum a  ̨
(pod wzgl ̨edem zbioru zawartych w nim słoni) cykli C 1 oraz C 2 , a także z założenia
min(A) = min(C 1 ) oraz nierówności: m f > min(C 2 ) i m e , min(A) > min, otrzymujemy
nast ̨epuj acy
 ̨ ci ag
 ̨ przekształceń:
metoda 1 (A) + m e + m f =

= suma(A) + |A| − 2 · min(A) + m e + m f >


> suma(C 1 ) + |C 1 | − 2 · min(C 1 ) + suma(C 2 ) + min(C 2 ) + |C 2 | + 1 · min =
= metoda 1 (C 1 ) + metoda 2 (C 2 ) > koszt(C 1 ) + koszt(C 2 ).
Intuicja tym razem jest taka, że zamiast ł aczyć
 ̨
cykle C 1 i C 2 i porz adkować
 ̨
otrzymany
cykl A metod a  ̨ 1, można sam cykl C 1 uporz adkować
 ̨
t a  ̨ metod a  ̨ (tu nic nie tracimy, gdyż
min(A) = min(C 1 )), natomiast cykl C 2 poł aczyć
 ̨
nie z C 1 , ale z cyklem zawieraj acym
 ̨
najlżejszego słonia min, co odpowiada zastosowaniu do C 2 drugiej metody porz adkowania.
 ̨
Przypadek 2.2: koszt(A) = metoda 2 (A). Podobnie jak poprzednio, na mocy warunków
min(A) = min(C 1 ), m f > min(C 2 ) oraz m e > min, mamy:
metoda 2 (A) + m e + m f =

= suma(A) + min(A) + |A| + 1 · min + m e + m f >


> suma(C 1 ) + min(C 1 ) + |C 1 | + 1 · min + suma(C 2 ) + min(C 2 ) + |C 2 | + 1 · min =
= metoda 2 (C 1 ) + metoda 2 (C 2 ) > koszt(C 1 ) + koszt(C 2 ).Słonie
Intuicyjnie, nie opłaca si ̨e ponosić kosztu poł aczenia
 ̨
cykli C 1 i C 2 , żeby potem uporz adkować
 ̨
wynikowy cykl A za pomoc a  ̨ najlżejszego słonia min, gdyż na pewno nie gorszym
rozwi azaniem
 ̨
jest wprowadzenie słonia min do każdego z cykli C 1 , C 2 z osobna. Innymi
słowy, min + min(A) + m e + m f > 2 · min + min(C 1 ) + min(C 2 ).
Inne rozwiązania
Wśród potencjalnych rozwi azań
 ̨
bł ̨ednych można wyróżnić przede wszystkim takie, które
przy porz adkowaniu
 ̨
cykli zapominaj a  ̨ o jednej z metod: drugiej (plik slob1.cpp, 20%
punktów) lub pierwszej (plik slob2.cpp, 10% punktów). Przypomnijmy, że takich bł ̨edów
można unikn ać,
 ̨ jeżeli przeprowadzi si ̨e dowód poprawności rozwi azania
 ̨
lub chociażby
sprawdzi poprawność swojego rozwi azania
 ̨
na wi ̨ekszej grupie losowych testów, porównuj ac
 ̨
jego wyniki z jakimkolwiek rozwi azaniem
 ̨
na pewno poprawnym, chociażby wykładniczym.
Innym bł ̨edem było wykonywanie wszystkich obliczeń na liczbach całkowitych 32-bitowych
— takie rozwi azanie,
 ̨
wskutek bł ̨edu przepełnienia typu, zdobywało 60% punktów za to
zadanie (implementacja w pliku slob3.cpp).
Wśród rozwi azań
 ̨
wolniejszych można wymienić rozwi azanie
 ̨
kwadratowe wzgl ̨edem n
(plik slos1.cpp), b ̨ed ace
 ̨ nieefektywn a  ̨ implementacj a  ̨ rozwi azania
 ̨
wzorcowego i zdobywa-
 ̨ 10% punktów
j ace
 ̨ 40% punktów, oraz zaimplementowane w pliku slos2.cpp i uzyskuj ace
rozwi azanie
 ̨
siłowe, rozważaj ace
 ̨ wszystkie możliwości zamian słoni, poczynaj ac
 ̨ od najtań-
szych.
Testy
Zadanie było sprawdzane na 10 zestawach danych testowych. Wszystkie testy za wyj atkiem
 ̨
tych z grupy b to testy w jakimś sensie losowe. Wi ̨ekszość testów zawiera losow a  ̨ permutacj ̨e
p słoni. Ponieważ zupełnie losowa permutacja zawiera statystycznie stosunkowo mało cykli,
to w testach 4 i 10a wygenerowano permutacje o dużych liczbach cykli. Poza tym specjaln a  ̨
postać maj a  ̨ testy 9a oraz te z grupy b — patrz opisy poniżej.
W nast ̨epuj acym
 ̨
zestawieniu testów n oznacza liczb ̨e słoni, natomiast pozostałe
parametry charakteryzuj a  ̨ własności permutacji p: c 1 to liczba cykli jednoelementowych
(czyli takich, które nie wymagaj a  ̨ żadnych zamian), m 1 to liczba cykli, których optymalne
uporz adkowanie
 ̨
otrzymuje si ̨e za pomoc a  ̨ metody 1, natomiast m 2 to liczba cykli, które
należy porz adkować
 ̨
metod a  ̨ 2.
Nazwa n c 1 m 1
m 2
Opis
slo1.in 10 1 1 1 test losowy
slo2.in 100 2 4 1 test losowy
slo3.in 1 000 2 8 0 test losowy
slo4.in 10 000 24 55 24 slo5.in 100 000 2 8 1
test losowy o zwi ̨ekszonej liczbie
cykli
test losowy
7980
Słonie
Nazwa n c 1 m 1
m 2
Opis
slo6.in 920 000 1 9 7 test losowy
slo7.in 960 000 2 6 11 test losowy
slo8a.in 980 000 0 6 8 test losowy
slo8b.in 980 000 979 998 1 0 potrzeba tylko jednej zamiany
slo9a.in 1 000 000 904 788 44 788 424 slo9b.in 1 000 000 0 500 000 0 slo10a.in 1 000 000 307 330 1212 slo10b.in 1 000 000 0 1 0
90% słoni na swoim miejscu
wszystkie cykle dwuelementowe
test losowy o zwi ̨ekszonej liczbie
cykli
jeden długi cykl
