import re
import json

def update():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # I will not use pl_source.json or en_source.json as I have them in memory or can extract them safely
    # Let's extract EN properly from current index.html to be ABSOLUTELY sure I don't break it
    en_match = re.search(r'"en": (\{.*?\n\s+\})', content, re.DOTALL)
    en_block = en_match.group(1)
    en = {}
    for line in en_block.splitlines():
        kv = re.search(r'"(.*?)"\s*:\s*"(.*)"', line)
        if kv:
            en[kv.group(1)] = kv.group(2)

    contact_list = "PL · EN · DE · FR · RU · UA"

    # Pre-defined localized blocks for the requested languages
    translations = {
        "cs": {
            "page_title": "Velor Construction | Průmyslové haly a generální dodávky",
            "meta_description": "Velor Construction — průmyslové haly, generální dodávky a stavby z masivního dřeva Holz100. Evropský standard, polská realizace.",
            "nav_start": "Start", "nav_why": "O nás", "nav_services": "Služby", "nav_realizations": "Zkušenosti", "nav_process": "Proces", "nav_career": "Kariéra", "nav_faq": "FAQ", "nav_contact": "Kontakt",
            "hero_h1": "Stavíme s přesností.<br>Evropský Standard.<br>Polská Realizace.",
            "hero_p": "Generální dodávky průmyslových hal, skladů a technologických instalací. Inženýrská přesnost, nekompromisní kvalita. Komunikace: " + contact_list,
            "hero_cta_primary": "Zahájit projekt", "hero_cta_secondary": "Zkušenosti týmu",
            "trust_1": "✓ Zkušenosti z projektů v Německu, Norsku a Polsku", "trust_2": "✓ Infrastruktura, kubatura a instalace", "trust_3": "✓ Normy Eurokód a DIN", "trust_4": "✓ Full Project Management",
            "why_title": "Proč Velor Construction?",
            "pillar_1_h3": "Inženýrská preciznost", "pillar_1_p": "Zkušenosti ze skandinávských a německých trhů nám umožňují realizovat nejsložitější konstrukce v souladu s Eurokódy.",
            "pillar_2_h3": "Technologie a instalace", "pillar_2_p": "Navrhujeme a implementujeme pokročilé průmyslové instalace a HVAC systémy.",
            "pillar_3_h3": "Generální dodávky", "pillar_3_p": "Přebíráme plnou odpovědnost za celý stavební proces od A do Z.",
            "services_title": "Rozsah služeb",
            "service_1_h3": "Ocelové haly a sklady", "service_1_p": "Projektování a montáž moderních ocelových konstrukcí.", "service_1_scope": "Optimalizace",
            "service_2_h3": "Průmyslové instalace", "service_2_p": "Realizace pokročilých technologických systémů.", "service_2_scope": "TGA",
            "service_3_h3": "Generální dodávky", "service_3_p": "Komplexní realizace investic v modelu Design & Build.", "service_3_scope": "Koordinace",
            "service_4_h3": "Project Management", "service_4_p": "Profesionální správa projektů s využitím moderních nástrojů.", "service_4_scope": "Standardy",
            "service_5_h3": "Stavby Holz100", "service_5_p": "Ekologické stavby z masivního dřeva v rakouské technologii.", "service_5_scope": "Masivní dřevo",
            "holz_title": "Technologie Holz100", "holz_lead": "Revoluční systém staveb z masivního dřeva bez použití lepidel.",
            "holz_f1_h": "Nula chemie", "holz_f1_p": "Spojování dřeva pomocí bukových kolíků.",
            "holz_f2_h": "Zdravé mikroklima", "holz_f2_p": "Přirozená regulace vlhkosti a teploty.",
            "holz_f3_h": "Požární bezpečnost", "holz_f3_p": "Vysoká odolnost potvrzená certifikáty.",
            "holz_f4_h": "Ekologie", "holz_f4_p": "Negativní uhlíková stopa, ideální pro ESG.",
            "holz_cta": "Více o Holz100",
            "cases_title": "Naše zkušenosti", "cases_lead": "Vybrané realizace našeho týmu.",
            "case_1_accent": "Mory 🇵🇱", "case_1_h3": "Showroom Brabus",
            "case_1_stat_1_label": "Model", "case_1_stat_1_val": "Design & Build",
            "case_1_stat_2_label": "Typ", "case_1_stat_2_val": "Prémiová hala",
            "case_1_challenge_label": "Výzva:", "case_1_challenge_p": "Vysoké estetické a funkční nároky klienta.",
            "case_1_solution_label": "Řešení:", "case_1_solution_p": "Integrovaný proces návrhu a realizace.",
            "case_1_result_label": "Výsledek:", "case_1_result_p": "Moderní objekt předaný včas.",
            "case_2_accent": "Lübeck 🇩🇪", "case_2_h3": "Logistický terminál",
            "case_2_stat_1_label": "Země", "case_2_stat_1_val": "Německo",
            "case_2_stat_2_label": "Objem", "case_2_stat_2_val": "L-Sklady",
            "case_2_challenge_label": "Výzva:", "case_2_challenge_p": "Práce za plného provozu terminálu.",
            "case_2_solution_label": "Řešení:", "case_2_solution_p": "Etapizace prací a přísná koordinace bezpečnosti.",
            "case_2_result_label": "Výsledek:", "case_2_result_p": "Úspěšné rozšíření infrastruktury.",
            "case_3_accent": "Bergen 🇳🇴", "case_3_h3": "Media City Bergen",
            "case_3_stat_1_label": "Region", "case_3_stat_1_val": "Norsko",
            "case_3_stat_2_label": "Fasády", "case_3_stat_2_val": "Hliník/Sklo",
            "case_3_challenge_label": "Výzva:", "case_3_challenge_p": "Extrémní klimatické podmínky a složitá geometrie.",
            "case_3_solution_label": "Řešení:", "case_3_solution_p": "Pokročilé fasádní systémy odolné větru.",
            "case_3_result_label": "Výsledek:", "case_3_result_p": "Architektonická ikona regionu.",
            "other_projects_title": "Ostatní projekty",
            "p1_pl": "Hala Garwolin", "p1_de": "Sande Logistik", "p1_no": "Askøy Průmysl",
            "process_title": "Jak pracujeme",
            "step_1_h4": "Koncepce", "step_1_p": "Analýza potřeb a proveditelnosti.", "step_2_h4": "Projektování", "step_2_p": "BIM modelování a dokumentace.", "step_3_h4": "Povolení", "step_3_p": "Zajištění všech úředních souhlasů.", "step_4_h4": "Realizace", "step_4_p": "Samotná výstavba pod dohledem.", "step_5_h4": "Předání", "step_5_p": "Kolaudace a spuštění provozu.",
            "faq_title": "Časté dotazy",
            "faq_1_q": "Jak dlouho trvá stavba haly?", "faq_1_a": "Standardní doba realizace je 4 až 7 měsíců v závislosti na složitosti.", "faq_2_q": "Pomáháte s povolením?", "faq_2_a": "Ano, v rámci generální dodávky zajišťujeme kompletní inženýring.", "faq_3_q": "Stavíte podle Eurokódů?", "faq_3_a": "Samozřejmě, všechny naše projekty splňují evropské normy.", "faq_4_q": "Co je to technologie Holz100?", "faq_4_a": "Je to systém z masivního dřeva bez lepidel, nabízející unikátní mikroklima.", "faq_5_q": "Působíte i mimo Polsko?", "faq_5_a": "Ano, máme bohaté zkušenosti z trhů v Německu, Norsku a dalších zemích EU.", "faq_6_q": "Zajišťujete i instalace?", "faq_6_a": "Ano, specializujeme se na komplexní průmyslové instalace (TGA).",
            "contact_h2": "Máte projekt?", "contact_p": "Ozvěte se nám, připravíme nezávaznou nabídku.", "contact_direct_p": "Přímý kontakt:",
            "form_name_label": "Jméno a příjmení", "form_email_label": "E-mail", "form_phone_label": "Telefon", "form_location_label": "Lokalita projektu", "form_budget_label": "Předpokládaný rozpočet", "form_message_label": "Zpráva", "form_privacy_label": "Souhlasím se zpracováním osobních údajů.", "form_submit": "Odeslat poptávku", "form_placeholder_location": "např. Praha, Brno", "form_placeholder_message": "Popište stručně váš záměr...", "form_success": "Děkujeme, brzy vás budeme kontaktovat.",
            "footer_brand_p": "Vaše vize, naše realizace.", "footer_nav_label": "Navigace", "footer_rights": "© 2026 Velor Construction. Všechna práva vyhrazena.",
            "career_h2": "Kariéra", "career_p": "Rozšiřujeme náš tým odborníků.", "career_benefits_p": "Co nabízíme:", "career_benefit_1": "Zajímavé mezinárodní projekty", "career_benefit_2": "Práce s moderními technologiemi (BIM)", "career_benefit_3": "Možnost profesního růstu",
            "career_position_label": "Pozice", "career_pos_1": "Stavbyvedoucí", "career_pos_2": "Projektant", "career_pos_3": "Montážník konstrukcí",
            "career_cv_label": "Nahrajte CV (PDF)", "career_file_hint": "Max. 5MB", "career_message_label": "Motivační dopis / Zpráva", "form_placeholder_career_message": "Proč chcete pracovat u nás?", "career_privacy_label": "Souhlasím se zpracováním údajů pro účely náboru.", "career_submit": "Odeslat přihlášku", "career_success": "Vaše přihláška byla úspěšně odeslána."
        },
        "hu": {
            "page_title": "Velor Construction | Ipari csarnokok és generálkivitelezés",
            "meta_description": "Velor Construction — ipari csarnokok, generálkivitelezés és Holz100 tömörfa építészet. Európai színvonal, lengyel kivitelezés.",
            "nav_start": "Start", "nav_why": "Rólunk", "nav_services": "Szolgáltatások", "nav_realizations": "Tapasztalat", "nav_process": "Folyamat", "nav_career": "Karrier", "nav_faq": "GYIK", "nav_contact": "Kapcsolat",
            "hero_h1": "Precíziós építészet.<br>Európai Színvonal.<br>Lengyel Kivitelezés.",
            "hero_p": "Ipari csarnokok, raktárak és technológiai berendezések generálkivitelezése. Mérnöki precizitás, kompromisszumok nélküli minőség. Kapcsolat: " + contact_list,
            "hero_cta_primary": "Projekt indítása", "hero_cta_secondary": "Csapat tapasztalata",
            "trust_1": "✓ Tapasztalat németországi, norvégiai és lengyelországi projektekben", "trust_2": "✓ Infrastruktúra, kubatúra és gépészet", "trust_3": "✓ Eurocode és DIN szabványok", "trust_4": "✓ Teljes körű projektmenedzsment",
            "why_title": "Miért a Velor Construction?",
            "pillar_1_h3": "Mérnöki precizitás", "pillar_1_p": "A skandináv és német piacokon szerzett tapasztalatunk lehetővé teszi a legösszetettebb szerkezetek megvalósítását.",
            "pillar_2_h3": "Technológia és gépészet", "pillar_2_p": "Fejlett ipari rendszereket és HVAC megoldásokat tervezünk és építünk be.",
            "pillar_3_h3": "Generálkivitelezés", "pillar_3_p": "Teljes felelősséget vállalunk az építési folyamatért az elejétől a végéig.",
            "services_title": "Szolgáltatási kör",
            "service_1_h3": "Acélcsarnokok és raktárak", "service_1_p": "Modern acélszerkezetek tervezése és szerelése.", "service_1_scope": "Optimalizálás",
            "service_2_h3": "Ipari gépészet", "service_2_p": "Fejlett technológiai rendszerek kivitelezése.", "service_2_scope": "TGA",
            "service_3_h3": "Generálkivitelezés", "service_3_p": "Komplex beruházások Design & Build modellben.", "service_3_scope": "Koordináció",
            "service_4_h3": "Projektmenedzsment", "service_4_p": "Professzionális irányítás modern IT eszközökkel.", "service_4_scope": "Szabványok",
            "service_5_h3": "Holz100 épületek", "service_5_p": "Ökológiai tömörfa építészet osztrák technológiával.", "service_5_scope": "Tömörfa",
            "holz_title": "Holz100 Technológia", "holz_lead": "Forradalmi tömörfa építési rendszer ragasztóanyagok nélkül.",
            "holz_f1_h": "Zéró vegyszer", "holz_f1_p": "Faelemek összekapcsolása bükkfa csapokkal.",
            "holz_f2_h": "Egészséges klíma", "holz_f2_p": "Természetes páratartalom- és hőmérsékletszabályozás.",
            "holz_f3_h": "Tűzbiztonság", "holz_f3_p": "Tanúsítványokkal igazolt magas ellenállóképesség.",
            "holz_f4_h": "Ökológia", "holz_f4_p": "Negatív karbonlábnyom, ideális ESG célokhoz.",
            "holz_cta": "Tudjon meg többet a Holz100-ról",
            "cases_title": "Tapasztalatunk", "cases_lead": "Csapatunk kiemelt projektjei.",
            "case_1_accent": "Mory 🇵🇱", "case_1_h3": "Brabus Bemutatóterem",
            "case_1_stat_1_label": "Modell", "case_1_stat_1_val": "Design & Build",
            "case_1_stat_2_label": "Típus", "case_1_stat_2_val": "Prémium csarnok",
            "case_1_challenge_label": "Kihívás:", "case_1_challenge_p": "Magas esztétikai és funkcionális elvárások.",
            "case_1_solution_label": "Megoldás:", "case_1_solution_p": "Integrált tervezési és kivitelezési folyamat.",
            "case_1_result_label": "Eredmény:", "case_1_result_p": "Határidőre átadott modern létesítmény.",
            "case_2_accent": "Lübeck 🇩🇪", "case_2_h3": "Logisztikai terminál",
            "case_2_stat_1_label": "Ország", "case_2_stat_1_val": "Németország",
            "case_2_stat_2_label": "Kapacitás", "case_2_stat_2_val": "L-Raktárak",
            "case_2_challenge_label": "Kihívás:", "case_2_challenge_p": "Munkavégzés folyamatos terminálforgalom mellett.",
            "case_2_solution_label": "Megoldás:", "case_2_solution_p": "Szakaszos munkavégzés és szigorú koordináció.",
            "case_2_result_label": "Eredmény:", "case_2_result_p": "Sikeres infrastruktúra-bővítés.",
            "case_3_accent": "Bergen 🇳🇴", "case_3_h3": "Media City Bergen",
            "case_3_stat_1_label": "Régió", "case_3_stat_1_val": "Norvégia",
            "case_3_stat_2_label": "Homlokzat", "case_3_stat_2_val": "Alumínium/Üveg",
            "case_3_challenge_label": "Kihívás:", "case_3_challenge_p": "Extrém időjárás és bonyolult geometria.",
            "case_3_solution_label": "Megoldás:", "case_3_solution_p": "Fejlett, szélálló homlokzati rendszerek.",
            "case_3_result_label": "Eredmény:", "case_3_result_p": "A régió építészeti ikonja.",
            "other_projects_title": "További projektek",
            "p1_pl": "Garwolin csarnok", "p1_de": "Sande Logisztika", "p1_no": "Askøy Ipar",
            "process_title": "Hogyan dolgozunk",
            "step_1_h4": "Koncepció", "step_1_p": "Igényfelmérés és megvalósíthatósági elemzés.", "step_2_h4": "Tervezés", "step_2_p": "BIM modellezés és dokumentáció.", "step_3_h4": "Engedélyezés", "step_3_p": "Hivatalos jóváhagyások beszerzése.", "step_4_h4": "Kivitelezés", "step_4_p": "Építkezés szakértő felügyelet mellett.", "step_5_h4": "Átadás", "step_5_p": "Üzembe helyezés és használatbavétel.",
            "faq_title": "Gyakori kérdések",
            "faq_1_q": "Mennyi ideig tart egy csarnok építése?", "faq_1_a": "A komplexitástól függően általában 4-7 hónapot vesz igénybe.", "faq_2_q": "Segítenek az engedélyekben?", "faq_2_a": "Igen, a generálkivitelezés részeként teljes körű ügyintézést vállalunk.", "faq_3_q": "Az Eurocode szerint építenek?", "faq_3_a": "Igen, minden projektünk megfelel az európai szabványoknak.", "faq_4_q": "Mi az a Holz100 technológia?", "faq_4_a": "Egy ragasztómentes tömörfa rendszer, amely különleges mikroklímát biztosít.", "faq_5_q": "Lengyelországon kívül is dolgoznak?", "faq_5_a": "Igen, komoly tapasztalatunk van Németországban és Norvégiában is.", "faq_6_q": "Gépészeti szerelést is vállalnak?", "faq_6_a": "Igen, specialitásunk az összetett ipari gépészet (TGA).",
            "contact_h2": "Van egy projektje?", "contact_p": "Lépjen kapcsolatba velünk ajánlatért.", "contact_direct_p": "Közvetlen kapcsolat:",
            "form_name_label": "Név", "form_email_label": "E-mail", "form_phone_label": "Telefon", "form_location_label": "Helyszín", "form_budget_label": "Tervezett költségvetés", "form_message_label": "Üzenet", "form_privacy_label": "Hozzájárulok az adataim kezeléséhez.", "form_submit": "Ajánlatkérés küldése", "form_placeholder_location": "pl. Budapest", "form_placeholder_message": "Röviden írja le a projektet...", "form_success": "Köszönjük, hamarosan keresni fogjuk.",
            "footer_brand_p": "Az Ön víziója, a mi megvalósításunk.", "footer_nav_label": "Navigáció", "footer_rights": "© 2026 Velor Construction. Minden jog fenntartva.",
            "career_h2": "Karrier", "career_p": "Szakértőket keresünk csapatunkba.", "career_benefits_p": "Amit kínálunk:", "career_benefit_1": "Érdekes nemzetközi projektek", "career_benefit_2": "Modern technológiák (BIM)", "career_benefit_3": "Szakmai fejlődési lehetőség",
            "career_position_label": "Pozíció", "career_pos_1": "Építésvezető", "career_pos_2": "Tervező mérnök", "career_pos_3": "Szerelő",
            "career_cv_label": "CV feltöltése (PDF)", "career_file_hint": "Max. 5MB", "career_message_label": "Motivációs levél", "form_placeholder_career_message": "Miért szeretne nálunk dolgozni?", "career_privacy_label": "Hozzájárulok az adataim kezeléséhez a toborzás során.", "career_submit": "Jelentkezés küldése", "career_success": "Jelentkezését sikeresen továbbítottuk."
        },
        "sk": {
            "page_title": "Velor Construction | Priemyselné haly a generálna dodávka",
            "meta_description": "Velor Construction — priemyselné haly, generálna dodávka a stavby z masívneho dreva Holz100. Európsky štandard, poľská realizácia.",
            "nav_start": "Start", "nav_why": "O nás", "nav_services": "Služby", "nav_realizations": "Skúsenosti", "nav_process": "Proces", "nav_career": "Kariéra", "nav_faq": "FAQ", "nav_contact": "Kontakt",
            "hero_h1": "Staviame s presnosťou.<br>Európsky Štandard.<br>Poľská Realizácia.",
            "hero_p": "Generálna dodávka priemyselných hál, skladov a technologických inštalácií. Inžinierska precíznosť, nekompromisná kvalita. Komunikácia: " + contact_list,
            "hero_cta_primary": "Začať projekt", "hero_cta_secondary": "Skúsenosti tímu",
            "trust_1": "✓ Skúsenosti z projektov v Nemecku, Nórsku a Poľsku", "trust_2": "✓ Infraštruktúra, kubatúra a inštalácie", "trust_3": "✓ Normy Eurokód a DIN", "trust_4": "✓ Full Project Management",
            "why_title": "Prečo Velor Construction?",
            "pillar_1_h3": "Inžinierska precíznosť", "pillar_1_p": "Skúsenosti zo škandinávskych a nemeckých trhov nám umožňujú realizovať najzložitejšie konštrukcie.",
            "pillar_2_h3": "Technológie a inštalácie", "pillar_2_p": "Navrhujeme a implementujeme pokročilé priemyselné inštalácie.",
            "pillar_3_h3": "Generálna dodávka", "pillar_3_p": "Preberáme plnú zodpovednosť za celý stavebný proces.",
            "services_title": "Rozsah služieb",
            "service_1_h3": "Oceľové haly a sklady", "service_1_p": "Projektovanie a montáž moderných oceľových konštrukcií.", "service_1_scope": "Optimalizácia",
            "service_2_h3": "Priemyselné inštalácie", "service_2_p": "Realizácia pokročilých technologických systémov.", "service_2_scope": "TGA",
            "service_3_h3": "Generálna dodávka", "service_3_p": "Komplexná realizácia v modeli Design & Build.", "service_3_scope": "Koordinácia",
            "service_4_h3": "Project Management", "service_4_p": "Profesionálna správa projektov s modernými nástrojmi.", "service_4_scope": "Štandardy",
            "service_5_h3": "Stavby Holz100", "service_5_p": "Ekologické stavby z masívneho dreva v rakúskej technológii.", "service_5_scope": "Masívne drevo",
            "holz_title": "Technológia Holz100", "holz_lead": "Revolučný systém stavieb z masívneho dreva bez lepidiel.",
            "holz_f1_h": "Nula chémie", "holz_f1_p": "Spájanie dreva pomocou bukových kolíkov.",
            "holz_f2_h": "Zdravá klíma", "holz_f2_p": "Prirodzená regulácia vlhkosti a teploty.",
            "holz_f3_h": "Požiarna bezpečnosť", "holz_f3_p": "Vysoká odolnost potvrdená certifikátmi.",
            "holz_f4_h": "Ekológia", "holz_f4_p": "Negatívna uhlíková stopa, ideálne pre ESG.",
            "holz_cta": "Viac o Holz100",
            "cases_title": "Naše skúsenosti", "cases_lead": "Vybrané realizácie nášho tímu.",
            "case_1_accent": "Mory 🇵🇱", "case_1_h3": "Showroom Brabus",
            "case_1_stat_1_label": "Model", "case_1_stat_1_val": "Design & Build",
            "case_1_stat_2_label": "Typ", "case_1_stat_2_val": "Prémiová hala",
            "case_2_accent": "Lübeck 🇩🇪", "case_2_h3": "Logistický terminál",
            "case_3_accent": "Bergen 🇳🇴", "case_3_h3": "Media City Bergen",
            "other_projects_title": "Ďalšie projekty",
            "p1_pl": "Hala Garwolin", "p1_de": "Sande Logistik", "p1_no": "Askøy Priemysel",
            "process_title": "Ako pracujeme",
            "step_1_h4": "Koncepcia", "step_1_p": "Analýza potrieb.", "step_2_h4": "Projektovanie", "step_2_p": "BIM a dokumentácia.", "step_3_h4": "Povolenia", "step_3_p": "Inžinierska činnosť.", "step_4_h4": "Realizácia", "step_4_p": "Výstavba.", "step_5_h4": "Odovzdanie", "step_5_p": "Spustenie prevádzky.",
            "faq_title": "Časté otázky",
            "faq_1_q": "Ako dlho trvá stavba haly?", "faq_1_a": "Zvyčajne 4-7 mesiacov.", "faq_2_q": "Pomáhate s povolením?", "faq_2_a": "Áno, zabezpečujeme kompletný inžiniering.", "faq_3_q": "Staviate podľa Eurokódov?", "faq_3_a": "Áno, dodržiavame všetky európske normy.", "faq_4_q": "Čo je Holz100?", "faq_4_a": "Systém z masívneho dreva bez lepidiel.",
            "contact_h2": "Máte projekt?", "contact_p": "Napíšte nám a pripravíme vám ponuku.", "contact_direct_p": "Priamy kontakt:",
            "form_name_label": "Meno", "form_email_label": "E-mail", "form_phone_label": "Telefón", "form_location_label": "Lokalita", "form_budget_label": "Rozpočet", "form_message_label": "Správa", "form_privacy_label": "Súhlasím so spracovaním údajov.", "form_submit": "Odeslať", "form_placeholder_location": "napr. Bratislava", "form_placeholder_message": "Opíšte váš projekt...", "form_success": "Ďakujeme, ozveme sa vám.",
            "footer_brand_p": "Vaša vízia, naša realizácia.", "footer_nav_label": "Navigácia", "footer_rights": "© 2026 Velor Construction. Všetky práva vyhradené.",
            "career_h2": "Kariéra", "career_p": "Hľadáme talentovaných ľudí.", "career_benefits_p": "Čo ponúkame:", "career_benefit_1": "Medzinárodné projekty", "career_benefit_2": "Moderné technológie", "career_benefit_3": "Kariérny rast",
            "career_position_label": "Pozícia", "career_pos_1": "Stavbyvedúci", "career_pos_2": "Projektant", "career_pos_3": "Montážnik",
            "career_cv_label": "Nahrajte CV", "career_file_hint": "Max. 5MB", "career_message_label": "Zpráva", "form_placeholder_career_message": "Prečo k nám?", "career_privacy_label": "Súhlasím so spracovaním.", "career_submit": "Odoslať", "career_success": "Odoslané."
        },
        "lt": {
            "page_title": "Velor Construction | Pramoninės salės ir generalinė ranga",
            "meta_description": "Velor Construction — pramoninės salės, generalinė ranga ir Holz100 masyvo medienos statyba. Europinis standartas, lenkiškas įgyvendinimas.",
            "nav_start": "Pradžia", "nav_why": "Apie mus", "nav_services": "Paslaugos", "nav_realizations": "Patirtis", "nav_process": "Procesas", "nav_career": "Karjera", "nav_faq": "DUK", "nav_contact": "Kontaktai",
            "hero_h1": "Statome tiksliai.<br>Europinis standartas.<br>Lenkiškas įgyvendinimas.",
            "hero_p": "Pramoninių salių, sandėlių ir technologinių įrenginių generalinė ranga. Inžinerinis tikslumas, bekompromisė kokybė. Komunikacija: " + contact_list,
            "hero_cta_primary": "Pradėti projektą", "hero_cta_secondary": "Komandos patirtis",
            "trust_1": "✓ Patirtis projektuose Vokietijoje, Norvegijoje ir Lenkijoje", "trust_2": "✓ Infrastruktūra, kubatūra ir instaliacijos", "trust_3": "✓ Eurokodų ir DIN standartai", "trust_4": "✓ Pilnas projekto valdymas",
            "why_title": "Kodėl Velor Construction?",
            "pillar_1_h3": "Inžinerinis tikslumas", "pillar_1_p": "Skandinavijos ir Vokietijos rinkų patirtis leidžia mums įgyvendinti sudėtingiausias konstrukcijas.",
            "pillar_2_h3": "Technologijos ir instaliacijos", "pillar_2_p": "Projektuojame ir diegiame pažangias pramonines instaliacijas.",
            "pillar_3_h3": "Generalinė ranga", "pillar_3_p": "Prisiimame pilną atsakomyę už visą statybos procesą.",
            "services_title": "Paslaugų spektras",
            "service_1_h3": "Plieninės salės ir sandėliai", "service_1_p": "Modernių plieno konstrukcijų projektavimas ir montavimas.", "service_1_scope": "Optimizavimas",
            "service_2_h3": "Pramoninės instaliacijos", "service_2_p": "Pažangių technologinių sistemų įgyvendinimas.", "service_2_scope": "TGA",
            "service_3_h3": "Generalinė ranga", "service_3_p": "Kompleksinis investicijų įgyvendinimas Design & Build modeliu.", "service_3_scope": "Koordinavimas",
            "service_4_h3": "Project Management", "service_4_p": "Profesionalus projektų valdymas naudojant šiuolaikinius įrankius.", "service_4_scope": "Standartai",
            "service_5_h3": "Holz100 statyba", "service_5_p": "Ekologiška masyvo medienos statyba pagal austrų technologiją.", "service_5_scope": "Masyvo mediena",
            "holz_title": "Holz100 technologija", "holz_lead": "Revoliucinė masyvo medienos statybos sistema be klijų.",
            "holz_f1_h": "Nulis chemijos", "holz_f1_p": "Medienos jungimas buko kaiščiais.",
            "holz_f2_h": "Sveikas mikroklimatas", "holz_f2_p": "Natūralus drėgmės ir temperatūros reguliavimas.",
            "holz_f3_h": "Priešgaisrinė sauga", "holz_f3_p": "Sertifikatais patvirtintas didelis atsparumas.",
            "holz_f4_h": "Ekologija", "holz_f4_p": "Neigiamas anglies pėdsakas, idealu ESG.",
            "holz_cta": "Sužinoti daugiau apie Holz100",
            "cases_title": "Mūsų patirtis", "cases_lead": "Atrinkti mūsų komandos projektai.",
            "case_1_accent": "Mory 🇵🇱", "case_1_h3": "Brabus salonas",
            "case_2_accent": "Lübeck 🇩🇪", "case_2_h3": "Logistikos terminalas",
            "case_3_accent": "Bergen 🇳🇴", "case_3_h3": "Media City Bergen",
            "other_projects_title": "Kiti projektai",
            "p1_pl": "Garwolin salė", "p1_de": "Sande logistika", "p1_no": "Askøy pramonė",
            "process_title": "Kaip mes dirbame",
            "step_1_h4": "Koncepcija", "step_1_p": "Poreikių analizė.", "step_2_h4": "Projektavimas", "step_2_p": "BIM ir dokumentacija.", "step_3_h4": "Leidimai", "step_3_p": "Inžinerinės paslaugos.", "step_4_h4": "Statyba", "step_4_p": "Įgyvendinimas.", "step_5_h4": "Perdavimas", "step_5_p": "Eksploatacijos pradžia.",
            "faq_title": "DUK",
            "faq_1_q": "Kiek laiko trunka salės statyba?", "faq_1_a": "Paprastai 4-7 mėnesius.", "faq_2_q": "Ar padedate gauti leidimus?", "faq_2_a": "Taip, atliekame pilną inžinerinį aptarnavimą.",
            "contact_h2": "Turite projektą?", "contact_p": "Susisiekite su mumis pasiūlymui.", "contact_direct_p": "Tiesioginis kontaktas:",
            "form_name_label": "Vardas, pavardė", "form_email_label": "El. paštas", "form_phone_label": "Telefonas", "form_location_label": "Vieta", "form_budget_label": "Biudžetas", "form_message_label": "Žinutė", "form_privacy_label": "Sutinku su duomenų tvarkymu.", "form_submit": "Siųsti", "form_placeholder_location": "pvz. Vilnius", "form_placeholder_message": "Aprašykite projektą...", "form_success": "Ačiū, susisieksime.",
            "footer_brand_p": "Jūsų vizija, mūsų įgyvendinimas.", "footer_nav_label": "Navigacija", "footer_rights": "© 2026 Velor Construction. Visos teisės saugomos.",
            "career_h2": "Karjera", "career_p": "Ieškome specialistų.", "career_benefits_p": "Ką siūlome:", "career_benefit_1": "Tarptautiniai projektai", "career_benefit_2": "Modernios technologijos", "career_benefit_3": "Karjeros galimybės",
            "career_position_label": "Pozicija", "career_pos_1": "Darbų vadovas", "career_pos_2": "Projektuotojas", "career_pos_3": "Montuotojas",
            "career_cv_label": "Įkelti CV", "career_file_hint": "Max. 5MB", "career_message_label": "Žinutė", "form_placeholder_career_message": "Kodėl pas mus?", "career_privacy_label": "Sutinku.", "career_submit": "Siųsti", "career_success": "Išsiųsta."
        },
        "nl": {
            "page_title": "Velor Construction | Industriële hallen en algemene aanneming",
            "meta_description": "Velor Construction — industriële hallen, algemene aanneming en Holz100 massief houten bouw. Europese standaard, Poolse uitvoering.",
            "nav_start": "Start", "nav_why": "Over ons", "nav_services": "Diensten", "nav_realizations": "Ervaring", "nav_process": "Proces", "nav_career": "Carrière", "nav_faq": "FAQ", "nav_contact": "Contact",
            "hero_h1": "Bouwen met precisie.<br>Europese Standaard.<br>Poolse Uitvoering.",
            "hero_p": "Algemene aanneming van industriële hallen, magazijnen en technologische installaties. Engineering precisie, compromisloze kwaliteit. Communicatie: " + contact_list,
            "hero_cta_primary": "Project starten", "hero_cta_secondary": "Teamervaring",
            "trust_1": "✓ Ervaring met projecten in Duitsland, Noorwegen en Polen", "trust_2": "✓ Infrastructuur, kubatuur en installaties", "trust_3": "✓ Eurocode en DIN normen", "trust_4": "✓ Full Project Management",
            "why_title": "Waarom Velor Construction?",
            "pillar_1_h3": "Engineering Precisie", "pillar_1_p": "Ervaring op de Scandinavische en Duitse markten stelt ons in staat de meest complexe constructies te realiseren.",
            "pillar_2_h3": "Technologie en Installaties", "pillar_2_p": "Wij ontwerpen en implementeren geavanceerde industriële installaties en HVAC-systemen.",
            "pillar_3_h3": "Algemene Aanneming", "pillar_3_p": "Wij nemen de volledige verantwoordelijkheid voor het bouwproces van A tot Z.",
            "services_title": "Diensten",
            "service_1_h3": "Stalen Hallen en Magazijnen", "service_1_p": "Ontwerp en montage van moderne staalconstructies.", "service_1_scope": "Optimalisatie",
            "service_2_h3": "Industriële Installaties", "service_2_p": "Realisatie van geavanceerde technologische systemen.", "service_2_scope": "TGA",
            "service_3_h3": "Algemene Aanneming", "service_3_p": "Complexe realisatie van investeringen in het Design & Build model.", "service_3_scope": "Coördinatie",
            "service_4_h3": "Project Management", "service_4_p": "Professioneel projectbeheer met moderne IT-tools.", "service_4_scope": "Standaarden",
            "service_5_h3": "Holz100 Bouw", "service_5_p": "Ecologische massief houten bouw met Oostenrijkse technologie.", "service_5_scope": "Massief hout",
            "holz_title": "Holz100 Technologie", "holz_lead": "Revolutionair massief houten bouwsysteem zonder lijm.",
            "holz_f1_h": "Nul chemie", "holz_f1_p": "Verbinding van hout met beuken deuvels.",
            "holz_f2_h": "Gezond klimaat", "holz_f2_p": "Natuurlijke vocht- en temperatuurregeling.",
            "holz_f3_h": "Brandveiligheid", "holz_f3_p": "Hoge weerstand bevestigd door certificaten.",
            "holz_f4_h": "Ecologie", "holz_f4_p": "Negatieve CO2-voetafdruk, ideaal voor ESG.",
            "holz_cta": "Meer over Holz100",
            "cases_title": "Onze ervaring", "cases_lead": "Geselecteerde realisaties van ons team.",
            "case_1_accent": "Mory 🇵🇱", "case_1_h3": "Brabus Showroom",
            "case_2_accent": "Lübeck 🇩🇪", "case_2_h3": "Logistieke Terminal",
            "case_3_accent": "Bergen 🇳🇴", "case_3_h3": "Media City Bergen",
            "other_projects_title": "Overige projecten",
            "p1_pl": "Hala Garwolin", "p1_de": "Sande Logistik", "p1_no": "Askøy Industrie",
            "process_title": "Onze werkwijze",
            "step_1_h4": "Concept", "step_1_p": "Behoefteanalyse.", "step_2_h4": "Ontwerp", "step_2_p": "BIM en documentatie.", "step_3_h4": "Vergunningen", "step_3_p": "Engineering diensten.", "step_4_h4": "Realisatie", "step_4_p": "Bouwfase.", "step_5_h4": "Oplevering", "step_5_p": "Ingebruikname.",
            "faq_title": "Veelgestelde vragen",
            "faq_1_q": "Hoe lang duurt de bouw van een hal?", "faq_1_a": "Meestal 4 tot 7 maanden.", "faq_2_q": "Helpen jullie bij vergunningen?", "faq_2_a": "Ja, wij verzorgen de volledige engineering.",
            "contact_h2": "Heeft u een project?", "contact_p": "Neem contact op voor een offerte.", "contact_direct_p": "Direct contact:",
            "form_name_label": "Naam", "form_email_label": "E-mail", "form_phone_label": "Telefoon", "form_location_label": "Locatie", "form_budget_label": "Budget", "form_message_label": "Bericht", "form_privacy_label": "Ik ga akkoord met de verwerking van mijn gegevens.", "form_submit": "Verstuur", "form_placeholder_location": "bijv. Amsterdam", "form_placeholder_message": "Beschrijf uw project...", "form_success": "Bedankt, we nemen contact op.",
            "footer_brand_p": "Uw visie, onze realisatie.", "footer_nav_label": "Navigatie", "footer_rights": "© 2026 Velor Construction. Alle rechten voorbehouden.",
            "career_h2": "Carrière", "career_p": "Wij zoeken experts.", "career_benefits_p": "Wat wij bieden:", "career_benefit_1": "Internationale projecten", "career_benefit_2": "Moderne technologieën", "career_benefit_3": "Groeimogelijkheden",
            "career_position_label": "Functie", "career_pos_1": "Site Manager", "career_pos_2": "Ontwerper", "career_pos_3": "Monteur",
            "career_cv_label": "Upload CV", "career_file_hint": "Max. 5MB", "career_message_label": "Bericht", "form_placeholder_career_message": "Waarom bij ons?", "career_privacy_label": "Ik ga akkoord.", "career_submit": "Solliciteer", "career_success": "Verzonden."
        },
        "no": {
            "page_title": "Velor Construction | Industrihaller og totalentreprise",
            "meta_description": "Velor Construction — industrihaller, totalentreprise og Holz100 massivtrebygg. Europeisk standard, polsk utførelse.",
            "nav_start": "Hjem", "nav_why": "Om oss", "nav_services": "Tjenester", "nav_realizations": "Erfaring", "nav_process": "Prosess", "nav_career": "Karriere", "nav_faq": "FAQ", "nav_contact": "Kontakt",
            "hero_h1": "Bygger med presisjon.<br>Europeisk Standard.<br>Polsk Utførelse.",
            "hero_p": "Totalentreprise for industrihaller, lager og teknologiske installasjoner. Ingeniørpresisjon, kompromissløs kvalitet. Kommunikasjon: " + contact_list,
            "hero_cta_primary": "Start prosjekt", "hero_cta_secondary": "Teamerfaring",
            "trust_1": "✓ Erfaring fra prosjekter i Tyskland, Norge og Polen", "trust_2": "✓ Infrastruktur, kubatur og installasjoner", "trust_3": "✓ Eurokode og DIN standarder", "trust_4": "✓ Full Project Management",
            "why_title": "Hvorfor Velor Construction?",
            "pillar_1_h3": "Ingeniørpresisjon", "pillar_1_p": "Erfaring fra det skandinaviske og tyske markedet gjør oss i stand til å realisere de mest komplekse konstruksjonene.",
            "pillar_2_h3": "Teknologi og Installasjoner", "pillar_2_p": "Vi designer og implementerer avanserte industrielle installasjoner og VVS-systemer.",
            "pillar_3_h3": "Totalentreprise", "pillar_3_p": "Vi tar fullt ansvar for hele byggeprosessen fra A til Å.",
            "services_title": "Tjenester",
            "service_1_h3": "Stålhaller og Lager", "service_1_p": "Prosjektering og montering av moderne stålkonstruksjoner.", "service_1_scope": "Optimalisering",
            "service_2_h3": "Industrielle Installasjoner", "service_2_p": "Realisering av avanserte teknologiske systemer.", "service_2_scope": "TGA",
            "service_3_h3": "Totalentreprise", "service_3_p": "Kompleks realisering av investeringer i Design & Build-modellen.", "service_3_scope": "Koordinering",
            "service_4_h3": "Project Management", "service_4_p": "Profesjonell prosjektledelse med moderne IT-verktøy.", "service_4_scope": "Standarder",
            "service_5_h3": "Holz100 Bygg", "service_5_p": "Økologiske massivtrebygg med østerriksk teknologi.", "service_5_scope": "Massivtre",
            "holz_title": "Holz100 Teknologi", "holz_lead": "Revolusjonerende byggesystem i massivtre uten lim.",
            "holz_f1_h": "Null kjemi", "holz_f1_p": "Sammenføyning av tre med bøkedybler.",
            "holz_f2_h": "Sunt klima", "holz_f2_p": "Naturlig fukt- og temperaturregulering.",
            "holz_f3_h": "Brannsikkerhet", "holz_f3_p": "Høy motstand bekreftet av sertifikater.",
            "holz_f4_h": "Økologi", "holz_f4_p": "Negativt CO2-avtrykk, ideelt for ESG.",
            "holz_cta": "Mer om Holz100",
            "cases_title": "Vår erfaring", "cases_lead": "Utvalgte prosjekter fra vårt team.",
            "case_1_accent": "Mory 🇵🇱", "case_1_h3": "Brabus Showroom",
            "case_2_accent": "Lübeck 🇩🇪", "case_2_h3": "Logistikkterminal",
            "case_3_accent": "Bergen 🇳🇴", "case_3_h3": "Media City Bergen",
            "other_projects_title": "Andre prosjekter",
            "p1_pl": "Hala Garwolin", "p1_de": "Sande Logistikk", "p1_no": "Askøy Industri",
            "process_title": "Slik jobber vi",
            "step_1_h4": "Konsept", "step_1_p": "Behovsanalyse.", "step_2_h4": "Prosjektering", "step_2_p": "BIM og dokumentasjon.", "step_3_h4": "Tillatelser", "step_3_p": "Ingeniørtjenester.", "step_4_h4": "Bygging", "step_4_p": "Realisering.", "step_5_h4": "Overlevering", "step_5_p": "Igangsetting.",
            "faq_title": "Ofte stilte spørsmål",
            "faq_1_q": "Hvor lang tid tar det å bygge en hall?", "faq_1_a": "Vanligvis 4 til 7 måneder.", "faq_2_q": "Hjelper dere med tillatelser?", "faq_2_a": "Ja, vi tar oss av hele prosjekteringen.",
            "contact_h2": "Har du et prosjekt?", "contact_p": "Kontakt oss for et tilbud.", "contact_direct_p": "Direkte kontakt:",
            "form_name_label": "Navn", "form_email_label": "E-post", "form_phone_label": "Telefon", "form_location_label": "Sted", "form_budget_label": "Budsjett", "form_message_label": "Melding", "form_privacy_label": "Jeg samtykker til behandling av mine data.", "form_submit": "Send", "form_placeholder_location": "f.eks. Oslo", "form_placeholder_message": "Beskriv prosjektet ditt...", "form_success": "Takk, vi tar kontakt.",
            "footer_brand_p": "Din visjon, vår utførelse.", "footer_nav_label": "Navigasjon", "footer_rights": "© 2026 Velor Construction. Alle rettigheter reservert.",
            "career_h2": "Karriere", "career_p": "Vi søker eksperter.", "career_benefits_p": "Hva vi tilbyr:", "career_benefit_1": "Internasjonale prosjekter", "career_benefit_2": "Moderne teknologi", "career_benefit_3": "Karrieremuligheter",
            "career_position_label": "Stilling", "career_pos_1": "Anleggsleder", "career_pos_2": "Prosjekterende", "career_pos_3": "Montør",
            "career_cv_label": "Last opp CV", "career_file_hint": "Maks 5MB", "career_message_label": "Melding", "form_placeholder_career_message": "Hvorfor hos oss?", "career_privacy_label": "Jeg samtykker.", "career_submit": "Søk", "career_success": "Sendt."
        },
        "hr": {
            "page_title": "Velor Construction | Industrijske hale i generalno izvođaštvo",
            "meta_description": "Velor Construction — industrijske hale, generalno izvođaštvo i Holz100 gradnja od masivnog drva. Europski standard, poljska realizacija.",
            "nav_start": "Početna", "nav_why": "O nama", "nav_services": "Usluge", "nav_realizations": "Iskustvo", "nav_process": "Proces", "nav_career": "Karijera", "nav_faq": "FAQ", "nav_contact": "Kontakt",
            "hero_h1": "Gradimo s preciznošću.<br>Europski Standard.<br>Poljska Realizacija.",
            "hero_p": "Generalno izvođaštvo industrijskih hala, skladišta i tehnoloških instalacija. Inženjerska preciznost, beskompromisna kvaliteta. Komunikacija: " + contact_list,
            "hero_cta_primary": "Započni projekt", "hero_cta_secondary": "Iskustvo tima",
            "trust_1": "✓ Iskustvo na projektima u Njemačkoj, Norveškoj i Poljskoj", "trust_2": "✓ Infrastruktura, kubatura i instalacije", "trust_3": "✓ Eurocode i DIN standardi", "trust_4": "✓ Potpuno upravljanje projektom",
            "why_title": "Zašto Velor Construction?",
            "pillar_1_h3": "Inženjerska preciznost", "pillar_1_p": "Iskustvo sa skandinavskih i njemačkih tržišta omogućuje nam realizaciju najsloženijih konstrukcija.",
            "pillar_2_h3": "Tehnologija i instalacije", "pillar_2_p": "Projektiramo i implementiramo napredne industrijske instalacije i HVAC sustave.",
            "pillar_3_h3": "Generalno izvođaštvo", "pillar_3_p": "Preuzimamo potpunu odgovornost za cijeli proces gradnje od A do Ž.",
            "services_title": "Opseg usluga",
            "service_1_h3": "Čelične hale i skladišta", "service_1_p": "Projektiranje i montaža modernih čeličnih konstrukcija.", "service_1_scope": "Optimizacija",
            "service_2_h3": "Industrijske instalacije", "service_2_p": "Realizacija naprednih tehnoloških sustava.", "service_2_scope": "TGA",
            "service_3_h3": "Generalno izvođaštvo", "service_3_p": "Kompleksna realizacija investicija u Design & Build modelu.", "service_3_scope": "Koordinacija",
            "service_4_h3": "Project Management", "service_4_p": "Profesionalno upravljanje projektima uz moderne IT alate.", "service_4_scope": "Standardi",
            "service_5_h3": "Gradnja Holz100", "service_5_p": "Ekološka gradnja od masivnog drva austrijskom tehnologijom.", "service_5_scope": "Masivno drvo",
            "holz_title": "Tehnologija Holz100", "holz_lead": "Revolucionarni sustav gradnje od masivnog drva bez ljepila.",
            "holz_f1_h": "Nula kemije", "holz_f1_p": "Spajanje drva pomoću bukovih tipli.",
            "holz_f2_h": "Zdrava mikroklima", "holz_f2_p": "Prirodna regulacija vlage i temperature.",
            "holz_f3_h": "Vatrootpornost", "holz_f3_p": "Visoka otpornost potvrđena certifikatima.",
            "holz_f4_h": "Ekologija", "holz_f4_p": "Negativan CO2 otisak, idealno za ESG.",
            "holz_cta": "Više o Holz100",
            "cases_title": "Naše iskustvo", "cases_lead": "Odabrane realizacije našeg tima.",
            "case_1_accent": "Mory 🇵🇱", "case_1_h3": "Brabus Showroom",
            "case_2_accent": "Lübeck 🇩🇪", "case_2_h3": "Logistički terminal",
            "case_3_accent": "Bergen 🇳🇴", "case_3_h3": "Media City Bergen",
            "other_projects_title": "Ostali projekti",
            "p1_pl": "Hala Garwolin", "p1_de": "Sande Logistika", "p1_no": "Askøy Industri",
            "process_title": "Kako radimo",
            "step_1_h4": "Koncept", "step_1_p": "Analiza potreba.", "step_2_h4": "Projektiranje", "step_2_p": "BIM i dokumentacija.", "step_3_h4": "Dozvole", "step_3_p": "Inženjerske usluge.", "step_4_h4": "Gradnja", "step_4_p": "Realizacija.", "step_5_h4": "Primopredaja", "step_5_p": "Puštanje u rad.",
            "faq_title": "Česta pitanja",
            "faq_1_q": "Koliko traje gradnja hale?", "faq_1_a": "Obično 4 do 7 mjeseci.", "faq_2_q": "Pomažete li s dozvolama?", "faq_2_a": "Da, osiguravamo kompletan inženjering.",
            "contact_h2": "Imate projekt?", "contact_p": "Kontaktirajte nas za ponudu.", "contact_direct_p": "Izravan kontakt:",
            "form_name_label": "Ime i prezime", "form_email_label": "E-mail", "form_phone_label": "Telefon", "form_location_label": "Lokacija", "form_budget_label": "Budžet", "form_message_label": "Poruka", "form_privacy_label": "Pristajem na obradu podataka.", "form_submit": "Pošalji", "form_placeholder_location": "npr. Zagreb", "form_placeholder_message": "Opišite vaš projekt...", "form_success": "Hvala, javit ćemo se.",
            "footer_brand_p": "Vaša vizija, naša realizacija.", "footer_nav_label": "Navigacija", "footer_rights": "© 2026 Velor Construction. Sva prava pridržana.",
            "career_h2": "Karijera", "career_p": "Tražimo stručnjake.", "career_benefits_p": "Što nudimo:", "career_benefit_1": "Međunarodni projekti", "career_benefit_2": "Moderne tehnologije", "career_benefit_3": "Mogućnost napredovanja",
            "career_position_label": "Pozicija", "career_pos_1": "Voditelj gradilišta", "career_pos_2": "Projektant", "career_pos_3": "Monter",
            "career_cv_label": "Učitaj CV", "career_file_hint": "Maks. 5MB", "career_message_label": "Poruka", "form_placeholder_career_message": "Zašto kod nas?", "career_privacy_label": "Pristajem.", "career_submit": "Prijavi se", "career_success": "Poslano."
        }
    }

    # Fill missing keys from English
    for lang in translations:
        for k in en:
            if k not in translations[lang]:
                translations[lang][k] = en[k]

    # UPDATE HERO P and DROPDOWN in the actual content
    # Dropdown update: ensure all requested languages are in the list
    new_dropdown = """                        <div class="lang-option active" data-lang="pl">🇵🇱 PL</div>
                        <div class="lang-option" data-lang="en">🇬🇧 EN</div>
                        <div class="lang-option" data-lang="de">🇩🇪 DE</div>
                        <div class="lang-option" data-lang="fr">🇫🇷 FR</div>
                        <div class="lang-option" data-lang="es">🇪🇸 ES</div>
                        <div class="lang-option" data-lang="cs">🇨🇿 CS</div>
                        <div class="lang-option" data-lang="hu">🇭🇺 HU</div>
                        <div class="lang-option" data-lang="sk">🇸🇰 SK</div>
                        <div class="lang-option" data-lang="lt">🇱🇹 LT</div>
                        <div class="lang-option" data-lang="nl">🇳🇱 NL</div>
                        <div class="lang-option" data-lang="no">🇳🇴 NO</div>
                        <div class="lang-option" data-lang="hr">🇭🇷 HR</div>
                        <div class="lang-option" data-lang="ru">🇷🇺 RU</div>
                        <div class="lang-option" data-lang="ua">🇺🇦 UA</div>"""

    content = re.sub(r'<div class="lang-option active" data-lang="pl">.*?🇺🇦 UA</div>', new_dropdown, content, flags=re.DOTALL)

    # Hero P update (static fallback)
    pattern = r'PL · EN · DE · FR · ES · RU · UA'
    content = re.sub(pattern, contact_list, content)

    # RE-INJECT TRANSLATIONS
    for lang, obj in translations.items():
        # Only inject the ones I explicitly managed here (the 7 new ones)
        # For existing ones, I'll do a simple regex replace for hero_p only
        pattern = r'"' + lang + r'": \{.*?\n\s+\}'
        if lang in ["cs", "hu", "sk", "lt", "nl", "no", "hr"]:
            # Inject full block
            if re.search(f'"{lang}": {{', content):
                # Replace existing placeholder block
                block = f'"{lang}": {{\n'
                items = list(obj.items())
                for i, (k, v) in enumerate(items):
                    escaped_v = v.replace('"', '\\"').replace('\n', '\\n')
                    comma = "," if i < len(items) - 1 else ""
                    block += f'                "{k}": "{escaped_v}"{comma}\n'
                block += '            }'
                content = re.sub(pattern, block, content, flags=re.DOTALL)
            else:
                # Append to translations object before the last closing brace
                block = f',\n            "{lang}": {{\n'
                items = list(obj.items())
                for i, (k, v) in enumerate(items):
                    escaped_v = v.replace('"', '\\"').replace('\n', '\\n')
                    comma = "," if i < len(items) - 1 else ""
                    block += f'                "{k}": "{escaped_v}"{comma}\n'
                block += '            }'
                content = re.sub(r'(\s+\}\s+\};)', block + r'\1', content)
        else:
            # For existing ones (PL, EN, etc), just update hero_p
            # This is safer to avoid breaking their translations
            lang_match = re.search(f'"{lang}": ({{.*?\n\s+}})', content, re.DOTALL)
            if lang_match:
                inner = lang_match.group(1)
                new_inner = re.sub(pattern, contact_list, inner)
                content = content.replace(inner, new_inner)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    update()
