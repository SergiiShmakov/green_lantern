from flask import Blueprint, render_template
from grocery_store.models import Good


goods_list = Blueprint('/goods_list', __name__)


@goods_list.route('/goods_list')
def get_goods_list():
    return render_template('goods_list.html', goods=Good.query.all())
