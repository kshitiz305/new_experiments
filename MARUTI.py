import requests

cookies = {
    'marutisuzuki#lang': 'en',
    'ASP.NET_SessionId': '3a4qnx404dcuqju3lrv3oqqc',
    '__RequestVerificationToken': 'VljnhOpugpu-ku8a99P1p-R62kPEAvtMccG_BWAHqkQlLVgPubkL5T5FgzG1dgKnqV5JcIBFX_cSK0abiRegyUidfnXbpODgFwqPjSeQPJ81',
    'ARRAffinity': 'a75f436fe1433e0a6050400ba97bd8e396794446f858ac4ca1d1981bfcf7c0d8',
    'ARRAffinitySameSite': 'a75f436fe1433e0a6050400ba97bd8e396794446f858ac4ca1d1981bfcf7c0d8',
    'SC_ANALYTICS_GLOBAL_COOKIE': 'e3bd8dbb37a44140bfa3f67808b00db2|True',
    'total_point': '0',
    '_gcl_au': '1.1.1709309226.1678662680',
    '_gid': 'GA1.2.2032298378.1678662686',
    '_fbp': 'fb.1.1678662687162.241960567',
    'AMP_TOKEN': '%24NOT_FOUND',
    'ADRUM': 's=1678662692554&r=https%3A%2F%2Fwww.marutisuzuki.com%2Fcorporate%2Fmedia%2Fpress-releases%2F2021%2Fseptember%2Fmaruti-suzuki-to-proactively-recall-181754-units-of-some-petrol-variants',
    '_ga_RM5D6V43B5': 'GS1.1.1678662684.1.1.1678662720.24.0.0',
    '_td': '66865d2c-0c95-46ca-bec1-154e384e0581',
    '_ga': 'GA1.2.1905266598.1678662684',
    '_gat_UA-4030537-51': '1',
    '_ga_B6Q4G64V89': 'GS1.1.1678662684.1.1.1678662977.56.0.0',
}

headers = {
    'authority': 'www.marutisuzuki.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'adrum': 'isAjax:true',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'marutisuzuki#lang=en; ASP.NET_SessionId=3a4qnx404dcuqju3lrv3oqqc; __RequestVerificationToken=VljnhOpugpu-ku8a99P1p-R62kPEAvtMccG_BWAHqkQlLVgPubkL5T5FgzG1dgKnqV5JcIBFX_cSK0abiRegyUidfnXbpODgFwqPjSeQPJ81; ARRAffinity=a75f436fe1433e0a6050400ba97bd8e396794446f858ac4ca1d1981bfcf7c0d8; ARRAffinitySameSite=a75f436fe1433e0a6050400ba97bd8e396794446f858ac4ca1d1981bfcf7c0d8; SC_ANALYTICS_GLOBAL_COOKIE=e3bd8dbb37a44140bfa3f67808b00db2|True; total_point=0; _gcl_au=1.1.1709309226.1678662680; _gid=GA1.2.2032298378.1678662686; _fbp=fb.1.1678662687162.241960567; AMP_TOKEN=%24NOT_FOUND; ADRUM=s=1678662692554&r=https%3A%2F%2Fwww.marutisuzuki.com%2Fcorporate%2Fmedia%2Fpress-releases%2F2021%2Fseptember%2Fmaruti-suzuki-to-proactively-recall-181754-units-of-some-petrol-variants; _ga_RM5D6V43B5=GS1.1.1678662684.1.1.1678662720.24.0.0; _td=66865d2c-0c95-46ca-bec1-154e384e0581; _ga=GA1.2.1905266598.1678662684; _gat_UA-4030537-51=1; _ga_B6Q4G64V89=GS1.1.1678662684.1.1.1678662977.56.0.0',
    'origin': 'https://www.marutisuzuki.com',
    'referer': 'https://www.marutisuzuki.com/important-information-for-customers',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'vechno': 'MBJTYKL1SPA116379',
    'model': '',
    'recallText': 'Maruti Suzuki to recall 17362 vehicles',
}

response = requests.post('https://www.marutisuzuki.com/api/sitecore/ImportantInfoCustomer/checkVehicleData', cookies=cookies, headers=headers, data=data)
