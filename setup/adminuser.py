from django.contrib.auth.models import User 
import api_v1.models as api_models


User.objects.create_superuser('superuser', 'admin@example.com', 'superuser')

def add_employees():
    e1 = api_models.Employee(photo=r'images\employees\photo_2023-09-23_10-00-48.jpg', 
                  post='РУКОВОДИТЕЛЬ ЛАБОРАТОРИИ', 
                  last_name='Пятаева', first_name='Анна', patronymic='Владимировна', 
                  link='https://structure.sfu-kras.ru/node/4384')
    e1.save()
    e1 = api_models.Employee(photo=r'images\employees\photo_2023-09-23_10-00-48.jpg', 
                  post='РУКОВОДИТЕЛЬ ЛАБОРАТОРИИ', 
                  last_name='Пятаева', first_name='Анна', patronymic='Владимировна', 
                  link='https://structure.sfu-kras.ru/node/4384')
    e1.save()
    e1 = api_models.Employee(photo=r'images\employees\photo_2023-09-23_10-00-48.jpg', 
                  post='РУКОВОДИТЕЛЬ ЛАБОРАТОРИИ', 
                  last_name='Пятаева', first_name='Анна', patronymic='Владимировна', 
                  link='https://structure.sfu-kras.ru/node/4384')
    e1.save()
    e1 = api_models.Employee(photo=r'images\employees\photo_2023-09-23_10-00-48.jpg', 
                  post='РУКОВОДИТЕЛЬ ЛАБОРАТОРИИ', 
                  last_name='Пятаева', first_name='Анна', patronymic='Владимировна', 
                  link='https://structure.sfu-kras.ru/node/4384')
    e1.save()
    e1 = api_models.Employee(photo=r'images\employees\photo_2023-09-23_10-00-48.jpg', 
                  post='РУКОВОДИТЕЛЬ ЛАБОРАТОРИИ', 
                  last_name='Пятаева', first_name='Анна', patronymic='Владимировна', 
                  link='https://structure.sfu-kras.ru/node/4384')
    e1.save()

def add_projects():
    p1 = api_models.Project(photo=r'images\projects\67943b630bde8608d8e59005be278dec.jpeg', 
                 title='НАЗВАНИЕ ОЧЕНЬ ДЛИННОЕ КАКОЕ-НИБУДЬ ТИПА ДА', 
                 description='Хочу спать, тут какой то умный текст, бурно иммитирую активную деятельность, почему с фигмы нельзя текст скопировать', 
                 is_realized=True, 
                 type=0, 
                 slug='tipa_slug1',
                 instruction='<ul><li><b>привет жирным </b><i>привет курсивом</i></li><li>просто привет <font color="#000000" style="background-color: rgb(255, 255, 0);">привет </font><font color="#000000" style="background-color: rgb(255, 255, 0);">жёлтым</font></li><li><span style="font-family: &quot;Times New Roman&quot;; font-size: 36px;">привет другим шрифтом и размером</span></li></ul><p><img src="/media/django-summernote/2023-12-05/ed32b7cb-c034-4063-af2f-cedb331bcad1.jpg" style="width: 698.857px;"><br></p><p><sub>&nbsp;</sub></p>')
    p1.save()
    p1.authors.add(1, 2)
    p1 = api_models.Project(photo=r'images\projects\67943b630bde8608d8e59005be278dec.jpeg', 
                 title='НАЗВАНИЕ ОЧЕНЬ ДЛИННОЕ КАКОЕ-НИБУДЬ ТИПА ДА', 
                 description='Хочу спать, тут какой то умный текст, бурно иммитирую активную деятельность, почему с фигмы нельзя текст скопировать', 
                 is_realized=True, 
                 type=1, 
                 slug='tipa_slug2',
                 instruction='<ul><li><b>привет жирным </b><i>привет курсивом</i></li><li>просто привет <font color="#000000" style="background-color: rgb(255, 255, 0);">привет </font><font color="#000000" style="background-color: rgb(255, 255, 0);">жёлтым</font></li><li><span style="font-family: &quot;Times New Roman&quot;; font-size: 36px;">привет другим шрифтом и размером</span></li></ul><p><img src="/media/django-summernote/2023-12-05/ed32b7cb-c034-4063-af2f-cedb331bcad1.jpg" style="width: 698.857px;"><br></p><p><sub>&nbsp;</sub></p>')
    p1.save()
    p1.authors.add(1, 2)
    p1 = api_models.Project(photo=r'images\projects\67943b630bde8608d8e59005be278dec.jpeg', 
                 title='НАЗВАНИЕ ОЧЕНЬ ДЛИННОЕ КАКОЕ-НИБУДЬ ТИПА ДА', 
                 description='Хочу спать, тут какой то умный текст, бурно иммитирую активную деятельность, почему с фигмы нельзя текст скопировать', 
                 is_realized=True, 
                 type=0, 
                 slug='tipa_slug3',
                 instruction='<ul><li><b>привет жирным </b><i>привет курсивом</i></li><li>просто привет <font color="#000000" style="background-color: rgb(255, 255, 0);">привет </font><font color="#000000" style="background-color: rgb(255, 255, 0);">жёлтым</font></li><li><span style="font-family: &quot;Times New Roman&quot;; font-size: 36px;">привет другим шрифтом и размером</span></li></ul><p><img src="/media/django-summernote/2023-12-05/ed32b7cb-c034-4063-af2f-cedb331bcad1.jpg" style="width: 698.857px;"><br></p><p><sub>&nbsp;</sub></p>')
    p1.save()
    p1.authors.add(1, 2)
    p1 = api_models.Project(photo=r'images\projects\67943b630bde8608d8e59005be278dec.jpeg', 
                 title='НАЗВАНИЕ ОЧЕНЬ ДЛИННОЕ КАКОЕ-НИБУДЬ ТИПА ДА', 
                 description='Хочу спать, тут какой то умный текст, бурно иммитирую активную деятельность, почему с фигмы нельзя текст скопировать', 
                 is_realized=True, 
                 type=1, 
                 slug='tipa_slug4',
                 instruction='<ul><li><b>привет жирным </b><i>привет курсивом</i></li><li>просто привет <font color="#000000" style="background-color: rgb(255, 255, 0);">привет </font><font color="#000000" style="background-color: rgb(255, 255, 0);">жёлтым</font></li><li><span style="font-family: &quot;Times New Roman&quot;; font-size: 36px;">привет другим шрифтом и размером</span></li></ul><p><img src="/media/django-summernote/2023-12-05/ed32b7cb-c034-4063-af2f-cedb331bcad1.jpg" style="width: 698.857px;"><br></p><p><sub>&nbsp;</sub></p>')
    p1.save()
    p1.authors.add(1, 2)
    p1 = api_models.Project(photo=r'images\projects\67943b630bde8608d8e59005be278dec.jpeg', 
                 title='НАЗВАНИЕ ОЧЕНЬ ДЛИННОЕ КАКОЕ-НИБУДЬ ТИПА ДА', 
                 description='Хочу спать, тут какой то умный текст, бурно иммитирую активную деятельность, почему с фигмы нельзя текст скопировать', 
                 is_realized=True, 
                 type=0, 
                 slug='tipa_slug5',
                 instruction='<ul><li><b>привет жирным </b><i>привет курсивом</i></li><li>просто привет <font color="#000000" style="background-color: rgb(255, 255, 0);">привет </font><font color="#000000" style="background-color: rgb(255, 255, 0);">жёлтым</font></li><li><span style="font-family: &quot;Times New Roman&quot;; font-size: 36px;">привет другим шрифтом и размером</span></li></ul><p><img src="/media/django-summernote/2023-12-05/ed32b7cb-c034-4063-af2f-cedb331bcad1.jpg" style="width: 698.857px;"><br></p><p><sub>&nbsp;</sub></p>')
    p1.save()
    p1.authors.add(1, 2)
    p1 = api_models.Project(photo=r'images\projects\67943b630bde8608d8e59005be278dec.jpeg', 
                 title='НАЗВАНИЕ ОЧЕНЬ ДЛИННОЕ КАКОЕ-НИБУДЬ ТИПА ДА', 
                 description='Хочу спать, тут какой то умный текст, бурно иммитирую активную деятельность, почему с фигмы нельзя текст скопировать', 
                 is_realized=False, 
                 type=1, 
                 slug='tipa_slug6',
                 instruction='<ul><li><b>привет жирным </b><i>привет курсивом</i></li><li>просто привет <font color="#000000" style="background-color: rgb(255, 255, 0);">привет </font><font color="#000000" style="background-color: rgb(255, 255, 0);">жёлтым</font></li><li><span style="font-family: &quot;Times New Roman&quot;; font-size: 36px;">привет другим шрифтом и размером</span></li></ul><p><img src="/media/django-summernote/2023-12-05/ed32b7cb-c034-4063-af2f-cedb331bcad1.jpg" style="width: 698.857px;"><br></p><p><sub>&nbsp;</sub></p>')
    p1.save()
    p1.authors.add(1, 2)
    p1 = api_models.Project(photo=r'images\projects\67943b630bde8608d8e59005be278dec.jpeg', 
                 title='НАЗВАНИЕ ОЧЕНЬ ДЛИННОЕ КАКОЕ-НИБУДЬ ТИПА ДА', 
                 description='Хочу спать, тут какой то умный текст, бурно иммитирую активную деятельность, почему с фигмы нельзя текст скопировать', 
                 is_realized=False, 
                 type=0, 
                 slug='tipa_slug7',
                 instruction='<ul><li><b>привет жирным </b><i>привет курсивом</i></li><li>просто привет <font color="#000000" style="background-color: rgb(255, 255, 0);">привет </font><font color="#000000" style="background-color: rgb(255, 255, 0);">жёлтым</font></li><li><span style="font-family: &quot;Times New Roman&quot;; font-size: 36px;">привет другим шрифтом и размером</span></li></ul><p><img src="/media/django-summernote/2023-12-05/ed32b7cb-c034-4063-af2f-cedb331bcad1.jpg" style="width: 698.857px;"><br></p><p><sub>&nbsp;</sub></p>')
    p1.save()
    p1.authors.add(1, 2)
    p1 = api_models.Project(photo=r'images\projects\67943b630bde8608d8e59005be278dec.jpeg', 
                 title='НАЗВАНИЕ ОЧЕНЬ ДЛИННОЕ КАКОЕ-НИБУДЬ ТИПА ДА', 
                 description='Хочу спать, тут какой то умный текст, бурно иммитирую активную деятельность, почему с фигмы нельзя текст скопировать', 
                 is_realized=False, 
                 type=1, 
                 slug='tipa_slug8',
                 instruction='<ul><li><b>привет жирным </b><i>привет курсивом</i></li><li>просто привет <font color="#000000" style="background-color: rgb(255, 255, 0);">привет </font><font color="#000000" style="background-color: rgb(255, 255, 0);">жёлтым</font></li><li><span style="font-family: &quot;Times New Roman&quot;; font-size: 36px;">привет другим шрифтом и размером</span></li></ul><p><img src="/media/django-summernote/2023-12-05/ed32b7cb-c034-4063-af2f-cedb331bcad1.jpg" style="width: 698.857px;"><br></p><p><sub>&nbsp;</sub></p>')
    p1.save()
    p1.authors.add(1, 2)
    p1 = api_models.Project(photo=r'images\projects\67943b630bde8608d8e59005be278dec.jpeg', 
                 title='НАЗВАНИЕ ОЧЕНЬ ДЛИННОЕ КАКОЕ-НИБУДЬ ТИПА ДА', 
                 description='Хочу спать, тут какой то умный текст, бурно иммитирую активную деятельность, почему с фигмы нельзя текст скопировать', 
                 is_realized=False, 
                 type=0, 
                 slug='tipa_slug9',
                 instruction='<ul><li><b>привет жирным </b><i>привет курсивом</i></li><li>просто привет <font color="#000000" style="background-color: rgb(255, 255, 0);">привет </font><font color="#000000" style="background-color: rgb(255, 255, 0);">жёлтым</font></li><li><span style="font-family: &quot;Times New Roman&quot;; font-size: 36px;">привет другим шрифтом и размером</span></li></ul><p><img src="/media/django-summernote/2023-12-05/ed32b7cb-c034-4063-af2f-cedb331bcad1.jpg" style="width: 698.857px;"><br></p><p><sub>&nbsp;</sub></p>')
    p1.save()
    p1.authors.add(1, 2)
    p1 = api_models.Project(photo=r'images\projects\67943b630bde8608d8e59005be278dec.jpeg', 
                 title='НАЗВАНИЕ ОЧЕНЬ ДЛИННОЕ КАКОЕ-НИБУДЬ ТИПА ДА', 
                 description='Хочу спать, тут какой то умный текст, бурно иммитирую активную деятельность, почему с фигмы нельзя текст скопировать', 
                 is_realized=False, 
                 type=1, 
                 slug='tipa_slug10',
                 instruction='<ul><li><b>привет жирным </b><i>привет курсивом</i></li><li>просто привет <font color="#000000" style="background-color: rgb(255, 255, 0);">привет </font><font color="#000000" style="background-color: rgb(255, 255, 0);">жёлтым</font></li><li><span style="font-family: &quot;Times New Roman&quot;; font-size: 36px;">привет другим шрифтом и размером</span></li></ul><p><img src="/media/django-summernote/2023-12-05/ed32b7cb-c034-4063-af2f-cedb331bcad1.jpg" style="width: 698.857px;"><br></p><p><sub>&nbsp;</sub></p>')
    p1.save()
    p1.authors.add(1, 2)

def add_publications():
    p1 = api_models.Publication(title='ОПРЕДЕЛЕНИЕ ПОРОДЫ ДЕРЕВА ПО ДАННЫМ БПЛА В ЗАДАЧЕ ЛЕСНОЙ ТАКСАЦИИ НА ТЕРРИТОРИИ КУЗНЕЦОВСКОГО ПЛАТО', 
                     authors='Жуковская В. А., Пятаева А. В., Гулютин Н. Н., Научный редактор Е. А. Ваганов, отв. редактор Г. М. Цибульский', 
                     journal='2023, Региональные проблемы дистанционного зондирования Земли', 
                     link='https://www.youtube.com/')
    p1.save()
    p1 = api_models.Publication(title='ИСПОЛЬЗОВАНИЕ ЯЗЫКОВЫХ МОДЕЛЕЙ TS ДЛЯ ЗАДАЧИ УПРОЩЕНИЯ ТЕКСТА', 
                     authors='Васильев Д. Д., Пятаева А. В.', 
                     journal='2023, Программные продукты и системы', 
                     link='https://www.youtube.com/')
    p1.save()
    p1 = api_models.Publication(title='ОПРЕДЕЛЕНИЕ ПОРОДЫ ДЕРЕВА ПО ДАННЫМ БПЛА В ЗАДАЧЕ ЛЕСНОЙ ТАКСАЦИИ НА ТЕРРИТОРИИ КУЗНЕЦОВСКОГО ПЛАТО', 
                     authors='Пятвева А. В.', 
                     journal='2022, Материвлы 20-й Международной конференции "Современные проблемы дистанционного зондирования Земли из космоса"', 
                     link='https://www.youtube.com/')
    p1.save()
    p1 = api_models.Publication(title='МОДЕЛЬ ПРЕДСТАВЛЕНИЯ ЯЗЫКА BERT', 
                     authors='Васильев Д. Д., Пятаева А. В.. Министерство науки и высшего образования Российской Федерации, Сибирский федеральный университет, Межинститутская базовая кафедра "Прикладная физика и космические технологии"', 
                     journal='2022, Робототехника и искусственный интеллект', 
                     link='https://www.youtube.com/')
    p1.save()
    p1 = api_models.Publication(title='РАСПОЗНАВАНИЕ ЖЕСТОВ НА ОСНОВЕ ТЕХНОЛОГИЙ ГЛУБОКОГО ОБУЧЕНИЯ', 
                     authors='Жуковская В. А., Пятвева', 
                     journal='2022, АКТУАЛЬНЫЕ ПРОБЛЕМЫ АВИАЦИИ И КОСМОНАВТИКИ', 
                     link='https://www.youtube.com/')
    p1.save()
    p1 = api_models.Publication(title='ИСПОЛЬЗОВАНИЕ ЯЗЫКОВЫХ МОДЕЛЕЙ TS ДЛЯ ЗАДАЧИ УПРОЩЕНИЯ ТЕКСТА', 
                     authors='Жуковская В. А., Пятаева', 
                     journal='2022, АКТУАЛЬНЫЕ ПРОБЛЕМЫ АВИАЦИИ И КОСМОНАВТИКИ', 
                     link='https://www.youtube.com/')
    p1.save()
    p1 = api_models.Publication(title='placeholder', 
                     authors='placeholder', 
                     journal='placeholder', 
                     link='https://www.youtube.com/')
    p1.save()
    p1 = api_models.Publication(title='placeholder', 
                     authors='placeholder', 
                     journal='placeholder', 
                     link='https://www.youtube.com/')
    p1.save()
    p1 = api_models.Publication(title='placeholder', 
                     authors='placeholder', 
                     journal='placeholder', 
                     link='https://www.youtube.com/')
    p1.save()

def add_articles():
    p1 = api_models.Article(photo='asdfasdfasd',
                     title='Искусственный интеллект открывает новые горизонты в медицинской диагностике 1', 
                     text='23 ноября в рамках открытого круглого стола на Красноярском Цифровом Форуме мы провели презентацию проекта "Создание центра компетенции ИИ, оценка уровня решений в промышленности и отраслях"Публично представили технологическим партнерам программу Центра, направленную на решение различных задач цифровой промышленности с помощью методов искусственного интеллекта. В рамках обсуждения получили полную поддержку от нашего главного партнера: компании ООО «РУСАЛ ИТЦ» и наметили план дальнейших действий.Особенно остро перед жителями Красноярского края сейчас стоит проблема экологии региона, поэтому Центр будет не просто применять ИИ-решения на производстве, но и активно влиять на экологию промышленных производств.',
                     is_published=True)
    p1.save()
    p1 = api_models.Article(photo='adsfasdf',
                     title='Искусственный интеллект закрывает новые горизонты в медицинской диагностике 2', 
                     text='23 ноября в рамках открытого круглого стола на Красноярском Цифровом Форуме мы провели презентацию проекта.',
                     is_published=True)
    p1.save()
    p1 = api_models.Article(photo='adsfasdf',
                     title='Искусственный интеллект закрывает новые горизонты в медицинской диагностике 3', 
                     text='23 ноября в рамках открытого круглого стола на Красноярском Цифровом Форуме мы провели презентацию проекта.',
                     is_published=True)
    p1.save()
    p1 = api_models.Article(photo='adsfasdf',
                     title='Искусственный интеллект закрывает новые горизонты в медицинской диагностике 4', 
                     text='23 ноября в рамках открытого круглого стола на Красноярском Цифровом Форуме мы провели презентацию проекта.',
                     is_published=True)
    p1.save()
    p1 = api_models.Article(photo='adsfasdf',
                     title='Искусственный интеллект закрывает новые горизонты в медицинской диагностике 5', 
                     text='23 ноября в рамках открытого круглого стола на Красноярском Цифровом Форуме мы провели презентацию проекта.',
                     is_published=True)
    p1.save()

add_employees()
add_projects()
add_publications()
add_articles()