def filter_by_state(data, state='EXECUTED'):
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param data: Список словарей для фильтрации
    :param state: Значение для фильтрации, по умолчанию 'EXECUTED'
    :return: Новый список словарей, соответствующих указанному значению ключа 'state'
    """
    return [item for item in data if item.get('state') == state]

    filtered_data = filter_by_state(data)
    print(filtered_data)  # [{'id': 1, 'state': 'EXECUTED'}, {'id': 3, 'state': 'EXECUTED'}]

    from datetime import datetime
    filtered_data = filter_by_state(data)
    print(filtered_data)  # [{'id': 1, 'state': 'EXECUTED'}, {'id': 3, 'state': 'EXECUTED'}]



    def sort_by_date(data, descending=True):
        """
        Сортирует список словарей по дате.

        :param data: Список словарей с ключом 'date'
        :param descending: Параметр, определяющий порядок сортировки (по умолчанию True — убывание)
        :return: Новый отсортированный список словарей
        """
        # Сортировка списка словарей по дате
        return sorted(data, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'), reverse=descending)
        sorted_data_descending = sort_by_date(data)
        print("Сортировка по убыванию:")
        print(sorted_data_descending)

        sorted_data_ascending = sort_by_date(data, descending=False)
        print("Сортировка по возрастанию:")
        print(sorted_data_ascending)