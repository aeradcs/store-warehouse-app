def equal(old_instance, instance):
    for v1, v2 in zip(old_instance.values(), instance.values()):
        if not v1 == v2:
            return False
    return True


def get_id_by_unique_identifier(table_rows, unique_identifier):
    for row in table_rows:
        if row['object_id'] == unique_identifier:
            id = row['id']
            del row['id']
            return id, row
