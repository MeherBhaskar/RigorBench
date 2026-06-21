def get_page(items, page_num, page_size):
    start = (page_num - 1) * page_size
    end = start + page_size
    return items[start:end]