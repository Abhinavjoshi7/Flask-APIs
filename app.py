from flask import Flask , request

app = Flask(__name__)

shops =  [
    {"name": "Shop1", 
     "product":[
        {
        "name": "Mic", 
         "price": 800
        }
        ]
    }
]

@app.route("/shops")
def get_shops():
    return shops


@app.route("/shops", methods = ['POST'])
def create_shop():
    shop = request.json
    shops.append(shop)
    print('Shop', shop)
    return shop, 201

# shop_name - Path parameter
@app.route("/shops/<shop_name>/product", methods = ["POST"])
def create_product(shop_name):
    product = request.json
    for shop in shops:
        if shop['name'] == shop_name:
            shop['product'].append(product)
            return product , 201
    return {"message": "Shop not found"}, 404

@app.route("/shops/<shop_name>")
def get_shop_by_name(shop_name):
    for shop in shops:
        if shop['name'] == shop_name:
            return shop, 200
        
    return {"message": "Shop not found"}, 404
if __name__ == '__main__':
    app.run(debug = True)