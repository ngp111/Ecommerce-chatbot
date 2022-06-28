from flask import Flask, request, jsonify, render_template, make_response
from multiprocessing import Pool
import os
import dialogflow
import requests
import json
import pandas as pd
import warnings
import csv
import re
from objects import *
warnings.filterwarnings("ignore")

app = Flask(__name__)
acc_score = 0
usab_score = 0
total = 0
prev = ""
potential = []
top = []
curr_brand = ""

mobiles = pd.read_csv("ShortDatasets/Mobiles.csv")
tablets = pd.read_csv("ShortDatasets/Tablets.csv")
powerbanks = pd.read_csv("ShortDatasets/PowerBanks.csv")
desktops = pd.read_csv("ShortDatasets/Desktops.csv")
laptops = pd.read_csv("ShortDatasets/Laptops.csv")
watches = pd.read_csv("ShortDatasets/Watches.csv")
drives = pd.read_csv("ShortDatasets/Drives.csv")

def bestsellers(category) :
    global curr_brand
    print(curr_brand)  
    response = {"fulfillmentMessages":[{"text":{"text" : ["Here are some bestsellers we found in "+curr_brand+" in "+category+" category."]}}]}
    response = json.dumps(response)
    response = json.loads(response)
    payload = {"payload":{"richContent":[[]]}}
    response["fulfillmentMessages"].append(payload)
    branded = []
    counter = 0
    if category == "Mobiles" :
        for index in top :
            response["fulfillmentMessages"][1]["payload"]["richContent"][0].append({"icon": {"color": "#878fac"}})
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["type"] = "button"
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["link"] = mobiles.iloc[index]["Product URL"]
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["text"] = mobiles.iloc[index]["Product Name"]
            counter += 1
    elif category == "Tablets" :
        for index in top :
            response["fulfillmentMessages"][1]["payload"]["richContent"][0].append({"icon": {"color": "#878fac"}})
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["type"] = "button"
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["link"] = tablets.iloc[index]["Product URL"]
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["text"] = tablets.iloc[index]["Product Name"]
            counter += 1
    elif category == "Powerbanks" :
        print("In top5")
        for index in top :
            response["fulfillmentMessages"][1]["payload"]["richContent"][0].append({"icon": {"color": "#878fac"}})
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["type"] = "button"
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["link"] = powerbanks.iloc[index]["Product URL"]
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["text"] = powerbanks.iloc[index]["Product Name"]
            counter += 1       
    elif category == "Desktops" :
        print("In top5")
        for index in top :
            response["fulfillmentMessages"][1]["payload"]["richContent"][0].append({"icon": {"color": "#878fac"}})
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["type"] = "button"
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["link"] = desktops.iloc[index]["Product URL"]
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["text"] = desktops.iloc[index]["Product Name"]
            counter += 1
    elif category == "Laptops" :
        print("In top5")
        for index in top :
            response["fulfillmentMessages"][1]["payload"]["richContent"][0].append({"icon": {"color": "#878fac"}})
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["type"] = "button"
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["link"] = laptops.iloc[index]["Product URL"]
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["text"] = laptops.iloc[index]["Product Name"]
            counter += 1
    elif category == "Smart Watches":
        print("In top5")
        for index in top :
            response["fulfillmentMessages"][1]["payload"]["richContent"][0].append({"icon": {"color": "#878fac"}})
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["type"] = "button"
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["link"] = watches.iloc[index]["Product URL"]
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["text"] = watches.iloc[index]["Product Name"]
            counter += 1
    elif category == "Drives/Storage":
        print("In top5")
        for index in top :
            response["fulfillmentMessages"][1]["payload"]["richContent"][0].append({"icon": {"color": "#878fac"}})
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["type"] = "button"
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["link"] = drives.iloc[index]["Product URL"]
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["text"] = drives.iloc[index]["Product Name"]
            counter += 1
    response["fulfillmentMessages"].append({"text":{"text" : ["Did the above links help you?"]}})
    response["fulfillmentMessages"].append({"payload":json.loads(bestsellers_display)})
    return response
        
def get_top5(category) :
    global top
    global potential
    if category == "Mobiles" :
        for index in range(len(mobiles)) :
            if curr_brand.lower() in mobiles.iloc[index]["Brand"].lower() :
                top.append(index)
            if len(top) == 5 :
                break
    elif category == "Tablets" :
        for index in range(len(tablets)) :
            if curr_brand.lower() in tablets.iloc[index]["Brand"].lower() :
                top.append(index)
            if len(top) == 5 :
                break
    elif category == "Powerbanks" :
        for index in range(len(powerbanks)) :
            if curr_brand.lower() in powerbanks.iloc[index]["Brand"].lower() :
                top.append(index)
            if len(top) == 5 :
                break
    elif category == "Desktops" :
        for index in range(len(desktops)) :
            if curr_brand.lower() in desktops.iloc[index]["Brand"].lower() :
                top.append(index)
            if len(top) == 5 :
                break
    elif category == "Laptops" :
        for index in range(len(laptops)) :
            if curr_brand.lower() in laptops.iloc[index]["Brand"].lower() :
                top.append(index)
            if len(top) == 5 :
                break
    elif category == "Smart Watches" :
        for index in range(len(watches)) :
            if curr_brand.lower() in watches.iloc[index]["Brand"].lower() :
                top.append(index)
            if len(top) == 5 :
                break
    elif category == "Drives/Storage" :
        for index in range(len(drives)) :
            if curr_brand.lower() in drives.iloc[index]["Brand"].lower() :
                top.append(index)
            if len(top) == 5 :
                break
    print("Top",top)

def get_potential_mobile(color, brand, mem) :
    global potential
    for index in range(len(mobiles)) :
        if brand in mobiles.iloc[index]["Brand"].lower() and color in mobiles.iloc[index]["Color"].lower() and mem in mobiles.iloc[index]["Memory Storage Capacity"]:
             potential.append(index)
    print(potential)
    if not potential :
        get_top5("Mobiles")
        potential = top
    print(potential)
def get_potential_tablet(color, brand, mem) :
    global potential
    for index in range(len(tablets)) :
        if brand in tablets.iloc[index]["Brand"].lower() and color in tablets.iloc[index]["Product Name"].lower() and mem in tablets.iloc[index]["Memory Storage Capacity"]:
             potential.append(index)
    print(potential)
    if not potential :
        get_top5("Tablets")
        potential = top
    print(potential)
def get_potential_powerbank(brand) :
    global potential
    for index in range(len(powerbanks)) :
        if brand in powerbanks.iloc[index]["Brand"].lower():
             potential.append(index)
    print(potential)
    if not potential :
        get_top5("Powerbanks")
        potential = top
    print(potential)
def get_potential_desktop(brand, processor, os) :
    global potential
    for index in range(len(desktops)) :
        if brand in desktops.iloc[index]["Brand"].lower() and processor in desktops.iloc[index]["Processor"].lower() and os in desktops.iloc[index]["Product Name"].lower():
             potential.append(index)
    print(potential)
    if not potential :
        get_top5("Desktops")
        potential = top
    print(potential)
def get_potential_laptop(brand, os, mem) :
    global potential
    for index in range(len(laptops)) :
        if brand in laptops.iloc[index]["Brand"].lower() and os.lower() in laptops.iloc[index]["Operating System"].lower() and mem in laptops.iloc[index]["Memory"]:
             potential.append(index)
    print(potential)
    if not potential :
        get_top5("Laptops")
        potential = top
    print(potential)
def get_potential_watch(brand, color, apps) :
    global potential
    potential1 = []
    for index in range(len(watches)) :
        if brand in watches.iloc[index]["Brand"].lower() and color.lower() in watches.iloc[index]["Color"].lower() :
             potential1.append(index)
    #print(potential1)
    apps = set(apps)
    #print(apps)
    for index in potential1 :
        if type(watches["Supported Application"][index]) == str :
            apps_present = set(watches["Supported Application"][index].split(','))
            #print(apps.intersection(apps_present))
            if len(apps.intersection(apps_present)) > 0 :
                potential.append(index)
        else :
            if len(potential) < 3 :
                terms = set(watches["Product Name"][index].lower().split())
                apps_present = []
                for term in apps :
                    apps_present.extend(term.lower().split())
                apps_present = set(apps_present)
                #print(apps_present)
                if len(apps.intersection(terms)) > 1 :
                    potential.append(index)
            else :
                continue
    print(potential)
    if not potential :
        get_top5("Smart Watches")
        potential = top
    print(potential)
def get_potential_drive(brand, conn, mem) :
    global potential
    for index in range(len(drives)) :
        if brand in drives.iloc[index]["Brand"].lower() and conn.lower() in drives.iloc[index]["Hardware Interface"].lower() and mem in drives.iloc[index]["Memory"]:
             potential.append(index)
    print(potential)
    if not potential :
        get_top5("Drives/Storage")
        potential = top
    print(potential)
def recommend_mobile(low, high) :
    global potential
    print(low, high)
    response = {"fulfillmentMessages":[{"text":{"text" : ["Here are some products we found according to your need."]}}]}
    response = json.dumps(response)
    response = json.loads(response)
    payload = {"payload":{"richContent":[[]]}}
    response["fulfillmentMessages"].append(payload)
    counter = 0
    for index in potential :
        price = float(mobiles.iloc[index]["Product Price"])
        if price >= low and price < high :
            response["fulfillmentMessages"][1]["payload"]["richContent"][0].append({"icon": {"color": "#878fac"}})
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["type"] = "button"
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["link"] = mobiles.iloc[index]["Product URL"]
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["text"] = mobiles.iloc[index]["Product Name"]
            counter += 1
    if counter==0 :
        response["fulfillmentMessages"][0] = {"text":{"text" : ["We didn't find products in your specified price range."]}}
        response["fulfillmentMessages"].append({"text":{"text" : ["Do you want to go to the main menu?"]}})
        response["fulfillmentMessages"].append({"payload":json.loads(satisfied_mobile)})
    else :
        response["fulfillmentMessages"].append({"text":{"text" : ["Did you find the product you were looking for?"]}})
        response["fulfillmentMessages"].append({"payload":json.loads(satisfied_mobile)})
    potential = []
    return response
def recommend_tablet(low, high) :
    global potential
    print(low, high)
    response = {"fulfillmentMessages":[{"text":{"text" : ["Here are some products we found according to your need."]}}]}
    response = json.dumps(response)
    response = json.loads(response)
    payload = {"payload":{"richContent":[[]]}}
    response["fulfillmentMessages"].append(payload)
    counter = 0
    for index in potential :
        price = float(tablets.iloc[index]["Product Price"])
        if price >= low and price < high :
            response["fulfillmentMessages"][1]["payload"]["richContent"][0].append({"icon": {"color": "#878fac"}})
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["type"] = "button"
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["link"] = tablets.iloc[index]["Product URL"]
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["text"] = tablets.iloc[index]["Product Name"]
            counter += 1
    if counter==0 :
        response["fulfillmentMessages"][0] = {"text":{"text" : ["We didn't find products in your specified price range."]}}
        response["fulfillmentMessages"].append({"text":{"text" : ["Do you want to go to the main menu?"]}})
        response["fulfillmentMessages"].append({"payload":json.loads(satisfied_tablet)})
    else :
        response["fulfillmentMessages"].append({"text":{"text" : ["Did you find the product you were looking for?"]}})
        response["fulfillmentMessages"].append({"payload":json.loads(satisfied_tablet)})
    potential = []
    return response
def recommend_powerbank(low, high) :
    global potential
    print(low, high)
    response = {"fulfillmentMessages":[{"text":{"text" : ["Here are some products we found according to your need."]}}]}
    response = json.dumps(response)
    response = json.loads(response)
    payload = {"payload":{"richContent":[[]]}}
    response["fulfillmentMessages"].append(payload)
    counter = 0
    for index in potential :
        price = float(powerbanks.iloc[index]["Product Price"])
        if price >= low and price < high :
            response["fulfillmentMessages"][1]["payload"]["richContent"][0].append({"icon": {"color": "#878fac"}})
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["type"] = "button"
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["link"] = powerbanks.iloc[index]["Product URL"]
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["text"] = powerbanks.iloc[index]["Product Name"]
            counter += 1
    if counter==0 :
        response["fulfillmentMessages"][0] = {"text":{"text" : ["We didn't find products in your specified price range."]}}
        response["fulfillmentMessages"].append({"text":{"text" : ["Do you want to go to the main menu?"]}})
        response["fulfillmentMessages"].append({"payload":json.loads(satisfied_powerbank)})
    else :
        response["fulfillmentMessages"].append({"text":{"text" : ["Did you find the product you were looking for?"]}})
        response["fulfillmentMessages"].append({"payload":json.loads(satisfied_powerbank)})
    potential = []
    return response 
def recommend_desktop(low, high) :
    global potential
    print(low, high)
    response = {"fulfillmentMessages":[{"text":{"text" : ["Here are some products we found according to your need."]}}]}
    response = json.dumps(response)
    response = json.loads(response)
    payload = {"payload":{"richContent":[[]]}}
    response["fulfillmentMessages"].append(payload)
    counter = 0
    for index in potential :
        price = float(desktops.iloc[index]["Product Price"])
        if price >= low and price < high :
            response["fulfillmentMessages"][1]["payload"]["richContent"][0].append({"icon": {"color": "#878fac"}})
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["type"] = "button"
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["link"] = desktops.iloc[index]["Product URL"]
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["text"] = desktops.iloc[index]["Product Name"]
            counter += 1
    if counter==0 :
        response["fulfillmentMessages"][0] = {"text":{"text" : ["We didn't find products in your specified price range."]}}
        response["fulfillmentMessages"].append({"text":{"text" : ["Do you want to go to the main menu?"]}})
        response["fulfillmentMessages"].append({"payload":json.loads(satisfied_desktop)})
    else :
        response["fulfillmentMessages"].append({"text":{"text" : ["Did you find the product you were looking for?"]}})
        response["fulfillmentMessages"].append({"payload":json.loads(satisfied_desktop)})
    potential = []
    return response
def recommend_laptop(low, high) :
    global potential
    print(low, high)
    response = {"fulfillmentMessages":[{"text":{"text" : ["Here are some products we found according to your need."]}}]}
    response = json.dumps(response)
    response = json.loads(response)
    payload = {"payload":{"richContent":[[]]}}
    response["fulfillmentMessages"].append(payload)
    counter = 0
    for index in potential :
        price = float(laptops.iloc[index]["Product Price"])
        if price >= low and price < high :
            response["fulfillmentMessages"][1]["payload"]["richContent"][0].append({"icon": {"color": "#878fac"}})
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["type"] = "button"
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["link"] = laptops.iloc[index]["Product URL"]
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["text"] = laptops.iloc[index]["Product Name"]
            counter += 1
    if counter==0 :
        response["fulfillmentMessages"][0] = {"text":{"text" : ["We didn't find products in your specified price range."]}}
        response["fulfillmentMessages"].append({"text":{"text" : ["Do you want to go to the main menu?"]}})
        response["fulfillmentMessages"].append({"payload":json.loads(satisfied_laptop)})
    else :
        response["fulfillmentMessages"].append({"text":{"text" : ["Did you find the product you were looking for?"]}})
        response["fulfillmentMessages"].append({"payload":json.loads(satisfied_laptop)})
    potential = []
    return response 
def recommend_watch(low, high) :
    global potential
    print(low, high)
    response = {"fulfillmentMessages":[{"text":{"text" : ["Here are some products we found according to your need."]}}]}
    response = json.dumps(response)
    response = json.loads(response)
    payload = {"payload":{"richContent":[[]]}}
    response["fulfillmentMessages"].append(payload)
    counter = 0
    for index in potential :
        price = float(watches.iloc[index]["Product Price"])
        if price >= low and price < high :
            print(price)
            response["fulfillmentMessages"][1]["payload"]["richContent"][0].append({"icon": {"color": "#878fac"}})
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["type"] = "button"
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["link"] = watches.iloc[index]["Product URL"]
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["text"] = watches.iloc[index]["Product Name"]
            counter += 1
    if counter==0 :
        response["fulfillmentMessages"][0] = {"text":{"text" : ["We didn't find products in your specified price range."]}}
        response["fulfillmentMessages"].append({"text":{"text" : ["Do you want to go to the main menu?"]}})
        response["fulfillmentMessages"].append({"payload":json.loads(satisfied_watch)})
    else :
        response["fulfillmentMessages"].append({"text":{"text" : ["Did you find the product you were looking for?"]}})
        response["fulfillmentMessages"].append({"payload":json.loads(satisfied_watch)})
    potential = []
    return response 
def recommend_drive(low, high) :
    global potential
    print(low, high)
    response = {"fulfillmentMessages":[{"text":{"text" : ["Here are some products we found according to your need."]}}]}
    response = json.dumps(response)
    response = json.loads(response)
    payload = {"payload":{"richContent":[[]]}}
    response["fulfillmentMessages"].append(payload)
    counter = 0
    for index in potential :
        price = float(drives.iloc[index]["Product Price"])
        print(price)
        if price >= low and price < high :
            response["fulfillmentMessages"][1]["payload"]["richContent"][0].append({"icon": {"color": "#878fac"}})
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["type"] = "button"
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["link"] = drives.iloc[index]["Product URL"]
            response["fulfillmentMessages"][1]["payload"]["richContent"][0][counter]["text"] = drives.iloc[index]["Product Name"]
            counter += 1
    if counter==0 :
        response["fulfillmentMessages"][0] = {"text":{"text" : ["We didn't find products in your specified price range."]}}
        response["fulfillmentMessages"].append({"text":{"text" : ["Do you want to go to the main menu?"]}})
        response["fulfillmentMessages"].append({"payload":json.loads(satisfied_drive)})
    else :
        response["fulfillmentMessages"].append({"text":{"text" : ["Did you find the product you were looking for?"]}})
        response["fulfillmentMessages"].append({"payload":json.loads(satisfied_drive)})
    potential = []
    return response      
     
@app.route('/')
def index():
    return render_template('index.html')

 
@app.route('/webhook', methods=['POST'])
def webhook():
    global curr_brand, potential, top, acc_score, usab_score, prev, total
    req = request.get_json(silent=True)
    try:
        action = req.get('queryResult').get('action')
        if action == 'welcome' :
            acc_score = 0
            usab_score = 0
            total = 0
            print("Session started")
            return make_response(jsonify(main))
        elif action == 'feedback.feedback-custom' :
            if prev == 'price' : 
                acc_score += 2
                total += 1
            text = req.get('queryResult').get('queryText')
            if text == 'It was nice' :
                usab_score += 3
            elif text == 'It was great' :
                usab_score += 5
            elif text == 'It was not good' :
                usab_score = 0
            print("Session ended with Usability score:",usab_score, "and Accuracy score:",acc_score/total)
            acc_score = 0
            usab_score = 0
            prev = ""
            return make_response(jsonify(main_redirect))
        elif(action == 'A1mobile.A1mobile-custom') :
            if prev == "features" :
                acc_score -= 1
                print(acc_score)
                total += 1
            prev = "features"
            potential = []
            curr_brand = ""
            parameters = req.get('queryResult').get('parameters')
            color = parameters.get('color')
            curr_brand = parameters.get('Model')
            mem = parameters.get('Memory')
            res = "Order till now: "+curr_brand+" "+color+" "+mem+" Mobile. Do you want to continue with these features?"
            print(color.lower(), curr_brand.lower(), mem)
            get_potential_mobile(color.lower(), curr_brand.lower(), mem)
            response = {"fulfillmentMessages":[{"text":{"text" : res}}, {"payload":json.loads(mobile_features_continue)}]}
            return make_response(jsonify(response))
        elif(action == 'A1mobile.A1mobile-custom.mobile-features-yes.mobile-features-yes-yes') :
            acc_score += 2
            total += 1
            prev = "price"
            print(acc_score)
            parameters = req.get('queryResult').get('parameters')
            low, high = parameters.get('category').split(',')
            print(low, high)
            return(make_response(jsonify(recommend_mobile(float(low), float(high)))))
        
        elif(action == 'A2tablet.A2tablet-custom') :
            if prev == "features" :
                acc_score -= 1
                total += 1
            prev = "features"
            potential = []
            curr_brand = ""
            parameters = req.get('queryResult').get('parameters')
            color = parameters.get('color')
            curr_brand = parameters.get('model1')
            mem = parameters.get('Memory')
            res = "Order till now: "+curr_brand+" "+color+" "+mem+" Tablet. Do you want to continue with these features?"
            print(color.lower(), curr_brand.lower(), mem)
            get_potential_tablet(color.lower(), curr_brand.lower(), mem)
            response = {"fulfillmentMessages":[{"text":{"text" : res}}, {"payload":json.loads(tablet_features_continue)}]}
            return make_response(jsonify(response))
        elif(action == 'A2tablet.A2tablet-custom.tablet-features-yes.tablet-features-yes-custom') :
            acc_score += 2
            total += 1
            prev = "price"
            parameters = req.get('queryResult').get('parameters')
            low, high = parameters.get('category').split(',')
            print(low, high)
            return(make_response(jsonify(recommend_tablet(float(low), float(high)))))
            
        elif(action == 'A3power.A3power-custom') :
            if prev == "features" :
                acc_score -= 1
                total += 1
            prev = "features"
            potential = []
            curr_brand = ""
            parameters = req.get('queryResult').get('parameters')
            curr_brand = parameters.get('brand')
            res = "Order till now: "+curr_brand+" Tablet. Do you want to continue with these features?"
            print(curr_brand.lower())
            get_potential_powerbank(curr_brand.lower())
            response = {"fulfillmentMessages":[{"text":{"text" : res}}, {"payload":json.loads(powerbank_features_continue)}]}
            return make_response(jsonify(response))
        elif(action == 'A3power.A3power-custom.power-features-yes.power-features-yes-custom') :
            acc_score += 2
            total += 1
            prev = "price"
            parameters = req.get('queryResult').get('parameters')
            low, high = parameters.get('category').split(',')
            print(low, high)
            return(make_response(jsonify(recommend_powerbank(float(low), float(high)))))
            
        elif(action == 'A4wear.A4wear-custom') :
            if prev == "features" :
                acc_score -= 1
                total += 1
            prev = "features"
            potential = []
            curr_brand = ""
            parameters = req.get('queryResult').get('parameters')
            curr_brand = parameters.get('Model')
            color = parameters.get('color')
            apps = parameters.get('Fitness_feature')
            res = "Order till now: "+curr_brand+" "+color+" Smart Watch. Do you want to continue with these features?"
            print(curr_brand.lower(), color.lower(), apps)
            get_potential_watch(curr_brand.lower(), color.lower(), apps)
            response = {"fulfillmentMessages":[{"text":{"text" : res}}, {"payload":json.loads(watch_features_continue)}]}
            return make_response(jsonify(response))
        elif(action == 'A4wear.A4wear-custom.wear-features-yes.wear-features-yes-custom') :
            acc_score += 2
            total += 1
            prev = "price"
            parameters = req.get('queryResult').get('parameters')
            low, high = parameters.get('category').split(',')
            print(low, high)
            return(make_response(jsonify(recommend_watch(float(low), float(high)))))
            
        elif(action == 'B2desktop.B2desktop-custom') :
            if prev == "features" :
                acc_score -= 1
                total += 1
            prev = "features"
            potential = []
            curr_brand = ""
            parameters = req.get('queryResult').get('parameters')
            curr_brand = parameters.get('Laptop_Brand')
            processor = parameters.get('Laptop_Processor')
            os = parameters.get('Laptop_OS')
            res = "Order till now: "+curr_brand+" "+processor+" "+os+" Desktop. Do you want to continue with these features?"
            print(curr_brand.lower(), processor.lower(), os.lower())
            get_potential_desktop(curr_brand.lower(), processor.lower(), os.lower())
            response = {"fulfillmentMessages":[{"text":{"text" : res}}, {"payload":json.loads(desktop_features_continue)}]}
            return make_response(jsonify(response))
        elif(action == 'B2desktop.B2desktop-custom.B2desktop-features-yes.B2desktop-features-yes-yes') :
            acc_score += 2
            total += 1
            prev = "price"
            parameters = req.get('queryResult').get('parameters')
            low, high = parameters.get('category').split(',')
            print(low, high)
            return(make_response(jsonify(recommend_desktop(float(low), float(high)))))
            
        elif(action == 'B1laptop.B1laptop-custom') :
            if prev == "features" :
                acc_score -= 1
                total += 1
            prev = "features"
            potential = []
            curr_brand = ""
            parameters = req.get('queryResult').get('parameters')
            curr_brand = parameters.get('laptop_brand')
            mem = parameters.get('Memory')
            os = parameters.get('laptop_os')
            res = "Order till now: "+curr_brand+" "+mem+" "+os+" Desktop. Do you want to continue with these features?"
            print(curr_brand.lower(), mem, os.lower())
            get_potential_laptop(curr_brand.lower(), os.lower(), mem)
            response = {"fulfillmentMessages":[{"text":{"text" : res}}, {"payload":json.loads(laptop_features_continue)}]}
            return make_response(jsonify(response))
        elif(action == 'B1laptop.B1laptop-custom.B1laptop-features-yes.B1laptop-features-yes-yes') :
            acc_score += 2
            total += 1
            prev = "price"
            parameters = req.get('queryResult').get('parameters')
            low, high = parameters.get('category').split(',')
            print(low, high)
            return(make_response(jsonify(recommend_laptop(float(low), float(high)))))
            
        elif(action == 'B4drive.B4drive-custom') :
            if prev == "features" :
                acc_score -= 1
                total += 1
            prev = "features"
            potential = []
            curr_brand = ""
            parameters = req.get('queryResult').get('parameters')
            curr_brand = parameters.get('drive_brand')
            mem = parameters.get('Drive_Size')
            conn = parameters.get('drive_connection_type')
            res = "Order till now: "+curr_brand+" "+mem+" "+conn+" Drive. Do you want to continue with these features?"
            print(curr_brand.lower(), conn.lower(), mem)
            get_potential_drive(curr_brand.lower(), conn.lower(), mem)
            response = {"fulfillmentMessages":[{"text":{"text" : res}}, {"payload":json.loads(drive_features_continue)}]}
            return make_response(jsonify(response))
        elif(action == 'B4drive.B4drive-custom.B4drive-features-yes.B4drive-features-yes-custom') :
            acc_score += 2
            total += 1
            prev = "price"
            parameters = req.get('queryResult').get('parameters')
            low, high = parameters.get('category').split(',')
            print(low, high)
            return(make_response(jsonify(recommend_drive(float(low), float(high)))))
        
        elif(action == 'get_top5') :
            acc_score -= 1
            total += 1
            print(acc_score)
            prev = "bestsellers"
            top = []
            parameters = req.get('queryResult').get('parameters')
            category = parameters.get('category')
            get_top5(category)
            res = "Do you want the links of BestSellers for "+curr_brand+" in "+category+" Category?"
            response = {"fulfillmentMessages":[{"text":{"text" : res}}, {"payload":json.loads(bestsellers_display)}]}
            return (make_response(jsonify(response)))
        elif(action == 'Recommend_top_5.Recommend_top_5-custom') :
            parameters = req.get('queryResult').get('parameters')
            category = parameters.get('category')
            return make_response(jsonify(bestsellers(category)))
            
        
    except AttributeError:
        return 'json error'


# run Flask app
if __name__ == "__main__":
    app.run()


