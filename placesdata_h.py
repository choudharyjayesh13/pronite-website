# -*- coding: utf-8 -*-
"""Places batch H — EAST INDIA, KERALA & THE HILLS.
Kolkata, Varanasi, Kerala (backwaters/hills/Kochi), Rishikesh, Shimla, Manali, Darjeeling.
New categories: Hill Station, Backwaters."""
POSTS = []
def P(**k): POSTS.append(k)

# ======================= KOLKATA =======================

P(slug="victoria-memorial-kolkata", city="Kolkata", region="West Bengal", cat="Landmark",
  name="Victoria Memorial", query="Victoria Memorial Kolkata",
  excerpt="A gleaming white-marble palace-museum set in gardens — Kolkata's grandest monument and a symbol of the city.",
  tags=["Kolkata","colonial","museum","landmark"],
  info=dict(timings="Gardens from early morning; museum ~10 AM – 5 PM (closed Mondays)", entry="Approx ₹30 (Indian) / ₹500 (foreign)",
            best="Late afternoon; evening for the light show", duration="1.5–2 hours", reach="Central Kolkata, near the Maidan"),
  body="""<p>The Victoria Memorial is Kolkata's most iconic landmark — a majestic domed palace of white Makrana marble, built in the early 20th century and set within manicured gardens on the edge of the vast Maidan. Part memorial, part museum, it's a serene and stately symbol of the city.</p>
<p>Inside, galleries trace the history of Kolkata and the colonial era through paintings, sculptures, manuscripts and artefacts. The building, floodlit at night and mirrored in its reflecting pools, is genuinely beautiful — and the gardens are a favourite local escape.</p>
<h2>Don't miss</h2>
<ul><li>The marble memorial and its dome, especially floodlit at dusk.</li><li>The history and art galleries inside.</li><li>The gardens and reflecting pools, and the evening light-and-sound show.</li></ul>
<h2>Good to know</h2>
<p>The museum is closed on Mondays; the gardens open earlier and are lovely for a stroll. Combine with St Paul's Cathedral and the Maidan nearby.</p>""")

P(slug="howrah-bridge-kolkata", city="Kolkata", region="West Bengal", cat="Landmark",
  name="Howrah Bridge", query="Howrah Bridge Kolkata",
  excerpt="The mighty cantilever bridge over the Hooghly — an engineering icon and the thundering, unforgettable gateway to Kolkata.",
  tags=["Kolkata","bridge","icon","river"],
  info=dict(timings="Open 24 hours (photography of the bridge itself is restricted)", entry="Free",
            best="Early morning at the flower market below; sunset from a river ferry", duration="1 hour", reach="Over the Hooghly, linking Kolkata and Howrah"),
  body="""<p>Few structures embody a city like the Howrah Bridge embodies Kolkata. This colossal steel cantilever bridge, opened in 1943, spans the Hooghly River without a single nut or bolt in its main span — held together entirely by rivets — and carries a staggering torrent of pedestrians, vehicles and hand-carts every day.</p>
<p>The best way to experience it is from below and around: the frenetic Mullick Ghat flower market at dawn beneath its girders, and a ride on one of the river ferries that offer the classic view of the bridge silhouetted against the sky.</p>
<h2>Don't miss</h2>
<ul><li>The dawn flower market (Mullick Ghat) beneath the bridge.</li><li>A Hooghly ferry ride for the classic bridge view.</li><li>The sheer human energy crossing it at rush hour.</li></ul>
<h2>Good to know</h2>
<p>Photography of the bridge itself is officially restricted (it's a key installation) — shoot from the ferries and ghats instead. The flower market is a photographer's dream at first light.</p>""")

P(slug="park-street-kolkata", city="Kolkata", region="West Bengal", cat="Nightlife",
  name="Park Street", query="Park Street Kolkata",
  excerpt="Kolkata's legendary avenue of live music, old-world restaurants and nightlife — the soul of the city's love of a good time.",
  tags=["Kolkata","nightlife","live music","food"],
  info=dict(timings="Restaurants & bars from midday till late", entry="Free to stroll; venues priced individually",
            best="Evening; Christmas–New Year is magical", duration="An evening", reach="Central Kolkata"),
  body="""<p>Park Street (officially Mother Teresa Sarani) has been the epicentre of Kolkata's nightlife and dining for generations. This is the city with a genuine live-music soul, and Park Street is where that heritage lives — in storied restaurants, jazz-era institutions and bars that have been pouring drinks and playing music for decades.</p>
<p>By day it's lined with cafés, bookshops and eateries; by night it glows with neon and buzzes with diners and revellers. At Christmas and New Year, Park Street erupts into a citywide festival of lights and celebration that's unlike anywhere else in India.</p>
<h2>Don't miss</h2>
<ul><li>The heritage restaurants and live-music institutions.</li><li>The Christmas–New Year illuminations and street festivities.</li><li>Old-school Anglo-Indian and Continental cuisine.</li></ul>
<h2>Good to know</h2>
<p>The Christmas-to-New-Year stretch is the most magical (and crowded) time. Kolkata's warmth and unpretentiousness make this one of India's most soulful nights out.</p>""")

P(slug="dakshineswar-temple-kolkata", city="Kolkata", region="West Bengal", cat="Temple",
  name="Dakshineswar Kali Temple", query="Dakshineswar Kali Temple",
  excerpt="A magnificent riverside temple complex dedicated to goddess Kali — a major pilgrimage site with deep spiritual history.",
  tags=["Kolkata","temple","Kali","pilgrimage"],
  info=dict(timings="Approx 6 AM – 12:30 PM & 3 PM – 8:30 PM", entry="Free",
            best="Early morning to avoid crowds", duration="1–1.5 hours", reach="On the Hooghly, ~12 km north of central Kolkata"),
  body="""<p>On the banks of the Hooghly north of the city, the Dakshineswar Kali Temple is one of the most important religious sites in Bengal. Built in 1855, its striking nine-spired main temple is dedicated to the goddess Kali and is surrounded by a courtyard of twelve identical Shiva temples.</p>
<p>The temple is deeply associated with the revered 19th-century mystic Ramakrishna Paramahamsa, who served as a priest here, and it draws a constant stream of devotees. The riverside setting and the grand architecture make it moving to visit even for the non-religious.</p>
<h2>Don't miss</h2>
<ul><li>The nine-spired main Kali temple.</li><li>The row of twelve Shiva shrines along the river.</li><li>The room associated with Sri Ramakrishna.</li></ul>
<h2>Good to know</h2>
<p>It gets very busy, especially on Kali Puja and weekends — go early. Leave shoes and cameras as directed; dress modestly. The Belur Math (Ramakrishna Mission HQ) sits across the river.</p>""")

P(slug="new-market-kolkata", city="Kolkata", region="West Bengal", cat="Street & Bazaar",
  name="New Market (Hogg Market)", query="New Market Kolkata Hogg",
  excerpt="Kolkata's grand old covered bazaar — a warren of hundreds of shops selling everything, wrapped in colonial-era character.",
  tags=["Kolkata","market","shopping","heritage"],
  info=dict(timings="Roughly 10 AM – 8 PM (Sundays limited)", entry="Free",
            best="Weekday; morning for produce, all day for shopping", duration="2 hours", reach="Central Kolkata, Lindsay Street"),
  body="""<p>Housed in a Victorian-Gothic building from 1874, New Market (officially Sir Stuart Hogg Market) is Kolkata's most famous and characterful bazaar. Behind its red-brick clock tower lies a labyrinth of hundreds of stalls selling clothes, leather, jewellery, flowers, spices, meat, cheese and the city's beloved bakery treats.</p>
<p>It's a place with genuine old-world soul — porters in red shirts, century-old shops, and the famous Nahoum's bakery tucked inside. Chaotic and crammed, it's a wonderful window into everyday Kolkata and a great spot for gifts and snacks.</p>
<h2>Don't miss</h2>
<ul><li>Nahoum's, the legendary Jewish bakery inside the market.</li><li>The clothing, leather and jewellery bargains.</li><li>The flower and produce sections.</li></ul>
<h2>Good to know</h2>
<p>Porters and touts can be pushy — a polite firm no works. Bargain everywhere. It's most manageable on a weekday.</p>""")

# ======================= VARANASI =======================

P(slug="dashashwamedh-ghat-varanasi", city="Varanasi", region="Uttar Pradesh", cat="Lake & Ghat",
  name="Dashashwamedh Ghat & Ganga Aarti", query="Dashashwamedh Ghat Varanasi",
  excerpt="The spiritual epicentre of India's holiest city — where the spectacular nightly Ganga Aarti unfolds on the banks of the sacred river.",
  tags=["Varanasi","ghat","Ganga aarti","pilgrimage"],
  info=dict(timings="Ghats open all day; Ganga Aarti at dusk (arrive ~1 hr early)", entry="Free (boat rides charged)",
            best="Sunrise boat ride and the evening aarti", duration="2–3 hours", reach="Riverfront, old city of Varanasi"),
  body="""<p>Varanasi — Kashi, one of the oldest continuously inhabited cities on earth — is the spiritual heart of India, and Dashashwamedh is its principal ghat. Here, life and death, ritual and river, all meet on the banks of the sacred Ganga in a way that can be overwhelming and unforgettable.</p>
<p>Each evening, priests perform the Ganga Aarti — a mesmerising ceremony of fire, incense, bells and chanting offered to the river, watched by thousands from the steps and from boats on the water. At dawn, a boat ride past the ghats as the city wakes and bathes is equally profound.</p>
<h2>Don't miss</h2>
<ul><li>The spectacular evening Ganga Aarti.</li><li>A sunrise boat ride along the ghats.</li><li>The intense, layered life of the riverfront.</li></ul>
<h2>Good to know</h2>
<p>Arrive early for the aarti — a boat gives the best view. Be respectful, especially near the cremation ghats (photography there is not allowed). The old-city lanes are a maze — embrace getting lost.</p>""")

P(slug="kashi-vishwanath-varanasi", city="Varanasi", region="Uttar Pradesh", cat="Temple",
  name="Kashi Vishwanath Temple", query="Kashi Vishwanath Temple Varanasi",
  excerpt="One of the holiest Shiva temples in the world — the golden-spired heart of Varanasi, now set in a grand riverfront corridor.",
  tags=["Varanasi","temple","Shiva","pilgrimage"],
  info=dict(timings="Darshan from very early morning till night (multiple aartis)", entry="Free (special darshan passes available)",
            best="Early morning; weekdays", duration="1–2 hours (queues vary)", reach="Old city, near the ghats, Varanasi"),
  body="""<p>The Kashi Vishwanath Temple is one of the twelve Jyotirlingas, the most sacred shrines of Lord Shiva, and the spiritual anchor of Varanasi. Its gold-plated spire and dome — gilded with over 750 kg of gold — rise above the old city, drawing millions of pilgrims each year.</p>
<p>Recently, the temple has been reconnected to the Ganga by the grand Kashi Vishwanath Corridor, a sweeping riverfront complex that has transformed access to the shrine. The devotion here is intense and the atmosphere electric.</p>
<h2>Don't miss</h2>
<ul><li>The golden-spired main shrine.</li><li>The new Kashi Vishwanath Corridor linking temple to river.</li><li>The charged atmosphere of the aartis.</li></ul>
<h2>Good to know</h2>
<p>Security is strict — phones and bags are usually not allowed inside (lockers available). Queues can be long; special-darshan passes speed entry. Dress modestly.</p>""")

P(slug="sarnath-varanasi", city="Sarnath", region="Uttar Pradesh", cat="Landmark",
  name="Sarnath", query="Sarnath Dhamek Stupa",
  excerpt="Where the Buddha gave his first sermon — a serene Buddhist pilgrimage site of ancient stupas, ruins and a fine museum.",
  tags=["Buddhism","pilgrimage","history","stupa"],
  info=dict(timings="Site sunrise–sunset; museum ~9 AM – 5 PM (closed Fridays)", entry="Approx ₹25 (Indian) / ₹300 (foreign)",
            best="Morning; a calm contrast to Varanasi", duration="2 hours", reach="~10 km from Varanasi"),
  body="""<p>Just outside the intensity of Varanasi lies one of the most sacred sites in Buddhism. It was at Sarnath that the Buddha, after attaining enlightenment, delivered his first sermon and set in motion the 'Wheel of Dharma'. The site is calm, green and deeply peaceful.</p>
<p>The great Dhamek Stupa, dating to the Gupta era, dominates the ruins of ancient monasteries and temples, and the excellent archaeological museum houses the original Lion Capital of Ashoka — the sculpture that became India's national emblem.</p>
<h2>Don't miss</h2>
<ul><li>The massive Dhamek Stupa.</li><li>The Lion Capital of Ashoka in the museum (India's national emblem).</li><li>The peaceful monastery ruins and modern temples.</li></ul>
<h2>Good to know</h2>
<p>The museum is closed on Fridays. It's a serene, reflective counterpoint to Varanasi's intensity — an easy and worthwhile half-day trip.</p>""")

# ======================= KERALA =======================

P(slug="alleppey-backwaters", city="Alappuzha", region="Kerala", cat="Backwaters",
  name="Alleppey Backwaters", query="Alleppey backwaters houseboat Kerala",
  excerpt="The 'Venice of the East' — a dreamy labyrinth of palm-fringed canals and lagoons best explored by traditional houseboat.",
  tags=["Kerala","backwaters","houseboat","nature"],
  info=dict(timings="Houseboat cruises usually noon to next-day morning", entry="Houseboat & shikara packages (varies widely)",
            best="November–February", duration="A day / overnight houseboat", reach="Alappuzha (Alleppey), coastal Kerala"),
  body="""<p>The Kerala backwaters are one of India's most magical landscapes — a serene, interconnected network of lakes, canals and rivers fringed by swaying coconut palms and emerald paddy fields. Alappuzha (Alleppey) is the gateway, and the classic way to experience them is aboard a kettuvallam, a traditional rice-barge converted into a houseboat.</p>
<p>Drifting slowly through the waterways, watching village life unfold on the banks, feasting on fresh Keralan seafood and mooring under the stars is one of the most relaxing experiences in the country. Smaller shikara canoe trips reach the narrower, quieter canals.</p>
<h2>Don't miss</h2>
<ul><li>An overnight houseboat cruise through the canals.</li><li>A shikara ride into the narrow village waterways.</li><li>Fresh Keralan cuisine cooked on board.</li></ul>
<h2>Good to know</h2>
<p>Book a reputable, well-maintained houseboat. Overnight cruises are the classic experience. The Nehru Trophy snake-boat race (usually August) is a spectacular time to visit.</p>""")

P(slug="munnar-kerala", city="Munnar", region="Kerala", cat="Hill Station",
  name="Munnar", query="Munnar tea plantations Kerala",
  excerpt="A hill station of endless rolling tea gardens, misty peaks and cool mountain air — the green jewel of Kerala's highlands.",
  tags=["Kerala","hill station","tea","nature"],
  info=dict(timings="Open destination; attractions ~9 AM – 5 PM", entry="Free town; individual attractions charge",
            best="September–March (avoid heavy monsoon)", duration="2–3 days", reach="Western Ghats, ~4 hrs from Kochi"),
  body="""<p>High in the Western Ghats, Munnar is Kerala at its most postcard-perfect — a landscape of endlessly rolling, manicured tea plantations, mist-wrapped peaks and cool, fragrant air. Once a British summer retreat, it remains one of South India's most beloved hill stations.</p>
<p>The green carpet of tea gardens is mesmerising, and there's plenty to do: visit a tea estate and museum, spot the rare Nilgiri tahr at Eravikulam National Park, chase waterfalls, and take in the views from Top Station. It's a refreshing, scenic escape from the coastal heat.</p>
<h2>Don't miss</h2>
<ul><li>The rolling tea plantations and a tea-estate visit.</li><li>Eravikulam National Park and the Nilgiri tahr.</li><li>The viewpoints at Top Station and Kolukkumalai.</li></ul>
<h2>Good to know</h2>
<p>Roads up are winding — allow time. The monsoon (June–Aug) is lush but wet and prone to landslides. Mornings are often misty and magical.</p>""")

P(slug="fort-kochi-kerala", city="Kochi", region="Kerala", cat="Landmark",
  name="Fort Kochi", query="Fort Kochi Chinese fishing nets",
  excerpt="A charming seaside quarter where Chinese fishing nets, colonial churches and spice-trade history meet a buzzing art scene.",
  tags=["Kerala","heritage","coast","art"],
  info=dict(timings="Wander any time; sites ~9 AM – 5 PM", entry="Free area; some sites charge",
            best="November–February; sunset by the fishing nets", duration="A day", reach="Kochi (Cochin), coastal Kerala"),
  body="""<p>Fort Kochi is one of India's most atmospheric coastal quarters — a laid-back peninsula where centuries of Portuguese, Dutch and British history layer over an ancient spice-trade port. Its streets of weathered colonial mansions, art cafés and boutiques invite slow, aimless wandering.</p>
<p>The signature sight is the row of giant cantilevered Chinese fishing nets on the waterfront, silhouetted at sunset. Add the historic St Francis Church, the Dutch Palace and the synagogue of nearby Jew Town, plus a thriving contemporary art scene (home to the Kochi-Muziris Biennale), and it's a uniquely cosmopolitan corner of Kerala.</p>
<h2>Don't miss</h2>
<ul><li>The iconic Chinese fishing nets at sunset.</li><li>St Francis Church and the Mattancherry (Dutch) Palace.</li><li>Jew Town's antique shops and the Paradesi Synagogue.</li></ul>
<h2>Good to know</h2>
<p>It's best explored slowly on foot or by bicycle. If you visit during the Kochi-Muziris Biennale (art festival), allow extra time. A great base for a relaxed Kerala coast stay.</p>""")

# ======================= RISHIKESH & THE HILLS =======================

P(slug="rishikesh", city="Rishikesh", region="Uttarakhand", cat="Lake & Ghat",
  name="Rishikesh", query="Rishikesh Ganga aarti Laxman Jhula",
  excerpt="The 'Yoga Capital of the World' on the banks of the Ganga — riverside temples, iconic bridges, evening aarti and white-water rafting.",
  tags=["Rishikesh","yoga","Ganga","adventure"],
  info=dict(timings="Ghats & town always open; Ganga Aarti at dusk", entry="Free (activities charged)",
            best="September–November & February–April", duration="2–3 days", reach="Foothills of the Himalayas, Uttarakhand; ~1 hr from Haridwar"),
  body="""<p>Where the holy Ganga rushes out of the Himalayas onto the plains sits Rishikesh — a town that is at once a sacred pilgrimage centre, the self-styled 'Yoga Capital of the World', and India's white-water adventure hub. It's a heady, uplifting mix of the spiritual and the adrenaline-fuelled.</p>
<p>Suspension bridges (the famous Laxman Jhula and Ram Jhula) span the river between temples and ashrams; riverside ghats host a beautiful evening Ganga Aarti at Parmarth Niketan and Triveni Ghat; and by day, rafts tumble down the rapids. Add yoga retreats, cliff cafés and the Beatles Ashram, and it's utterly unique.</p>
<h2>Don't miss</h2>
<ul><li>The evening Ganga Aarti at the riverside ashrams.</li><li>White-water rafting on the Ganga.</li><li>The Laxman Jhula and Ram Jhula bridges, and a yoga class.</li></ul>
<h2>Good to know</h2>
<p>Rishikesh is a vegetarian, alcohol-free holy town. Rafting season runs roughly Sept–June (paused in peak monsoon). It draws a big international traveller crowd — book yoga/retreats ahead in season.</p>""")

P(slug="shimla-mall-road", city="Shimla", region="Himachal Pradesh", cat="Hill Station",
  name="Shimla & the Mall Road", query="Shimla Mall Road The Ridge",
  excerpt="The former summer capital of British India — a colonial-era hill station of pine slopes, the Ridge and a lively pedestrian Mall.",
  tags=["Shimla","hill station","colonial","Himalayas"],
  info=dict(timings="Town always open; shops on the Mall ~10 AM – 9 PM", entry="Free",
            best="March–June & September–November; snow in winter", duration="2–3 days", reach="Himachal Pradesh; the heritage toy train runs up from Kalka"),
  body="""<p>Once the summer capital of British India, Shimla remains the grande dame of Himalayan hill stations — a town of steep pine-clad slopes, colonial architecture and cool mountain air spread along a ridge at 2,200 metres. Reaching it aboard the UNESCO-listed Kalka–Shimla 'toy train' is half the fun.</p>
<p>Life centres on the Ridge and the pedestrianised Mall Road, lined with old-world shops, cafés and the mock-Tudor Gaiety Theatre, with the neo-Gothic Christ Church as its landmark. Around town, viewpoints like Jakhoo Hill and Kufri offer Himalayan panoramas.</p>
<h2>Don't miss</h2>
<ul><li>Strolling the Ridge and Mall Road.</li><li>The scenic Kalka–Shimla toy train ride.</li><li>Jakhoo Temple and the mountain viewpoints.</li></ul>
<h2>Good to know</h2>
<p>Peak summer and snow season get crowded. Much of the centre is pedestrian — expect to walk (and climb). Winters bring snow and a very different, magical feel.</p>""")

P(slug="manali-solang", city="Manali", region="Himachal Pradesh", cat="Hill Station",
  name="Manali & Solang Valley", query="Manali Solang Valley Himachal",
  excerpt="A Himalayan resort town of snow peaks, adventure sports and riverside charm — gateway to the high mountains and a backpacker favourite.",
  tags=["Manali","hill station","adventure","Himalayas"],
  info=dict(timings="Open destination; activities daytime", entry="Free town; activities & permits charged",
            best="March–June & October–February (snow)", duration="3–4 days", reach="Himachal Pradesh, ~10 hrs from Delhi by road"),
  body="""<p>Cradled in the Kullu Valley beside the rushing Beas River, Manali is one of India's most popular mountain getaways — a lively town backed by snow-capped Himalayan peaks, with a heady mix of honeymooners, backpackers, adventurers and pilgrims. It's the gateway to some of the country's most dramatic high-mountain routes.</p>
<p>Nearby Solang Valley is the adventure playground — paragliding, zorbing and skiing in winter — while the Rohtang Pass, old Manali's cafés, the Hadimba Temple and the hot springs at Vashisht round out the appeal. It's a base for spectacular road trips to Leh, Spiti and Lahaul.</p>
<h2>Don't miss</h2>
<ul><li>Adventure sports at Solang Valley.</li><li>The ancient wooden Hadimba Devi Temple.</li><li>Old Manali's cafés and the Vashisht hot springs.</li></ul>
<h2>Good to know</h2>
<p>The Rohtang Pass and high roads need permits and are seasonal (often closed in winter). Peak season is busy — book ahead. A base for epic Himalayan road trips.</p>""")

P(slug="darjeeling", city="Darjeeling", region="West Bengal", cat="Hill Station",
  name="Darjeeling", query="Darjeeling Himalayan Railway",
  excerpt="The 'Queen of the Hills' — world-famous tea, a UNESCO toy train and sunrise views of mighty Kanchenjunga.",
  tags=["Darjeeling","hill station","tea","Himalayas"],
  info=dict(timings="Town always open; toy train & sites daytime", entry="Free town; toy train & attractions charged",
            best="October–November & March–May (clear mountain views)", duration="2–3 days", reach="Northern West Bengal, in the eastern Himalayas"),
  body="""<p>Perched in the eastern Himalayas, Darjeeling is a hill station like no other — the source of some of the world's most prized tea, and blessed with jaw-dropping views of Kanchenjunga, the third-highest mountain on earth. Its misty ridges, tea gardens and colonial charm have enchanted travellers for over a century.</p>
<p>The star attraction is the Darjeeling Himalayan Railway, a UNESCO World Heritage 'toy train' that puffs up the mountainside. Add a pre-dawn trip to Tiger Hill for the sunrise over Kanchenjunga, a visit to a working tea estate, and the vibrant local culture, and it's unforgettable.</p>
<h2>Don't miss</h2>
<ul><li>Sunrise over Kanchenjunga from Tiger Hill.</li><li>The UNESCO 'toy train' (Darjeeling Himalayan Railway).</li><li>A tea-estate tour and a fresh cup of Darjeeling first flush.</li></ul>
<h2>Good to know</h2>
<p>Mountain views depend on clear weather — spring and autumn are best. Tiger Hill sunrise means a very early, cold start. The toy train's shorter 'joy rides' are easy to book on the day.</p>""")
