def get_body_attr_or_replace(tag, body, obj):
    if tag in body:
        return body[tag]
    else:
        return obj.__dict__[tag]
