"""Builds tours.json from TripADeal data captured on 12 Sep 2026.

Two deals (5836, 6363) have exact day-by-day stops parsed from the deal page.
The rest use the headline cities from the homepage listing, ordered into a
sensible route by hand, and are flagged itinerary="headline" so the UI can say so.
Coordinates come from the gazetteer below; scrape_tripadeal.py uses the same one.
"""
import json, pathlib, sys
HERE=pathlib.Path(__file__).resolve().parent; sys.path.insert(0,str(HERE)); DATA=HERE.parent/"data"; DATA.mkdir(exist_ok=True)

G = {  # city -> (lng, lat)
 "Sydney":(151.21,-33.87),"Melbourne":(144.96,-37.81),"Brisbane":(153.03,-27.47),"Perth":(115.86,-31.95),
 "Tokyo":(139.69,35.69),"Mt Fuji":(138.73,35.36),"Nagano":(138.08,36.04),"Takayama":(137.25,36.14),"Kyoto":(135.77,35.01),
 "Okayama":(133.92,34.66),"Hiroshima":(132.46,34.39),"Osaka":(135.5,34.69),"Fukuoka":(130.4,33.59),"Kanazawa":(136.66,36.56),
 "Nagasaki":(129.87,32.75),"Kagoshima":(130.56,31.6),"Busan":(129.08,35.18),"Taipei":(121.56,25.03),"Hong Kong":(114.17,22.32),
 "Beijing":(116.4,39.9),"Xi'an":(108.94,34.34),"Luoyang":(112.45,34.62),"Zhengzhou":(113.63,34.75),"Wuxi":(120.31,31.49),
 "Suzhou":(120.59,31.3),"Hangzhou":(120.15,30.27),"Shanghai":(121.47,31.23),
 "Hanoi":(105.85,21.03),"Ha Long Bay":(107.08,20.91),"Pu Luong":(105.23,20.47),"Hue":(107.59,16.46),"Hoi An":(108.34,15.88),
 "Ho Chi Minh City":(106.63,10.82),"Phnom Penh":(104.92,11.56),"Siem Reap":(103.86,13.36),
 "Singapore":(103.82,1.35),"Penang":(100.33,5.41),"Phuket":(98.39,7.88),
 "Vancouver":(-123.12,49.28),"Kamloops":(-120.33,50.68),"Banff":(-115.57,51.18),"Lake Louise":(-116.18,51.42),"Whistler":(-122.96,50.12),
 "Ketchikan":(-131.65,55.34),"Juneau":(-134.42,58.3),"Skagway":(-135.31,59.46),"Seattle":(-122.33,47.61),"Calgary":(-114.07,51.05),"Canmore":(-115.36,51.09),"Glacier Bay":(-136.9,58.66),
 "Yellowstone":(-110.59,44.43),"Jackson Hole":(-110.76,43.48),"Salt Lake City":(-111.89,40.76),
 "Lima":(-77.03,-12.05),"Cusco":(-71.97,-13.53),"Machu Picchu":(-72.54,-13.16),"Puerto Maldonado":(-69.19,-12.59),
 "Buenos Aires":(-58.38,-34.6),"Iguazu Falls":(-54.44,-25.69),"Rio de Janeiro":(-43.17,-22.91),
 "Cairo":(31.24,30.04),"Giza":(31.13,29.98),"Luxor":(32.64,25.69),"Aswan":(32.9,24.09),"Hurghada":(33.81,27.26),
 "Casablanca":(-7.59,33.57),"Chefchaouen":(-5.26,35.17),"Fes":(-4.98,34.03),"Erg Chebbi":(-4.01,31.15),"Ouarzazate":(-6.91,30.92),"Marrakech":(-7.98,31.63),
 "Rome":(12.5,41.9),"Naples":(14.27,40.85),"Mykonos":(25.33,37.45),"Santorini":(25.43,36.39),"Kuşadası":(27.26,37.86),"Athens":(23.73,37.98),
 "Helsinki":(24.94,60.17),"Rovaniemi":(25.72,66.5),"Tromsø":(18.96,69.65),"Lofoten":(14.5,68.2),"Bergen":(5.32,60.39),"Flåm":(7.11,60.86),"Oslo":(10.75,59.91),
}

# Day-by-day detail: (day, title, city, one-line summary in our own words). Only for deals parsed in full.
DAYS = {
 # (day, title, city, one-line summary, fuller detail, meals, overnight, optional activities) — all written in our own words
 5836: [
  (1,"Australia – Tokyo","Tokyo","Fly to Tokyo, transfer to hotel.","Depart Australia on the overnight flight to Tokyo. On arrival you're met and transferred to the hotel; the rest of the day is free to settle in.","","Tokyo hotel",""),
  (2,"Tokyo sightseeing, free afternoon","Tokyo","Morning at Tsukiji Outer Market and Meiji Shrine; afternoon free.","A morning of the classic Tokyo pairing: the food stalls and knife shops of the Tsukiji Outer Market, then the forested calm of Meiji Shrine. The afternoon is yours.","Breakfast","Tokyo hotel","Tokyo Tower and city tour"),
  (3,"Tokyo free day","Tokyo","Free day, or an optional Hakone day trip.","A full free day. Good choices are Asakusa and Senso-ji, teamLab, or a Shinjuku evening.","Breakfast","Tokyo hotel","Hakone day trip: Lake Ashi cruise, Owakudani volcanic valley and the Open-Air Museum"),
  (4,"Tokyo – Mt Fuji – Nagano","Nagano","Drive to Mt Fuji's 5th Station and the Five Lakes, then on to the Nagano region.","Leave Tokyo for Mt Fuji, climbing by coach to the 5th Station at about 2,300 m (weather permitting) with views across the Fuji Five Lakes. Continue north to the Nagano region for the night.","Breakfast, dinner","Nagano region hotel",""),
  (5,"Nagano – Narai-juku – Takayama","Takayama","Wasabi farm, the Edo-era post town of Narai-juku, then Takayama's old town.","Start at a working wasabi farm, then walk the wooden main street of Narai-juku, one of the best-preserved post towns on the old Nakasendo trail. Arrive in Takayama with time to wander the merchant district of Sanmachi Suji.","Breakfast","Takayama hotel",""),
  (6,"Takayama – Kyoto","Kyoto","Drive to Kyoto for Fushimi Inari and the Golden Pavilion.","Head south-west to Kyoto. Walk part of the vermilion tunnel of torii at Fushimi Inari, then visit the Golden Pavilion (Kinkaku-ji) before checking in.","Breakfast","Kyoto hotel","Evening Maiko dinner show"),
  (7,"Kyoto free day","Kyoto","Free day, or an optional trip to the Kyoto coast.","A free day in Kyoto. Arashiyama's bamboo grove, Nijo Castle, Gion at dusk or a Nara day trip are all easy on your own.","Breakfast","Kyoto hotel","'Kyoto by the Sea': Amanohashidate sandbar and the boathouses of Ine"),
  (8,"Kyoto – Okayama – Hiroshima","Hiroshima","Kurashiki's canal quarter and Korakuen garden en route to Hiroshima.","Travel west via Okayama. Stroll Kurashiki's willow-lined canal and white-walled storehouses, then Korakuen, one of Japan's three great landscape gardens, before continuing to Hiroshima.","Breakfast","Hiroshima hotel",""),
  (9,"Hiroshima & Miyajima","Hiroshima","Boat to Miyajima's floating torii, then the Peace Memorial Park.","Ferry to Miyajima to see Itsukushima Shrine and its torii standing in the water (tide permitting). Back in the city, visit the Peace Memorial Park and Museum and the A-Bomb Dome.","Breakfast","Hiroshima hotel",""),
  (10,"Hiroshima – Osaka by bullet train","Osaka","Shinkansen from Himeji to Shin-Kobe, then on to Osaka.","Coach to Himeji station, then board the Shinkansen for a short bullet-train ride to Shin-Kobe before continuing to Osaka.","Breakfast","Osaka hotel",""),
  (11,"Osaka free day","Osaka","Free day in Osaka.","Free day. Dotonbori's neon and street food, Osaka Castle, or a day trip to Nara are the usual picks.","Breakfast","Osaka hotel",""),
  (12,"Depart Osaka","Osaka","Transfer to the airport for the flight home.","Transfer to Kansai Airport for the flight back to Australia.","Breakfast","",""),
  (13,"Arrive Australia",None,"","Arrive home.","","","")],
 6363: [
  (1,"Australia – Beijing","Beijing","Fly to Beijing and transfer to the hotel.","Depart Australia for Beijing. Meet your guide on arrival and transfer to the hotel.","","Beijing hotel",""),
  (2,"Tiananmen Square & Forbidden City","Beijing","Tiananmen Square and the Forbidden City (or Temple of Heaven).","Walk Tiananmen Square and into the Forbidden City's succession of courtyards and halls (the Temple of Heaven substitutes on days the palace is closed).","Breakfast, lunch","Beijing hotel","Summer Palace and a panda visit"),
  (3,"Great Wall of China","Beijing","Great Wall at Juyong Pass.","Visit a jade museum, have a picnic lunch, then climb a section of the Great Wall at Juyong Pass, one of the wall's great fortified gateways.","Breakfast, lunch","Beijing hotel","Hutong pedicab tour with a local family visit"),
  (4,"Beijing – Xi'an","Xi'an","High-speed train or flight to Xi'an.","A morning visit to a traditional Chinese medicine centre, then travel to Xi'an by high-speed rail (about four and a half hours) or flight depending on departure.","Breakfast, lunch","Xi'an hotel",""),
  (5,"Terracotta Warriors","Xi'an","The Terracotta Warriors and Horses Museum.","The day belongs to the Terracotta Army: the three excavation pits and the bronze chariots, with time in the museum halls.","Breakfast, lunch","Xi'an hotel","Tang Dynasty music and dance show with dumpling dinner"),
  (6,"Xi'an – Luoyang","Luoyang","Small Wild Goose Pagoda, then train to Luoyang.","See the Small Wild Goose Pagoda before boarding the high-speed train to Luoyang, the ancient capital on the Luo River. Group dinner tonight.","Breakfast, lunch, dinner","Luoyang hotel",""),
  (7,"Longmen Grottoes – Zhengzhou","Zhengzhou","Longmen Grottoes, then on to Zhengzhou.","Spend the morning at the Longmen Grottoes, where some 100,000 Buddhist figures are carved into the limestone cliffs above the river. Continue to Zhengzhou.","Breakfast, lunch","Zhengzhou hotel",""),
  (8,"Zhengzhou at leisure","Zhengzhou","Free day, or the Shaolin Temple.","A day to rest, or take the optional trip to the Shaolin Temple, birthplace of kung fu, with a martial-arts performance.","Breakfast","Zhengzhou hotel","Shaolin Temple and kung fu show"),
  (9,"Zhengzhou – Wuxi","Wuxi","Zhengzhou Museum, then high-speed train to Wuxi.","Visit the Zhengzhou Museum in the morning, then a long high-speed rail leg south-east to Wuxi on the shores of Lake Tai.","Breakfast, lunch","Wuxi hotel",""),
  (10,"Wuxi – Suzhou","Suzhou","Lihu Park and a pearl factory, then Suzhou.","Walk Lihu Park on the lakeside and visit a freshwater pearl workshop, then a short drive to Suzhou.","Breakfast, lunch","Suzhou hotel",""),
  (11,"Suzhou – Hangzhou","Hangzhou","Lingering Garden and a silk factory; Tangxi Ancient Town.","Suzhou's Lingering Garden and a silk factory in the morning, then Tangxi Ancient Town's canals on the way to Hangzhou.","Breakfast, lunch","Hangzhou hotel",""),
  (12,"Hangzhou – Shanghai","Shanghai","Tea village, West Lake boat ride, then Shanghai's Bund.","Visit Meijiawu tea village in the Longjing hills and cruise West Lake, then travel to Shanghai for an evening on the Bund.","Breakfast, lunch","Shanghai hotel",""),
  (13,"Shanghai History Museum","Shanghai","Museum morning; afternoon free.","Shanghai History Museum in the morning; the afternoon is free.","Breakfast","Shanghai hotel","Half-day city tour, or a Huangpu River night cruise"),
  (14,"Shanghai – Australia","Shanghai","Transfer to the airport for the flight home.","Transfer to Pudong Airport for the flight back to Australia.","Breakfast","",""),
  (15,"Arrive Australia",None,"","Arrive home.","","","")],
 6154: [
  (1,"Australia – Calgary","Calgary","Fly to Calgary and make your own way to the hotel.","Fly to Calgary. Transfers aren't included on arrival, so make your own way to the airport hotel.","","Country Inn & Suites Calgary Airport or similar",""),
  (2,"Calgary – Lake Louise – Banff – Canmore","Canmore","Lake Louise, Banff National Park sightseeing, overnight in Canmore.","An early start west into the Rockies. See Lake Louise, then a sightseeing tour of Banff National Park before settling into Canmore, the quieter town just outside the park gate.","Breakfast","Canmore Inn & Suites or similar",""),
  (3,"Canmore free day","Canmore","Free day, or the Icefields Parkway.","A free day in Canmore. The optional Icefields Parkway trip takes you north past Bow Lake and Peyto Lake to the Athabasca Glacier for a ride onto the ice in an Ice Explorer.","Breakfast","Canmore Inn & Suites or similar","Icefields Parkway with the Columbia Icefield Ice Explorer"),
  (4,"Banff – Kamloops on the Rocky Mountaineer","Kamloops","Rocky Mountaineer day one: Continental Divide, Spiral Tunnels, Kicking Horse Canyon.","Board the Rocky Mountaineer at Banff. The route crosses the Continental Divide, loops through the Spiral Tunnels and follows the Kicking Horse River before descending into the dry interior at Kamloops.","Breakfast, lunch on board","DoubleTree by Hilton Kamloops or similar",""),
  (5,"Kamloops – Vancouver","Vancouver","Rocky Mountaineer day two through the Fraser Canyon.","Second rail day: the Thompson River, Hell's Gate and the Fraser Canyon, then into the Fraser Valley and Vancouver.","Breakfast, lunch on board","Sandman Suites or similar, Vancouver",""),
  (6,"Embark Inside Passage cruise","Vancouver","Board Holland America's Koningsdam at Canada Place.","Free morning in Vancouver, then board the Koningsdam at Canada Place. The ship sails in the late afternoon under the Lions Gate Bridge.","All meals on board","Koningsdam",""),
  (7,"Cruising the Inside Passage","Juneau","A day at sea through the fjords.","At sea threading the sheltered channels of the Inside Passage. Whales, eagles and the occasional bear on shore are all possible from the deck.","All meals on board","Koningsdam",""),
  (8,"Juneau","Juneau","Alaska's capital: glaciers, whales and floatplanes.","A day in Juneau, reachable only by sea or air. Mendenhall Glacier, whale-watching boats and floatplane flights over the icefield are the usual shore excursions.","All meals on board","Koningsdam","Shore excursions: Mendenhall Glacier, whale watching, helicopter or floatplane"),
  (9,"Skagway","Skagway","Klondike gold-rush town and the White Pass railway.","Skagway's boardwalks and false-front storefronts date from the 1898 gold rush. The White Pass & Yukon Route railway climbs the same pass the prospectors walked.","All meals on board","Koningsdam","White Pass & Yukon Route railway"),
  (10,"Glacier Bay National Park","Glacier Bay","Scenic cruising among tidewater glaciers.","Scenic cruising in Glacier Bay with park rangers on board (Endicott Arm and Dawes Glacier on some sailings). Expect calving ice and seals on the floes.","All meals on board","Koningsdam",""),
  (11,"Ketchikan","Ketchikan","Alaska's 'First City': totems, Tlingit culture, salmon.","Ketchikan is built on stilts over the water. Totem poles, Creek Street and Tlingit heritage sites are within walking distance of the dock.","All meals on board","Koningsdam","Misty Fjords flightseeing, salmon fishing"),
  (12,"Cruising the Inside Passage","Ketchikan","Second day at sea heading south.","A final sea day heading south through the Inside Passage towards Vancouver.","All meals on board","Koningsdam",""),
  (13,"Vancouver – Australia","Vancouver","Disembark and make your own way to the airport.","Disembark in Vancouver and make your own way to the airport for the flight home.","Breakfast on board","",""),
  (14,"In transit",None,"","In transit.","","",""),
  (15,"Arrive Australia",None,"","Arrive home.","","","")],
}

# Representative points for destinations that are regions rather than towns
G.update({"Inside Passage":(-133.5,56.5),"Lapland":(25.72,66.5),"Red Sea":(33.81,27.26),"Great Wall":(116.02,40.36),"Amalfi Coast":(14.48,40.63)})
# Country / area centroids for the world-level dots (TripADeal-style destination areas, so Alaska is its own)
COUNTRIES = {
 "Japan":(138.0,36.5),"China":(105.0,35.0),"Vietnam":(106.0,16.5),"Cambodia":(104.9,12.5),"Singapore":(103.82,1.35),"Malaysia":(101.7,4.2),"Thailand":(100.9,15.0),
 "South Korea":(127.8,36.3),"Taiwan":(120.96,23.7),"Hong Kong":(114.17,22.32),"Canada":(-106.0,56.0),"Alaska":(-150.0,63.0),"USA":(-98.0,39.5),
 "Peru":(-75.0,-9.2),"Argentina":(-64.0,-34.0),"Brazil":(-51.9,-14.2),"Egypt":(30.8,26.8),"Morocco":(-6.5,31.8),"Italy":(12.6,42.5),"Greece":(22.0,39.0),"Türkiye":(35.2,38.9),
 "Finland":(26.0,64.0),"Norway":(9.0,62.0),
}
# headline destinations per deal: the cities TripADeal lists under the title, plus the countries they sit in
DEST = {
 5836:(["Tokyo","Mt Fuji","Kyoto","Hiroshima","Osaka"],["Japan"]),
 6363:(["Beijing","Great Wall","Xi'an","Shanghai"],["China"]),
 6380:(["Tokyo","Mt Fuji","Kyoto","Osaka"],["Japan"]),
 6098:(["Tokyo","Mt Fuji","Kyoto","Hiroshima","Fukuoka"],["Japan"]),
 5684:(["Ha Long Bay","Hanoi","Hoi An","Phnom Penh","Siem Reap"],["Vietnam","Cambodia"]),
 5863:(["Ha Long Bay","Hanoi","Pu Luong"],["Vietnam"]),
 6370:(["Singapore","Penang","Phuket"],["Singapore","Malaysia","Thailand"]),
 6181:(["Tokyo","Kagoshima","Nagasaki","Busan"],["Japan","South Korea"]),
 6369:(["Tokyo","Taipei","Hong Kong"],["Japan","Taiwan","Hong Kong"]),
 6154:(["Vancouver","Banff","Juneau","Ketchikan"],["Canada","Alaska"]),
 6141:(["Lake Louise","Inside Passage","Whistler"],["Canada","Alaska"]),
 6169:(["Yellowstone","Lake Louise","Juneau"],["USA","Canada","Alaska"]),
 5619:(["Lima","Machu Picchu","Buenos Aires","Iguazu Falls","Rio de Janeiro"],["Peru","Argentina","Brazil"]),
 5858:(["Cairo","Luxor","Aswan","Red Sea"],["Egypt"]),
 5716:(["Casablanca","Chefchaouen","Fes","Erg Chebbi","Marrakech"],["Morocco"]),
 6371:(["Rome","Naples","Mykonos","Santorini","Kuşadası"],["Italy","Greece","Türkiye"]),
 6112:(["Helsinki","Lapland","Lofoten","Bergen","Oslo"],["Finland","Norway"]),
}

import details_extra as X
G.update(X.G_EXTRA)

def s(city, nights=0, note="", mode="coach"):
    """mode = how you travel INTO this stop: coach | rail | cruise | river | flight"""
    lng, lat = G[city]; return [city, lng, lat, nights, note, mode]

def tour(id, name, slug, days, price, dates, region, type_, stops, months, itinerary="headline", was=None, save=None, per="pp", special=None, ends=0, from_="Sydney", tags=()):
    return dict(id=id, name=name, url=f"https://www.tripadeal.com.au/deals/{id}-{slug}", days=days, price=price, was=was, save=save, per=per,
                dates=dates, region=region, type=type_, from_city=from_, months=months, special=bool(special), special_label=special or "", ends=ends,
                itinerary=itinerary, tags=list(tags), stops=stops)

AU = lambda c="Sydney": s(c,0,"Depart Australia")
BLS = "Bucket List Sale"   # sitewide, ends 22 Sep
CAN = "Canada Sale"        # ends 15 Sep

TOURS = [
 tour(5836,"Japan Discovery","japan-discovery",13,3999,"27 Nov 2026 – 22 Nov 2027","Asia","Guided",
  [s("Melbourne",0,"Depart Australia"),s("Tokyo",3,"Tsukiji Outer Market, Meiji Shrine, free day"),s("Mt Fuji",0,"5th Station, 2300m"),
   s("Nagano",1,"Overnight in the Nagano region"),s("Takayama",1,"Wasabi farm, Narai-juku, old town"),s("Kyoto",2,"Fushimi Inari, Golden Pavilion, free day"),
   s("Okayama",0,"Kurashiki canals and Korakuen garden"),s("Hiroshima",2,"Miyajima Island, Peace Memorial Park"),s("Osaka",2,"Bullet train in, free day, fly home","rail")],
  ["Nov","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct"],"exact",save="37%",special=BLS,ends=10,from_="Melbourne",tags=["Trip Only option","Rail"]),
 tour(6363,"Warriors of China","warriors-of-china",15,1899,"24 Nov 2026 – 20 Nov 2027","Asia","Guided",
  [AU(),s("Beijing",3,"Tiananmen Square, Forbidden City, Great Wall at Juyong Pass"),s("Xi'an",2,"Terracotta Warriors, Small Wild Goose Pagoda","rail"),
   s("Luoyang",1,"High-speed train in, group dinner","rail"),s("Zhengzhou",2,"Longmen Grottoes, day at leisure"),s("Wuxi",1,"Lake Tai","rail"),
   s("Suzhou",1,"Lihu Park, pearl factory"),s("Hangzhou",1,"Lingering Garden, Tangxi Ancient Town"),s("Shanghai",2,"Meijiawu tea village, West Lake, The Bund")],
  ["Nov","Mar","Apr","May","Jun","Aug","Sep","Oct"],"exact",save="52%",special=BLS,ends=10,tags=["Trip Only option","Adults only"]),
 tour(6380,"Unbelievable Japan","unbelievable-japan",9,2499,"2 Mar – 26 May 2027","Asia","Guided",
  [AU(),s("Tokyo",3),s("Mt Fuji",0),s("Kyoto",2),s("Osaka",2)],["Mar","Apr","May"],save="30%",special=BLS,ends=10,tags=["Trip Only option"]),
 tour(6098,"Best of Japan","best-of-japan",16,5199,"26 Feb – 23 Nov 2027","Asia","Guided",
  [AU(),s("Tokyo",3),s("Mt Fuji",1),s("Kanazawa",1),s("Kyoto",3,"","rail"),s("Hiroshima",2),s("Fukuoka",2,"","rail")],["Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov"],
  save="35%",special=BLS,ends=10,tags=["Trip Only option","Rail","Cruise"]),
 tour(5684,"Vietnam & Cambodia Discovery","vietnam-cambodia-discovery",15,2699,"1 Dec 2026 – 20 Dec 2027","Asia","Small group",
  [AU(),s("Hanoi",2),s("Ha Long Bay",1),s("Hue",1,"","flight"),s("Hoi An",2),s("Ho Chi Minh City",2,"","flight"),s("Phnom Penh",1),s("Siem Reap",3)],
  ["Dec","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov"],save="35%",special=BLS,ends=10,tags=["Trip Only option","Small group"]),
 tour(5863,"Vietnam for 2","vietnam-for-2",12,4399,"30 Nov 2026 – 21 Dec 2027","Asia","Small group",
  [AU(),s("Hanoi",3),s("Pu Luong",2),s("Ha Long Bay",1),s("Hanoi",1)],["Nov","Dec","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct"],
  per="for2",tags=["Deal for 2","Small group"]),
 tour(6370,"Singapore, Malaysia & Thailand Getaway","singapore-malaysia-thailand-getaway-cruise",9,2399,"25 Jan – 19 Nov 2027","Asia","Ocean cruise",
  [AU(),s("Singapore",2),s("Penang",1,"","cruise"),s("Phuket",1,"","cruise"),s("Singapore",1,"","cruise")],["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov"],tags=["Royal Caribbean"]),
 tour(6181,"Japan Explorer Cruise","japan-explorer-cruise",15,3599,"15 May – 17 Oct 2027","Asia","Ocean cruise",
  [AU(),s("Tokyo",2),s("Kagoshima",1,"","cruise"),s("Nagasaki",1,"","cruise"),s("Busan",1,"","cruise"),s("Tokyo",1,"","cruise")],["May","Jun","Jul","Aug","Sep","Oct"],tags=["Trip Only option","Princess Cruises"]),
 tour(6369,"Japan to Taiwan & Hong Kong Cruise","japan-to-taiwan-and-hong-kong-cruise",15,5099,"8 Jan 2027","Asia","Ocean cruise",
  [AU(),s("Tokyo",2),s("Osaka",1,"","cruise"),s("Taipei",1,"","cruise"),s("Hong Kong",3,"","cruise")],["Jan"],tags=["Royal Caribbean"]),
 tour(6154,"Rockies Rail & Cruise","rockies-rail-and-cruise",15,7499,"19 Apr – 30 Aug 2027","Americas","Rail",
  [AU(),s("Calgary",1,"Arrive, own transfer to hotel"),s("Lake Louise",0,"Canada's 'Diamond in the Wilderness'"),s("Banff",0,"National park sightseeing"),s("Canmore",2,"Free day or Icefields Parkway option"),
   s("Kamloops",1,"Rocky Mountaineer day 1","rail"),s("Vancouver",1,"Rocky Mountaineer day 2, then embark","rail"),s("Juneau",2,"Day at sea, then Juneau","cruise"),s("Skagway",1,"Gold-rush town","cruise"),
   s("Glacier Bay",1,"Scenic cruising","cruise"),s("Ketchikan",2,"Port day, then day at sea","cruise"),s("Vancouver",0,"Disembark, fly home","cruise")],
  ["Apr","May","Jun","Jul","Aug"],"exact",was=7699,save="$200",special=CAN,ends=3,tags=["Trip Only option","Rocky Mountaineer","Cruise"]),
 tour(6141,"Alaska & Canada Discovery","alaska-canada-discovery",16,5299,"18 Apr – 12 Sep 2027","Americas","Ocean cruise",
  [AU(),s("Vancouver",2),s("Whistler",1),s("Lake Louise",1),s("Banff",2),s("Vancouver",1),s("Ketchikan",0,"","cruise"),s("Juneau",0,"","cruise"),s("Skagway",0,"","cruise"),s("Vancouver",0,"","cruise")],
  ["Apr","May","Jun","Jul","Aug","Sep"],was=5499,save="$200",special=CAN,ends=3,tags=["Trip Only option"]),
 tour(6169,"Yellowstone, Alaska & Canada 2027","yellowstone-alaska-canada-2027",19,6499,"22 Apr – 9 Sep 2027","Americas","Guided",
  [AU(),s("Salt Lake City",1),s("Jackson Hole",1),s("Yellowstone",2),s("Calgary",1),s("Banff",1),s("Lake Louise",1),s("Vancouver",1),s("Ketchikan",0,"","cruise"),s("Juneau",0,"","cruise"),s("Skagway",0,"","cruise"),s("Vancouver",0,"","cruise")],
  ["Apr","May","Jun","Jul","Aug","Sep"],was=6699,save="$200",special=CAN,ends=3,tags=["Trip Only option","Cruise"]),
 tour(5619,"Ultimate South American Adventure","ultimate-south-american-adventure",24,10499,"1 Feb – 25 Nov 2027","Americas","Small group",
  [AU(),s("Lima",2),s("Cusco",2,"","flight"),s("Machu Picchu",1,"","rail"),s("Puerto Maldonado",3,"","flight"),s("Buenos Aires",3,"","flight"),s("Iguazu Falls",2,"","flight"),s("Rio de Janeiro",3,"","flight")],
  ["Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov"],save="41%",special=BLS,ends=10,tags=["Trip Only option","Small group"]),
 tour(5858,"Best of Egypt for 2","best-of-egypt-for-2",14,9199,"22 Jan – 17 Dec 2027","Africa","Guided",
  [AU(),s("Cairo",2),s("Giza",0),s("Luxor",2),s("Aswan",2,"","river"),s("Luxor",1,"","river"),s("Hurghada",3),s("Cairo",1)],
  ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],per="for2",tags=["Deal for 2","River cruise"]),
 tour(5716,"Colours of Morocco","colours-of-morocco",17,5999,"23 Feb – 16 Nov 2027","Africa","Small group",
  [AU(),s("Casablanca",1),s("Chefchaouen",1),s("Fes",2),s("Erg Chebbi",1),s("Ouarzazate",1),s("Marrakech",3),s("Casablanca",1)],
  ["Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov"],save="35%",special=BLS,ends=10,tags=["Small group"]),
 tour(6371,"Italy, Türkiye & Greek Islands Cruise","italy-turkiye-greek-islands-cruise",13,4599,"12 May – 20 Oct 2027","Europe","Ocean cruise",
  [AU(),s("Rome",2),s("Naples",0,"","cruise"),s("Mykonos",0,"","cruise"),s("Kuşadası",0,"","cruise"),s("Santorini",0,"","cruise"),s("Athens",0,"","cruise"),s("Rome",1,"","cruise")],["May","Jun","Jul","Aug","Sep","Oct"],tags=["Royal Caribbean"]),
 tour(6112,"Iconic Northern Lights Rail & Sail","iconic-northern-lights-rail-sail",16,10599,"21 Sep 2027 – 23 Mar 2028","Europe","Rail",
  [AU(),s("Helsinki",2),s("Rovaniemi",2,"","rail"),s("Tromsø",1,"","flight"),s("Lofoten",1,"","cruise"),s("Bergen",2,"","cruise"),s("Flåm",1,"","rail"),s("Oslo",2,"","rail")],["Sep","Oct","Nov","Dec","Jan","Feb","Mar"],tags=["Hurtigruten","Cruise"]),
]

CDN = "https://images.tripadeal.com.au/cdn-cgi/image/format=auto,width=800/https://cstad.s3.ap-southeast-2.amazonaws.com/"
IMAGES = {  # exact gallery captured from the deal page; other deals get candidate hero URLs generated below
 6363: [("6363_Warriors_of_China_WEB_HERO_1.jpg","Stand in awe of the Terracotta Warriors in Xi'an"),
        ("6363_Warriors_of_China_WEB_HERO_2.jpg","Admire the Great Wall of China"),
        ("6363_Warriors_of_China_WEB_HERO_3.jpg","Visit Luoyang to explore the famed Longmen Grottoes"),
        ("6363_Warriors_of_China_WEB_HERO_4.jpg","The iconic skyline of Shanghai"),
        ("PUBS+LIBRARY/1+-+Destinations/ASIA+-+EAST+%26+SOUTHEAST/CHINA/G-China-Beijing-TiananmenSquareGarden-AS.jpeg","Wander through Tiananmen Square in Beijing")],
}
def hero_candidates(t):
    slug = "".join(ch for ch in t["name"].replace("&","").replace(",","").replace("'","") if ch.isalnum() or ch==" ").strip()
    slug = "_".join(slug.split())
    return [dict(src=f"{CDN}{t['id']}_{slug}_WEB_HERO_{n}.jpg", caption="", guessed=True) for n in range(1,5)]
FEATURED_ORDER = [6154,6380,6141,6363,5684,6169,5836,5619,6098,5863,5858,5716,6371,6181,6112,6370,6369]  # homepage order, 12 Sep 2026
DAYS.update(X.DAYS); IMAGES.update(X.IMAGES); DEST.update(X.DEST)
for t in TOURS:
    if t["id"] in X.STOPS:
        t["stops"] = [AU(t["from_city"])] + [s(*x) for x in X.STOPS[t["id"]]]
        t["itinerary"] = "exact"
    t["featured"] = FEATURED_ORDER.index(t["id"])+1 if t["id"] in FEATURED_ORDER else 0
    t["images"] = [dict(src=CDN+p, caption=c) for p,c in IMAGES[t["id"]]] if t["id"] in IMAGES else hero_candidates(t)
    cities, countries = DEST[t["id"]]
    t["destinations"] = [dict(name=c, lng=G[c][0], lat=G[c][1]) for c in cities]
    t["countries"] = countries
    if t["id"] in DAYS:
        t["days_detail"]=[dict(d=d,title=ti,city=c,text=tx,detail=dt,meals=me,hotel=ho,optional=op,lng=G[c][0] if c else None,lat=G[c][1] if c else None) for d,ti,c,tx,dt,me,ho,op in DAYS[t["id"]]]
if __name__ == "__main__":
    json.dump(TOURS, open(DATA/"tours.json","w"), ensure_ascii=False, indent=1)
    json.dump({k:list(v) for k,v in COUNTRIES.items()}, open(DATA/"countries_pts.json","w"))
    print(len(TOURS), "tours;", sum(t["itinerary"]=="exact" for t in TOURS), "exact")
