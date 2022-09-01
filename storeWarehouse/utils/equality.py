def equal(old_instance, instance):
    for v1, v2 in zip(old_instance.values(), instance.values()):
        if not v1 == v2:
            return False
    return True
