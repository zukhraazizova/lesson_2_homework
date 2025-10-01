class StringUtils:
    """
    Класс с полезными утилитами для обработки и анализа строк
    """

    def capitalize(self, string: str) -> str:
        """
        Делает первую букву заглавной
        """
        return string.capitalize()

    def trim(self, string: str) -> str:
        """
        Убирает пробелы в начале строки
        """
        whitespace = " "
        while string.startswith(whitespace):
            string = string.removeprefix(whitespace)
        return string

    def contains(self, string: str, symbol: str) -> bool:
        """
        Проверяет, есть ли символ в строке
        """
        res = False
        try:
            res = string.index(symbol) > -1
        except ValueError:
            pass
        return res

    def delete_symbol(self, string: str, symbol: str) -> str:
        """
        Удаляет символ или подстроку из строки
        """
        if self.contains(string, symbol):
            string = string.replace(symbol, "")
        return string