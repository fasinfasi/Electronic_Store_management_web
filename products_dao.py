from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()
    query = ("SELECT products.product_id, products.product_name, products.uom_id, products.price_per_unit, uom.uom_name "
            "FROM electronic_store.products INNER JOIN uom on products.uom_id=uom.uom_id")
    cursor.execute(query)
    
    response = []
    for (product_id, product_name, uom_id, price_per_unit, uom_name) in cursor:
        response.append(
            {
                'product_id': product_id,
                'product_name': product_name,
                'uom_id': uom_id,
                'price_per-unit': price_per_unit,
                'uom_name': uom_name
            }
            )
    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(product_name, uom_id, price_per_unit)"
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products WHERE product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

if __name__=='__main__':
    connection = get_sql_connection()
    #print(get_all_products(connection))
    """print(insert_new_product(connection, {
        'product_name': 'Fun Regulator',
        'uom_id': '1',
        'price_per_unit': '60'
    }))"""
    
    print(delete_product(connection, 115))
