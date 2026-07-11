# -*- coding: utf-8 -*-
"""Places to Visit — Rajasthan travel guide. Consumed by fetch_place_photos.py + build_places.py.
Each P(...) is one place page. Photos are fetched from Wikimedia Commons (free-licensed, attributed)
using the `query` term. Fields:
  slug, city, region, cat, name, excerpt, body(HTML),
  info = dict(timings, entry, best, duration, reach),
  query (Commons search for photos), gallery (# extra gallery photos, default 3), tags(list)
Entry fees / timings are approximate and clearly labelled 'verify locally' in the UI."""
POSTS = []
def P(**k): POSTS.append(k)

# ============================================================
# UDAIPUR & MEWAR REGION
# ============================================================

P(slug="city-palace-udaipur", city="Udaipur", region="Mewar", cat="Palace & Fort",
  name="City Palace, Udaipur", query="City Palace Udaipur",
  excerpt="The largest royal palace complex in Rajasthan — a towering maze of courtyards, balconies and museums above Lake Pichola.",
  tags=["palace","Udaipur","heritage","museum"],
  info=dict(timings="9:30 AM – 5:30 PM (daily)", entry="Approx ₹300 (Indian) / ₹600 (foreign); museum & extra galleries priced separately",
            best="October–March; sunset for the lake views", duration="2–3 hours", reach="City centre, Old City Udaipur — walkable from Jagdish Temple & Lake Pichola ghats"),
  body="""<p>Rising in a wall of cream stone above Lake Pichola, the City Palace is the beating heart of Udaipur and the grandest palace complex in Rajasthan. Built and expanded over nearly four centuries by successive Maharanas of Mewar, it's less a single building than a small city of interconnected palaces, courtyards, terraces and towers.</p>
<p>Inside, the museum leads you through a dizzying sequence of mirror-work halls, peacock mosaics, painted chambers and balconies that frame postcard views of the lake and the Aravalli hills beyond. The higher you climb, the better the panorama — and at sunset, the whole complex glows.</p>
<h2>Don't miss</h2>
<ul><li>The Mor Chowk (Peacock Courtyard) and its glittering glass-mosaic peacocks.</li><li>The views over Lake Pichola, Jag Mandir and the Lake Palace from the upper terraces.</li><li>The Crystal Gallery at the adjoining Fateh Prakash Palace.</li></ul>
<h2>Good to know</h2>
<p>It's the busiest attraction in the city — go early to beat the crowds and the heat. The complex is large and involves plenty of stairs; wear comfortable shoes. Guides are available at the entrance and genuinely add to the visit.</p>""")

P(slug="lake-pichola", city="Udaipur", region="Mewar", cat="Lake & Ghat",
  name="Lake Pichola", query="Lake Pichola Udaipur",
  excerpt="The shimmering lake at the soul of the City of Lakes — ringed by palaces, ghats and the famous island Lake Palace.",
  tags=["lake","Udaipur","boat ride","sunset"],
  info=dict(timings="Open all day; boat rides typically 10 AM – sunset", entry="Free to view; boat rides approx ₹400–₹800 (sunset rides cost more)",
            best="Golden hour — the sunset boat ride is unmissable", duration="1–2 hours", reach="Old City Udaipur; board boats from Rameshwar Ghat inside City Palace"),
  body="""<p>Everything in Udaipur seems to orbit Lake Pichola. This 14th-century artificial lake is the reason the city is called the Venice of the East — its still waters mirror the palaces, ghats and hills that crowd its shores, and the view across it is one of the most photographed in India.</p>
<p>The classic way to experience it is a boat ride, ideally as the sun drops. You'll glide past the island palaces — the luxury Lake Palace hotel seeming to float on the water, and Jag Mandir with its domed pavilions — while the City Palace turns gold behind you.</p>
<h2>Don't miss</h2>
<ul><li>A sunset boat cruise with a stop at Jag Mandir island.</li><li>Ambrai Ghat and Lal Ghat for the best free lakeside views (and cafés).</li><li>The reflections at Gangaur Ghat, especially in the evening light.</li></ul>
<h2>Good to know</h2>
<p>Water levels are highest and the lake at its most beautiful after the monsoon (September onward). Boat rides run from within the City Palace complex and require a separate ticket.</p>""")

P(slug="jag-mandir", city="Udaipur", region="Mewar", cat="Palace & Fort",
  name="Jag Mandir", query="Jag Mandir Udaipur",
  excerpt="A 17th-century island palace of white marble and domes, floating on Lake Pichola — a serene escape reached only by boat.",
  tags=["palace","island","Udaipur","lake"],
  info=dict(timings="10 AM – 6 PM (via boat)", entry="Boat ride ticket applies (approx ₹400–₹800); garden entry included",
            best="Late afternoon into sunset", duration="1 hour", reach="Island on Lake Pichola — reached by boat from the City Palace jetty"),
  body="""<p>Set on its own island in Lake Pichola, Jag Mandir is a palace of white and yellow marble crowned by domes and guarded by a row of carved stone elephants. Built in the 17th century, it once sheltered a fleeing Mughal prince and, legend has it, inspired elements of the Taj Mahal's design.</p>
<p>Today it's a tranquil garden retreat — courtyards, a domed pavilion, fragrant trees and lake views on every side. Reached only by boat, it feels wonderfully removed from the bustle of the city.</p>
<h2>Don't miss</h2>
<ul><li>The Gul Mahal pavilion and the elephant statues at the entrance jetty.</li><li>The garden courtyard and its uninterrupted views back to the City Palace.</li><li>A coffee or meal at the island café as the sun sets.</li></ul>
<h2>Good to know</h2>
<p>Access is by boat from the City Palace complex; the ride is part of the experience. Combine it with a Lake Pichola cruise for the full effect.</p>""")

P(slug="fateh-sagar-lake", city="Udaipur", region="Mewar", cat="Lake & Ghat",
  name="Fateh Sagar Lake", query="Fateh Sagar Lake Udaipur",
  excerpt="Udaipur's breezy second lake, ringed by hills and dotted with islands — the local favourite for an evening out.",
  tags=["lake","Udaipur","boating","sunset"],
  info=dict(timings="Open all day; boating usually 9 AM – 6 PM", entry="Free; boating & Nehru Garden island approx ₹100–₹300",
            best="Evening, for the breeze and sunset", duration="1–2 hours", reach="~4 km from the Old City; easy by auto or taxi"),
  body="""<p>If Lake Pichola is Udaipur's showpiece, Fateh Sagar is its living room — the lake where locals come to walk, snack and watch the sun go down. Ringed by the Aravalli hills and studded with three islands, it has a fresher, more relaxed feel than the palace-lined Pichola.</p>
<p>The lakeside promenade is lined with stalls and cafés, and boats ferry visitors out to Nehru Garden, the leafy island park in the middle of the water. It's the city's favourite spot for an easy, unhurried evening.</p>
<h2>Don't miss</h2>
<ul><li>A boat ride out to Nehru Garden island.</li><li>The sunset from the promenade, with the hills silhouetted across the water.</li><li>Street snacks and coffee along the lakeside drive.</li></ul>
<h2>Good to know</h2>
<p>It's a great counterpoint to the monument-heavy Old City — come here to slow down. The connecting drive between Fateh Sagar and Pichola passes several viewpoints worth a stop.</p>""")

P(slug="jagdish-temple", city="Udaipur", region="Mewar", cat="Temple",
  name="Jagdish Temple", query="Jagdish Temple Udaipur",
  excerpt="A soaring 17th-century Indo-Aryan temple in the Old City, covered in intricate carving and always alive with devotion.",
  tags=["temple","Udaipur","architecture","heritage"],
  info=dict(timings="Approx 5 AM – 2 PM & 4 PM – 10 PM; aartis at set times", entry="Free",
            best="Morning or evening aarti for the atmosphere", duration="30–45 minutes", reach="Old City, a short walk from the City Palace entrance"),
  body="""<p>Just steps from the City Palace, Jagdish Temple rises above the Old City in a mass of intricately carved stone. Built in 1651 and dedicated to Lord Vishnu, it's the largest and most important temple in Udaipur, and a living centre of worship rather than a museum piece.</p>
<p>Climb the marble steps flanked by stone elephants and you enter a world of detailed sculpture — dancers, musicians, elephants and deities carved across every surface, rising to a tall shikhara (spire) that dominates the surrounding streets.</p>
<h2>Don't miss</h2>
<ul><li>The elaborately carved exterior walls and the towering spire.</li><li>The bronze image of Garuda facing the sanctum.</li><li>The evening aarti, when the temple fills with light, bells and chanting.</li></ul>
<h2>Good to know</h2>
<p>Remove your shoes before entering and dress respectfully. It's an active place of worship — photography inside the sanctum may be restricted. Its central location makes it an easy add-on to a City Palace visit.</p>""")

P(slug="saheliyon-ki-bari", city="Udaipur", region="Mewar", cat="Garden & Park",
  name="Saheliyon Ki Bari", query="Saheliyon ki Bari Udaipur",
  excerpt="The 'Garden of the Maidens' — an elegant 18th-century pleasure garden of fountains, lotus pools and marble pavilions.",
  tags=["garden","Udaipur","fountains","heritage"],
  info=dict(timings="8 AM – 7 PM (daily)", entry="Approx ₹10–₹50",
            best="Morning or late afternoon", duration="45 minutes – 1 hour", reach="~3 km north of the Old City, near Fateh Sagar Lake"),
  body="""<p>Built in the 18th century for the royal ladies of the court and their attendant maidens, Saheliyon Ki Bari is a jewel-box of a garden designed purely for pleasure and shade. It's a cool, green retreat from the city's stone monuments.</p>
<p>The garden is famous for its fountains — many powered entirely by gravity from the lake above, without any pumps — along with lotus pools, marble elephants, a graceful pavilion and beds of seasonal flowers. It's compact, serene and beautifully kept.</p>
<h2>Don't miss</h2>
<ul><li>The gravity-fed fountains, especially the ring of them around the central pavilion.</li><li>The lotus pool and the marble kiosks.</li><li>The small museum near the entrance.</li></ul>
<h2>Good to know</h2>
<p>It's a quick, easy visit that pairs naturally with nearby Fateh Sagar Lake. The fountains are at their best when running — visit in the cooler parts of the day.</p>""")

P(slug="sajjangarh-monsoon-palace", city="Udaipur", region="Mewar", cat="Viewpoint",
  name="Sajjangarh (Monsoon Palace)", query="Sajjangarh Palace Udaipur",
  excerpt="A hilltop palace built to watch the monsoon clouds — and now the finest sunset viewpoint over Udaipur and its lakes.",
  tags=["viewpoint","Udaipur","palace","sunset"],
  info=dict(timings="8 AM – 6 PM (daily)", entry="Approx ₹100 (Indian) / ₹200 (foreign) incl. sanctuary; vehicle/shuttle charges extra",
            best="Sunset — arrive an hour before", duration="1–1.5 hours", reach="Atop a hill ~8 km west of the city, inside Sajjangarh Sanctuary; taxi or shuttle up"),
  body="""<p>Perched on a hilltop high above the city, the Monsoon Palace was built in the late 19th century by Maharana Sajjan Singh, originally intended as an observatory to watch the monsoon clouds roll in over the Aravalli hills. It never quite fulfilled that purpose — but it did become the best seat in Udaipur.</p>
<p>The palace itself is a weathered, romantic shell, but nobody comes for the interiors. They come for the view: a 360-degree panorama of Udaipur, its lakes glinting below, the hills stretching to the horizon, and one of the most spectacular sunsets in Rajasthan.</p>
<h2>Don't miss</h2>
<ul><li>The sunset — the whole reason to make the trip up.</li><li>The sweeping views over Fateh Sagar and Pichola lakes.</li><li>Wildlife spotting on the drive up through the sanctuary.</li></ul>
<h2>Good to know</h2>
<p>The palace sits inside a wildlife sanctuary; private vehicles are often restricted, with shuttle jeeps ferrying visitors up the final stretch. Go for sunset but head down before it's fully dark.</p>""")

P(slug="bagore-ki-haveli", city="Udaipur", region="Mewar", cat="Museum",
  name="Bagore Ki Haveli", query="Bagore ki Haveli Udaipur",
  excerpt="An 18th-century lakeside mansion turned museum — and the home of Udaipur's beloved nightly Rajasthani folk dance show.",
  tags=["museum","Udaipur","culture","dance"],
  info=dict(timings="Museum 10 AM – 6 PM; Dharohar folk show usually ~7 PM", entry="Museum approx ₹100; folk dance show ticketed separately",
            best="Evening, for the folk performance", duration="1–2 hours", reach="Gangaur Ghat, on the edge of Lake Pichola in the Old City"),
  body="""<p>Standing right on the water at Gangaur Ghat, Bagore Ki Haveli is a sprawling 18th-century mansion of over a hundred rooms, now restored as a museum of Mewari life. Its courtyards, balconies and chambers are filled with period costumes, jewellery, utensils, puppets and even a famous display of turbans.</p>
<p>But its real draw is the evening: the haveli's courtyard hosts the Dharohar folk dance show, one of the best cultural performances in the city — a whirl of Rajasthani music, puppetry, and the astonishing Bhavai dance, where women balance stacks of pots on their heads.</p>
<h2>Don't miss</h2>
<ul><li>The Dharohar folk dance and music show in the evening.</li><li>The turban and costume galleries.</li><li>The lakeside setting at Gangaur Ghat.</li></ul>
<h2>Good to know</h2>
<p>The folk show is very popular — arrive early to get a good seat in the courtyard. Photography of the performance may carry a small extra charge.</p>""")

P(slug="gulab-bagh", city="Udaipur", region="Mewar", cat="Garden & Park",
  name="Gulab Bagh & Zoo", query="Gulab Bagh Udaipur",
  excerpt="Udaipur's largest garden — a sprawling green park of rose beds, a lake, a small zoo and a toy train for families.",
  tags=["garden","Udaipur","family","park"],
  info=dict(timings="Approx 8 AM – 6 PM", entry="Nominal; zoo & toy train small extra charge",
            best="Early morning or evening", duration="1 hour", reach="Near the City Palace, on the south-east edge of the Old City"),
  body="""<p>Laid out in the 19th century by Maharana Sajjan Singh, Gulab Bagh (the Rose Garden) is the largest park in Udaipur — a rambling green space of rose beds, shady trees, a lotus pond and winding paths, right beside the City Palace.</p>
<p>It's more a local's park than a tourist monument, and that's the charm: joggers in the morning, families in the evening, a small zoo and a toy train that delights children. A relaxed, leafy break from sightseeing.</p>
<h2>Don't miss</h2>
<ul><li>The rose beds in bloom (best in winter and spring).</li><li>The Sajjan Niwas library and the lotus pond.</li><li>The toy train, if you're travelling with kids.</li></ul>
<h2>Good to know</h2>
<p>It's a genuine city park rather than a manicured heritage garden — come for green space and local life. Easy to combine with the City Palace nearby.</p>""")

P(slug="shilpgram", city="Udaipur", region="Mewar", cat="Museum",
  name="Shilpgram Crafts Village", query="Shilpgram Udaipur",
  excerpt="A living crafts village recreating the rural life of western India — huts, artisans, folk performers and a handicrafts bazaar.",
  tags=["crafts","Udaipur","culture","shopping"],
  info=dict(timings="11 AM – 7 PM (daily)", entry="Approx ₹30–₹50; camera charge extra",
            best="During the winter Shilpgram crafts fair (late December)", duration="1.5–2 hours", reach="~3 km west of the city, near Havala village"),
  body="""<p>Set in the hills on the edge of Udaipur, Shilpgram is a 'rural arts and crafts village' — an open-air museum of traditional huts and dwellings from across Rajasthan, Gujarat, Goa and Maharashtra, each authentically built and decorated.</p>
<p>Beyond the architecture, it's a hub of living craft: potters, weavers and artisans at work, folk musicians and dancers performing, camel rides for kids, and a bazaar of handmade textiles, pottery and jewellery. During its famous winter fair, the whole village comes alive with performers and craftspeople from across the country.</p>
<h2>Don't miss</h2>
<ul><li>The recreated village huts of different regions and communities.</li><li>Live folk music, dance and artisan demonstrations.</li><li>Shopping for authentic handicrafts direct from makers.</li></ul>
<h2>Good to know</h2>
<p>The annual Shilpgram Utsav (crafts fair) around late December is the best time to visit, but the village is worth seeing year-round. It's a great stop for souvenirs.</p>""")

# ---- Mewar day trips ----

P(slug="kumbhalgarh-fort", city="Kumbhalgarh", region="Mewar", cat="Palace & Fort",
  name="Kumbhalgarh Fort", query="Kumbhalgarh Fort",
  excerpt="A mighty hill fortress wrapped in the second-longest wall on earth — the 'Great Wall of India', a UNESCO World Heritage Site.",
  tags=["fort","UNESCO","day trip","Mewar"],
  info=dict(timings="9 AM – 6 PM; light & sound show in the evening", entry="Approx ₹50 (Indian) / ₹200 (foreign)",
            best="October–March; stay for the evening light show", duration="Half day (plus ~2.5 hr drive each way)", reach="~85 km north of Udaipur — a popular full-day trip by car"),
  body="""<p>Coiling over the Aravalli hills for some 36 kilometres, the ramparts of Kumbhalgarh form the second-longest continuous wall in the world — earning it the nickname the Great Wall of India. Built in the 15th century by Rana Kumbha, this UNESCO-listed fortress was the birthplace of the legendary Maharana Pratap and was never taken by direct assault.</p>
<p>Inside the walls lie over 300 temples, palaces and the crowning Badal Mahal (Palace of Clouds), from which the views across the hills and into the plains are staggering. Walking a stretch of the vast wall, wide enough for horses to ride abreast, is the highlight.</p>
<h2>Don't miss</h2>
<ul><li>Walking along the immense fort wall.</li><li>The Badal Mahal at the summit and its panoramic views.</li><li>The evening sound-and-light show that tells the fort's history.</li></ul>
<h2>Good to know</h2>
<p>It's a long day trip from Udaipur, often combined with Ranakpur. Wear good shoes — reaching the top involves a steep climb. The surrounding wildlife sanctuary is a draw in its own right.</p>""")

P(slug="ranakpur-jain-temple", city="Ranakpur", region="Mewar", cat="Temple",
  name="Ranakpur Jain Temple", query="Ranakpur Jain Temple",
  excerpt="A breathtaking 15th-century marble temple held up by 1,444 uniquely carved pillars — no two alike.",
  tags=["temple","Jain","marble","day trip"],
  info=dict(timings="Visitors usually 12 PM – 5 PM (mornings reserved for worship)", entry="Free for darshan; a ticket applies for tourists/photography",
            best="Midday, when light streams through the marble", duration="1–1.5 hours (plus drive)", reach="~90 km from Udaipur, in the Aravalli valley — often paired with Kumbhalgarh"),
  body="""<p>Deep in a forested Aravalli valley stands one of the most astonishing temples in India. The main Chaumukha temple at Ranakpur, dedicated to the Jain Tirthankara Adinatha and built in the 15th century, is carved entirely from light-coloured marble and supported by 1,444 pillars — and, famously, no two are carved alike.</p>
<p>The effect inside is otherworldly: a forest of intricately sculpted columns, domed ceilings dripping with detail, and shifting light that seems to make the whole structure glow. It's considered a masterpiece of Jain temple architecture.</p>
<h2>Don't miss</h2>
<ul><li>The 1,444 individually carved pillars and the layered domed ceilings.</li><li>The marble elephants and the intricate torana carvings.</li><li>The peaceful forest setting around the temple.</li></ul>
<h2>Good to know</h2>
<p>Tourists are usually admitted from around midday, after morning worship. Dress modestly, remove shoes and leather items, and expect a calm, reverent atmosphere. Commonly combined with Kumbhalgarh in one day trip.</p>""")

P(slug="chittorgarh-fort", city="Chittorgarh", region="Mewar", cat="Palace & Fort",
  name="Chittorgarh Fort", query="Chittorgarh Fort",
  excerpt="The largest fort in India and the proud, tragic heart of Rajput history — a UNESCO site of towers, palaces and legend.",
  tags=["fort","UNESCO","history","day trip"],
  info=dict(timings="9:45 AM – 6:30 PM; evening light & sound show", entry="Approx ₹40 (Indian) / ₹600 (foreign)",
            best="October–March; allow a full day", duration="Half to full day (~2 hr drive each way)", reach="~115 km north-east of Udaipur, on the way to Kota/Bundi"),
  body="""<p>Sprawling across a 180-metre hill, Chittorgarh is the largest fort in India and perhaps the most storied. For centuries the capital of Mewar, it witnessed some of the most heroic and tragic episodes in Rajput history — sieges, sacrifices and the legendary defiance of rulers like Rani Padmini.</p>
<p>The vast complex, a UNESCO World Heritage Site, contains palaces, temples, water bodies and two soaring victory towers. The Vijay Stambh (Tower of Victory) and the older Kirti Stambh rise above it all, covered in exquisite carving.</p>
<h2>Don't miss</h2>
<ul><li>The Vijay Stambh (Tower of Victory) — climb it for the views.</li><li>Rana Kumbha's Palace and the Padmini Palace, tied to the fort's legends.</li><li>The evening sound-and-light show recounting Chittor's history.</li></ul>
<h2>Good to know</h2>
<p>The fort is enormous — driving between the monuments inside is common. It's a longer day trip from Udaipur; an early start helps. The history here is deeply woven into Rajasthani identity.</p>""")

P(slug="nathdwara-shrinathji", city="Nathdwara", region="Mewar", cat="Temple",
  name="Nathdwara (Shrinathji Temple)", query="Nathdwara Shrinathji",
  excerpt="One of the most revered Krishna pilgrimage towns in India — home of Shrinathji and the giant Statue of Belief.",
  tags=["temple","pilgrimage","Krishna","day trip"],
  info=dict(timings="Temple darshan at fixed slots through the day (checks recommended)", entry="Free",
            best="Weekdays to avoid the biggest crowds", duration="2–3 hours (plus drive)", reach="~48 km north of Udaipur on the Udaipur–Ajmer highway"),
  body="""<p>The temple town of Nathdwara is one of the holiest centres of Krishna worship in India, drawing pilgrims from across the country to the shrine of Shrinathji — a form of Krishna as a seven-year-old child. The town's religious life, art and famous Pichwai paintings all revolve around the deity.</p>
<p>In recent years Nathdwara has also become known for the towering 'Statue of Belief' — one of the world's tallest statues of Lord Shiva, visible for miles and a striking sight in its own right.</p>
<h2>Don't miss</h2>
<ul><li>Darshan at the Shrinathji temple (note the timed viewing slots).</li><li>The colossal Statue of Belief (Vishwas Swaroopam) statue of Shiva.</li><li>Shopping for traditional Pichwai paintings, a local art form.</li></ul>
<h2>Good to know</h2>
<p>Temple darshan happens in specific timed sessions — check current timings before you go. Phones and cameras are usually not allowed inside the shrine. An easy half-day trip from Udaipur, often combined with Eklingji.</p>""")

P(slug="eklingji-temple", city="Kailashpuri", region="Mewar", cat="Temple",
  name="Eklingji Temple", query="Eklingji Temple",
  excerpt="The ancient family deity of the Mewar rulers — a complex of 108 intricately carved stone temples around a four-faced Shiva.",
  tags=["temple","Shiva","heritage","day trip"],
  info=dict(timings="Darshan in fixed morning & evening sessions", entry="Free",
            best="Combine with a morning trip to Nathdwara", duration="1 hour (plus drive)", reach="~22 km north of Udaipur at Kailashpuri, on the Nathdwara road"),
  body="""<p>For centuries, the Maharanas of Mewar ruled not in their own name but as the earthly regents of Eklingji — the form of Lord Shiva enshrined in this temple complex north of Udaipur. It remains the royal family's deity, and one of the most sacred sites in the region.</p>
<p>Rebuilt in the 15th century over far older foundations, the walled complex holds 108 temples in intricately carved stone, centred on a striking four-faced black marble image of Shiva. The craftsmanship and the living devotion make it a compelling, atmospheric stop.</p>
<h2>Don't miss</h2>
<ul><li>The four-faced (Chaumukha) Shiva in the main sanctum.</li><li>The elaborate carving across the temple complex.</li><li>The evening aarti, if your timing allows.</li></ul>
<h2>Good to know</h2>
<p>Darshan is only during set morning and evening sessions — plan around them. Photography inside is generally not permitted. Very often paired with Nathdwara in a single half-day trip from Udaipur.</p>""")

P(slug="jaisamand-lake", city="Jaisamand", region="Mewar", cat="Lake & Ghat",
  name="Jaisamand Lake", query="Jaisamand Lake",
  excerpt="One of Asia's largest artificial lakes — a vast 17th-century reservoir of islands, marble ghats and summer palaces.",
  tags=["lake","nature","day trip","Mewar"],
  info=dict(timings="Open all day; boating during daylight hours", entry="Free; boating & sanctuary charges apply",
            best="Winter; morning for birdlife", duration="Half day (~1 hr drive each way)", reach="~50 km south-east of Udaipur"),
  body="""<p>Also known as Dhebar Lake, Jaisamand was built in the 17th century by Maharana Jai Singh and was, for a long time, one of the largest artificial lakes in Asia. Away from the tourist crowds of the city, it offers a wilder, more expansive kind of beauty.</p>
<p>Marble ghats and steps line the embankment, punctuated by carved elephants and domed pavilions, while several islands dot the water. The surrounding hills form a wildlife sanctuary, and the whole scene has a peaceful, off-the-map feel.</p>
<h2>Don't miss</h2>
<ul><li>The marble embankment with its carved elephants and cenotaphs.</li><li>A boat ride out among the islands.</li><li>Birdwatching and the sanctuary's forested surroundings.</li></ul>
<h2>Good to know</h2>
<p>It's quieter and less developed than the city lakes — come for nature and calm rather than facilities. Best paired with a relaxed half-day drive out of Udaipur.</p>""")
