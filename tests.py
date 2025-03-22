import pytest

from main import BooksCollector

class TestBooksCollector:

    @pytest.mark.parametrize("book_name", ["Война и мир", "Мастер и Маргарита", "1984"])
    def test_add_new_books_with_parameterization_book_added(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre
        assert collector.books_genre[book_name] == ''


    def test_set_book_genre_the_genre_is_set(self, collector):
        collector.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        collector.books_genre = {'Книга 1': ''}
        collector.set_book_genre('Книга 1', 'Фантастика')
        assert collector.books_genre['Книга 1'] == 'Фантастика'

    def test_get_book_genre_fantastic_genre_received(self, collector):
        collector.books_genre['Книга 1'] = 'Фантастика'
        result = collector.get_book_genre('Книга 1')
        assert result == 'Фантастика'

    @pytest.fixture()
    def collector(self):
        return BooksCollector()

    def test_get_books_with_specific_genre_simple_check(self, collector):
        collector.books_genre = {
                'Книга 1': 'Фантастика',
                'Книга 2': 'Ужасы',
                'Книга 3': 'Фантастика',
                'Книга 4': 'Детективы',
                'Книга 5': 'Фантастика'
            }

        result = collector.get_books_with_specific_genre('Фантастика')
        expected = ['Книга 1', 'Книга 3', 'Книга 5']
        assert result == expected

    def test_get_books_genre_returns_dict_got_a_dict(self, collector):
        collector.books_genre = {
            'Книга 1': 'Фантастика',
            'Книга 2': 'Ужасы',
            'Книга 3': 'Фантастика',
            'Книга 4': 'Детективы',
            'Книга 5': 'Фантастика'
        }

        result = collector.get_books_genre()
        expected = {
            'Книга 1': 'Фантастика',
            'Книга 2': 'Ужасы',
            'Книга 3': 'Фантастика',
            'Книга 4': 'Детективы',
            'Книга 5': 'Фантастика'
        }
        assert result == expected

    def test_books_for_children_genres_of_books_no_books_with_a_rating(self, collector):
        collector.books_genre = {
            'Книга 1': 'Фантастика',
            'Книга 2': 'Ужасы',
            'Книга 3': 'Фантастика',
            'Книга 4': 'Детективы',
            'Книга 5': 'Фантастика'
        }

        result = collector.get_books_for_children()

        expected = ['Книга 1', 'Книга 3', 'Книга 5']
        assert result == expected

    def test_add_book_in_favorites_insert_a_book_added_list(self, collector):
        collector.books_genre = {
            'Книга 1': 'Фантастика',
            'Книга 2': 'Ужасы',
            'Книга 3': 'Фантастика',
            'Книга 4': 'Детективы',
            'Книга 5': 'Фантастика'
        }
        collector.add_book_in_favorites('Книга 1')
        assert 'Книга 1' in collector.favorites, "Книга не добавлена в избранное"

    def test_delete_book_from_favorites_book_delete(self, collector):
        collector.books_genre = {
            'Книга 1': 'Фантастика',
            'Книга 2': 'Ужасы',
            'Книга 3': 'Фантастика',
            'Книга 4': 'Детективы',
            'Книга 5': 'Фантастика'
        }

        collector.add_book_in_favorites('Книга 1')
        assert 'Книга 1' in collector.favorites, "Книга не добавлена в избранное"

        collector.delete_book_from_favorites('Книга 1')
        assert 'Книга 1' not in collector.favorites, "Книга не удалена из избранного"

    def test_get_list_of_favorites_books_two_books_list_received(self, collector):
        collector.favorites = ['Книга 1', 'Книга 2']
        result = collector.get_list_of_favorites_books()
        expected = ['Книга 1', 'Книга 2']
        assert result == expected
