"""Hand-written detail for deals read in full on 12 Sep 2026 (own words). Merged by build_data.py."""
G_EXTRA = {"Nagoya":(136.91,35.18),"Komaki":(136.91,35.29),"Whistler":(-122.96,50.12),"Vancouver":(-123.12,49.28)}
STOPS = {}    # id -> list of s(...) tuples (city, nights, note, mode)  — replaces the headline route
DAYS = {}     # id -> [(d,title,city,text,detail,meals,hotel,optional)]
IMAGES = {}   # id -> [(path, caption)]
DEST = {}     # id -> (cities, countries) overrides

STOPS[6380] = [("Osaka",2,"Arrive; free day or Hiroshima option","flight"),("Kyoto",0,"Kiyomizu-dera, free time"),("Nagoya",2,"Free day or Shirakawa-go option"),
               ("Tokyo",2,"Toyota museum en route; Tsukiji and Meiji Shrine"),("Mt Fuji",0,"5th Station and Five Lakes"),("Komaki",1,"Overnight in Aichi Prefecture"),("Osaka",0,"Fly home")]
DEST[6380] = (["Osaka","Kyoto","Nagoya","Tokyo","Mt Fuji"],["Japan"])
DAYS[6380] = [
 (1,"Australia – Osaka","Osaka","Fly to Osaka and transfer to the hotel.","Fly to Osaka (usually via China; some departures leave a day early). Transfer to the hotel on arrival.","","Hotel Sobial Osaka Dome or similar",""),
 (2,"Osaka free day","Osaka","Free day, or the optional Hiroshima trip.","A free day in Osaka. The optional Hiroshima trip goes by bullet train, ferries to Miyajima for Itsukushima Shrine, then visits the Peace Memorial Park and A-Bomb Dome before returning.","Breakfast","Hotel Sobial Osaka Dome or similar","Hiroshima & Miyajima full-day trip by bullet train"),
 (3,"Osaka – Kyoto – Nagoya","Nagoya","Kiyomizu-dera, free time in Kyoto, then on to Nagoya.","Drive to Kyoto for Kiyomizu-dera and its wooden stage above the hillside, then free time in the old capital (or an optional half-day tour) before continuing to Nagoya in the evening. About 200 km.","Breakfast","Travelodge Nagoya Sakae or similar","Kyoto half-day: Fushimi Inari, Golden Pavilion, Arashiyama bamboo grove"),
 (4,"Nagoya free day","Nagoya","Free day, or Shirakawa-go and Takayama.","Free day, or the optional 380 km round trip to the thatched farmhouses of Shirakawa-go, Takayama's old town and a Japanese knife museum.","Breakfast","Travelodge Nagoya Sakae or similar","Shirakawa-go, Takayama & Japanese Knife Museum"),
 (5,"Nagoya – Tokyo","Tokyo","Toyota Commemorative Museum, then drive to Tokyo.","Visit the Toyota Commemorative Museum of Industry and Technology in the original 1911 factory buildings, then drive about 360 km to Tokyo.","Breakfast","Hotel Mystays Tachikawa or similar",""),
 (6,"Tokyo sightseeing","Tokyo","Tsukiji Outer Market and Meiji Shrine; afternoon free.","Morning tour of the Tsukiji Outer Market and Meiji Shrine's gardens. Afternoon free, or the optional tour taking in Tokyo Tower, Shinjuku and Shibuya Crossing.","Breakfast","Hotel Mystays Tachikawa or similar","Tokyo afternoon tour with Tokyo Tower"),
 (7,"Tokyo – Mt Fuji – Aichi","Komaki","Mt Fuji's 5th Station and the Five Lakes, then Aichi Prefecture.","Drive to Mt Fuji's 5th Station at 2,300 m for views over the Fuji Five Lakes, then continue to Aichi Prefecture for the night. About 420 km.","Breakfast","Route-Inn Grantia Komaki or similar",""),
 (8,"Aichi – Osaka – Australia","Osaka","Early drive to Osaka for the flight home.","Early departure for the 250 km drive to Osaka and the afternoon flight home.","Breakfast","",""),
 (9,"Arrive Australia",None,"","Arrive home.","","","")]
IMAGES[6380] = [("6380_Unbelievable_Japan_WEB_HERO_1.jpg","Mount Fuji, Japan's tallest and most iconic peak"),
 ("6380_Unbelievable_Japan_WEB_HERO_2-Kyoto_Higashiyama.jpg","Kyoto, Japan's ancient capital"),
 ("6380_Unbelievable_Japan_WEB_HERO_3_Osaka.jpg","Osaka Castle"),
 ("6380_Unbelievable_Japan_WEB_HERO_4-Tokyo_Akihabara.jpg","Akihabara, Tokyo's technology and anime district"),
 ("PUBS+LIBRARY/1+-+Destinations/ASIA+-+EAST+%26+SOUTHEAST/JAPAN/G-Japan-Osaka-Takoyaki-AS.jpg","Street food in Osaka")]

# ---------------- 6141 Alaska & Canada Discovery (Itinerary 1, Holland America) ----------------
STOPS[6141] = [("Calgary",1,"Arrive, own transfer","flight"),("Lake Louise",0,"'Diamond in the Wilderness'"),("Banff",0,"Bow River, Hoodoos, Bow Falls"),("Canmore",2,"Free day or Icefields Parkway option"),
               ("Kamloops",1,"Through Yoho, Glacier and Mt Revelstoke parks"),("Whistler",2,"Gold Rush route; free day"),("Vancouver",0,"City tour, embark"),
               ("Juneau",2,"Day at sea, then Juneau","cruise"),("Skagway",1,"","cruise"),("Glacier Bay",1,"Scenic cruising","cruise"),("Ketchikan",2,"Port day, then day at sea","cruise"),("Vancouver",0,"Disembark, fly home","cruise")]
DEST[6141] = (["Lake Louise","Banff","Whistler","Vancouver","Juneau","Ketchikan"],["Canada","Alaska"])
DAYS[6141] = [
 (1,"Australia – Calgary","Calgary","Fly to Calgary and make your own way to the hotel.","Fly to Calgary; transfers aren't included, so make your own way to the airport hotel. Check-in from 3pm with luggage storage for early arrivals.","","Country Inn & Suites Calgary Airport or similar",""),
 (2,"Calgary – Lake Louise – Banff – Canmore","Canmore","Lake Louise, a Banff sightseeing tour, then Canmore.","Early meet-up, then about 190 km west to Lake Louise for time on the lakeshore and a look inside the Fairmont Chateau. Continue to Banff for the Bow River, the Hoodoos and Bow Falls, finishing in Canmore.","","Canmore Inn & Suites or similar",""),
 (3,"Canmore free day","Canmore","Free day, or the Icefields Parkway.","A free day in Canmore, or the optional 420 km return trip along the Icefields Parkway past Crowfoot Glacier, Bow Summit and Mistaya Canyon to the Athabasca Glacier for an Ice Explorer ride.","","Canmore Inn & Suites or similar","Jasper National Park & Columbia Icefield ($300 pp)"),
 (4,"Canmore – Kamloops","Kamloops","A big drive through three national parks to Kamloops.","About 600 km and eight hours through Yoho, Glacier and Mount Revelstoke national parks, stopping at Eagle Pass for the 'Last Spike' of the transcontinental railway. Overnight in the Kamloops / Sun Peaks area.","","Ramada Kamloops or similar",""),
 (5,"Kamloops – Whistler","Whistler","The Cariboo Wagon Trail to Whistler.","Follow the old Gold Rush route along the Cariboo Wagon Trail, about 300 km, into the alpine village of Whistler beneath Blackcomb Mountain.","","Aava Whistler Hotel or similar",""),
 (6,"Whistler free day","Whistler","A free day in Whistler.","A full day at leisure in Whistler: the village, the Peak 2 Peak gondola, or the lakes and trails.","","Aava Whistler Hotel or similar",""),
 (7,"Whistler – Vancouver, embark","Vancouver","Vancouver city tour, then board the Koningsdam.","Drive about 120 km to Vancouver for a tour of Chinatown, Gastown and Stanley Park, then board Holland America's Koningsdam at Canada Place and sail in the afternoon.","Dinner","Koningsdam",""),
 (8,"Inside Passage, scenic cruising","Juneau","A day at sea through the Inside Passage.","At sea through the glacier-cut fjords and rainforest of the Inside Passage. Humpbacks, orca, bald eagles and shoreline bears are all possible.","All meals on board","Koningsdam",""),
 (9,"Juneau","Juneau","Alaska's remote capital, 1:30pm to 10pm.","Docked from early afternoon until late evening. Hike Mount Roberts, take a whale-watching boat to Auke Bay, or a floatplane to see bears on Admiralty Island.","All meals on board","Koningsdam","Whale watching, Mendenhall Glacier, floatplane bear viewing"),
 (10,"Skagway","Skagway","Gold-rush town, 7am to 8pm.","A full day in the Klondike gateway: the historic district, the Red Onion Saloon and the White Pass & Yukon Route railway into the mountains.","All meals on board","Koningsdam","White Pass & Yukon Route railway"),
 (11,"Glacier Bay, scenic cruising","Glacier Bay","Tidewater glaciers from the deck, 6:15am to 3:15pm.","A morning and early afternoon among Glacier Bay's seven tidewater glaciers with park rangers aboard. Dress for rain and bring binoculars. (Endicott Arm on the 25 April sailing.)","All meals on board","Koningsdam",""),
 (12,"Ketchikan","Ketchikan","Alaska's First City, 11am to 7pm.","Totem poles at the Totem Heritage Center and Totem Bight, Tlingit culture at Saxman Village, and salmon everywhere.","All meals on board","Koningsdam","Misty Fjords flightseeing, sportfishing"),
 (13,"Inside Passage, scenic cruising","Ketchikan","Second sea day heading south.","A final day at sea through the Inside Passage back towards Vancouver.","All meals on board","Koningsdam",""),
 (14,"Vancouver – Australia","Vancouver","Disembark 7am and make your own way to the airport.","Disembark after breakfast and make your own way to the airport; luggage storage is available at the port and airport.","Breakfast on board","",""),
 (15,"In transit",None,"","In transit.","","",""),
 (16,"Arrive Australia",None,"","Arrive home.","","","")]
IMAGES[6141] = [("6141_Alaska_and_Canada_Discovery_2027_WEB_HERO_1_LakeLouise.jpg","Lake Louise, Alberta"),
 ("6141_Alaska_and_Canada_Discovery_2027_WEB_HERO_2_Banff.jpg","Banff, in the Canadian Rockies"),
 ("6141_Alaska_and_Canada_Discovery_2027_WEB_HERO_3_Vancouver.jpg","Vancouver, where the cruise begins and ends"),
 ("6141_Alaska_and_Canada_Discovery_2027_WEB_HERO_4_AlaskanGlacier.jpg","Glaciers from the ship in Alaska"),
 ("PUBS+LIBRARY/1+-+Destinations/AMERICA+-+NORTH/CANADA/G-Canada-Calgary-City-AS.jpg","Calgary, where the trip begins")]

# ---------------- 5684 Vietnam & Cambodia Discovery (15-day itinerary) ----------------
G_EXTRA.update({"Da Nang":(108.2,16.05)})
STOPS[5684] = [("Hanoi",1,"Arrive","flight"),("Ha Long Bay",1,"Overnight junk-boat cruise on the bay"),("Hanoi",1,"Sung Sot Cave, cooking class, back to Hanoi"),
               ("Hoi An",3,"Fly Hanoi–Da Nang; walking tour; free day","flight"),("Ho Chi Minh City",3,"Fly Da Nang–HCMC; Cu Chi Tunnels; free day","flight"),
               ("Phnom Penh",2,"Shared bus via Moc Bai border; free day"),("Siem Reap",2,"Shared bus; full-day Angkor tour; fly home")]
DEST[5684] = (["Ha Long Bay","Hanoi","Hoi An","Ho Chi Minh City","Phnom Penh","Siem Reap"],["Vietnam","Cambodia"])
DAYS[5684] = [
 (1,"Australia – Hanoi","Hanoi","Fly to Hanoi and transfer to the hotel.","Fly to Hanoi; met on arrival and transferred to the hotel.","","Flower Garden Hotel or similar, Hanoi",""),
 (2,"Hanoi – Ha Long Bay overnight cruise","Ha Long Bay","Drive to Ha Long Bay and board a traditional junk for the night.","About 180 km through rice country to Ha Long Bay. Board a junk-style boat for an overnight cruise among the limestone islands: seafood lunch, swimming or kayaking, a pearl farm, a cooking demonstration and dinner on board.","Breakfast, lunch, dinner","Le Journey Cruise or similar (on board)",""),
 (3,"Ha Long Bay – Hanoi","Hanoi","Tai chi on deck, Sung Sot Cave, cooking class, return to Hanoi.","Optional sunrise tai chi, then a tender to Sung Sot ('Surprise') Cave, a spring-roll cooking class and light lunch before sailing back to port and driving to Hanoi.","Breakfast, lunch","Flower Garden Hotel or similar, Hanoi","Water puppet show & Vietnamese dinner ($60)"),
 (4,"Hanoi – Hoi An","Hoi An","Hanoi walking tour, then fly to Da Nang.","Morning walk through a local market, around West Lake, into Quan Thanh Taoist temple and the Cua Bach church. Afternoon flight to Da Nang and transfer to Hoi An.","Breakfast","Le Pavillon Luxury Resort or similar, Hoi An",""),
 (5,"Hoi An walking tour","Hoi An","Old-town walking tour; free afternoon.","Museum of History and Culture, the 1590s Japanese Covered Bridge, the central market, Phuc Kien Assembly Hall and the 200-year-old Tan Ky house. Afternoon free.","Breakfast","Le Pavillon Luxury Resort or similar, Hoi An","Market tour & cooking class at Tra Que village ($60)"),
 (6,"Hoi An free day","Hoi An","A free day in Hoi An.","A free day, or the optional trip to Ba Na Hills by cable car for the Golden Bridge, the French wine cellar and gardens, with lunch.","Breakfast","Le Pavillon Luxury Resort or similar, Hoi An","Ba Na Hills & Golden Bridge full day ($170)"),
 (7,"Hoi An – Ho Chi Minh City","Ho Chi Minh City","Fly from Da Nang to Ho Chi Minh City.","Transfer to Da Nang airport for the flight south to Ho Chi Minh City. Rest of the day free.","Breakfast","Muong Thanh Saigon Centre or similar",""),
 (8,"Cu Chi Tunnels","Ho Chi Minh City","The Cu Chi Tunnels, 60 km from the city.","Drive to the Cu Chi Tunnels and walk a section of the network that once held hospitals, kitchens and command posts. Drop-off at the hotel or the War Remnants Museum.","Breakfast","Muong Thanh Saigon Centre or similar",""),
 (9,"Ho Chi Minh City free day","Ho Chi Minh City","A free day, or the Mekong Delta.","Free day, or the optional Mekong Delta trip: motor boat from My Tho, canoes through the small canals, fruit and music at a village home, lunch on an islet.","Breakfast","Muong Thanh Saigon Centre or similar","Mekong Delta day tour ($80)"),
 (10,"Ho Chi Minh City – Phnom Penh","Phnom Penh","Shared bus across the Moc Bai border to Phnom Penh.","Early pick-up for the 230 km shared tourist bus to Cambodia, with visa processing at the Moc Bai / Bavet border; six to eight hours. A flight upgrade is available. Free afternoon.","Breakfast","The Onra Hotel or similar, Phnom Penh","Flight upgrade instead of the bus ($280)"),
 (11,"Phnom Penh free day","Phnom Penh","A free day in the capital.","Free day, or the optional city tour: Central Market, Independence Monument, Wat Ounalom, the Tuol Sleng museum and Choeung Ek killing fields, then the Royal Palace and Silver Pagoda.","Breakfast","The Onra Hotel or similar, Phnom Penh","Choeung Ek & Phnom Penh city tour ($120)"),
 (12,"Phnom Penh – Siem Reap","Siem Reap","Shared bus 320 km to Siem Reap.","An early start for the shared bus north through Kandal, Kampong Cham and Kampong Thom provinces to Siem Reap. Afternoon free.","Breakfast","Tara Angkor Hotel or similar, Siem Reap",""),
 (13,"Temples of Angkor","Siem Reap","A full day at Angkor Wat, Angkor Thom and Ta Prohm.","The south gate of Angkor Thom, the Terrace of Elephants and Terrace of the Leper King, lunch, then jungle-wrapped Ta Prohm and finally Angkor Wat itself.","Breakfast, lunch","Tara Angkor Hotel or similar, Siem Reap",""),
 (14,"Siem Reap – Australia","Siem Reap","Transfer to the airport for the flight home.","Transfer to Siem Reap airport for the flight home; packed breakfast for early departures.","Breakfast","",""),
 (15,"Arrive Australia",None,"","Arrive home.","","","")]
IMAGES[5684] = [("5684_15D_Vietnam_Cambodia_WEB_HERO_1_Ankor_Wat.jpg","Angkor Wat, near Siem Reap"),
 ("5684_15D_Vietnam_Cambodia_WEB_HERO_2_HalongBay.jpg","The emerald waters of Ha Long Bay"),
 ("5684_15D_Vietnam_Cambodia_WEB_HERO_3_HOIAN.jpg","The ancient town of Hoi An"),
 ("5684_15D_Vietnam_Cambodia_WEB_HERO_4_VIETNAM.jpg","Vietnamese cuisine in Hanoi"),
 ("5684+-+Ha+Long+Bay+2.jpeg","Floating fishing villages in Ha Long Bay")]

# ---------------- 6169 Yellowstone, Alaska & Canada 2027 ----------------
G_EXTRA.update({"Seattle":(-122.33,47.61),"Kellogg":(-116.12,47.54),"Gardiner":(-110.71,45.03),"Great Falls":(-111.3,47.5),"Abbotsford":(-122.33,49.05),"Endicott Arm":(-133.5,57.7)})
STOPS[6169] = [("Seattle",1,"Arrive, own transfer","flight"),("Kellogg",1,"Through eastern Washington wine country"),("Gardiner",2,"Yellowstone National Park, two days"),
               ("Great Falls",1,"North through Montana"),("Canmore",3,"Cross into Canada; Lake Louise and Banff day; free day"),("Abbotsford",1,"Big drive through Yoho, Glacier, Mt Revelstoke"),
               ("Vancouver",0,"City tour, embark Princess Cruises"),("Juneau",2,"Day at sea, then Juneau","cruise"),("Skagway",1,"","cruise"),("Endicott Arm",1,"Scenic cruising to Dawes Glacier","cruise"),
               ("Ketchikan",2,"Port day, then day at sea","cruise"),("Vancouver",0,"Disembark, fly home","cruise")]
DEST[6169] = (["Seattle","Yellowstone","Lake Louise","Banff","Vancouver","Juneau","Ketchikan"],["USA","Canada","Alaska"])
DAYS[6169] = [
 (1,"Australia – Seattle","Seattle","Fly to Seattle and make your own way to the hotel.","Fly to Seattle; own transfer to the hotel.","","Ramada Tukwila or similar, Seattle",""),
 (2,"Seattle – Kellogg, Idaho","Kellogg","Across Washington's wheat and wine country to Idaho.","About 590 km east through eastern Washington's rolling farmland and wine country, past the Columbia Gorge on the old Lewis and Clark route, to the mining town of Kellogg.","","Silver Inn or similar, Kellogg",""),
 (3,"Kellogg – Yellowstone","Gardiner","Cowboy country to the world's first national park.","A 680 km drive through Montana's gold-rush rivers and ranch country into Yellowstone. First look at the geysers, mud pots and hot springs, then overnight at Gardiner or West Yellowstone.","","Big Rock Inn or similar, Yellowstone area",""),
 (4,"Yellowstone National Park","Gardiner","A full day in Yellowstone.","A second day in the park; your guide chooses the route by weather and conditions. Old Faithful, Grand Prismatic Spring and the Lamar Valley wildlife are the usual targets.","","Big Rock Inn or similar, Yellowstone area",""),
 (5,"Yellowstone – Great Falls","Great Falls","Early wildlife drive, then north to Great Falls.","An early start for wildlife, then leave the park and drive about 360 km north through mountains and national forest to Great Falls, Montana.","","The Great Falls Inn or similar",""),
 (6,"Great Falls – Canmore, Canada","Canmore","Cross the border into the Rockies.","About 650 km north across the Canadian border into increasingly mountainous country, arriving in Canmore with the evening free.","","Canmore Inn & Suites or similar",""),
 (7,"Lake Louise & Banff","Canmore","Lake Louise, then a Banff sightseeing tour.","Time at Lake Louise and the Fairmont Chateau, then Banff for the Bow River, the Hoodoos and Bow Falls before returning to Canmore.","","Canmore Inn & Suites or similar",""),
 (8,"Canmore free day","Canmore","Free day, or the Icefields Parkway.","A free day, or the optional Icefields Parkway trip to the Columbia Icefield and an Ice Explorer ride on the Athabasca Glacier (about 460 km).","","Canmore Inn & Suites or similar","Jasper National Park & Columbia Icefield ($300 pp)"),
 (9,"Canmore – Abbotsford","Abbotsford","Nine hours through three national parks to the Fraser Valley.","The long day: about 890 km through Yoho, Glacier and Mount Revelstoke national parks, the 'Last Spike' at Eagle Pass, then down to the Abbotsford / Chilliwack area.","","Comfort Inn or similar, Abbotsford",""),
 (10,"Vancouver, embark","Vancouver","Vancouver city tour, then board your Princess ship.","Drive into Vancouver for Chinatown, Gastown and Stanley Park, then board at Canada Place for the seven-night Alaska cruise (Crown, Discovery or Emerald Princess by date).","Dinner","Princess Cruises ship",""),
 (11,"At sea","Juneau","A day at sea in Alaskan waters.","A day at sea with whales, orca and eagles possible from the deck.","All meals on board","Princess Cruises ship",""),
 (12,"Juneau","Juneau","Alaska's capital: glaciers, gold-rush history, indigenous culture.","A day in Juneau, founded on an 1880 gold strike and now known for Mendenhall Glacier, whale watching and Tlingit culture.","All meals on board","Princess Cruises ship","Shore excursions"),
 (13,"Skagway","Skagway","The Klondike gateway and the White Pass railway.","Skagway's restored Broadway Avenue, local Tlingit culture and the vintage White Pass & Yukon Route railway.","All meals on board","Princess Cruises ship","White Pass & Yukon Route railway"),
 (14,"Endicott Arm & Dawes Glacier","Endicott Arm","Scenic cruising to a calving tidewater glacier.","Cruise 48 km into the Endicott Arm fjord to the calving face of Dawes Glacier, past waterfalls, icebergs, seals and bears. (Glacier Bay on the 9 and 16 May sailings.)","All meals on board","Princess Cruises ship",""),
 (15,"Ketchikan","Ketchikan","The Salmon Capital of the World.","Ketchikan's totem poles at the Totem Heritage Center, Haida, Tlingit and Tsimshian heritage, and salmon everywhere.","All meals on board","Princess Cruises ship",""),
 (16,"Inside Passage, scenic cruising","Ketchikan","A last day at sea heading south.","A final day cruising the Inside Passage back towards Vancouver.","All meals on board","Princess Cruises ship",""),
 (17,"Vancouver – Australia","Vancouver","Disembark 7am and make your own way to the airport.","Disembark after breakfast and make your own way to the airport.","Breakfast on board","",""),
 (18,"In transit",None,"","In transit.","","",""),
 (19,"Arrive Australia",None,"","Welcome home.","","","")]
IMAGES[6169] = [("6169_Yellowstone_Alaska_and_Canada_2027_WEB_HERO_1_Yellowstone.jpg","Grand Prismatic Spring, Yellowstone"),
 ("6169_Yellowstone_Alaska_and_Canada_2027_WEB_HERO_2_LakeLou.jpg","Lake Louise"),
 ("6169_Yellowstone_Alaska_and_Canada_2027_WEB_HERO_3.jpg","Your Princess Cruises ship"),
 ("6169_Yellowstone_Alaska_and_Canada_2027_WEB_HERO_4_Alaska_Humpback.jpg","Humpback whales in Alaskan waters"),
 ("5259+-+Yellowstone+2.jpg","Bison in Yellowstone National Park")]

# ---------------- 5619 Ultimate South American Adventure (24-day itinerary) ----------------
G_EXTRA.update({"Urubamba":(-72.12,-13.31),"Aguas Calientes":(-72.53,-13.15),"Puno":(-70.02,-15.84),"Puerto Iguazu":(-54.57,-25.6)})
STOPS[5619] = [("Lima",2,"Arrive; city tour","flight"),("Puerto Maldonado",2,"Amazon lodge, two nights","flight"),("Cusco",3,"City tour; free day","flight"),
               ("Urubamba",1,"Sacred Valley: Pisac and Ollantaytambo"),("Aguas Calientes",1,"Peru Expedition Train","rail"),("Machu Picchu",0,"Sunrise guided tour"),("Cusco",1,"Train and road back to Cusco","rail"),
               ("Puno",2,"Andean road with stops; Lake Titicaca"),("Lima",1,"Fly from Juliaca","flight"),("Buenos Aires",3,"City tour, tango dinner, free day","flight"),
               ("Puerto Iguazu",2,"Argentinian side of the falls","flight"),("Rio de Janeiro",3,"Brazilian side, then fly to Rio; Christ the Redeemer","flight")]
DEST[5619] = (["Lima","Puerto Maldonado","Cusco","Machu Picchu","Puno","Buenos Aires","Iguazu Falls","Rio de Janeiro"],["Peru","Argentina","Brazil"])
DAYS[5619] = [
 (1,"Australia – Lima","Lima","Fly to Lima and transfer to the hotel.","Fly to Lima, the 'City of Kings'; met and transferred to the hotel. Perth departures may leave two days early.","","Hotel Jose Antonio Executive or similar",""),
 (2,"Lima city tour","Lima","Huaca Pucllana, the historic centre and the San Francisco catacombs.","A morning at the pre-Inca Huaca Pucllana, then the UNESCO-listed centre: Plaza de Armas, the Government Palace and cathedral, and the Convent of San Francisco with its 25,000-volume library and bone-lined catacombs.","Breakfast","Hotel Jose Antonio Executive or similar",""),
 (3,"Lima – Puerto Maldonado – Amazon","Puerto Maldonado","Fly to the Amazon and boat to your lodge.","Fly to Puerto Maldonado, store your main bag in town and take a motor boat (30 minutes to two hours) to the lodge. Lunch, then a first walk or boat trip into the forest.","Breakfast, lunch, dinner","EcoAmazonia Lodge or similar",""),
 (4,"Amazon Jungle","Puerto Maldonado","A full day of jungle walks and boat trips.","Walks and boat excursions around oxbow lakes and side channels with your Amazon guide: monkeys, birdlife, caimans, capybara and, with luck, giant river otters.","Breakfast, lunch, dinner","EcoAmazonia Lodge or similar",""),
 (5,"Amazon – Cusco","Cusco","Boat back to town, fly to Cusco.","Return by river to Puerto Maldonado and fly to Cusco at 3,399 m. Rest of the day free to acclimatise.","Breakfast","San Agustin Plaza or similar",""),
 (6,"Cusco city tour","Cusco","Koricancha, the cathedral, Sacsayhuaman, Qenqo and Tambomachay.","A half-day through Inca and colonial Cusco: the gold-walled Koricancha, the cathedral on the Plaza de Armas, then the fortress of Sacsayhuaman, the Qenqo labyrinth and the Inca baths at Tambomachay above the city.","Breakfast","San Agustin Plaza or similar",""),
 (7,"Cusco free day","Cusco","A free day, or Maras & Moray or Rainbow Mountain.","A free day in the old Inca capital. Optional half-day to the Moray terraces and Maras salt pans, or the full-day Rainbow Mountain trek to 5,036 m (one or the other), plus a folklore dinner show in the evening.","Breakfast","San Agustin Plaza or similar","Maras & Moray; Rainbow Mountain trek; folklore dinner & show"),
 (8,"Sacred Valley of the Incas","Urubamba","Pisac market and ruins, then Ollantaytambo.","Over the mountains into the Sacred Valley: Pisac's market and hilltop ruins, lunch in Urubamba, then Ollantaytambo's Temple of the Sun and living Inca town. Pack an 8 kg bag for the train tomorrow.","Breakfast","San Agustin Monasterio de la Recoleta or similar, Urubamba",""),
 (9,"Peru Expedition Train – Aguas Calientes","Aguas Calientes","Train along the Urubamba to the foot of Machu Picchu.","Board the Peru Expedition Train at Ollantaytambo for the ride along the Urubamba River into cloud forest and the pedestrian town of Aguas Calientes. Hot springs and markets; early night.","Breakfast","Hatun Inti Boutique or similar, Aguas Calientes","Express Inca Trail trek from Km 104 via Wiñay Wayna to the Sun Gate"),
 (10,"Machu Picchu","Machu Picchu","Sunrise at the citadel, then train and road to Cusco.","Bus up at 5:40am for a two-hour guided tour: the House of the Guardian, Intihuatana, the Temple of the Sun and the Sacred Plaza. Back down for lunch, then train to Poroy and road to Cusco, arriving about 7pm.","Breakfast","San Agustin Plaza or similar, Cusco",""),
 (11,"Cusco – Puno","Puno","The Andean road to Lake Titicaca with stops.","A 7am bus south with stops at the painted chapel of Andahuaylillas, the Temple of Wiracocha at Raqchi, a buffet lunch, La Raya Pass at 4,335 m and the Pukara museum, arriving in Puno about 5pm.","Breakfast, lunch","Hotel Jose Antonio Puno or similar","Andean Explorer-style train upgrade (selected days)"),
 (12,"Lake Titicaca & the Uros Islands","Puno","The reed islands of the Uros, then Taquile Island.","Motorboat to the floating totora-reed islands of the Uros, then on to Taquile for a walk across the island, a family visit and lunch before returning to Puno.","Breakfast, lunch","Hotel Jose Antonio Puno or similar",""),
 (13,"Puno – Lima","Lima","Fly from Juliaca back to Lima.","Transfer to Juliaca airport for the flight to Lima. Rest of the day free.","Breakfast","Hotel Jose Antonio Lima or similar",""),
 (14,"Lima – Buenos Aires","Buenos Aires","Fly to Argentina.","Fly from Lima to Buenos Aires and transfer to a central hotel.","Breakfast","Libertador Hotel or similar",""),
 (15,"Buenos Aires city tour & tango","Buenos Aires","Plaza de Mayo, San Telmo, La Boca, Recoleta, then a tango dinner.","A morning through Plaza de Mayo, the Casa Rosada, San Telmo's cobbles, La Boca's Caminito and Recoleta Cemetery with Evita's grave. Evening three-course dinner and tango show at Aljibe Tango in San Telmo.","Breakfast, dinner","Libertador Hotel or similar",""),
 (16,"Buenos Aires free day","Buenos Aires","A free day, or a gaucho ranch day.","Free day in the city, or the optional full day at a traditional estancia: horse riding, an asado lunch, folk music and a gaucho skills display.","Breakfast","Libertador Hotel or similar","Gaucho full-day ranch experience"),
 (17,"Buenos Aires – Iguazu Falls","Puerto Iguazu","Fly to Puerto Iguazu.","Fly north to Puerto Iguazu on the Argentinian side of the falls. Afternoon free.","Breakfast","El Pueblito Theme Hotel or similar",""),
 (18,"Iguazu Falls, Argentinian side","Puerto Iguazu","A day on the walkways above the falls.","Guided day in Iguazu National Park on the raised jungle walkways to the Devil's Throat and the upper and lower circuits.","Breakfast","El Pueblito Theme Hotel or similar","The Great Adventure boat tour under the falls (about US$100)"),
 (19,"Iguazu, Brazilian side – Rio de Janeiro","Rio de Janeiro","The Brazilian panorama, then fly to Rio.","Cross into Brazil for the half-day panoramic circuit of the canyon, Salto Rivadavia and the Devil's Throat, then fly from Foz do Iguaçu to Rio de Janeiro.","Breakfast","Windsor Plaza Hotel or similar, Rio",""),
 (20,"Christ the Redeemer","Rio de Janeiro","Corcovado and the Selarón Stairs.","Up Corcovado to Christ the Redeemer (renovation scaffolding possible until July 2027, with 220 steps in place of the lifts), then Jorge Selarón's tiled staircase in Lapa.","Breakfast","Windsor Plaza Hotel or similar, Rio",""),
 (21,"Rio free day","Rio de Janeiro","A free day, or Sugar Loaf.","A free day for Copacabana and Ipanema, or the optional half-day city tour with the cable car up Sugar Loaf Mountain.","Breakfast","Windsor Plaza Hotel or similar, Rio","City tour & Sugar Loaf Mountain"),
 (22,"Rio – Australia","Rio de Janeiro","Transfer to the airport for the flight home.","Transfer to the airport for the flight home.","Breakfast","",""),
 (23,"In transit",None,"","In transit.","","",""),
 (24,"Arrive Australia",None,"","Arrive home.","","","")]

# ---------------- 6098 Best of Japan ----------------
G_EXTRA.update({"Beppu":(131.49,33.28),"Kumamoto":(130.74,32.8),"Himeji":(134.69,34.82),"Yufuin":(131.36,33.26)})
STOPS[6098] = [("Tokyo",3,"Sightseeing tour; free day","flight"),("Mt Fuji",0,"5th Station and Five Lakes"),("Nagano",1,"Japanese Alps"),("Takayama",1,"Wasabi farm, Narai-juku, old town"),
               ("Kyoto",2,"Fushimi Inari, Golden Pavilion; free day"),("Osaka",1,"Nara deer park, Dotonbori"),("Himeji",0,"Sake brewery, White Heron Castle"),("Hiroshima",2,"Bullet train Himeji–Okayama, then coach; Miyajima","rail"),
               ("Beppu",1,"Kintaikyo Bridge, Hells of Beppu"),("Kumamoto",1,"Yufuin, Mt Aso, Kusasenri"),("Fukuoka",2,"Kumamoto Castle, Yanagawa canals, Dazaifu; free day")]
DEST[6098] = (["Tokyo","Mt Fuji","Takayama","Kyoto","Osaka","Hiroshima","Beppu","Fukuoka"],["Japan"])
DAYS[6098] = [
 (1,"Australia – Tokyo","Tokyo","Fly to Tokyo and transfer to the hotel.","Fly to Tokyo (direct not guaranteed) and transfer to the hotel.","","Hotel Mystays Tachikawa or similar",""),
 (2,"Tokyo sightseeing","Tokyo","Tsukiji Outer Market and Meiji Shrine; afternoon free.","A morning at the Tsukiji Outer Market and Meiji Shrine's gardens, then a free afternoon or the optional tour with Tokyo Tower, Shinjuku and Shibuya Crossing.","Breakfast","Hotel Mystays Tachikawa or similar","Tokyo afternoon tour with Tokyo Tower (¥8,000)"),
 (3,"Tokyo free day","Tokyo","Free day, or Hakone.","A free day, or the optional Hakone trip: Lake Ashi cruise, cable car to the Owakudani sulphur vents, and the Open-Air Museum.","Breakfast","Hotel Mystays Tachikawa or similar","Hakone day tour (¥15,000)"),
 (4,"Tokyo – Mt Fuji – Nagano","Nagano","Mt Fuji's 5th Station and the Five Lakes, then the Japanese Alps.","About 370 km: up to Mt Fuji's 5th Station at 2,300 m, the Five Lakes, then inland to the Nagano region.","Breakfast","Hotel Route Inn Suwa Inter or similar, Nagano region",""),
 (5,"Nagano – Narai-juku – Takayama","Takayama","Wasabi farm, an Edo post town, then Takayama.","A wasabi farm fed by Alpine spring water, the preserved Edo-period post town of Narai-juku, then Takayama's old town (a Gifu hotel may substitute).","Breakfast","Hotel Hana or similar, Takayama",""),
 (6,"Takayama – Kyoto","Kyoto","Fushimi Inari and the Golden Pavilion.","Drive 270 km to Kyoto for a half-day tour: the torii tunnels of Fushimi Inari and the gold-leaf Kinkaku-ji. Evening free.","Breakfast","Kyoto Ubell Hotel or similar","Maiko dinner show in Gion (¥35,000)"),
 (7,"Kyoto free day","Kyoto","Free day, or 'Kyoto by the Sea'.","Free day, or the optional 250 km trip to the Amanohashidate sandbar, the boathouses of Ine and the thatched village of Miyama.","Breakfast","Kyoto Ubell Hotel or similar","Kyoto by the Sea day tour (¥15,000)"),
 (8,"Kyoto – Nara – Osaka","Osaka","Nara's bowing deer, then Dotonbori.","Nara Park and its thousand sacred deer, then Osaka's Shinsaibashi and Dotonbori districts at leisure. About 90 km.","Breakfast","Hotel Sobial Osaka Dome or similar",""),
 (9,"Osaka – Himeji – bullet train – Hiroshima","Hiroshima","Sake brewery, Himeji Castle, Shinkansen to Okayama, coach to Hiroshima.","The Hakutsuru sake museum, then the White Heron castle at Himeji. Board the Shinkansen for a 20-minute run to Okayama, then coach 160 km to Hiroshima.","Breakfast","Vessel Hotel Hiroshima or similar",""),
 (10,"Hiroshima & Miyajima","Hiroshima","Miyajima's floating shrine, then the Peace Park.","Ferry to Miyajima for Itsukushima Shrine, then the Peace Memorial Park, museum and A-Bomb Dome.","Breakfast","Vessel Hotel Hiroshima or similar",""),
 (11,"Hiroshima – Kintaikyo – Beppu","Beppu","The Kintaikyo Bridge, then the Hells of Beppu on Kyushu.","Stop at the five-arched Kintaikyo Bridge, cross to Kyushu and tour the seven 'Hells of Beppu': Sea Hell, Blood Pond Hell, the mud pools and the Tornado geyser. About 330 km.","Breakfast","Amanek Hotel or similar, Beppu/Oita",""),
 (12,"Beppu – Yufuin – Mt Aso – Kumamoto","Kumamoto","Onsen town, an active volcano, then Kumamoto.","Free time in the onsen town of Yufuin, then Mt Aso's vast caldera and the Kusasenri grassland with views of Nakadake, before Kumamoto. About 160 km.","Breakfast","Hotel Route Inn or similar, Kumamoto",""),
 (13,"Kumamoto – Yanagawa – Fukuoka","Fukuoka","Kumamoto Castle, Yanagawa's canals, Dazaifu shrine.","Kumamoto Castle, the 930 km of canals in Yanagawa ('the Venice of Kyushu'), and Dazaifu Tenmangu Shrine before arriving in Fukuoka. About 150 km.","Breakfast","U-BELL Hotel or similar, Fukuoka",""),
 (14,"Fukuoka free day","Fukuoka","A free day in Kyushu's biggest city.","A free day: Fukuoka Castle, Hakata ramen, the Daibutsu.","Breakfast","U-BELL Hotel or similar, Fukuoka",""),
 (15,"Fukuoka – Australia","Fukuoka","Transfer to the airport for the flight home.","Transfer to the airport for the flight home.","Breakfast","",""),
 (16,"Arrive Australia",None,"","Arrive home.","","","")]
IMAGES[6098] = [("6098_Best_of_Japan_WEB_HERO_1_Himeji.jpg","Himeji Castle"),("6098_Best_of_Japan_WEB_HERO_2_Kyoto.jpg","Yasaka Pagoda from Sannen-zaka, Kyoto"),
 ("6098_Best_of_Japan_WEB_HERO_3.jpg","Mt Fuji from the Five Lakes area"),("6098_Best_of_Japan_WEB_HERO_4_Beppu_Sea-Hell.jpg","Umi Jigoku, one of the Hells of Beppu"),
 ("PUBS+LIBRARY/1+-+Destinations/ASIA+-+EAST+%26+SOUTHEAST/JAPAN/G-Japan-Nara-manydeerinshrine2-AS.jpeg.jpg","The deer of Nara Park")]

# ---------------- 5863 Vietnam for 2 (12-day itinerary) ----------------
G_EXTRA.update({"Ninh Binh":(105.97,20.25)})
STOPS[5863] = [("Hanoi",2,"Arrive; walking tour","flight"),("Ha Long Bay",1,"Overnight junk cruise on the bay"),("Hanoi",1,"Sung Sot Cave, cooking class, back to Hanoi"),
               ("Ninh Binh",2,"Hoa Lu, Tam Coc boat ride; Trang An, Bich Dong"),("Pu Luong",3,"Nature reserve: villages, waterfall"),("Hanoi",1,"Return to Hanoi; fly home")]
DEST[5863] = (["Hanoi","Ha Long Bay","Ninh Binh","Pu Luong"],["Vietnam"])
DAYS[5863] = [
 (1,"Australia – Hanoi","Hanoi","Fly to Hanoi and transfer to the hotel.","Fly to Hanoi; met and transferred to the hotel.","","Flower Garden Hotel or similar, Hanoi",""),
 (2,"Hanoi walking tour","Hanoi","A local market, West Lake, Quan Thanh temple.","A morning walk through a local market and around West Lake, into the Taoist temple of Quan Thanh and the French-built Cua Bach church. Afternoon free.","Breakfast","Flower Garden Hotel or similar, Hanoi",""),
 (3,"Hanoi – Ha Long Bay overnight cruise","Ha Long Bay","Board a traditional junk for a night among the karsts.","About 180 km to Ha Long Bay and aboard a junk-style boat: seafood lunch, swimming or kayaking, a pearl farm, a cooking demonstration and dinner at anchor among the limestone islands.","Breakfast, lunch, dinner","Le Journey Cruise or similar (on board)",""),
 (4,"Ha Long Bay – Hanoi","Hanoi","Sung Sot Cave, cooking class, back to Hanoi.","Tender to Sung Sot ('Surprise') Cave, a spring-roll cooking class and light lunch, then back to port and 180 km to Hanoi.","Breakfast, lunch","Flower Garden Hotel or similar, Hanoi","Water puppet show & Vietnamese dinner ($60)"),
 (5,"Hanoi – Hoa Lu – Tam Coc","Ninh Binh","The ancient capital, then a bamboo boat through Tam Coc.","Drive to Ninh Binh province for the 10th-century temples of Hoa Lu, lunch, then a two-hour bamboo boat ride on the Hoang Long River through the three caves of Tam Coc.","Breakfast, lunch","The Reed Hotel or similar, Ninh Binh",""),
 (6,"Trang An & Bich Dong Pagoda","Ninh Binh","'Ha Long Bay on land' by boat, then a cliffside pagoda.","Another two-hour boat trip through the UNESCO-listed Trang An grottoes, lunch, then the tiered Bich Dong Pagoda built into the Truong Yen cliffs.","Breakfast, lunch","The Reed Hotel or similar, Ninh Binh",""),
 (7,"Ninh Binh – Pu Luong","Pu Luong","Phat Diem church, then into the nature reserve.","Stop at the stone cathedral of Phat Diem, then drive into Pu Luong Nature Reserve: terraced rice, limestone peaks and Thai villages. Hillside resorts mean stairs to your room.","Breakfast","Pu Luong Eco Garden or similar",""),
 (8,"Kho Muong & Ban Don villages","Pu Luong","Thai villages and a mountain hike.","A short drive to the traditional Thai villages of Kho Muong and Ban Don above the terraces, then a leisurely hike in the reserve looking for caves and waterfalls. Some steep sections; a pool day is the alternative.","Breakfast","Pu Luong Eco Garden or similar",""),
 (9,"Hieu Waterfall","Pu Luong","An easy trek through rice terraces to Hieu Waterfall.","Trek from Hieu village along the terraces and through jungle to Hieu Waterfall for a swim, then back to the retreat.","Breakfast","Pu Luong Eco Garden or similar",""),
 (10,"Pu Luong – Hanoi","Hanoi","A slow morning, then back to Hanoi.","A relaxed morning at the resort before the drive back to Hanoi. Afternoon free.","Breakfast","Flower Garden Hotel or similar, Hanoi",""),
 (11,"Hanoi – Australia","Hanoi","Morning free, then the flight home.","Morning at leisure, then transfer to the airport.","Breakfast","",""),
 (12,"Arrive Australia",None,"","Arrive home.","","","")]
IMAGES[5863] = [("4713_North_Vietnam_Discovery_WEB_HERO_1_Halong+bay.jpg","Ha Long Bay"),("4713_North_Vietnam_Discovery_WEB_HERO_3_Hotel.jpg","Your resort in the Pu Luong reserve"),
 ("5670_2_for_1_Vietnam_WEB_HERO_4_NinhBinh.jpg","Ninh Binh province")]

# ---------------- 5858 Best of Egypt for 2 (14-day itinerary) ----------------
G_EXTRA.update({"Kom Ombo":(32.93,24.45),"Edfu":(32.87,24.98)})
STOPS[5858] = [("Cairo",3,"Pyramids, Sphinx, Egyptian Museum, Old Cairo","flight"),("Aswan",1,"Fly in; High Dam, Unfinished Obelisk; board cruise","flight"),
               ("Kom Ombo",1,"Twin temples of Sobek and Horus","river"),("Edfu",0,"Temple of Horus","river"),("Luxor",1,"Valley of the Kings, Karnak, Luxor Temple","river"),
               ("Hurghada",3,"Red Sea resort, two free days"),("Cairo",1,"Five-hour transfer; fly home")]
DEST[5858] = (["Cairo","Giza","Aswan","Luxor","Hurghada"],["Egypt"])
DAYS[5858] = [
 (1,"Australia – Cairo",None,"Depart for Cairo.","Depart Australia for Cairo; some flights arrive the next day.","","",""),
 (2,"Welcome to Cairo","Cairo","Arrive and transfer to the hotel.","Met at the airport and transferred to the hotel near the pyramids.","","Jaz Pyramids Resort or similar, Cairo",""),
 (3,"Pyramids & Sphinx","Cairo","The Pyramids of Giza, the Sphinx and the Valley Temple.","With an Egyptologist guide: the Great Pyramid of Khufu, the Valley Temple, Chephren's pyramid and the Sphinx, then the Papyrus Institute, or swap in the new Grand Egyptian Museum.","Breakfast","Jaz Pyramids Resort or similar, Cairo","Grand Egyptian Museum with Tutankhamun's treasures ($140)"),
 (4,"Egyptian Museum & Old Cairo","Cairo","The Egyptian Museum, Tahrir Square and Coptic Cairo.","A guided morning in the Egyptian Museum's 5,000 years of treasures, then through Tahrir Square to Coptic Cairo: the Babylon Fortress, the Hanging Church and St Sergius. Evening free.","Breakfast","Jaz Pyramids Resort or similar, Cairo","5-star Dahabiya sailboat upgrade for the Nile ($1,100 pp)"),
 (5,"Cairo – Aswan, board the Nile cruise","Aswan","Fly to Aswan, see the High Dam and Unfinished Obelisk, board.","Fly to Aswan for the High Dam and the Unfinished Obelisk in its quarry, a perfume factory, then board the MS Nile Crown 1 (or similar) for lunch, the pool and a traditional dinner.","Breakfast, lunch, dinner","MS Nile Crown 1 or similar (on board)",""),
 (6,"Aswan – Kom Ombo","Kom Ombo","Optional Abu Simbel, then sail to Kom Ombo.","A morning on board or the optional dawn coach to Abu Simbel's colossal Ramses II temples. Sail to Kom Ombo for the twin temples of Sobek and Horus, then on to Edfu with a galabeya party on board.","Breakfast, lunch, dinner","MS Nile Crown 1 or similar (on board)","Abu Simbel guided tour ($150)"),
 (7,"Edfu – Luxor","Luxor","Temple of Horus at Edfu, then sail to Luxor.","Morning visit to the Temple of Horus at Edfu, then sail past Esna to Luxor with lunch on board and a belly dance and Tanoura show in the evening.","Breakfast, lunch, dinner","MS Nile Crown 1 or similar (on board)",""),
 (8,"Valley of the Kings, Karnak & Luxor","Luxor","The West Bank tombs, then Luxor and Karnak temples.","Disembark for the Valley of the Kings, the Temple of Hatshepsut and the Colossi of Memnon, then cross to the East Bank for Luxor Temple and the vast Karnak complex.","Breakfast","Aracan Eatabe Hotel or similar, Luxor",""),
 (9,"Luxor – Hurghada","Hurghada","Transfer to a Red Sea beach resort.","Drive to Hurghada on the Red Sea for three nights at a beachfront resort.","Breakfast, dinner","Amwaj Hurghada Resort or similar",""),
 (10,"Hurghada free day","Hurghada","A free day on the Red Sea.","A free day for the beach, snorkelling or diving on the reefs, or the Giftun Islands.","Breakfast, lunch, dinner","Amwaj Hurghada Resort or similar",""),
 (11,"Hurghada free day","Hurghada","A second free day.","Another free day; desert safaris, submarine and boat trips can be booked at the resort.","Breakfast, lunch, dinner","Amwaj Hurghada Resort or similar",""),
 (12,"Hurghada – Cairo","Cairo","A five-hour road transfer back to Cairo.","About 465 km and five hours by road back to Cairo with rest stops. Evening free.","Breakfast","Hotel Tolip El Galaa or similar, Cairo",""),
 (13,"Cairo – Australia","Cairo","Transfer to the airport for the flight home.","Transfer to the airport; some flights leave in the early hours of Day 14.","Breakfast","",""),
 (14,"Arrive Australia",None,"","Arrive home.","","","")]
IMAGES[5858] = [("5858_H_Best+of+Egypt+for+2_WEB_HERO_1_Giza.jpg","Camels at Giza"),("5858_H_Best+of+Egypt+for+2_WEB_HERO_2Aswan-Nile.jpg","The Nile at Aswan"),
 ("5858_H_Best+of+Egypt+for+2_WEB_HERO_3_Karnak.jpg","Karnak Temple, Luxor"),("5858_H_Best+of+Egypt+for+2_WEB_HERO_4_Hurdugha.jpg","The Red Sea at Hurghada")]

# ---------------- 5716 Colours of Morocco ----------------
G_EXTRA.update({"Rabat":(-6.85,34.02),"Merzouga":(-4.01,31.1),"Boumalne Dades":(-5.98,31.37),"Taroudant":(-8.88,30.47),"Essaouira":(-9.77,31.51),"Volubilis":(-5.55,34.07),"Todgha Gorge":(-5.59,31.58)})
STOPS[5716] = [("Rabat",1,"Arrive Casablanca, drive to Rabat","flight"),("Chefchaouen",1,"Rabat tour, then the blue town"),("Fes",2,"Volubilis en route; full-day Fes tour"),("Merzouga",1,"Middle Atlas, Ziz Valley"),
               ("Erg Chebbi",1,"4x4, nomads, camel ride, desert camp"),("Boumalne Dades",1,"Rissani market, Todgha Gorge"),("Ouarzazate",1,"Valley of Roses, Berber lunch"),("Taroudant",2,"Ait Benhaddou; free day"),
               ("Essaouira",1,"Via Agadir along the coast"),("Marrakech",2,"City tour, Jemaa el-Fnaa"),("Casablanca",1,"Hassan II Mosque; fly home")]
DEST[5716] = (["Rabat","Chefchaouen","Fes","Erg Chebbi","Ouarzazate","Essaouira","Marrakech","Casablanca"],["Morocco"])
DAYS[5716] = [
 (1,"Australia – Casablanca",None,"Depart for Casablanca.","Depart Australia for Casablanca.","","",""),
 (2,"Casablanca – Rabat","Rabat","Arrive and drive to the capital.","Met at Casablanca airport and driven about an hour and a half to Rabat.","","ONOMO Hotel Rabat Terminus or similar",""),
 (3,"Rabat – Chefchaouen","Chefchaouen","Rabat's monuments, then the blue-washed town.","A guided morning in Rabat: the Kasbah des Oudaias, the Mausoleum of Mohammed V and Hassan Tower. Then about 250 km to Chefchaouen for a walking tour from the 18th-century Kasbah Museum through the blue lanes.","Breakfast, dinner","Dar Echchaouen Maison d'Hôte & Riad or similar",""),
 (4,"Chefchaouen – Volubilis – Fes","Fes","Roman Volubilis through the Rif Mountains, then Fes.","Through the Rif to the UNESCO-listed Roman city of Volubilis and its mosaics, then on to Fes, with the view over the old city from the North Borj. About 250 km.","Breakfast, dinner","Riad Marjana Suites & Spa or similar, Fes",""),
 (5,"Fes full-day tour","Fes","The world's oldest working medina.","A full day in Fes el-Bali: the 9th-century Karaouine, the carved cedar of Medersa Bou Inania, the souks and tanneries, then the Mellah, the Royal Palace gates and a viewpoint over the medina.","Breakfast","Riad Marjana Suites & Spa or similar, Fes",""),
 (6,"Fes – Merzouga","Merzouga","Over the Middle Atlas to the edge of the Sahara.","A long 460 km day through the cedar forests near Ifrane and Azrou (Barbary macaques possible), over the Tizi n'Talremt pass, down the Ziz Gorge and valley past Erfoud to Merzouga at the foot of Erg Chebbi.","Breakfast, dinner","Riad Madu or similar, Merzouga",""),
 (7,"Erg Chebbi: 4x4, camels & desert camp","Erg Chebbi","Dunes by 4x4, tea with nomads, Gnawa music, sunset camel ride.","4x4 through the dunes, tea in a nomad family's tent, then Gnawa music and lunch at Khamlia village. In the afternoon ride a camel into the dunes to a Bedouin camp for sunset, dinner and music by the fire.","Breakfast, lunch, dinner","Madu Desert Camp (private facilities) or similar",""),
 (8,"Merzouga – Todgha Gorge – Boumalne Dades","Boumalne Dades","Rissani market, a Berber museum, the Todgha Gorge.","Optional sunrise on the dunes, then 4x4 back to Merzouga and 250 km via Rissani market and the Berber Oasis Museum at Khorbat to the ochre cliffs of Todgha Gorge and the Road of a Thousand Kasbahs.","Breakfast, dinner","Hotel Xaluca Dades or similar",""),
 (9,"Boumalne Dades – Ouarzazate","Ouarzazate","The Valley of Roses and lunch with a Berber family.","The Valley of Roses and the adobe village of Boutaghrar, lunch in a Berber family home, then 120 km to Ouarzazate.","Breakfast, lunch, dinner","Riad Dar Chamaa or similar, Ouarzazate",""),
 (10,"Ouarzazate – Ait Benhaddou – Taroudant","Taroudant","The film-set kasbah, then across the Anti-Atlas.","Ait Benhaddou's UNESCO-listed ksar, then 290 km through the Anti-Atlas via the carpet town of Taznakht and saffron capital Taliouine to the walled city of Taroudant.","Breakfast, dinner","Riad Dar Zitoune or similar, Taroudant",""),
 (11,"Taroudant free day","Taroudant","A free day in 'Little Marrakech'.","A free day inside Taroudant's ochre walls.","Breakfast, dinner","Riad Dar Zitoune or similar, Taroudant",""),
 (12,"Taroudant – Agadir – Essaouira","Essaouira","The Atlantic coast to Essaouira.","About 260 km to the port of Agadir, then the coast road to Essaouira (old Mogador): the Skala du Port, the Jewish quarter and the silver craft centre.","Breakfast","Riad Mimouna or similar, Essaouira",""),
 (13,"Essaouira – Marrakech","Marrakech","A free morning, then to the red city.","Morning at leisure in Essaouira, then 180 km inland to Marrakech with the evening free.","Breakfast","Riad Passali or similar, Marrakech",""),
 (14,"Marrakech city tour","Marrakech","Koutoubia, the Saadian Tombs, Bahia Palace, Jemaa el-Fnaa.","A guided day through the Koutoubia Mosque, the Saadian Tombs, the Bahia Palace and into Jemaa el-Fnaa as the evening entertainment begins.","Breakfast","Riad Passali or similar, Marrakech","Carriage ride ($150); Chez Ali dinner & Fantasia show ($240); cooking class ($150)"),
 (15,"Marrakech – Casablanca","Casablanca","The Hassan II Mosque.","Drive 240 km to Casablanca for the Hassan II Mosque and its 210 m minaret over the sea. Afternoon free.","Breakfast","Hotel Odyssee Center or similar, Casablanca",""),
 (16,"Casablanca – Australia","Casablanca","Transfer to the airport.","Transfer to Casablanca airport for the flight home.","Breakfast","",""),
 (17,"Arrive Australia",None,"","Arrive home.","","","")]
IMAGES[5716] = [("5716_Colours_of_Morocco_WEB_HERO_1_Erg_Chebbi.jpg","Camel trek on the dunes of Erg Chebbi"),("5716_Colours_of_Morocco_WEB_HERO_2_Chefchaouen.jpg","The blue-washed town of Chefchaouen"),
 ("5716_Colours_of_Morocco_WEB_HERO_3_Ait_Benhaddou.jpg","Ait Benhaddou"),("5716_Colours_of_Morocco_WEB_HERO_4_Essaouira.jpg","Essaouira on the Atlantic coast"),("5716+-+Hassan+II+Mosque.jpg","The Hassan II Mosque, Casablanca")]

# ---------------- 6371 Italy, Türkiye & Greek Islands Cruise ----------------
G_EXTRA.update({"Civitavecchia":(11.8,42.09)})
STOPS[6371] = [("Rome",3,"Three nights at leisure","flight"),("Civitavecchia",0,"Own way to the port; embark Odyssey of the Seas"),("Santorini",2,"Day at sea, then Santorini","cruise"),
               ("Kuşadası",1,"Gateway to Ephesus","cruise"),("Mykonos",1,"","cruise"),("Naples",2,"Day at sea, then Naples","cruise"),("Civitavecchia",0,"Disembark 5am, own way to Rome airport","cruise")]
DEST[6371] = (["Rome","Santorini","Kuşadası","Mykonos","Naples"],["Italy","Greece","Türkiye"])
DAYS[6371] = [
 (1,"Australia – Rome",None,"Fly to Rome.","Fly to Rome; some departures arrive the next day.","","",""),
 (2,"Arrive in Rome","Rome","Make your own way to a central hotel.","Arrive and make your own way (or take the optional private transfer) to a centrally located hotel.","","Hotel Diana Roof Garden or similar, Rome","Private airport transfer ($95 pp)"),
 (3,"Rome free day","Rome","A free day: Trevi Fountain, Colosseum, Spanish Steps.","A free day in the Eternal City; the Trevi Fountain, Colosseum and Spanish Steps are all walkable.","Breakfast","Hotel Diana Roof Garden or similar, Rome",""),
 (4,"Rome free day","Rome","A second free day: the Vatican and the Pantheon.","Another free day; St Peter's, the Sistine Chapel and the Pantheon are the obvious picks.","Breakfast","Hotel Diana Roof Garden or similar, Rome",""),
 (5,"Embark at Civitavecchia","Civitavecchia","Make your own way to the port; sail at 3pm.","Free morning, then make your own way 75 km to Civitavecchia to board Royal Caribbean's Odyssey of the Seas, departing 3pm.","Breakfast, dinner","Odyssey of the Seas","Private transfer hotel to port ($245 pp)"),
 (6,"At sea","Santorini","A day at sea.","A day at sea on a Quantum Ultra-class ship: pools, the North Star capsule, FlowRider and 15-plus dining venues.","All meals on board","Odyssey of the Seas",""),
 (7,"Santorini","Santorini","Whitewashed villages above the caldera, 9am to 11pm.","A long tender day on Santorini: cable car to Fira, Oia's blue domes, black-sand beaches or the Akrotiri excavations.","All meals on board","Odyssey of the Seas","Royal Beach Club Santorini"),
 (8,"Kuşadası (Ephesus)","Kuşadası","Türkiye's coast and the ruins of Ephesus, 9am to 7pm.","Docked in Kuşadası; the ruins of Ephesus with its Great Theatre and Library of Celsus are a short excursion away.","All meals on board","Odyssey of the Seas","Ephesus shore excursion"),
 (9,"Mykonos","Mykonos","The Island of the Winds, 7am to 5pm.","A tender day on Mykonos: Chora's white lanes, the windmills and Little Venice.","All meals on board","Odyssey of the Seas",""),
 (10,"At sea","Naples","A day at sea.","A day at sea heading west.","All meals on board","Odyssey of the Seas",""),
 (11,"Naples","Naples","Pizza, palaces and Vesuvius, 7am to 6pm.","A day in Naples: the Royal Palace, the Sanità district, or excursions to Pompeii and the Amalfi Coast.","All meals on board","Odyssey of the Seas",""),
 (12,"Disembark – Rome – Australia","Civitavecchia","Disembark 5am and make your own way to the airport.","Disembark at Civitavecchia after breakfast and make your own way about 65 km to Rome Fiumicino for the flight home.","Breakfast on board","","Private transfer port to airport ($215 pp)"),
 (13,"Arrive Australia",None,"","Welcome home.","","","")]
IMAGES[6371] = [("6371_Italy_Turkiye_and_Greek_Islands_Cruise_WEB_HERO_1.jpg","Royal Caribbean's Odyssey of the Seas"),("6371_Italy_Turkiye_and_Greek_Islands_Cruise_WEB_HERO_2_Santorini.jpg","Santorini"),
 ("6371_Italy_Turkiye_and_Greek_Islands_Cruise_WEB_HERO_3_Rome.jpg","Rome at leisure"),("6371_Italy_Turkiye_and_Greek_Islands_Cruise_WEB_HERO_4_Ephasus.jpg","The ruins of Ephesus near Kuşadası"),
 ("PUBS+LIBRARY/1+-+Destinations/EUROPE+-+SOUTHERN/ITALY/G-Italy-Rome-Food-Drink-AS.jpg","Italian food in Rome")]

# ---------------- 6181 Japan Explorer Cruise (Itinerary 1) ----------------
G_EXTRA.update({"Yokohama":(139.64,35.44),"Hakodate":(140.73,41.77),"Niigata":(139.02,37.92),"Kochi":(133.53,33.56),"Shimizu":(138.49,35.02)})
STOPS[6181] = [("Tokyo",3,"Three nights at leisure","flight"),("Yokohama",0,"Own way to the port; embark Diamond Princess"),("Hakodate",2,"Day at sea, then Hakodate","cruise"),
               ("Niigata",1,"Sake country","cruise"),("Busan",2,"Day at sea, then Busan","cruise"),("Nagasaki",1,"","cruise"),("Kagoshima",1,"Sakurajima volcano","cruise"),
               ("Kochi",1,"Castle town on Shikoku","cruise"),("Shimizu",1,"Port for Mt Fuji","cruise"),("Yokohama",0,"Disembark 6:30am; own way to the airport","cruise")]
DEST[6181] = (["Tokyo","Hakodate","Niigata","Busan","Nagasaki","Kagoshima","Kochi","Shimizu"],["Japan","South Korea"])
DAYS[6181] = [
 (1,"Australia – Tokyo","Tokyo","Fly to Tokyo and make your own way to the hotel.","Fly to Tokyo; own way (or optional private transfer) to the Shinagawa Prince Hotel for three nights.","","Shinagawa Prince Hotel or similar, Tokyo","Private airport transfer ($159 pp)"),
 (2,"Tokyo free day","Tokyo","A free day in Tokyo.","A free day: Shibuya, Senso-ji, Tsukiji, the Imperial Palace gardens.","","Shinagawa Prince Hotel or similar, Tokyo",""),
 (3,"Tokyo free day","Tokyo","A second free day.","Another free day; Ginza and the Imperial Palace are close by.","","Shinagawa Prince Hotel or similar, Tokyo",""),
 (4,"Embark at Yokohama","Yokohama","Make your own way to the port; sail at 3pm.","Free morning, then make your own way to the Yokohama cruise terminal to board Diamond Princess, sailing at 3pm.","Dinner","Diamond Princess","Private transfer hotel to port ($149 pp)"),
 (5,"At sea","Hakodate","A day at sea heading north.","A day at sea; the Izumi Japanese bath is the largest of its kind afloat.","All meals on board","Diamond Princess",""),
 (6,"Hakodate","Hakodate","Hokkaido's historic port, 7am to 4pm.","Hakodate's Motomachi district of Western-style houses, the star-shaped Goryokaku fort and the Morning Market's sea urchin and crab.","All meals on board","Diamond Princess",""),
 (7,"Niigata","Niigata","Rice, sake and craftsmanship, 9am to 6pm.","Niigata, Japan's sake heartland on the Sea of Japan; the Suwada open factory and Yahiko Shrine are nearby.","All meals on board","Diamond Princess",""),
 (8,"At sea","Busan","A day at sea across the Sea of Japan.","A day at sea towards Korea.","All meals on board","Diamond Princess",""),
 (9,"Busan, South Korea","Busan","Korea's second city, 7am to 4pm.","Busan: Yongdusan Park, the Haedong Yonggungsa seaside temple, Gamcheon Culture Village and the UN Memorial Cemetery.","All meals on board","Diamond Princess",""),
 (10,"Nagasaki","Nagasaki","The 'San Francisco of Japan', 7am to 4pm.","Nagasaki's Peace Park and Atomic Bomb Museum, and the hillside city that was Japan's only window on the world for two centuries.","All meals on board","Diamond Princess",""),
 (11,"Kagoshima","Kagoshima","Samurai history and the Sakurajima volcano, 7am to 4pm.","Kagoshima, stronghold of the Shimazu clan, facing the smoking cone of Sakurajima across the bay; hot springs all around.","All meals on board","Diamond Princess",""),
 (12,"Kochi","Kochi","Shikoku's castle town, 9am to 5pm.","Kochi and its 1611 castle, Sakamoto Ryoma's home town, with a subtropical coast beyond.","All meals on board","Diamond Princess",""),
 (13,"Shimizu (for Mt Fuji)","Shimizu","Port for Mt Fuji, 1pm to 7pm.","Shimizu Port, about 13 km from Shizuoka and 75 km from the Mt Fuji viewing stations; shore excursions available.","All meals on board","Diamond Princess",""),
 (14,"Yokohama – Australia","Yokohama","Disembark 6:30am and make your own way to the airport.","Disembark at Yokohama after breakfast and make your own way to the airport.","Breakfast on board","","Shuttle to airport ($135 pp)"),
 (15,"Arrive Australia",None,"","Welcome home.","","","")]
IMAGES[6181] = [("6181_Japan_Explorer_Cruise_WEB_HERO_1_Park_Tokyo_Autumn_Generic.jpg","Tokyo at leisure"),("6181_Japan_Explorer_Cruise_WEB_HERO_2_Busan_Haedong_Yonggungsa_Temple.jpg","Haedong Yonggungsa Temple, Busan"),
 ("6181_Japan_Explorer_Cruise_WEB_HERO_3.jpg","Princess Cruises' Diamond Princess"),("6181_Japan_Explorer_Cruise_WEB_HERO_4_Tokyo_SensojiTemple.jpg","Senso-ji, Tokyo"),
 ("PUBS+LIBRARY/1+-+Destinations/ASIA+-+EAST+%26+SOUTHEAST/JAPAN/G-Japan-Cuisine-TraditionalFoodMarket-AS.jpg","A traditional food market")]

# ---------------- 6112 Iconic Northern Lights Rail & Sail (Itinerary 3, 16 days) ----------------
G_EXTRA.update({"Saariselkä":(27.42,68.42),"Inari":(27.03,68.91),"Kirkenes":(30.05,69.73),"Berlevåg":(29.09,70.86),"Tromsø":(18.96,69.65),"Svolvær":(14.57,68.23),"Brønnøysund":(12.21,65.47),"Trondheim":(10.4,63.43),"Bergen":(5.32,60.39),"Flåm":(7.11,60.86),"Oslo":(10.75,59.91),"Helsinki":(24.94,60.17),"Rovaniemi":(25.72,66.5)})
STOPS[6112] = [("Helsinki",1,"Arrive; welcome dinner","flight"),("Rovaniemi",2,"Train north across the Arctic Circle; husky day","rail"),("Saariselkä",1,"Santa Claus Village; glass igloo"),
               ("Inari",0,"SIIDA Sami museum"),("Kirkenes",1,"Snow Resort, king crab; Gamme cabin"),("Berlevåg",1,"Embark Hurtigruten; Vardø, Båtsfjord","cruise"),("Tromsø",1,"Honningsvåg, Hammerfest; Arctic Cathedral","cruise"),
               ("Svolvær",1,"Lofoten and Vesterålen, Trollfjord","cruise"),("Brønnøysund",1,"Cross the Arctic Circle; Torghatten","cruise"),("Trondheim",1,"Nidaros Cathedral","cruise"),("Bergen",1,"Disembark; city tour, Fløibanen","cruise"),
               ("Flåm",1,"Train to Voss, coach, Nærøyfjord ferry","rail"),("Oslo",1,"Flåm Railway to Myrdal, train to Oslo; farewell dinner","rail")]
DEST[6112] = (["Helsinki","Rovaniemi","Saariselkä","Kirkenes","Tromsø","Lofoten","Bergen","Flåm","Oslo"],["Finland","Norway"])
DAYS[6112] = [
 (1,"Australia – Helsinki",None,"Fly to Helsinki.","Fly to Helsinki; make your own way to the airport.","","",""),
 (2,"Arrive in Helsinki","Helsinki","Make your own way to the hotel; welcome dinner.","Arrive in Helsinki, make your own way to the hotel (luggage storage for early arrivals), free afternoon and a welcome dinner with the group.","Dinner","Radisson Blu Plaza or similar, Helsinki","Private airport transfer"),
 (3,"Train to Rovaniemi","Rovaniemi","Rail north into Finnish Lapland.","A short walk to the station and the train north through snowy forests to Rovaniemi, capital of Finnish Lapland, above the Arctic Circle. Afternoon free.","Breakfast","Original Sokos Vaakuna or similar, Rovaniemi",""),
 (4,"Husky experience","Rovaniemi","A husky kennel and a sled or cart ride.","Meet the dogs at a husky kennel, light lunch, then a husky-drawn sled (or cart) ride through the wilderness. Evening free.","Breakfast, lunch","Original Sokos Vaakuna or similar, Rovaniemi",""),
 (5,"Santa Claus Village – Saariselkä","Saariselkä","Santa's village, then a glass igloo night.","A morning at Santa Claus Village, then north via Sodankylä's old church to Saariselkä. Meet a reindeer herder, dinner, and a night in an Aurora Cabin with a glass roof, far from any light pollution.","Breakfast, dinner","Northern Lights Village Aurora Cabin, Saariselkä",""),
 (6,"Inari – Kirkenes, Norway","Kirkenes","The Sami museum, then a king crab lunch at the Snow Resort.","Stop at Inari's SIIDA Sami museum, cross into Norway to the Snow Resort Kirkenes: reindeer, huskies, a king crab presentation on the pier and a crab lunch, then a night in a Gamme cabin.","Breakfast, lunch, dinner","Snow Resort Kirkenes, Gamme cabin",""),
 (7,"Embark Hurtigruten – Vardø – Berlevåg","Berlevåg","Board the Coastal Express in the Arctic.","Board the Hurtigruten Coastal Express at Kirkenes. Vardø's star fort, then Båtsfjord and Berlevåg on the Barents Sea; an overnight stop at Mehamn with an optional snowmobile ride.","All meals on board","Hurtigruten Coastal Express","Snowmobile in the polar night (15 Dec–30 Apr)"),
 (8,"Honningsvåg – Hammerfest – Tromsø","Tromsø","Along the top of Norway to Tromsø.","Honningsvåg, gateway to the North Cape, then Hammerfest's Meridian Column, arriving in Tromsø late in the evening.","All meals on board","Hurtigruten Coastal Express","Midnight concert in Tromsø's Arctic Cathedral"),
 (9,"Lofoten & Vesterålen","Svolvær","The Lofoten Wall and the Trollfjord.","Harstad, the Risøyrenna channel, Stokmarknes where Hurtigruten began, then the narrow Raftsund and (conditions permitting) the Trollfjord between thousand-metre cliffs.","All meals on board","Hurtigruten Coastal Express","A Taste of Vesterålen"),
 (10,"Brønnøysund","Brønnøysund","Cross the Arctic Circle heading south.","Cross the Arctic Circle (cod liver oil optional), then the Helgeland coast: Torghatten with its hole and the Seven Sisters range.","All meals on board","Hurtigruten Coastal Express",""),
 (11,"Trondheim","Trondheim","Norway's first capital.","Time in Trondheim for Nidaros Cathedral, the cafés of Bakklandet and Kristiansten Fort; overnight calls at Kristiansund, Ålesund and Måløy.","All meals on board","Hurtigruten Coastal Express",""),
 (12,"Bergen, disembark","Bergen","Nordfjord and Sognefjord, then a Bergen city tour.","Past the Jostedal Glacier and across the mouth of the Sognefjord to Bergen. Disembark for a tour of the UNESCO-listed Bryggen, St Mary's Church and Håkon's Hall, and the Fløibanen funicular up Mount Fløyen.","Breakfast, lunch, dinner","Clarion Admiral Hotel or similar, Bergen",""),
 (13,"Bergen – Nærøyfjord – Flåm","Flåm","Train, coach and fjord ferry to Flåm.","The 'Norway in a Nutshell' route: train to Voss, coach past waterfalls to Gudvangen, ferry along the narrow UNESCO-listed Nærøyfjord to the village of Flåm.","Breakfast, lunch, dinner","Fretheim Hotel or similar, Flåm",""),
 (14,"Flåm Railway – Oslo","Oslo","One of the world's great rail journeys, then Oslo.","The Flåm Railway climbs 900 m to Myrdal, then the main line east to Oslo. Farewell dinner at the hotel.","Breakfast, lunch, dinner","Thon Hotel Opera or similar, Oslo",""),
 (15,"Oslo – Australia","Oslo","Make your own way to the airport.","Make your own way to Oslo airport for the flight home.","Breakfast","","Private airport transfer"),
 (16,"Arrive Australia",None,"","Arrive home.","","","")]
IMAGES[6112] = [("6112_Iconic_Northern_Lights_Rail_and_Sail_26-27_WEB_HERO_1.jpg","A Hurtigruten Coastal Express voyage"),("6112_Iconic_Northern_Lights_Rail_and_Sail_26-27_WEB_HERO_2_Igloos.jpg","A night in a glass igloo"),
 ("6112_Iconic_Northern_Lights_Rail_and_Sail_26-27_WEB_HERO_3_Rovaniemi.jpg","Husky safari in Lapland"),("6112_Iconic_Northern_Lights_Rail_and_Sail_26-27_WEB_HERO_4_Hamnoy.jpg","The Lofoten Islands"),
 ("PUBS+LIBRARY/1+-+Destinations/EUROPE+-+NORTHERN+%26+WESTERN/FINLAND/G-Finland-Helsinki-WaterfrontHelsinkiCathedral-AS.jpeg.jpg","Helsinki's waterfront")]

# ---------------- 6370 Singapore, Malaysia & Thailand Getaway ----------------
STOPS[6370] = [("Singapore",3,"Three nights at leisure; embark Royal Caribbean","flight"),("Penang",1,"George Town, 2:30pm to 9pm","cruise"),("Phuket",2,"Port day, then day at sea","cruise"),("Singapore",0,"Disembark 7am, own way to the airport","cruise")]
DEST[6370] = (["Singapore","Penang","Phuket"],["Singapore","Malaysia","Thailand"])
DAYS[6370] = [
 (1,"Australia – Singapore","Singapore","Fly to Singapore and make your own way to the hotel.","Fly to Singapore; make your own way (or take the optional private transfer) to the hotel.","","Copthorne King's Hotel or similar, Singapore","Private airport transfer ($70 pp)"),
 (2,"Singapore free day","Singapore","Gardens by the Bay, Chinatown, Little India, Orchard Road.","A free day: the Merlion, Gardens by the Bay's Cloud Forest, Chinatown and Little India, Orchard Road, and a hawker centre for chicken rice or laksa.","","Copthorne King's Hotel or similar, Singapore",""),
 (3,"Singapore free day","Singapore","A second free day.","Another free day in Singapore.","","Copthorne King's Hotel or similar, Singapore",""),
 (4,"Embark","Singapore","Board your Royal Caribbean ship; sail at 4pm.","Make your own way to the cruise terminal to board Navigator of the Seas (Jan–Mar) or Quantum of the Seas (from Oct), sailing at 4pm.","Dinner","Royal Caribbean ship",""),
 (5,"Penang, Malaysia","Penang","George Town's UNESCO zone, 2:30pm to 9pm.","Walk from the port into George Town's heritage zone: Fort Cornwallis, the Goddess of Mercy temple, or the funicular up Penang Hill and Batu Ferringhi beach.","All meals on board","Royal Caribbean ship",""),
 (6,"Phuket, Thailand","Phuket","Beaches, elephants and James Bond Island, 8am to 8pm.","A tender day in Phuket: Kata Noi beach, the elephant sanctuary, Monkey Hill or a boat to James Bond Island in Phang Nga Bay.","All meals on board","Royal Caribbean ship",""),
 (7,"At sea","Phuket","A day at sea in the Strait of Malacca.","A day at sea: the FlowRider, waterslides, North Star or RipCord depending on the ship.","All meals on board","Royal Caribbean ship",""),
 (8,"Disembark – Australia","Singapore","Disembark 7am and make your own way to the airport.","Disembark in Singapore after breakfast and make your own way to the airport.","Breakfast on board","","Private transfer port to airport ($70 pp)"),
 (9,"Arrive Australia",None,"","Welcome home.","","","")]
IMAGES[6370] = [("6370_Singapore_Malaysia_and_Thailand_Getaway_Cruise_WEB_HERO_1_Singapore.jpg","Gardens by the Bay, Singapore"),("6370_Singapore_Malaysia_and_Thailand_Getaway_Cruise_WEB_HERO_2_Phuket_Kata-Noi.jpg","Kata Noi beach, Phuket"),
 ("6370_Singapore_Malaysia_and_Thailand_Getaway_Cruise_WEB_HERO_3.jpg","Your Royal Caribbean ship"),("6370_Singapore_Malaysia_and_Thailand_Getaway_Cruise_WEB_HERO_4_Penang.jpg","Penang, Malaysia"),
 ("PUBS+LIBRARY/1+-+Destinations/ASIA+-+EAST+%26+SOUTHEAST/SINGAPORE/G-Singapore-DayCityView-AS-.jpg","Singapore skyline")]

# ---------------- 6369 Japan to Taiwan & Hong Kong Cruise ----------------
G_EXTRA.update({"Miyazaki":(131.42,31.91),"Keelung":(121.74,25.13)})
STOPS[6369] = [("Tokyo",3,"Three nights at leisure; embark Spectrum of the Seas","flight"),("Osaka",2,"Overnight in port; gateway to Kyoto","cruise"),("Miyazaki",1,"Aoshima, Udo shrine, Obi","cruise"),
               ("Kagoshima",1,"Sengan-en, Shiroyama lookout","cruise"),("Keelung",2,"Day at sea, then Keelung for Taipei and Jiufen","cruise"),("Hong Kong",3,"Day at sea, disembark; two nights at leisure","cruise")]
DEST[6369] = (["Tokyo","Osaka","Kyoto","Miyazaki","Kagoshima","Taipei","Hong Kong"],["Japan","Taiwan","Hong Kong"])
DAYS[6369] = [
 (1,"Australia – Tokyo","Tokyo","Fly to Tokyo and make your own way to the hotel.","Fly to Tokyo; own way (or optional private transfer) to the Shinagawa Prince Hotel for three nights.","","Shinagawa Prince Hotel or similar, Tokyo","Private airport transfer"),
 (2,"Tokyo free day","Tokyo","A free day in Tokyo.","A free day: neon districts, temples, the Imperial Palace gardens.","","Shinagawa Prince Hotel or similar, Tokyo",""),
 (3,"Tokyo free day","Tokyo","A second free day.","Another free day; Ginza and the Imperial Palace are close.","","Shinagawa Prince Hotel or similar, Tokyo",""),
 (4,"Embark in Tokyo","Tokyo","Board Spectrum of the Seas; sail at 5pm.","Make your own way to the cruise terminal and board Royal Caribbean's Spectrum of the Seas, sailing at 5pm.","Dinner","Spectrum of the Seas","Private transfer hotel to port"),
 (5,"Osaka (for Kyoto), overnight in port","Osaka","Arrive 3pm; the ship stays overnight.","Dock in Osaka mid-afternoon with the ship overnight in port, so Kyoto's Fushimi Inari, Nishiki Market and Kyoto Tower are 30 minutes away by train.","All meals on board","Spectrum of the Seas",""),
 (6,"Osaka","Osaka","A second day; sail at 3pm.","A morning in Osaka's Shinsaibashi and Dotonbori districts before sailing at 3pm.","All meals on board","Spectrum of the Seas",""),
 (7,"Miyazaki (Aburatsu)","Miyazaki","Beaches, a seaside shrine and a samurai town, 9am to 7pm.","Aoshima Beach, the cliffside Udo Shrine, the samurai town of Obi and Miyazaki wagyu.","All meals on board","Spectrum of the Seas",""),
 (8,"Kagoshima","Kagoshima","Samurai gardens and the volcano, 8am to 7pm.","The Sengan-en samurai garden overlooking the bay, kurobuta pork, and the view of Sakurajima from Shiroyama Lookout.","All meals on board","Spectrum of the Seas",""),
 (9,"At sea","Keelung","A day at sea.","A day at sea heading south-west to Taiwan.","All meals on board","Spectrum of the Seas",""),
 (10,"Keelung (for Taipei), Taiwan","Keelung","Taipei's Longshan Temple and the lanes of Jiufen, 7am to 7pm.","Into Taipei for the 1600s Longshan Temple, then the hillside teahouses and lanes of Jiufen above the bay.","All meals on board","Spectrum of the Seas",""),
 (11,"At sea","Hong Kong","A day at sea.","A day at sea towards Hong Kong.","All meals on board","Spectrum of the Seas",""),
 (12,"Disembark in Hong Kong","Hong Kong","Arrive 6:30am; make your own way to the hotel.","Disembark in Hong Kong after breakfast and make your own way to the hotel in Kowloon. Rest of the day free.","Breakfast on board","New World Millennium or similar, Hong Kong",""),
 (13,"Hong Kong free day","Hong Kong","A free day in Hong Kong.","A free day: the Peak, the Star Ferry, Wong Tai Sin Temple, Nan Lian Garden and 60-plus Michelin-starred restaurants.","","New World Millennium or similar, Hong Kong",""),
 (14,"Hong Kong – Australia","Hong Kong","Make your own way to the airport.","Make your own way to the airport for the flight home.","","","Private transfer hotel to airport"),
 (15,"Arrive Australia",None,"","Welcome home.","","","")]
IMAGES[6369] = [("6369_Japan_to_Taiwan_and_Hong_Kong_Cruise_WEB_HERO_1_HK.jpg","Hong Kong at leisure"),("6369_Japan_to_Taiwan_and_Hong_Kong_Cruise_WEB_HERO_2_Tokyo_Akihabara.jpg","Akihabara, Tokyo"),
 ("6369_Japan_to_Taiwan_and_Hong_Kong_Cruise_WEB_HERO_3_Spectrum.jpg","Royal Caribbean's Spectrum of the Seas"),("6369_Japan_to_Taiwan_and_Hong_Kong_Cruise_WEB_HERO_4_Teipei_Jiufen.jpg","Teahouses of Jiufen, near Taipei"),
 ("PUBS+LIBRARY/1+-+Destinations/ASIA+-+EAST+%26+SOUTHEAST/JAPAN/5600-all-inclusive-japan-south-korea-cruise-ADOBS-tokyo5.jpg","Traditional Japanese food")]
