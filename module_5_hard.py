from time import sleep


class Video:
    def __init__(self, *args, **kwargs):
        self.title = args[0]
        self.duration = args[1]
        self.time_now = 0
        for key, value in kwargs.items():
            if key == 'adult_mode':
                self.adult_mode = value
            else:
                self.adult_mode = False


class User:
    def __init__(self, *args):
        self.nickname = args[0]
        self.password = hash(args[1])
        self.age = args[2]


class UrTube:
    users = []
    videos = []
    current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user['nickname'] == nickname and user['password'] == hash(password):
                self.current_user = user['nickname']
                break
            else:
                self.current_user = None

    def register(self, nickname, password, age):
        user_register = User(nickname, password, age).__dict__
        if not self.users or user_register["nickname"] not in [user['nickname'] for user in self.users]:
            self.users.append(user_register)
            self.current_user = user_register['nickname']
        else:
            print(f"Пользователь {nickname} уже существует")

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in args:
            if not self.videos or video.__dict__["title"] not in [video['title'] for video in self.videos]:
                self.videos.append(video.__dict__)

    def get_videos(self, search_word):
        list_videos_title = [video['title'] for video in self.videos]
        get_list_title = []
        list_videos_title_lower = ' '.join(word.lower() for word in ' . '.join(list_videos_title).split()).split(' . ')
        for title in range(len(list_videos_title_lower)):
            if search_word.lower() in list_videos_title_lower[title]:
                get_list_title.append(list_videos_title[title])
        return get_list_title

    def watch_video(self, video_title):
        video_now = {}
        if self.current_user:
            user_now = {}
            for user in self.users:
                if self.current_user == user['nickname']:
                    user_now = user
                    break
            for video in self.videos:
                if video_title == video["title"]:
                    video_now = video
                    break
            if video_now:
                if video_now['adult_mode']:
                    if 0 < user_now['age'] < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                        return
                while video_now['duration'] != video_now['time_now']:
                    video_now['time_now'] += 1
                    print(video_now['time_now'], end=' ')
                    sleep(1)
                print('Конец видео')
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)
# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
