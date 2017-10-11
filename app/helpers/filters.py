from app import app


@app.template_filter('truncate_after_tag')
def truncate_after_tag(text, target_length):
    last_closing_tag_beginning = text.find('</', target_length)
    end = text.find('>', last_closing_tag_beginning)
    new_text = text[:end + 1]
    if len(new_text) == 0:
        return text
    return new_text
