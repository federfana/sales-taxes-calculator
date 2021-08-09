import json


def calculateImported(price, imported):
    if imported == 'Y':
        return round((price * 0.05), 1)
    else:
        return 0.0


def calculateTax(price):
    return price * 0.10


def sendReceipt(shoplist):
    message = ""
    for item in shoplist['items']:
        message += str(item['qty']) + " " + item['product'] + \
            ": " + str(item['price']) + "\n"
    message += "Sales Taxes: " + str(shoplist['SalesTaxes']) + "\n"
    message += "Total: " + str(shoplist['Total']) + "\n"
    return message


def lambda_handler(event, context):
    itemTaxes = 0.0
    salesTaxes = 0.0
    total = 0.0
    for item in event['items']:
        if item['specialproduct'] == 'Y':
            itemTaxes = calculateImported(
                item['price'], item['imported']) * item['qty']
            salesTaxes += itemTaxes
        else:
            itemTaxes = calculateTax(item['price']) * item['qty'] + calculateImported(
                item['price'], item['imported']) * item['qty']
            salesTaxes += itemTaxes
        item['price'] = round(item['price'] * item['qty'] + itemTaxes, 2)
        total += item['price']
    event['SalesTaxes'] = round(salesTaxes, 2)
    event['Total'] = total
    return sendReceipt(event)


