import json


def calculateImported(price, imported):
    if imported:
        return round((price * 0.05), 1)
    else:
        return 0.0


def calculateTax(price):
    return price * 0.10


def processItems(items):
    itemTaxes = 0.0
    salesTaxes = 0.0
    total = 0.0
    try:
        for item in items['items']:
            if item['specialproduct']:
                itemTaxes = calculateImported(
                    item['price'], item['imported']) * item['qty']
                salesTaxes += itemTaxes
            else:
                itemTaxes = calculateTax(item['price']) * item['qty'] + calculateImported(
                    item['price'], item['imported']) * item['qty']
                salesTaxes += itemTaxes
            item['price'] = round(item['price'] * item['qty'] + itemTaxes, 2)
            total += item['price']
        items['SalesTaxes'] = round(salesTaxes, 2)
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
    return processItems(event)
