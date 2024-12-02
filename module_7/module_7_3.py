class WordsFinder:
    def __init__(self, *args):
        self.file_names = list(args)

    def get_all_words(self):
        all_words = dict()
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                list_words = []
                for string in file:
                    for i in string:
                        if i in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                            string = string.replace(i, '')
                    for word in string.split():
                        list_words.append(word.lower())
                all_words[file_name] = list_words
        return all_words

    def find(self, word):
        find_word = dict()
        all_words = self.get_all_words()
        for key, item in all_words.items():
            if word.lower() in item:
                find_word[key] = item.index(word.lower()) + 1
        return find_word

    def count(self, word):
        count_words = dict()
        all_words = self.get_all_words()
        for key, item in all_words.items():
            count_words[key] = item.count(word.lower())
        return count_words


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
