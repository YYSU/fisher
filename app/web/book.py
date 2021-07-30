from flask import jsonify, request

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web


@web.route('/book/search')
def search():
    """
        q : keyword or isbn
        page
    :return:
    """
    # validate query string
    form = SearchForm(request.args)
    if not form.validate():
        return jsonify(form.errors), 400

    q = form.q.data.strip()
    page = form.page.data
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q, page)
    return jsonify(result)
