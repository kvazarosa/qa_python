1. `test_add_new_books_with_parameterization_book_added`:
   - Эта проверка тестирует метод `add_new_book`. Она использует параметризацию для проверки добавления нескольких книг с разными названиями. Проверяется, что после добавления книга присутствует в словаре `books_genre` с пустым жанром.

2. `test_set_book_genre_the_genre_is_set`:
   - Эта проверка тестирует метод `set_book_genre`. Она проверяет, что после присвоения жанру книги, этот жанр действительно присваивается книге в словаре `books_genre`.

3. `test_get_book_genre_fantastic_genre_received`:
   - Эта проверка тестирует метод `get_book_genre`. Она проверяет, что метод возвращает правильный жанр для указанной книги.

4. `test_get_books_with_specific_genre_simple_check`:
   - Эта проверка тестирует метод `get_books_with_specific_genre`. Она проверяет, что метод возвращает правильный список книг, соответствующих указанному жанру.

5. `test_get_books_genre_returns_dict_got_a_dict`:
   - Эта проверка тестирует метод `get_books_genre`. Она проверяет, что метод возвращает словарь `books_genre`, содержащий все книги и их жанры.

6. `test_books_for_children_genres_of_books_no_books_with_a_rating`:
   - Эта проверка тестирует метод `get_books_for_children`. Она проверяет, что метод возвращает список книг, которые подходят для детей, исключая книги с возрастным рейтингом.

7. `test_add_book_in_favorites_insert_a_book_added_list`:
   - Эта проверка тестирует метод `add_book_in_favorites`. Она проверяет, что после добавления книги в избранное, она действительно присутствует в списке `favorites`.

8. test_delete_book_from_favorites_book_delete`:
   - Эта проверка тестирует метод `delete_book_from_favorites`. Она проверяет, что после удаления книги из избранного, она действительно удаляется из списка `favorites`.

9. `test_get_list_of_favorites_books_two_books_list_received`:
   - Эта проверка тестирует метод `get_list_of_favorites_books`. Она проверяет, что метод возвращает правильный список избранных книг.
