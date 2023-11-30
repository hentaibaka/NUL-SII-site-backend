from django.utils.text import slugify

def my_slugify(string: str):
    alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}
    return slugify(''.join(alphabet.get(w, w) for w in string.lower()))

def handle_project_photo(instance, filename: str):
    project_slug = my_slugify(instance.title)
    filename = f'{project_slug}.{filename.split(".")[1]}'
    return f'images/projects/{filename}'

def handle_employee_photo(instance, filename: str):
    employee_slug = my_slugify(f'{instance.last_name} {instance.first_name}' + 
                               f' {instance.patronymic}' if instance.patronymic else '')
    filename = f'{employee_slug}.{filename.split(".")[1]}'
    return f'images/employees/{filename}'