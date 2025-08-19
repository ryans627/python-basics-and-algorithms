class Movie:
    def __init__(self, name, director, time):
        self.name = name
        self.director = director
        self.time = time

    def print_movie_name(self):
        print(f"电影的名称是: {self.name}")

    def print_director(self):
        print(f"电影的导演是：{self.director}")

    def print_time(self):
        print(f"电影时长为：{self.time}")


def input_and_output_movie_info():
    name = input("请输入电影名称：")
    director = input("请输入电影导演：")
    time = input("请输入电影时长：")
    movie = Movie(name, director, time)

    movie.print_movie_name()
    movie.print_director()
    movie.print_time()

input_and_output_movie_info()