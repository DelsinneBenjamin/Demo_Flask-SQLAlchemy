from flask import jsonify, request
from app.forms.product_forms.product_form import ProductForm
from app import app
from app.services.product_service import ProductService


@app.get('/products')
def get_products():
    product_service = ProductService()
    return jsonify([p.serialize() for p in product_service.find_all()])


@app.get('/products/<int:productid>')
def get_product(productid):
    product_service = ProductService()
    product = product_service.find_one(productid)
    return jsonify(product.serialize()) if product else ('', 404)


@app.post('/products')
def post_product():
    product_service = ProductService()
    form = ProductForm()

    if form.validate():
        product = product_service.insert(form)
        return jsonify(product.serialize()), 201

    return jsonify(form.errors), 400


@app.put('/products/<int:productid>')
def put_product(productid):
    product_service = ProductService()
    form = ProductForm()

    if form.validate():
        product = product_service.update(productid, form)
        return jsonify(product.serialize()) if product else ('', 404)

    return jsonify(form.errors), 400


@app.delete('/products/<int:productid>')
def delete_product(productid):
    product_service = ProductService()
    success = product_service.delete(productid)
    return ('', 204) if success else ('', 404)
