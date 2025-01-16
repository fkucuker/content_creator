import re

def sanitize_filename(filename, max_length=50):
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    if len(filename) > max_length:
        filename = filename[:max_length] + "_"
    return filename

def sanitize_date(date):
    return date.replace(":", "-")
