# Ezequiel Zapata PSID: 001863257

# Final Project part 1 creating a program that manages the inventory of an electronics store.
# This program will be able to any manufacturer, price, and service dates lists and output .csv files that are required
# using the OS path to the .csv files.

import os
import datetime

INCLUDE_HEADER = False


def createRow(header, data):
    # creates a row for a csv with the data as a dict and the header (to get the correct order)
    result = []
    # loop over the header and the corresponding data to the result
    for h in header:
        result.append(str(data[h]))
    return ','.join(result)


def createCSV(data, cols, path):
    # create csv with given data and columns and save it at path
    saveData = []
    if INCLUDE_HEADER:
        # add header, if selected
        saveData.append(','.join(cols))
    for dataRow in data:
        # loop over all of the data and append row
        saveData.append(createRow(cols, dataRow))
    with open(path, "w") as f:
        # save in file
        f.write('\n'.join(saveData))


def parseRow(header, row):
    # parse row of csv as a dict
    result = dict()
    for h, r in zip(header, row.split(',')):
        result[h] = r.strip()
    return result


def parseCSV(path, cols):
    # parse csv as a list of dictionaries for each row
    result = []
    with open(path, "r") as f:
        lines = f.read().splitlines()
        for line in lines:
            result.append(parseRow(cols, line))
    return result


def main(mP, pP, sP):
    # main function with path to all input .csv files
    # get all the data
    manufacturerList = parseCSV(
        mP, ["item ID", "manufacturer name", "item type", "damaged indicator"])
    priceList = parseCSV(pP, ["item ID", "price"])
    serviceList = parseCSV(sP, ["item ID", "service date"])
    allItems = dict()
    # join all the data in the allItems dict, which maps from id to the item dict
    for m in manufacturerList:
        allItems[m["item ID"]] = m
    # created base data, add price and service date to the list
    for p in priceList:
        allItems[p["item ID"]]["price"] = p["price"]
    for s in serviceList:
        allItems[s["item ID"]]["service date"] = s["service date"]
    # create fullInventory csv
    createCSV(sorted(list(allItems.values()), key=lambda x: x["manufacturer name"]), [
              "item ID", "manufacturer name", "item type", "price", "service date", "damaged indicator"], "FullInventory.csv")

    # create for each other result csv a list (or dict with lists for each item)
    damagedItems = []
    itemTypes = dict()
    pastService = []
    now = datetime.datetime.now().date()
    for item in allItems.values():
        # loop over all items and add to needed list
        if item["damaged indicator"] != "":
            damagedItems.append(item)
        if item["item type"] not in itemTypes:
            # add list, if there wasn't this item type
            itemTypes[item["item type"]] = []
        itemTypes[item["item type"]].append(item)
        # create date from service date string
        dateParts = item["service date"].split('/')
        date = datetime.date(int(dateParts[2]), int(
            dateParts[0]), int(dateParts[1]))
        item["date"] = date
        if date < now:
            pastService.append(item)

    # create damaged csv
    createCSV(sorted(damagedItems, key=lambda x: x["price"], reverse=True), [
              "item ID", "manufacturer name", "item type", "price", "service date"], "DamagedInventory.csv")

    for t, items in itemTypes.items():
        # loop over each item type and create csv with all items
        createCSV(sorted(items, key=lambda x: x["item ID"]), [
            "item ID", "manufacturer name", "item type", "price", "service date", "damaged indicator"], "{}Inventory.csv".format(t))

    # create past service data csv
    createCSV(sorted(pastService, key=lambda x: x["date"]), [
              "item ID", "manufacturer name", "item type", "price", "service date"], "PastServiceDateInventory.csv")


if __name__ == '__main__':
    # get all the correct paths
    manufacturerPath = "ManufacturerList.csv"
    while not os.path.exists(manufacturerPath):
        manufacturerPath = input('Path to the manufacturer list: ')
    pricePath = "PriceList.csv"
    while not os.path.exists(pricePath):
        pricePath = input('Path to the Price list: ')
    servicePath = "ServiceDatesList.csv"
    while not os.path.exists(servicePath):
        servicePath = input('Path to the service dates list: ')
    # call main function
    main(manufacturerPath, pricePath, servicePath)
