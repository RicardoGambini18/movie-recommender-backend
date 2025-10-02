import ast
from faker import Faker
from datetime import datetime, date
from enums import MovieStatus, Gender, Department


faker = Faker('es_ES')


def validate_and_convert_dict(value):
    if isinstance(value, dict):
        return value
    if not value or not isinstance(value, str) or value.strip() == '':
        return None
    try:
        result = ast.literal_eval(value)
        if not isinstance(result, dict):
            return None
        return result
    except (ValueError, SyntaxError):
        return None


def validate_and_convert_list(value):
    if isinstance(value, list):
        return value
    if not value or not isinstance(value, str) or value.strip() == '' or value.strip() == '[]':
        return []
    try:
        result = ast.literal_eval(value)
        if isinstance(result, list):
            return result
        else:
            return None
    except (ValueError, SyntaxError):
        return None


def validate_and_convert_int(value):
    if isinstance(value, int):
        return value
    if not value or not isinstance(value, str) or value.strip() == '':
        return None
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def validate_and_convert_float(value):
    if isinstance(value, float):
        return value
    if not value or not isinstance(value, str) or value.strip() == '' or value.strip() == 'nan':
        return None
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def validate_and_convert_boolean(value):
    if isinstance(value, bool):
        return value
    if not value or not isinstance(value, str) or (value.strip().lower() != 'true' and value.strip().lower() != 'false'):
        return None
    return value.strip().lower() == 'true'


def is_row_valid(row, required_fields):
    for field in required_fields:
        if not row[field] or str(row[field]).strip() == '':
            return False
    return True


def validate_and_convert_movie_status(status):
    if status == 'Released':
        return MovieStatus.RELEASED
    elif status == 'Rumored':
        return MovieStatus.RUMORED
    elif status == 'Post Production':
        return MovieStatus.POST_PRODUCTION
    elif status == 'In Production':
        return MovieStatus.IN_PRODUCTION
    elif status == 'Planned':
        return MovieStatus.PLANNED
    elif status == 'Canceled':
        return MovieStatus.CANCELED
    else:
        return None


def validate_and_convert_date(value):
    if isinstance(value, date):
        return value
    if not value or not isinstance(value, str) or value.strip() == '':
        return None
    try:
        return datetime.strptime(value, '%Y-%m-%d').date()
    except (ValueError, TypeError):
        return None


def validate_and_convert_gender(gender):
    if gender == 1:
        return Gender.FEMALE
    elif gender == 2:
        return Gender.MALE
    else:
        return None


def validate_and_convert_department(department):
    if department == 'Directing':
        return Department.DIRECTING
    elif department == 'Writing':
        return Department.WRITING
    elif department == 'Production':
        return Department.PRODUCTION
    elif department == 'Editing':
        return Department.EDITING
    elif department == 'Art':
        return Department.ART
    elif department == 'Sound':
        return Department.SOUND
    elif department == 'Visual Effects':
        return Department.VISUAL_EFFECTS
    elif department == 'Crew':
        return Department.CREW
    elif department == 'Lighting':
        return Department.LIGHTING
    elif department == 'Camera':
        return Department.CAMERA
    elif department == 'Costume & Make-Up':
        return Department.COSTUME_AND_MAKE_UP
    elif department == 'Actors':
        return Department.ACTORS
    else:
        return None


def get_email(name):
    name_section = name.replace(' ', '.').lower()
    number_section = faker.random_int(min=10, max=99)
    domain_section = faker.random_element(elements=(
        'hotmail.com',
        'gmail.com',
        'yahoo.com',
        'outlook.com',
    ))
    return f"{name_section}{number_section}@{domain_section}"


def get_image_url(width=400, height=400, grayscale=False, blur=0):
    base_url = "https://picsum.photos"
    params = []

    if grayscale:
        params.append("grayscale")
    if blur > 0:
        params.append(f"blur={blur}")

    param_string = f"/?{'&'.join(params)}" if len(params) > 0 else ""
    return f"{base_url}/{width}/{height}{param_string}"


def process_batch(items: list[dict], callback: callable, batch_size: int = 300):
    for i in range(0, len(items), batch_size):
        batch = items[i:i + batch_size]
        batch_number = i // batch_size + 1
        current_batch_size = len(batch)
        callback(batch, batch_number, current_batch_size)
