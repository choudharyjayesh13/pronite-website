# -*- coding: utf-8 -*-
"""Places batch J — CLUBS & CAFÉS to visit across India.
New categories: Club, Café. City-level scene guides (venues named as examples,
without asserting exact current prices/timings)."""
POSTS = []
def P(**k): POSTS.append(k)

# ============================ CLUBS ============================

P(slug="delhi-clubs", city="Delhi", region="Delhi", cat="Club",
  name="Delhi & Gurugram Clubs", query="Connaught Place Delhi night",
  excerpt="The capital goes big — glossy high-rise clubs and Bollywood-EDM nights across Gurugram's Cyber Hub, Aerocity and Connaught Place.",
  tags=["Delhi","Gurugram","clubs","nightlife"],
  info=dict(timings="Clubs typically 9 PM – 3 AM (peak Fri–Sat)", entry="Free–moderate cover; table minimums at premium clubs",
            best="Weekend nights", duration="A night out", reach="Gurugram (Cyber Hub), Aerocity & Connaught Place; Metro-connected"),
  body="""<p>Delhi-NCR does nightlife on a grand scale. The serious clubbing has largely migrated to Gurugram, where Cyber Hub and the surrounding hubs pack in glossy, high-energy clubs playing commercial, Bollywood and big-room EDM to dressed-up weekend crowds. Aerocity's hotel clubs and Connaught Place's rooftops round out the scene.</p>
<p>Expect big production, big crowds and a love of an occasion — Delhi responds hard to a marquee DJ or a themed night. Dress codes are real at the premium venues, and table bookings help on busy weekends.</p>
<h2>Know before you go</h2>
<ul><li>Gurugram's Cyber Hub is the densest cluster of clubs and bars.</li><li>Dress sharp — premium clubs enforce dress codes.</li><li>Weekends and big DJ nights book out; reserve a table for groups.</li></ul>
<h2>Good to know</h2>
<p>NCR is huge — pick a zone (Gurugram, Aerocity or CP) for the night rather than crossing the city. Always plan a safe cab home.</p>""")

P(slug="mumbai-clubs", city="Mumbai", region="Maharashtra", cat="Club",
  name="Mumbai Clubs", query="Lower Parel Mumbai skyline",
  excerpt="India's deepest club calendar — rooftop lounges and warehouse line-ups across Lower Parel, Worli, Bandra and the Kamala Mills district.",
  tags=["Mumbai","clubs","rooftop","nightlife"],
  info=dict(timings="Clubs ~9 PM – 1:30 AM (city licensing); afterparties vary", entry="Cover/table minimums at top venues; guest lists help",
            best="Any weekend (weeknights are lively too)", duration="A night out", reach="Lower Parel/Worli & Bandra; nearest stations Lower Parel, Bandra"),
  body="""<p>Mumbai has the most consistent, highest-quality club scene in India — a real year-round ecosystem rather than a seasonal one. Lower Parel and Worli (around the Kamala Mills and Todi Mills compounds) hold the glossy high-rise clubs and rooftop lounges, while Bandra brings the cooler, more eclectic west-side energy.</p>
<p>The city pulls the best touring DJs and hosts everything from commercial rooftops to underground warehouse nights. Licensing means many clubs wind down around 1:30 AM, so start on time — and the real heads know where the afterparties are.</p>
<h2>Know before you go</h2>
<ul><li>Lower Parel/Worli for glossy clubs; Bandra for cooler bars and gigs.</li><li>Guest lists and table bookings matter at marquee venues on weekends.</li><li>Distances are real — plan the night around one or two areas.</li></ul>
<h2>Good to know</h2>
<p>Weeknights are genuinely good here thanks to the city's size. Sort your cab in advance; the suburbs are far.</p>""")

P(slug="bengaluru-clubs", city="Bengaluru", region="Karnataka", cat="Club",
  name="Bengaluru Clubs & Indiranagar", query="Indiranagar Bangalore",
  excerpt="India's original pub city — microbreweries, rooftop clubs and a discerning dancefloor across Indiranagar, Koramangala and MG Road.",
  tags=["Bengaluru","clubs","microbrewery","nightlife"],
  info=dict(timings="Bars from evening; clubs till ~1 AM", entry="Free–moderate; some clubs have cover",
            best="Weekend nights (start early — deadlines are earlier here)", duration="A night out", reach="Indiranagar, Koramangala & MG Road/Brigade Road"),
  body="""<p>Bengaluru practically invented modern Indian nightlife, and it still has one of the country's most knowledgeable dancefloors. Indiranagar and Koramangala are the buzzing hubs — dense with microbreweries, rooftop bars, live-music venues and clubs — while MG Road/Brigade Road holds the classic scene.</p>
<p>The crowd here comes for the music as much as the party, so the house and techno nights run deep, alongside the craft-beer-and-live-band culture the city is famous for. Just note the earlier closing times — start your night sooner than in Mumbai or Delhi.</p>
<h2>Know before you go</h2>
<ul><li>Indiranagar and Koramangala are the nightlife hearts.</li><li>Follow the promoters/collectives — the best nights are curated.</li><li>Deadlines are earlier — begin the evening on time.</li></ul>
<h2>Good to know</h2>
<p>The microbrewery-and-music format is a Bengaluru speciality — even a casual night here is a good one.</p>""")

P(slug="goa-clubs", city="Goa", region="Goa", cat="Club",
  name="Goa Clubs (Vagator & Anjuna)", query="Vagator Goa",
  excerpt="Beyond Baga's mainstream strip — the cliffside clubs and sunrise floors of Vagator, Anjuna and Morjim where Goa's real dance culture lives.",
  tags=["Goa","clubs","techno","sunrise"],
  info=dict(timings="Clubs late into the night; sunrise sessions in season", entry="Cover varies; big NYE/season nights are ticketed",
            best="Peak season (Nov–Feb); weekends & full moons", duration="A big night (or till sunrise)", reach="North Goa — Vagator, Anjuna, Morjim"),
  body="""<p>Baga's Tito's Lane is the mainstream face of Goa nightlife, but the state's real dance culture lives a little further north. The cliffside clubs of Vagator and Anjuna and the beach floors of Morjim are where the serious techno, house and afro-house nights happen — often running from sunset deep into the next day.</p>
<p>This is the Goa that put India on the global dance map: open-air floors, world-class touring selectors, and the famous sunrise sessions that are a rite of passage. Peak season (November–February) and the New Year run are legendary.</p>
<h2>Know before you go</h2>
<ul><li>Vagator/Anjuna for cliffside clubs; Morjim for beach floors.</li><li>Season nights and NYE are ticketed and sell out — book ahead.</li><li>Pace yourself — Goa is a marathon, and the best moment is often dawn.</li></ul>
<h2>Good to know</h2>
<p>Rent a scooter — the good clubs are spread across kilometres of coast. Look after each other on the late/sunrise sessions.</p>""")

P(slug="hyderabad-clubs", city="Hyderabad", region="Telangana", cat="Club",
  name="Hyderabad Clubs (Jubilee Hills)", query="Jubilee Hills Hyderabad",
  excerpt="A fast-rising scene of high-rise clubs and rooftop lounges across Jubilee Hills, Banjara Hills and the HITEC City tech corridor.",
  tags=["Hyderabad","clubs","rooftop","nightlife"],
  info=dict(timings="Clubs ~8 PM – 1 AM (peak weekends)", entry="Cover/table minimums at premium venues",
            best="Weekend nights", duration="A night out", reach="Jubilee Hills & Banjara Hills; HITEC City for the tech crowd"),
  body="""<p>Hyderabad's nightlife has grown up fast alongside its tech boom. Jubilee Hills and Banjara Hills hold the premium clubs and rooftop lounges, while the HITEC City / Gachibowli corridor serves the young tech crowd with newer, high-energy venues.</p>
<p>The scene leans commercial and Bollywood-forward on the mainstream nights, with a small but committed underground pushing house and techno. Promoters increasingly bring festival-grade shows to the city — it's a scene on a clear upward curve.</p>
<h2>Know before you go</h2>
<ul><li>Jubilee/Banjara Hills for the premium clubs and rooftops.</li><li>Dress codes and reservations apply at top venues.</li><li>Weekends are where the marquee nights land.</li></ul>
<h2>Good to know</h2>
<p>Pleasant winter months are peak going-out season. Round off the night with the city's legendary late-night biryani.</p>""")

P(slug="udaipur-nights-pronite", city="Udaipur", region="Mewar", cat="Club",
  name="Udaipur Nights (with Pronite)", query="Udaipur night lake",
  excerpt="Boutique lakeside nightlife you won't find anywhere else — pool parties, open-air techno and rooftop sundowners, curated by Pronite.",
  tags=["Udaipur","Pronite","pool party","nightlife"],
  info=dict(timings="Sundowners from evening; events run late", entry="Guest list (free) or ticketed events — join via WhatsApp",
            best="Winter & the festive/Holi/NYE season", duration="A night (or a whole weekend)", reach="The Udaisarovar & the city's best venues, Udaipur"),
  body="""<p>Udaipur isn't a warehouse-and-basement club city — its nightlife is boutique, scenic and unlike anywhere else in India. The magic is the setting: pool parties by the lake, open-air techno under Rajasthan skies, camping nights, and rooftop sundowners with palace views.</p>
<p>This is home turf for Pronite, the collective that has built the city's party calendar — Holi pool parties (Rangilo Rajasthan), OFFGRID underground nights, Bollywood evenings and New Year's countdowns at The Udaisarovar and the city's finest venues. It's a curated scene rather than a dense club strip, and all the better for it.</p>
<h2>Know before you go</h2>
<ul><li>Events are seasonal and often guest-list or ticket only — plan ahead.</li><li>Winter and the festive stretch (Holi, NYE) are peak.</li><li>Pair the party with a lakeside stay — Udaipur rewards a full weekend.</li></ul>
<h2>Good to know</h2>
<p>Get on the free Pronite guest list on WhatsApp (+91 91160 20099) — the best nights drop there before they're ever public.</p>""")

# ============================ CAFÉS ============================

P(slug="bengaluru-cafes", city="Bengaluru", region="Karnataka", cat="Café",
  name="Bengaluru Café Culture", query="Church Street Bangalore",
  excerpt="India's café capital — from third-wave coffee roasters and Church Street hangouts to legendary filter-coffee and dosa institutions.",
  tags=["Bengaluru","cafe","coffee","hangout"],
  info=dict(timings="Cafés roughly 8 AM – 11 PM", entry="Free (pay for what you order)",
            best="Any day; mornings for coffee, evenings for the buzz", duration="A relaxed few hours", reach="Church Street, Indiranagar, Koramangala"),
  body="""<p>No Indian city takes its café culture more seriously than Bengaluru. The pleasant climate, the huge young population and a genuine coffee heritage have made it the country's café capital — home to a thriving third-wave coffee scene of independent roasters and specialty cafés, especially around Church Street, Indiranagar and Koramangala.</p>
<p>But the coffee story runs deeper than lattes: Bengaluru is also the land of the classic South Indian filter coffee and legendary old institutions serving crisp dosas with a steel tumbler of decoction. From hipster roastery to heritage darshini, it's a café lover's dream.</p>
<h2>Know before you go</h2>
<ul><li>Church Street and Indiranagar for the specialty-coffee scene.</li><li>Don't skip a classic filter coffee at a heritage institution.</li><li>Cafés double as co-working and hangout spots — lovely for a slow morning.</li></ul>
<h2>Good to know</h2>
<p>Many cafés get busy (and laptop-heavy) on weekdays. Weekend mornings are the sweet spot for a relaxed cup.</p>""")

P(slug="mumbai-irani-cafes", city="Mumbai", region="Maharashtra", cat="Café",
  name="Mumbai's Irani Cafés", query="Irani cafe Mumbai",
  excerpt="A vanishing institution worth seeking out — old-world Irani cafés serving bun maska, keema and chai amid marble tables and faded charm.",
  tags=["Mumbai","cafe","Irani","heritage"],
  info=dict(timings="Roughly breakfast till evening (varies)", entry="Free (pay as you order)",
            best="Breakfast or an afternoon chai break", duration="An hour", reach="South Mumbai — Fort, Kala Ghoda, Ballard Estate"),
  body="""<p>Among Mumbai's most beloved and endangered institutions are its Irani cafés — century-old establishments founded by Zoroastrian immigrants from Iran, with their high ceilings, marble-topped tables, bentwood chairs and gloriously faded charm. Sitting in one feels like stepping into old Bombay.</p>
<p>The menu is a comfort classic: soft bun maska (buttered bun) dunked in sweet Irani chai, spicy keema-pav, berry pulao and crumbly mawa cakes. Once numbering in the hundreds, only a handful of these cafés survive — which is exactly why they're worth seeking out.</p>
<h2>Know before you go</h2>
<ul><li>Order bun maska and Irani chai — the signature combination.</li><li>Look for the surviving classics around Fort and Kala Ghoda.</li><li>Soak up the old-world atmosphere; it's the whole point.</li></ul>
<h2>Good to know</h2>
<p>These are casual, cash-friendly, no-frills spots with bags of character — not fancy cafés. Go for the heritage as much as the food.</p>""")

P(slug="delhi-cafes", city="Delhi", region="Delhi", cat="Café",
  name="Delhi Cafés (Khan Market & Hauz Khas)", query="Khan Market Delhi",
  excerpt="From chic Khan Market brunch spots to the boho cafés of Hauz Khas and the artsy lanes of Champa Gali — Delhi's café scene has range.",
  tags=["Delhi","cafe","brunch","hangout"],
  info=dict(timings="Cafés roughly 9 AM – 11 PM", entry="Free (pay as you order)",
            best="Weekend brunch; evenings in Hauz Khas", duration="A relaxed few hours", reach="Khan Market, Hauz Khas Village, Champa Gali, SDA"),
  body="""<p>Delhi's café culture has exploded, and it spans the full spectrum. Khan Market — one of the priciest retail streets in the world — is dense with chic brunch cafés and coffee bars for the city's well-heeled crowd. Hauz Khas Village pairs its nightlife with boho cafés overlooking medieval ruins.</p>
<p>For something more offbeat, the hidden artsy lanes of Champa Gali and the student-friendly spots around SDA and North Campus offer quirky, characterful hangouts. Whether you want a power brunch or a lazy afternoon with a book, Delhi delivers.</p>
<h2>Know before you go</h2>
<ul><li>Khan Market for polished brunch cafés; Hauz Khas for boho views.</li><li>Champa Gali is a hidden lane of quirky cafés worth hunting down.</li><li>Weekend brunch is a Delhi institution — book ahead at popular spots.</li></ul>
<h2>Good to know</h2>
<p>Winters are perfect for Delhi's many open-air and rooftop cafés; summers push everyone indoors to the AC.</p>""")

P(slug="goa-beach-cafes", city="Goa", region="Goa", cat="Café",
  name="Goa Beach Cafés & Shacks", query="beach shack Goa",
  excerpt="The soul of a Goa day — barefoot beach shacks and cliff-top cafés for fresh seafood, cold beer, sunsets and slow, salty afternoons.",
  tags=["Goa","cafe","beach shack","sunset"],
  info=dict(timings="Roughly all day into the evening (season only)", entry="Free (pay as you order)",
            best="Season (Nov–Apr); lunch to sunset", duration="A lazy afternoon", reach="Beaches across North & South Goa"),
  body="""<p>Half the magic of Goa happens in its beach shacks and cliff-top cafés. These barefoot, sand-floored institutions — springing up each season along the coast — are where a Goa day unfolds: fresh-caught seafood, cold beer, endless chai and coffee, and the best sunset seats on the beach.</p>
<p>From the buzzing shacks of Baga and Calangute to the mellow cliff cafés of Vagator and the yoga-and-smoothie spots of the south, each stretch of coast has its own vibe. Settling into a lounger with a thali and a view is a Goan art form.</p>
<h2>Know before you go</h2>
<ul><li>Fresh seafood thalis and grilled fish are the shack speciality.</li><li>Cliff cafés at Vagator and Chapora for the best sunset views.</li><li>South Goa's cafés lean healthy, yogic and laid-back.</li></ul>
<h2>Good to know</h2>
<p>Most shacks are seasonal (roughly Nov–Apr) and dismantled for the monsoon. Prices and quality vary — the busy ones are usually a safe bet.</p>""")

P(slug="pondicherry-cafes", city="Puducherry", region="Puducherry", cat="Café",
  name="Pondicherry Cafés", query="Pondicherry White Town street",
  excerpt="French-colonial charm in a cup — bakeries and courtyard cafés serving croissants, crêpes and great coffee in the pastel White Town lanes.",
  tags=["Pondicherry","cafe","French","bakery"],
  info=dict(timings="Cafés roughly 8 AM – 10 PM", entry="Free (pay as you order)",
            best="Morning for bakeries; evening by the Promenade", duration="A relaxed few hours", reach="French Quarter (White Town), Puducherry"),
  body="""<p>Pondicherry's French heritage shows up most deliciously in its cafés. The pastel-hued lanes of White Town are dotted with charming bakeries and courtyard cafés serving proper croissants, baguettes, crêpes and excellent coffee — a genuine slice of France on the Tamil coast.</p>
<p>Many occupy restored colonial villas with leafy courtyards, making them idyllic spots to linger over breakfast or an afternoon coffee. Combined with the seafront Promenade and the boho-chic boutiques, café-hopping is one of the great pleasures of a Pondy weekend.</p>
<h2>Know before you go</h2>
<ul><li>French bakeries for croissants and fresh bread.</li><li>Courtyard cafés in restored heritage villas.</li><li>Pair a morning café crawl with the seafront Promenade.</li></ul>
<h2>Good to know</h2>
<p>The French Quarter is small and best explored on foot or by bicycle. Weekdays are calmer than the Chennai-weekend rush.</p>""")

P(slug="himalayan-cafes", city="Manali", region="Himachal Pradesh", cat="Café",
  name="Himalayan Café Culture (Manali & Kasol)", query="Old Manali cafe",
  excerpt="Mountain-view cafés with a backpacker soul — riverside terraces, wood fires and world cuisine across Old Manali, Kasol and the Parvati Valley.",
  tags=["Manali","Kasol","cafe","mountains"],
  info=dict(timings="Cafés roughly 9 AM – 11 PM (season-dependent)", entry="Free (pay as you order)",
            best="Summer (Apr–Jun) & autumn; sunny mountain mornings", duration="A relaxed few hours", reach="Old Manali, Kasol & the Parvati Valley, Himachal"),
  body="""<p>The Himalayan backpacker trail has its own beloved café culture. In Old Manali, Kasol and across the Parvati Valley, riverside cafés with wooden terraces, floor cushions, wood fires and mountain views serve a surprisingly global menu — Israeli, Italian, Tibetan and hearty local fare — to a laid-back crowd of travellers.</p>
<p>These cafés are as much about the vibe as the food: nursing a coffee or a hot chocolate while the Beas or Parvati river rushes below and the peaks glow is the whole Himachal café experience. They're social hubs, workspaces and chill-out spots all in one.</p>
<h2>Know before you go</h2>
<ul><li>Riverside terraces in Old Manali and Kasol for the views.</li><li>The eclectic international menus (a legacy of the traveller trail).</li><li>Go for the slow, mountain-time atmosphere.</li></ul>
<h2>Good to know</h2>
<p>Many cafés are seasonal and quieter in deep winter. Connectivity can be patchy — embrace the digital detox.</p>""")

P(slug="udaipur-rooftop-cafes", city="Udaipur", region="Mewar", cat="Café",
  name="Udaipur Rooftop Cafés", query="Udaipur rooftop lake view",
  excerpt="Some of India's most beautiful café seats — rooftop terraces gazing over Lake Pichola and the City Palace, perfect for a sundowner coffee.",
  tags=["Udaipur","cafe","rooftop","lake view"],
  info=dict(timings="Cafés roughly 8 AM – 10 PM", entry="Free (pay as you order)",
            best="Sunset, for the lake-and-palace views", duration="A relaxed few hours", reach="Around Lal Ghat, Gangaur Ghat & Hanuman Ghat, old-city Udaipur"),
  body="""<p>Udaipur's old city is stacked with rooftop cafés, and they offer some of the most beautiful café views in India. Terraces around Lal Ghat, Gangaur Ghat and Hanuman Ghat look straight out over Lake Pichola to the City Palace and the island Lake Palace — a backdrop no city café can match.</p>
<p>Nursing a coffee, a lassi or a meal as the sun sets over the water and the palaces turn gold is the quintessential slow Udaipur moment. Many cafés stack several storeys high, competing for the best view — and they're an ideal way to soak in the City of Lakes between sightseeing.</p>
<h2>Know before you go</h2>
<ul><li>Sunset is the golden hour — arrive early to claim a lake-facing table.</li><li>The ghats (Lal, Gangaur, Hanuman) have the best rooftop clusters.</li><li>Great for a relaxed break between the City Palace and a boat ride.</li></ul>
<h2>Good to know</h2>
<p>Food is often secondary to the view — come for the setting and a drink. Rooftops can be busy at sunset; a little patience gets you the best seat.</p>""")
