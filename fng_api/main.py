import requests
from bs4 import BeautifulSoup

def getIdentity(nameset=["us"], state=["tx"], gender="50", minage="19", maxage="85"):
    
    # State abbreviation and full name mapping
    state_mapping = {
        "Alabama": "al", "Alaska": "ak", "Arizona": "az", "Arkansas": "ar", "California": "ca",
        "Colorado": "co", "Connecticut": "ct", "Delaware": "de", "District Of Columbia": "dc",
        "Florida": "fl", "Georgia": "ga", "Hawaii": "hi", "Idaho": "id", "Illinois": "il",
        "Indiana": "in", "Iowa": "ia", "Kansas": "ks", "Kentucky": "ky", "Louisiana": "la",
        "Maine": "me", "Maryland": "md", "Massachusetts": "ma", "Michigan": "mi", "Minnesota": "mn",
        "Mississippi": "ms", "Missouri": "mo", "Montana": "mt", "Nebraska": "ne", "Nevada": "nv",
        "New Hampshire": "nh", "New Jersey": "nj", "New Mexico": "nm", "New York": "ny",
        "North Carolina": "nc", "North Dakota": "nd", "Ohio": "oh", "Oklahoma": "ok", "Oregon": "or",
        "Pennsylvania": "pa", "Puerto Rico": "pr", "Rhode Island": "ri", "South Carolina": "sc",
        "South Dakota": "sd", "Tennessee": "tn", "Texas": "tx", "Utah": "ut", "US Virgin Islands": "usvi",
        "Vermont": "vt", "Virginia": "va", "Washington": "wa", "West Virginia": "wv", "Wisconsin": "wi",
        "Wyoming": "wy"
    }

    # Reverse mapping from abbreviations to full names
    reverse_state_mapping = {v: k for k, v in state_mapping.items()}

    # Check if args are valid
    if not isinstance(nameset, list):
        raise TypeError("Argument nameset must be list")
    if not isinstance(state, list):
        raise TypeError("Argument state must be list")
    if not isinstance(gender, str):
        raise TypeError("Argument gender must be str")
    if int(gender) > 100:
        raise ValueError("Gender must be less than or equal to 100")
    if int(gender) < 0:
        raise ValueError("Gender must be greater than or equal to 0")
    if not isinstance(minage, str):
        raise TypeError("Argument minage must be str")
    if int(minage) < 0:
        raise ValueError("minage must be greater than or equal to 0")
    if not isinstance(maxage, str):
        raise TypeError("Argument maxage must be str")
    if int(maxage) > 100:
        raise ValueError("maxage must be less than or equal to 100")
    if int(minage) > int(maxage):
        raise ValueError("minage must be less than maxage")
    
    for i in range(len(nameset)):
        if not isinstance(nameset[i], str):
            raise TypeError("nameset values must be a str")
    for i in range(len(state)):
        if not isinstance(state[i], str):
            raise TypeError("state values must be a str")
        # Normalize state input
        normalized_state = state[i].strip().title()
        if normalized_state in state_mapping:
            state[i] = state_mapping[normalized_state]
        elif normalized_state.lower() in reverse_state_mapping:
            state[i] = normalized_state.lower()
        else:
            raise ValueError("state \'" + state[i] + "\' not supported")
    
    # Construct URL
    url = "https://www.fakenamegenerator.com/advanced.php?t=region"
    for i in range(len(nameset)):
        url = url + "&n%5B%5D=" + nameset[i]
    for i in range(len(state)):
        url = url + "&c%5B%5D=us-" + state[i]
    url = url + "&gen=" + gender
    url = url + "&age-min=" + minage
    url = url + "&age-max=" + maxage
    
    # Get data
    soup = BeautifulSoup(requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text, "html.parser")

    name = soup.find("h3").text
    fullAddress = soup.find("div", class_="adr").contents
    address = (fullAddress[0] + ", " + fullAddress[2]).strip()
    street = fullAddress[0].strip()
    city = fullAddress[2].split(", ")[0]
    
    # Extract state and convert abbreviation to full name if necessary
    state_abbr = fullAddress[2].strip().split(" ")[-2]
    state = reverse_state_mapping.get(state_abbr.lower(), state_abbr.capitalize())
    
    zip = fullAddress[2].split(" ")[2]
    motherMaidenName = soup.find("dd").text
    ssn = soup.find_all("dd")[1].text.split(" ")[0]
    coords = soup.find("a", id="geo").text
    phone = soup.find_all("dd")[3].text
    countryCode = soup.find_all("dd")[4].text
    birthday = soup.find_all("dd")[5].text
    birthdayYear = birthday.split(" ")[2]
    birthdayMonth = birthday.split(" ")[0]
    birthdayDay = birthday.split(" ")[1][:-1]
    age = soup.find_all("dd")[6].text.split(" ")[0]
    zodiac = soup.find_all("dd")[7].text
    email = soup.find_all("dd")[8].contents[0]
    username = soup.find_all("dd")[9].text
    password = soup.find_all("dd")[10].text
    website = soup.find_all("dd")[11].text
    useragent = soup.find_all("dd")[12].text
    card = soup.find_all("dd")[13].text
    expiration = soup.find_all("dd")[14].text
    cvv2 = soup.find_all("dd")[15].text
    company = soup.find_all("dd")[16].text
    occupation = soup.find_all("dd")[17].text
    height = soup.find_all("dd")[18].text.split(" ")[0] + soup.find_all("dd")[18].text.split(" ")[1]
    heightcm = soup.find_all("dd")[18].text.split("(")[1][:-1].split(" ")[0]
    weight = soup.find_all("dd")[19].text.split(" ")[0]
    weightkg = soup.find_all("dd")[19].text.split("(")[1].split(" ")[0]
    blood = soup.find_all("dd")[20].text
    ups = soup.find_all("dd")[21].text
    westernunion = soup.find_all("dd")[22].text
    moneygram = soup.find_all("dd")[23].text
    color = soup.find_all("dd")[24].text
    vehicle = soup.find_all("dd")[25].text
    guid = soup.find_all("dd")[26].text
    
    class identity:
        def __init__(self, name, address, street, city, state, zip, motherMaidenName, ssn, coords, phone, countryCode, birthday, birthdayMonth, birthdayDay, birthdayYear, age, zodiac, email, username, password, website, useragent, card, expiration, cvv2, company, occupation, height, heightcm, weight, weightkg, blood, ups, westernunion, moneygram, color, vehicle, guid):
            self.name = name
            self.address = address
            self.street = street
            self.city = city
            self.state = state
            self.zip = zip
            self.motherMaidenName = motherMaidenName
            self.ssn = ssn
            self.coords = coords
            self.phone = phone
            self.countryCode = countryCode
            self.birthday = birthday
            self.birthdayMonth = birthdayMonth
            self.birthdayYear = birthdayYear
            self.birthdayDay = birthdayDay
            self.age = age
            self.zodiac = zodiac
            self.email = email
            self.username = username
            self.password = password
            self.website = website
            self.useragent = useragent
            self.card = card
            self.expiration = expiration
            self.cvv2 = cvv2
            self.company = company
            self.occupation = occupation
            self.height = height
            self.heightcm = heightcm
            self.weight = weight
            self.weightkg = weightkg
            self.blood = blood
            self.ups = ups
            self.westernunion = westernunion
            self.moneygram = moneygram
            self.color = color
            self.vehicle = vehicle
            self.guid = guid
    
    return identity(name, address, street, city, state, zip, motherMaidenName, ssn, coords, phone, countryCode, birthday, birthdayMonth, birthdayDay, birthdayYear, age, zodiac, email, username, password, website, useragent, card, expiration, cvv2, company, occupation, height, heightcm, weight, weightkg, blood, ups, westernunion, moneygram, color, vehicle, guid)
