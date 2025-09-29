class StringUtils:
    # Делает первую букву заглавной
    def capitilize(self, string: str) -> str:
        return string.capitalize()

    # Убирает пробелы по краям
    def trim(self, string: str) -> str:
        return string.strip()

    # Делает список из строки по разделителю
    def to_list(self, string: str, delimeter: str = ",") -> list:
        if string == "":
            return []
        return string.split(delimeter)

    # Проверяет, пустая ли строка
    def contains(self, string: str, symbol: str) -> bool:
        return symbol in string

    # Удаляет из строки все указанные символы
    def delete_symbol(self, string: str, symbol: str) -> str:
        return string.replace(symbol, "")

    # Проверяет, начинается ли строка с символа
    def starts_with(self, string: str, symbol: str) -> bool:
        return string.startswith(symbol)

    # Проверяет, заканчивается ли строка символом
    def end_with(self, string: str, symbol: str) -> bool:
        return string.endswith(symbol)

    # Проверяет, пустая ли строка
    def is_empty(self, string: str) -> bool:
        return string == "" or string.isspace()
