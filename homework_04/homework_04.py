          # Импорт библиотеки для печати атрибутов объекта
from pprint import pprint
"""
Для проектирования классовой иерархии для работы с медиа-файлами можно использовать объектно-ориентированный подход.
Основная идея заключается в создании базового класса для работы с файлами и его наследовании для различных типов медиа-файлов и способов их хранения.

Исходные данные:
В проекте мы работаем с **медиа-файлами** (аудио, видео, фото).
Есть некоторый общий набор данных о файле, необходимый для реализации бизнес-логики (имя, размер, дата создания, владелец, страна...).
Для каждого типа медиа-файлов есть свой набор метаданных.

Задание:
1. Попробуйте написать классы для работы с медиа-файлами (они будут основой для пользовательского кода остальных команд).
2. Приведите примеры кода, как можно создать, обновить, удалить или провести какое-нибудь действие (конвертация, извлечение фич) над файлом (можно без реализации деталей).
3. Попробуйте дописать классы для работы с файлами, расположенными не на локальном диске (облако, удаленный сервер, s3-like storage).
4. Попробуйте ответить на вопросы: много ли кода придется дописать / переписать при добавлении новых типов файлов и способов их хранения?

P.S. Суть задания — именно проектирование классовой иерархии, а не реализация самой логики, поэтому достаточно, например, просто объявить метод `.save(...)` и в комментарии уточнить, что он должен делать, без конкретной реализации.
"""
          # Создание базового класса MediaFile, который содержит общие атрибуты и методы для всех типов медиа-файлов
class MediaFile:
    def __init__(self, name, size, creation_date, owner, country):
        self.name = name
        self.size = size
        self.creation_date = creation_date
        self.owner = owner
        self.country = country
          # Метод для сохранения файла
    def save(self): pass
          # Метод для удаления файла
    def delete(self): pass
        # Метод для извлечения основных параметров файла
    def main_features_extract(self): pass

        # Создание классов для различных типов файлов с наследованием от базового класса MediaFile
class AudioFile(MediaFile):
    def __init__(self, name, size, creation_date, owner, country, duration, bitrate):
        super().__init__(name, size, creation_date, owner, country)
        self.duration = duration
        self.bitrate = bitrate
        # Метод для извлечения всех параметров файла
    def all_features_extract (self): pass

class VideoFile(MediaFile):
    def __init__(self, name, size, creation_date, owner, country, duration, resolution):
        super().__init__(name, size, creation_date, owner, country)
        self.duration = duration
        self.resolution = resolution
        # Метод для конвертации файла
    def convert(self, format): pass

class PhotoFile(MediaFile):
    def __init__(self, name, size, creation_date, owner, country, resolution, format):
        super().__init__(name, size, creation_date, owner, country)
        self.resolution = resolution
        self.format = format
        # Метод для извлечения всех параметров файла
    def all_features_extract (self): pass

        # Создание классов для различных типов файлов, расположенными не на локальном диске, с наследованием от базового класса MediaFile
class CloudMediaFile(MediaFile):
    def __init__(self, name, size, creation_date, owner, country, cloud_provider):
        super().__init__(name, size, creation_date, owner, country)
        self.cloud_provider = cloud_provider
        # Метод для сохранения файла в облаке
    def save_on_cloud(self): pass
        # Метод для удаления файла в облаке
    def delete_from_cloud(self): pass

class RemoteMediaFile(MediaFile):
    def __init__(self, name, size, creation_date, owner, country, remote_server):
        super().__init__(name, size, creation_date, owner, country)
        self.remote_server = remote_server
        # Метод для копирования файла с удаленного сервера
    def copy_to_remote_disk(self): pass

class S3MediaFile(MediaFile):
    def __init__(self, name, size, creation_date, owner, country, s3_server):
        super().__init__(name, size, creation_date, owner, country)
        self.s3_server = s3_server
        # Метод для копирования файла в s3-хранилище
    def copy_to_s3_server(self): pass
        # Метод для удаления файла в s3-хранилище
    def delete_on_s3_server(self): pass

          # Создание экземпляров медиа-файлов
photo = PhotoFile(name="photo.jpg", size=2000, creation_date="2018-01-01", owner="user", country="RU", resolution="720x540", format="jpg")
photo.all_features_extract()

audio = AudioFile(name="song.mp3", size=5000, creation_date="2018-01-02", owner="user-2", country="DE", duration=120, bitrate=128)
audio.main_features_extract()

video = VideoFile(name="movie.mp4", size=10000, creation_date="2018-01-03", owner="user-3", country="EN", duration=360, resolution="720p")
video.convert("mkv")

cloud_audio = CloudMediaFile(name="song-2.mp3", size=5000, creation_date="2018-01-04", owner="user", country="RU", cloud_provider="AWS")
cloud_audio.save_on_cloud()

remote_video = RemoteMediaFile(name="movie-2.mp4", size=10000, creation_date="2018-01-05", owner="user-2", country="DE", remote_server="server")
remote_video.copy_to_remote_disk()

s3_photo = S3MediaFile(name="photo-2.jpg", size=2000, creation_date="2018-01-06", owner="user-3", country="EN", s3_server="S3_Srv")
s3_photo.copy_to_s3_server()

          # Вывод на печать для контроля атрибутов и методов
for attr in dir(photo):
    if not attr.startswith("__"): print(f"{attr}: {getattr(photo, attr)}")
obj_vars = vars(photo)
pprint(obj_vars)

          # Ответы на вопросы
"""
1) Много ли кода придется дописать/переписать при добавлении новых типов файлов?

При добавлении новых типов файлов (например, текстовых файлов) потребуется:
    создать новые классы, наследуемые от базового класса MediaFile;
    определить в этих классах специфичные атрибуты для данного типа файла, а также уникальные методы обработки.
Общая структура и методы базового класса остаются неизменными, при этом изменения будут реализованы в новых классах


2) Много ли кода придется дописать / переписать при добавлении новых способов хранения файлов?

При добавлении новых способов хранения (например, новых облачных провайдеров) будет необходимо:
    создать новые классы-наследники MediaFile;
    реализовать специфичные методы обработки файлов (сохранения, удаления и, возможно, дополнительные методы работы с хранилищем) 
"""