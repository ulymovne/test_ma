from flask import Flask, jsonify
from product import get_data, responce

app = Flask(__name__)

index_html = f'<h2><a href="/test1/"> Список продуктов </a><br><a href="/test2/">Список категорий</a><br><a href="/test3/">Список всех пар</a>'

@app.route('/')
def index():
    return index_html

@app.route("/test1/")
def route_product():
    query = "SELECT product_name, category_name FROM pairs JOIN products ON products.product_id=pairs.product_id LEFT JOIN categories ON categories.category_id=pairs.category_id "
    data = get_data('lite.db', query)
    return responce(1, data)

@app.route("/test2/")
def route_cat():
    query = "SELECT category_name, product_name FROM pairs JOIN categories ON categories.category_id=pairs.category_id LEFT JOIN products ON products.product_id=pairs.product_id  "
    data = get_data('lite.db', query)
    return responce(2, data)

@app.route("/test3/")
def route_pare():
    query = "SELECT product_name, category_name FROM pairs JOIN categories ON categories.category_id=pairs.category_id JOIN products ON products.product_id=pairs.product_id"
    data = get_data('lite.db', query)
    return responce(3, data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)