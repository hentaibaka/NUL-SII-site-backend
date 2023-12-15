from django.db import migrations


def add_employees(apps, schema_editor):
    Employee = apps.get_model('api_v1', 'Employee')
    e1 = Employee(photo=r'images\employees\photo_2023-09-23_10-00-48.jpg', 
                  post='РУКОВОДИТЕЛЬ ЛАБОРАТОРИИ', 
                  last_name='Пятаева', first_name='Анна', patronymic='Владимировна', 
                  link='https://structure.sfu-kras.ru/node/4384')
    e1.save()
    e1 = Employee(photo=r'images\employees\photo_2023-09-23_10-00-48.jpg', 
                  post='РУКОВОДИТЕЛЬ ЛАБОРАТОРИИ', 
                  last_name='Пятаева', first_name='Анна', patronymic='Владимировна', 
                  link='https://structure.sfu-kras.ru/node/4384')
    e1.save()
    e1 = Employee(photo=r'images\employees\photo_2023-09-23_10-00-48.jpg', 
                  post='РУКОВОДИТЕЛЬ ЛАБОРАТОРИИ', 
                  last_name='Пятаева', first_name='Анна', patronymic='Владимировна', 
                  link='https://structure.sfu-kras.ru/node/4384')
    e1.save()
    e1 = Employee(photo=r'images\employees\photo_2023-09-23_10-00-48.jpg', 
                  post='РУКОВОДИТЕЛЬ ЛАБОРАТОРИИ', 
                  last_name='Пятаева', first_name='Анна', patronymic='Владимировна', 
                  link='https://structure.sfu-kras.ru/node/4384')
    e1.save()
    e1 = Employee(photo=r'images\employees\photo_2023-09-23_10-00-48.jpg', 
                  post='РУКОВОДИТЕЛЬ ЛАБОРАТОРИИ', 
                  last_name='Пятаева', first_name='Анна', patronymic='Владимировна', 
                  link='https://structure.sfu-kras.ru/node/4384')
    e1.save()

def add_projects(apps, schema_editor):
    Project = apps.get_model('api_v1', 'Project')
    p1 = Project(photo=r'images\projects\67943b630bde8608d8e59005be278dec.jpeg', 
                 title='НАЗВАНИЕ ОЧЕНЬ ДЛИННОЕ КАКОЕ-НИБУДЬ ТИПА ДА', 
                 description='Хочу спать, тут какой то умный текст, бурно иммитирую активную деятельность, почему с фигмы нельзя текст скопировать', 
                 is_realized=True, 
                 type=0, 
                 slug='tipa_slug1',
                 instruction='')
    p1.save()
    p1.authors.add(1, 2)
    Project = apps.get_model('api_v1', 'Project')
    p1 = Project(photo=r'images\projects\67943b630bde8608d8e59005be278dec.jpeg', 
                 title='НАЗВАНИЕ ОЧЕНЬ ДЛИННОЕ КАКОЕ-НИБУДЬ ТИПА ДА', 
                 description='Хочу спать, тут какой то умный текст, бурно иммитирую активную деятельность, почему с фигмы нельзя текст скопировать', 
                 is_realized=True, 
                 type=1, 
                 slug='tipa_slug2',
                 instruction='')
    p1.save()
    p1.authors.add(1, 2)
    Project = apps.get_model('api_v1', 'Project')
    p1 = Project(photo=r'images\projects\67943b630bde8608d8e59005be278dec.jpeg', 
                 title='НАЗВАНИЕ ОЧЕНЬ ДЛИННОЕ КАКОЕ-НИБУДЬ ТИПА ДА', 
                 description='Хочу спать, тут какой то умный текст, бурно иммитирую активную деятельность, почему с фигмы нельзя текст скопировать', 
                 is_realized=True, 
                 type=0, 
                 slug='tipa_slug3',
                 instruction='')
    p1.save()
    p1.authors.add(1, 2)
    Project = apps.get_model('api_v1', 'Project')
    p1 = Project(photo=r'images\projects\67943b630bde8608d8e59005be278dec.jpeg', 
                 title='НАЗВАНИЕ ОЧЕНЬ ДЛИННОЕ КАКОЕ-НИБУДЬ ТИПА ДА', 
                 description='Хочу спать, тут какой то умный текст, бурно иммитирую активную деятельность, почему с фигмы нельзя текст скопировать', 
                 is_realized=True, 
                 type=1, 
                 slug='tipa_slug4',
                 instruction='')
    p1.save()
    p1.authors.add(1, 2)
    Project = apps.get_model('api_v1', 'Project')
    p1 = Project(photo=r'images\projects\67943b630bde8608d8e59005be278dec.jpeg', 
                 title='НАЗВАНИЕ ОЧЕНЬ ДЛИННОЕ КАКОЕ-НИБУДЬ ТИПА ДА', 
                 description='Хочу спать, тут какой то умный текст, бурно иммитирую активную деятельность, почему с фигмы нельзя текст скопировать', 
                 is_realized=True, 
                 type=0, 
                 slug='tipa_slug5',
                 instruction='')
    p1.save()
    p1.authors.add(1, 2)
    Project = apps.get_model('api_v1', 'Project')
    p1 = Project(photo=r'images\projects\67943b630bde8608d8e59005be278dec.jpeg', 
                 title='НАЗВАНИЕ ОЧЕНЬ ДЛИННОЕ КАКОЕ-НИБУДЬ ТИПА ДА', 
                 description='Хочу спать, тут какой то умный текст, бурно иммитирую активную деятельность, почему с фигмы нельзя текст скопировать', 
                 is_realized=False, 
                 type=1, 
                 slug='tipa_slug6',
                 instruction='')
    p1.save()
    p1.authors.add(1, 2)
    Project = apps.get_model('api_v1', 'Project')
    p1 = Project(photo=r'images\projects\67943b630bde8608d8e59005be278dec.jpeg', 
                 title='НАЗВАНИЕ ОЧЕНЬ ДЛИННОЕ КАКОЕ-НИБУДЬ ТИПА ДА', 
                 description='Хочу спать, тут какой то умный текст, бурно иммитирую активную деятельность, почему с фигмы нельзя текст скопировать', 
                 is_realized=False, 
                 type=0, 
                 slug='tipa_slug7',
                 instruction='')
    p1.save()
    p1.authors.add(1, 2)
    Project = apps.get_model('api_v1', 'Project')
    p1 = Project(photo=r'images\projects\67943b630bde8608d8e59005be278dec.jpeg', 
                 title='НАЗВАНИЕ ОЧЕНЬ ДЛИННОЕ КАКОЕ-НИБУДЬ ТИПА ДА', 
                 description='Хочу спать, тут какой то умный текст, бурно иммитирую активную деятельность, почему с фигмы нельзя текст скопировать', 
                 is_realized=False, 
                 type=1, 
                 slug='tipa_slug8',
                 instruction='')
    p1.save()
    p1.authors.add(1, 2)
    Project = apps.get_model('api_v1', 'Project')
    p1 = Project(photo=r'images\projects\67943b630bde8608d8e59005be278dec.jpeg', 
                 title='НАЗВАНИЕ ОЧЕНЬ ДЛИННОЕ КАКОЕ-НИБУДЬ ТИПА ДА', 
                 description='Хочу спать, тут какой то умный текст, бурно иммитирую активную деятельность, почему с фигмы нельзя текст скопировать', 
                 is_realized=False, 
                 type=0, 
                 slug='tipa_slug9',
                 instruction='')
    p1.save()
    p1.authors.add(1, 2)
    Project = apps.get_model('api_v1', 'Project')
    p1 = Project(photo=r'images\projects\67943b630bde8608d8e59005be278dec.jpeg', 
                 title='НАЗВАНИЕ ОЧЕНЬ ДЛИННОЕ КАКОЕ-НИБУДЬ ТИПА ДА', 
                 description='Хочу спать, тут какой то умный текст, бурно иммитирую активную деятельность, почему с фигмы нельзя текст скопировать', 
                 is_realized=False, 
                 type=1, 
                 slug='tipa_slug10',
                 instruction='')
    p1.save()
    p1.authors.add(1, 2)

def add_publications(apps, schema_editor):
    Publication = apps.get_model('api_v1', 'Publication')
    p1 = Publication(title='ОПРЕДЕЛЕНИЕ ПОРОДЫ ДЕРЕВА ПО ДАННЫМ БПЛА В ЗАДАЧЕ ЛЕСНОЙ ТАКСАЦИИ НА ТЕРРИТОРИИ КУЗНЕЦОВСКОГО ПЛАТО', 
                     authors='Жуковская В. А., Пятаева А. В., Гулютин Н. Н., Научный редактор Е. А. Ваганов, отв. редактор Г. М. Цибульский', 
                     journal='2023, Региональные проблемы дистанционного зондирования Земли', 
                     link='https://www.youtube.com/')
    p1.save()
    p1 = Publication(title='ИСПОЛЬЗОВАНИЕ ЯЗЫКОВЫХ МОДЕЛЕЙ TS ДЛЯ ЗАДАЧИ УПРОЩЕНИЯ ТЕКСТА', 
                     authors='Васильев Д. Д., Пятаева А. В.', 
                     journal='2023, Программные продукты и системы', 
                     link='https://www.youtube.com/')
    p1.save()
    p1 = Publication(title='ОПРЕДЕЛЕНИЕ ПОРОДЫ ДЕРЕВА ПО ДАННЫМ БПЛА В ЗАДАЧЕ ЛЕСНОЙ ТАКСАЦИИ НА ТЕРРИТОРИИ КУЗНЕЦОВСКОГО ПЛАТО', 
                     authors='Пятвева А. В.', 
                     journal='2022, Материвлы 20-й Международной конференции "Современные проблемы дистанционного зондирования Земли из космоса"', 
                     link='https://www.youtube.com/')
    p1.save()
    p1 = Publication(title='МОДЕЛЬ ПРЕДСТАВЛЕНИЯ ЯЗЫКА BERT', 
                     authors='Васильев Д. Д., Пятаева А. В.. Министерство науки и высшего образования Российской Федерации, Сибирский федеральный университет, Межинститутская базовая кафедра "Прикладная физика и космические технологии"', 
                     journal='2022, Робототехника и искусственный интеллект', 
                     link='https://www.youtube.com/')
    p1.save()
    p1 = Publication(title='РАСПОЗНАВАНИЕ ЖЕСТОВ НА ОСНОВЕ ТЕХНОЛОГИЙ ГЛУБОКОГО ОБУЧЕНИЯ', 
                     authors='Жуковская В. А., Пятвева', 
                     journal='2022, АКТУАЛЬНЫЕ ПРОБЛЕМЫ АВИАЦИИ И КОСМОНАВТИКИ', 
                     link='https://www.youtube.com/')
    p1.save()
    p1 = Publication(title='ИСПОЛЬЗОВАНИЕ ЯЗЫКОВЫХ МОДЕЛЕЙ TS ДЛЯ ЗАДАЧИ УПРОЩЕНИЯ ТЕКСТА', 
                     authors='Жуковская В. А., Пятаева', 
                     journal='2022, АКТУАЛЬНЫЕ ПРОБЛЕМЫ АВИАЦИИ И КОСМОНАВТИКИ', 
                     link='https://www.youtube.com/')
    p1.save()
    p1 = Publication(title='placeholder', 
                     authors='placeholder', 
                     journal='placeholder', 
                     link='https://www.youtube.com/')
    p1.save()
    p1 = Publication(title='placeholder', 
                     authors='placeholder', 
                     journal='placeholder', 
                     link='https://www.youtube.com/')
    p1.save()
    p1 = Publication(title='placeholder', 
                     authors='placeholder', 
                     journal='placeholder', 
                     link='https://www.youtube.com/')
    p1.save()


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_employees),
        migrations.RunPython(add_projects),
        migrations.RunPython(add_publications),
    ]