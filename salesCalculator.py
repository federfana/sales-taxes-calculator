def calculate_imported(price, imported):
    return round((price * 0.05), 1) if imported else 0.0


def calculate_tax(price):
    return price * 0.10


def process_items(items):
    sales_taxes = 0.0
    total = 0.0
    try:
        for item in items['items']:
            if item['specialproduct']:
                item_taxes = calculate_imported(
                    item['price'], item['imported']) * item['qty']
                sales_taxes += item_taxes
            else:
                item_taxes = calculate_tax(item['price']) * item['qty'] + calculate_imported(
                    item['price'], item['imported']) * item['qty']
                sales_taxes += item_taxes
            item['price'] = round(item['price'] * item['qty'] + item_taxes, 2)
            total += item['price']
        items['SalesTaxes'] = round(sales_taxes, 2)
        items['Total'] = total
        return {
            'statusCode': 200,
            'body': items
        }
    except:
        return {
            'statusCode': 500,
            'body': "Invalid Request"
        }


def lambda_handler(event, context):
    return process_items(event)
