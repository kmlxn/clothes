from django.template import Library
register = Library()

@register.inclusion_tag('catalog/filters_partial.html')
def render_filters(filters_list):
    return {'filters_list': filters_list}


@register.inclusion_tag('catalog/clothes_partial.html')
def render_clothes_grid(clothes):
    return {'clothes': clothes}


@register.inclusion_tag('catalog/pagination_partial.html')
def render_pagination(cur_page_num, pages_num):
    paginator = MyPaginator(cur_page_num, pages_num)

    return {
        'buttons': paginator.make_buttons(),
    }


class MyPaginator:
    simple_buttons_count = 3

    def __init__(self, cur_page_num, pages_num):
        self.cur_page_num = cur_page_num
        self.pages_num = pages_num
        self.paging_end, self.paging_start = self.determine_pagination_range()


    def make_buttons(self):
        if self.pages_num == 1:
            return None

        collector = []

        collector.append(self.make_first_page_button())
        collector.append(self.make_prev_page_button())
        collector.extend(self.make_pages_buttons())
        collector.append(self.make_next_page_button())
        collector.append(self.make_last_page_button())

        buttons = [e for e in collector if e is not None]

        return buttons


    def make_last_page_button(self):
        if self.paging_end < self.pages_num:
            return 'last', self.pages_num
        else:
            return None


    def make_next_page_button(self):
        if self.paging_end < self.pages_num:
            next_page_num = self.cur_page_num + 1 if self.cur_page_num < self.pages_num else None
            return 'next', next_page_num
        else:
            return None


    def make_pages_buttons(self):
        buttons = []
        for page_num in range(self.paging_start, self.paging_end + 1):
            if page_num == self.cur_page_num:
                buttons.append(('cur_page', page_num))
            else:
                buttons.append(('page', page_num))
        return buttons


    def make_prev_page_button(self):
        if self.paging_start > 1:
            prev_page_num = self.cur_page_num - 1 if self.cur_page_num > 1 else None
            return 'prev', prev_page_num
        else:
            return None


    def make_first_page_button(self):
        if self.paging_start > self.simple_buttons_count // 2:
            return 'first', 1
        else:
            return None


    def determine_pagination_range(self):
        paging_start = self.cur_page_num - (self.simple_buttons_count - 1) // 2
        if paging_start < 1:
            paging_start = 1
        elif paging_start > 1:
            if paging_start + self.simple_buttons_count - 1 > self.pages_num:
                paging_start = self.pages_num - self.simple_buttons_count + 1

        paging_end = paging_start + self.simple_buttons_count - 1
        if paging_end > self.pages_num:
            paging_end = self.pages_num

        return paging_end, paging_start
