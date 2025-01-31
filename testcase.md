# Test Case Table

| ID   | TC002 |
|------|--------------------------|
| **Opis** | Sprawdza, czy funkcja `tablice()` zwraca poprawne długości list i typy danych. |
| **Preconditions** | Funkcja `tablice` istnieje w module `main.py`. |
| **Dane wejściowe** | Brak bezpośrednich danych wejściowych. |
| **Kroki testowe** | 1. Importuj moduł `main`.<br> 2. Wywołaj funkcję `tablice()`.<br> 3. Sprawdź długości zwróconych list.<br> 4. Sprawdź, czy elementy list `normal_times` i `comprehension_times` są typu `float`. |
| **Oczekiwany rezultat** | - `len(number) == 5`<br> - `len(normal_times) == 5`<br> - `len(comprehension_times) == 5`<br> - Wszystkie elementy `normal_times` i `comprehension_times` są typu `float`. |
| **Środowisko** | Python 3.10, pytest 7.0. |
| **Uwagi** | Dodać osobny test na porównanie wyników. |

---

| ID   | TC003 |
|------|--------------------------|
| **Opis** | Sprawdza, czy funkcja `slowniki()` zwraca poprawne długości list i typy danych. |
| **Preconditions** | Funkcja `slowniki` istnieje w module `main.py`. |
| **Dane wejściowe** | Brak bezpośrednich danych wejściowych. |
| **Kroki testowe** | 1. Importuj moduł `main`.<br> 2. Wywołaj funkcję `slowniki()`.<br> 3. Sprawdź długości zwróconych list.<br> 4. Sprawdź, czy elementy list `normal_times` i `comprehension_times` są typu `float`. |
| **Oczekiwany rezultat** | - `len(number) == 5`<br> - `len(normal_times) == 5`<br> - `len(comprehension_times) == 5`<br> - Wszystkie elementy `normal_times` i `comprehension_times` są typu `float`. |
| **Środowisko** | Python 3.10, pytest 7.0. |
| **Uwagi** | Dodać osobny test na porównanie wyników. |