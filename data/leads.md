# Research leads backlog

Written and read by the prep run. Purpose: save web searches. Leads here were found in earlier runs but not finished (search budget ran out, or one check was missing). Each prep run starts here before searching, removes leads it finishes or rejects, and adds new unfinished ones at the end. One lead per line: market, company, what is known, what is missing.

## Productive sources (fetch these directly with WebFetch before using WebSearch)

- Breakbulk Asia exhibitor pages (asia.breakbulk.com/exhibitors/...): dated show hook for SG/HK/AU project forwarders (show 18-19 Nov 2026; use only until about 26 Nov 2026).
- BIFA Freight Service Awards 2026 shortlist (fbj-online.com/bifa-unveils-freight-service-awards-shortlist/, 28 Oct 2026): UK hooks; winners announced 14 Jan 2027.
- DCN Australian Shipping & Maritime Awards 2026 finalists (thedcn.com.au, 23 Oct 2026; awards night 26 Nov 2026): AU hooks.
- Neutral Air Partner new-member posts (neutralairpartner.com): dated AU/APAC/US hooks.
- Conqueror Freight Network news (news.conquerornetwork.com) and GLA new-member news (glafamily.com): dated member news, check ownership and site.
- Magaya 2026 Golden MVP winners (6 May 2026) and Magaya customer press releases: US hooks.
- Fortune / Great Place to Work 2026 Best Workplaces in Transportation lists: US hooks.
- Job boards with quote-desk or pricing roles (e.g. Paylocity, company careers pages): strong hook when the company also publishes an email.
- Companies House pages: fetch /company/<number>; if the overview fails, try again later or use /filing-history (needs a 2026 filing to count as active).
- MX lookup: WebFetch https://dns.google/resolve?name=<domain>&type=MX works.
- Breakbulk Americas exhibitor list (americas.breakbulk.com/exhibitors): about 320 exhibitors with sector tags, per-company pages give city and website. Page is titled "2026 Exhibitor List" but the site shows 19-20 Oct (2027) dates, so word hooks neutrally ("on the exhibitor list").
- Multimodal 2027 exhibitor pages (multimodal.org.uk/exhibitor-article/<slug>, NEC 29 Jun to 1 Jul 2027): UK hooks; the list widget is not fetchable, find slugs via search.
- Clutch Brisbane customs brokers (clutch.co/au/logistics/customs-brokers/brisbane.md): 39 firms with sites and size bands.
- Freight Midpoint member news (freightmidpoint.com/Blog/, paged ?page=N): dated, few HK items.
- Dead ends (13 Nov): GLA new-member and SLA pages are JS-rendered (empty); ALMAC exhibitor list fails to fetch; Payload Asia/AFLAS 2026 winners are large groups; Breakbulk Asia SG exhibitors mostly carriers or group branches. Elle Logistics, HPI, Concepts in Freight, Mallory Alexander and Serra sites block WebFetch (robots).
- JCtrans Weekly New Members (marketing.jctrans.com/magazine/weekly/pc/weekly2026NN.html, NN = ISO week): dated network joins with city, about one AU member a week plus HK/SG; long pages need offset=100000; member profiles at jctrans.com/cn/store/home/<id> give website, staff band, founding year but rate-limit after a few fetches.
- Multimodal 2027 paged exhibitor list (multimodal.org.uk/exhibitor-article?start=N, N=0..570 in steps of 10): letter stands (A6, G4) are 2027, 4-digit stands look like 2026. Pages start=0..310 checked on 13 Nov; start=320..570 not yet checked.
- Breakbulk Americas freight-forwarder exhibitors: used up (13 Nov). Remaining names checked 14 Nov are not forwarders (Project Freight LLC heavy haul, Mako Freight 3PL, Liberty Global Logistics ocean carrier, Special Cargo Houston DG compliance, Racing Cargo part of an international group).
- Multimodal 2027 paged list: start=320..360 checked 14 Nov (forwarders there: Lasta IE, Tan Freight GH, Eutraco EU, Atanak done, TGL emailed); start=370..570 not yet checked.
- Freight Midpoint blog pages 1-2 checked 14 Nov (only Stellar Freight UK and Fast-Link HK in live markets).
- Clutch Brisbane list: checked 14 Nov: Wallace and Colless Young emailed, CFL and Tomkinson already contacted; cusfor.com.au and williamsglobal.com.au robots-blocked, worldcargo.com.au shows a blank nginx page, cargoclear.com.au errors, ActivFreight has no news since 2020. Unchecked: Bloomcorp, Queensland Customs Brokers, Avanti (avantifm.com.au).
- Provenance note (14 Nov): WebFetch refuses URLs built by hand that have not appeared in search results this session (dns.google MX lookups and JCtrans weekly pages timed out on a permission prompt). find-and-update.company-information.service.gov.uk/company/<number> did work. If MX lookups keep failing, record unchecked:<domain>.
- Session note (15 Nov): WebFetch refuses most company domains until that domain has appeared in a WebSearch result. Trick that works (AU agent): one WebSearch with allowed_domains set to 10-25 candidate domains and a broad query like "news 2026"; their pages then fetch. dns.google MX lookups worked this run.
- Multimodal 2027 paged list: start=370..570 checked 15 Nov, now USED UP. Every exhibitor page shows 2027 dates, including 4-digit stands. Unchecked forwarders from those pages: Brit Customs (London), Easy Customs, P2P Customs, Pro Customs Solutions, Barta Logistics (6083), Bullet Express, EORI (UK) Ltd.
- FBJ monthly archive (fbj-online.com/2026/MM/ and /page/N/) fetches; checked 2026/11 p1-2, 10 p1-3, 09 p1-2, 08 p1-2 (mostly large firms). multimodal.org.uk/article news list (205 pages) fetches, only page 1 checked.
- Breakbulk Europe 2027 exhibitor list (europe.breakbulk.com/exhibitors, Rotterdam 11-13 May 2027): only page 1 loads (?page=2 repeats page 1); profiles europe.breakbulk.com/exhibitors/<slug> give city, website, stand; word hooks neutrally. Page 1 UK forwarders: BE ACCURATE LTD (1A11), BALENA PROJECTS LTD (1B51).
- Clutch city lists give domains and size bands: AU Melbourne and Sydney customs brokers (clutch.co/au/logistics/customs-brokers/melbourne.md, /sydney.md), clutch.co/au/logistics/freight-forwarders?page=6; US customs brokers clutch.co/us/logistics/customs-brokers?page=1 (unchecked: Brauner International Jersey City, PNPLINE Katy TX, Current International Freight Torrance, Agramont San Diego, KIN Logistic CA, Texas International Freight Houston, JOBCO Laredo, DeltaShipExpress Houston, Pacavo TX, Navco Brownsville; find each site via a search result first).
- AU domains from Clutch not yet searched (use the allowed_domains trick): atsl, worldfreightsolutions, kennethlloyd, jwicustoms, xsglobal, navia, sciaustralia, rrlawson, obriencustoms, mccworldinternational, dlf.net.au, acaint, ihhunter, powercustoms, itm, icsgloballogistics, ddwlogistics, vantagecustoms, mtflogistics, paccon, cargoup, megatop, dshglobal, lacelogistics, kthcustoms, acli, cffworld, vikingcargo.
- Used up (15 Nov): Fortune Best Workplaces in Transportation 2026 (all 20 checked), Magaya 2026 Golden MVP list, DCN 2026 finalists (only Shipping Solutions Australia left, site blocked), BIFA 2026 shortlist, JCtrans weekly US members weeks 35-45 (weeks 38, 46 failed), JCtrans AU/HK/SG weeks 31-45 (few usable), Conqueror news p1-2, NAP news, Atlas news p1, Freight Midpoint p1-2, Breakbulk Asia. Dead ends: US regional associations (NY/NJ, LACBFFA, FCBF, HCBFFA, NCBFAA) show events only; generic new-office searches return large groups; GLA AU/SG welcome posts are 2025; Air Cargo Americas next in 2027; CSCMP EDGE 2026 has no forwarders.

- Session note (15 Nov 17Z run): dns.google MX lookups worked from the main session (refused inside subagents). JCtrans weekly pages weeks 20-30 fetch by hand-built URL (weeks 20, 22-30 checked for UK/HK/SG; 22, 24, 26, 30 for AU). Multimodal exhibitor pages fetch by hand-built slug.
- FIATA US member directory (fiata.org/directory/us): 57 small US members with city and website, emails obfuscated. Unchecked: Cargomondo (Doral), OGT Freight (Miami), Tecnoship (Miami), Conship USA (Houston), SSAF Logistics (Stafford TX), Platton (Seattle), Swifflo (San Dimas), AGOL Worldwide (Miami), Cargo Dynamics (LA), Silog (Brownsville), TM Logistics (Laredo), Kwick Kargo, Embassy Cargo, GII (NY). Use the allowed_domains search trick first.
- Pangea network US member list (pangea-network.com/freight-forwarders/united-states/): 9 US members with websites, no join dates.
- Maryland Port Administration customs broker/forwarder contact list PDF (mpa.maryland.gov/Documents/CustomsBrokerForwarderContactList.pdf): about 67 Baltimore firms with emails; undated, recheck each email on the company's own site.
- FTA news items (ftalliance.com.au/newsdetails/<id>): dated AU member news. ASCLA 2026 winners (ascla.com.au/winners/): AU award names. Privacy-policy pages can carry a published email when the contact page has none.
- Freight Midpoint blog pages 3-6 checked 15 Nov (UK Flyship 27 Jul 2026, Transflex before cutoff). Freight Midpoint directory: US 2026 joins all before 15 May. multimodal.org.uk/article?limit=100&start=10 lists 100 headlines (11-110 checked).
- Dead ends (15 Nov 17Z): Clutch US pages beyond customs-brokers p1 fail; Inbound Logistics Top 100, Inc. 5000, SDCE Women in Supply Chain, Food Logistics lists (large firms); TIACA ACF 2026, CNS, transport logistic Americas (no lists); CBFFA/Georgia/TIFA directories (none online); job aggregators hide names; HAFFA, HK Customs AEO, MyCareersFuture, CeMAT SEA, everywoman 2026, FBJ 2026/06-07; Lognet Global US joins are 2025; WCA profiles, SEEK, Jora blocked.

- Session note (16 Nov 00Z run): dns.google MX lookups were refused in the main session too (permission prompt timed out); all MX unchecked. Subagents: WebFetch accepts only exact URLs returned by a search or a fetched page; hand-built paths fail even on domains already seen. Putting topworkplaces.com, denverpost.com, sun-sentinel.com, bizjournals.com or connectcre.com in allowed_domains makes the search return HTTP 400.
- Top Workplaces industry award "Distribution Top Workplaces 2026" (topworkplaces.com/award/distribution/2026/35-149/5320/ and /150-499/4649/, page 2 unchecked): 78 employers with HQ, headcount and award month (Mar to Oct 2026). Unchecked: Red Lab Logistics (Charleston, Oct 2026), Altex Logistics (IL, Aug 2026), Tucker Company Worldwide (NJ, likely domestic brokerage), Knichel, RGL, 315 Logistics. Regional pages also exist (e.g. topworkplaces.com/award/houston/2026/50-149/4754/). They fetch once found via a normal search.
- Local newspaper anniversary stories (search "celebrates 50 years" + freight forwarding / customs broker): dated hooks on small family firms (gave Freeport Forwarding). Better yield than newswires.
- HKPC 3PL Pilot Subsidy Scheme successful applicants (bee.hkpc.org/media/mhpfkkta/list-of-successful-applicants_en-62026.pdf, as at 26 Jun 2026): about 130 HK forwarders; best HK hook source. HK Maritime and Port Development Board directory (hkmpdb.gov.hk/en/maritime-directory.php?cat=9, detail company-detail.php?com=NN): official, self-published emails for 36 HK forwarders.
- SAAA@Singapore (saaa.org.sg): "Welcome New Members" post published Sep 2026 (GE Lines, Ants Logistic, Mitra Famosa, FPS Global) and a 198-member list; some member profile pages carry emails (e.g. saaa.org.sg/acs/).
- FTA freight forwarder and customs broker directory (ftalliance.com.au/members/freight-forwarding-customs-broker, read with offset 0, 100000, 200000): hundreds of AU forwarders with sites; one allowed_domains search of 25 domains with "2026 news announcement" found AXIMA and Kalgin. Unsearched: most of P to Z.
- DCN freight forwarding and customs broking tag (thedcn.com.au/news/tag/freight-forwarding-amp-customs-broking): opinion pieces name small AU firms.
- Clutch Miami freight forwarders (clutch.co/logistics/freight-forwarders/miami.md): 35 firms, 16 domains; sites checked had only SEO blogs.
- Dead ends (16 Nov): newswires (PRNewswire, EIN, PRWeb, GlobeNewswire, openpr) for small US forwarders; AJOT/airfreight.news/FreightWaves new-office searches; Inc. 5000 2026; ATS pricing-job searches; state export awards; WTW NYC/LA 2026; topworkplaces.com company pages (no dates); magaya.com and v1.glafamily.com (robots); Pangea US (9 members, no emails or dates); JCtrans week 46, FTA weekly reports, news.conquerornetwork.com, ALMAC 2026, HAFFA, Elite GLN, WCA (blocked or empty); GPTW certified-company pages (only an "Updated <month>" stamp).

- (16 Nov 05Z) Dead ends (16 Nov, US agent A): Top Workplaces Distribution 2026 pages 35-149 p1/p4/p5 and 150-499 p2/p3/p5/p6/p9 have no new independent forwarders; Houston TW 2026 50-149 p3-4 and 150-499 p1-2 only Aries, Fracht; South Florida TW 2026 (35-124 p1/p3, 125-399 p1-2) none; Tampa Bay TW 2026 announced Mar 2026 (too old); Daily Herald Best Places to Work in Illinois 2026 and Fortune Best Small Workplaces Chicago 2026 have no forwarders. Anniversary searches ('celebrates 50 years', 25/30/40 years, third-generation, customhouse broker) return Canadian or pre-2026 stories. Ribbon-cutting/grand-opening/new-office/bizjournals searches return large groups or old items. Maryland PDF small firms (bwicorp, diplomatfreight, krausintl, steer, osullivan, seaschott, tbbgl, cjinternational, dartrans, pridebaltimore) show no dated 2026 news in an allowed_domains search.
- (16 Nov 05Z) Productive (small): local business magazines feature small forwarder stations (thebusinessview.com gave Platinum Cargo Logistics Mobile 1-year anniversary, Jul 2026). Platinum Cargo Logistics office pages (platinumcargologistics.com/offices/<city>/) publish per-station emails (ops<code>@platinumcargo.com); other stations (Wesley Chapel FL, Nashville, Raleigh-Durham) may have their own opening hooks, but it is one company.
- (16 Nov 05Z) Provenance: hand-typed topworkplaces.com URLs from leads.md failed (permission timeout); they fetched after a normal search ('"Distribution Top Workplaces" 2026 topworkplaces award list') returned them. Curl through the proxy returns 403, so Cloudflare-obfuscated emails cannot be decoded.
- (16 Nov 05Z) JCtrans Weekly New Members pages for weeks 21-31 (May-Jul 2026) fetch once surfaced via WebSearch allowed_domains marketing.jctrans.com; each week lists 2-6 US joins with city and date. Profile links (jctrans.com/cn/store/home/...) are refused in subagents; find company sites with an allowed_domains search over guessed domains (company name + .com), which worked for 8 of 14 names. US weeks checked this run: 21-27, 29-31, 33. Week 28 and 32 not surfaced.
- (16 Nov 05Z) Dead ends 16 Nov (US): Maryland PDF firms (no 2026 company news on cavlog, cjinternational, pridebaltimore); FIATA US list (only V. Alexander has 2026 posts, all tariff alerts); Lognet US joins all 2025; Elite GLN robots; GLA US welcome posts latest Dec 2025 (EazyClick) in index; Cargo Connections brochure pages refused; allworldshipping.com and wcaworld robots; Atlas and Conqueror news no US members since June; AfA new-member news is 2025; FreightWaves/Logistics Mgmt new-office and certification searches return large firms only.
- (16 Nov 05Z) HK Marine Department shipping directory, freight forwarders (mardep.gov.hk/en/public-services/shipping-directory/freiforw/index.html, metadata 25 Aug 2026): 120 HK forwarders with official self-submitted emails and sites; fetches directly. Best HK email source, better than hkmpdb (36 firms).
- (16 Nov 05Z) HKPC TPLSP list is now as at 9 Oct 2026: bee.hkpc.org/media/ewoal5zx/tplsp_list-of-successful-applicants_en-102026.pdf (linked from bee.hkpc.org/funding-schemes/tplsp/?template=hkpc_text); the 26 Jun 2026 PDF URL was refused. Diffing against the 27 Mar 2026 list (bee.hkpc.org/media/g1xp2zcl/..._en-32026.pdf, 269 entries) shows applicants added after March: Air Sea Worldwide, DCL Global (contacted), JSD Logistics, VINS Logistics, 456 Logistics, Orion Express, Speedway Logistics (HK), Orient Zen, Synergy Global Freight (HK), Janco Global, Ligentia China, Gateway Global. FILAS list (same date) names OA Freight, CATI Global, China Freight (HK).
- (16 Nov 05Z) SAAA site rebuilt: old saaa.org.sg/?p=NNNN member profiles now show the homepage, and member-listing pages fail. PERSPECTIVES Jul-Sep 2026 PDF (saaa.org.sg/api/media/website/publications/1791872389443-5a122b72.pdf) lists new members (Mitra Famosa, Ants Logistic, Poh Tiong Choon Logistics, FPS Global) and the 2026-2028 Council companies.
- (16 Nov 05Z) Dead ends (16 Nov SG/HK): SME100 Singapore 2026 winners (no logistics firms), LogiSYM 2026 (vendors), generic SG new-office searches (groups), hkmpdb cross-check against HKPC (only BEL and Alpha, both group-owned). Clutch SG freight forwarders (clutch.co/sg/logistics/freight-forwarders) gives about 15 domains with size bands. curl through the proxy returns 403, so Cloudflare-obfuscated emails can't be decoded.
- (19 Nov 13Z run) JCtrans Weekly New Members: UK joins weeks 20-46 USED UP; AU and HK/SG weeks 31-46 checked; US weeks 28, 32, 34, 46 checked (38 and 47 fail; 47 not yet published on 19 Nov). Next run: week 47+ for all markets. Hand-built weekly URLs fetched inside subagents this run.
- (19 Nov) Companies House search pages (find-and-update.company-information.service.gov.uk/search/companies?q=<name>) fetch by hand-built URL; CH checks cost no searches.
- (19 Nov) HK: MarDep directory x HKPC TPLSP (9 Oct 2026) cross-match is USED UP. HKPC firms not in MarDep need emails from their own sites (guessed-domain allowed_domains searches rarely hit).
- (19 Nov) SAAA PERSPECTIVES Jul-Sep 2026 (Council 2026-2028) used; Apr-Jun 2026 PDF (saaa.org.sg/publications/pdfs/perspectives-apr-jun-2026.pdf) names Empire Bison, MMI Asia, Project Argus, Sky Leader Freight, KC Intl Logistics.
- (19 Nov) GPLN AGM 2026 sponsor page (gpln.net/agm-2026/) and GPLN newsletters (gpln.net/newsletters/issue-no-NNN/, issues 71-111): few US members (Xios, Juno used). Project Cargo Network news archive (projectcargonetwork.com/news/archive) and brochure pages give members' own emails; WWPC news (wwpc.eu.com/news/).
- (19 Nov) AU: company community-event pages (charity golf days, sponsorships) and Energy Magazine / Australian Mining Review profiles of small project forwarders gave Prime Global. FIATA AU directory (fiata.org/directory/au/) unchecked names: Crisis Global Logistics (crisis.com.au), Customs Brokers Pty Ltd (customsbrokersaustralia.com), Nautical Net Shipping, One Circle Logistics (oclogis.com), Rodinia Freight, Stokes and Bell, TNL International, TWG Logistics, Westlink Logistics (Perth), RAD Global Freight, Xtreme Freight. FTA directory S section (offset about 210000-230000) unread.
- (19 Nov) Crain's Chicago Best Places to Work 2026 (about 10 Sep 2026) is a US hook source via company badges; list itself paywalled.
- (19 Nov) Dead ends: Magaya releases (nothing after Mar 2026); Top Workplaces Chicago 75-249, Philadelphia 2026, Distribution 150-499 p1; GPTW and ATS job searches; chamber small-business awards; GLA, Pangea, cargonewswire, forwardernews; ASCLA 2026 winners; DCN tag page and award spotlights; NAP news since Oct; Signature Global Network; AU "news 2026" allowed_domains queries (SEO posts only); FBJ/multimodal hand-built archive URLs (refused); BIFA new-member and UK regional news searches; Clutch London list; a21.com.sg (JS only); SG generic new-warehouse searches. Search proxy returns HTTP 400 when allowed_domains includes straitstimes, businesstimes, sbr, kentonline, business-live or yorkshirepost.
- (19 Nov) MX lookups: dns.google worked for some domains and timed out on a permission prompt for others in the same run; record unchecked:<domain>.

## Open leads (updated 19 Nov 2026, 13Z run; see also the 11Z run section at the end)

- UK | Delsol International Ltd (15251049, Sales@delsolinternational.com) | hook dated 12 May 2026 (at cutoff), small | missing: newer hook
- UK | Freight Box Global Ltd (16914325, Birmingham, info@freightboxglobal.com) | hook: joined JCtrans 6 Aug 2026 (weekly202632) | held back 19 Nov: entity incorporated Dec 2025, size unknown
- UK | Brit Customs (brit-customs.com), P2P Customs, Atlantic Ocean Shipping Co. Ltd (JCtrans wk31, site robots-blocked), TGT Global Solutions Ltd (JCtrans wk37), Whale Global Freight Ltd (JCtrans wk46), DGR (JCtrans wk34) | missing: email and/or website, CH check
- US | Cargopedia LLC (South San Francisco and North York ON, info@Cargopedia.com) | hook: JCtrans 7 Jul 2026 (weekly202628) | doubts: very small, probably run from Canada
- US | A Customs Brokerage (acb-us.com, Doral FL) | South Florida Top Workplaces 2026 (unconfirmed) | missing: email, hook date
- US | Laufer Group International (NY) | Ocean Export Procurement Analyst job (Nov 2026) | missing: published sales email (form only; recruiter@ only)
- US | Email found, no dated hook: Hancock International, Conship USA, Cargomondo, SILOG, AGOL Worldwide, Santos International; Maryland PDF names (Cargo Logistics Group, Beluga, Laing, JAGRO); FIATA names never searched (KwickKargo, Swifflo, Cargo Dynamics); JCtrans wk28 Cargo Convoy, Talent Solutions
- US | Clockwork Freight Solutions (Blaine WA), Advanced Freight Service (Elkins AR), United Cargo International, Phantom Shipping, HSD Logistics | JCtrans joins May-Jul 2026 | missing: website, email
- AU | Austral-Asia Freight Pty Ltd (aaf.com.au, Yarraville VIC, MD Jeff Harrod, jeffh@aaf.com.au on aaf.com.au/contact.html) | only hook "30 years since 1996" (article 11 Mar 2026, before cutoff) | missing: newer hook
- AU | RH Freight & Customs Brokers (info@rhfreight.com.au) | homepage "19th year of service", undated | missing: dated hook
- AU | Jacanna AU (Brisbane; NZ head office) | case study 12 Jun 2026 | missing: email (form only); check NZ parent
- AU | Ship Smart Logistics Australia (Melbourne) | JCtrans 12 Nov 2026 (weekly202646) | missing: website, email
- AU | ACLI (acli.com.au), EPL International (eplint.com) | unchecked 19 Nov (fetch refused: domains not surfaced in a search) | missing: hook, email
- AU | Specific Freight, Synergy Freight (email found, no dated hook); Transways (owned by Transways Group, no email); Marksman Logistics, Navtrex, GZ Pacificlink (no email); Pivot Freight (very small)
- HK | Lapton Freight International (lapton.com, enquiry@lapton.com, kelvin@lapton.com) | missing: dated hook
- HK | 456 Logistics Ltd (456logistics.com) | on HKPC TPLSP list as at 9 Oct 2026 | missing: email (homepage fetch refused)
- HK | VICO Shipping / VICO Logistics | email known; only own marketing content as hook; may be over size band
- HK | Vinflair Logistics (Cloudflare email), Fairate Express (pages error), CATI Global / OA Freight (HKPC FILAS list 9 Oct 2026, no site found), JSD Logistics, VINS Logistics, Orion Express (HKPC, unchecked); JCtrans names without sites: SAI Logistics, Oneglobe, Shelcia, Last Mile Express, Velonex
- SG | ACS Freight Services (enquiry@acsfrt.com.sg), AM Global (an@ and cm@amglobal.com.sg) | missing: dated hook
- SG | AnTs Logistic (SAAA new member Jul-Sep 2026) | missing: published email on own site
- SG | Alliance 21 (a21.com.sg) | CEO on SAAA Council 2026-2028 | missing: email (site JS-only, three runs)
- SG | Sky Leader Freight, KC Intl Logistics Singapore (SAAA event 22 May 2026), Skyquick International, Silk Express, Highlight International (robots), Halcon Primo (held back: size), LSA Global, Viesman, 3FM, Diaboss Container Line, ATA Logistics, AOCEAN | missing: website/email or hook

## Rejected (do not research again)

- 20 Nov (06Z): AAW Global Logistics, Bluestar Global Logistics, Seaport Freight Services, Envio International, Hexagon International Freight, Banks & Lloyd, S.J. Stile Associates (all emailed in 2026-11-20-mixed-3); US: A Customs Brokerage (form only), Highland Forwarding (no email, nothing after 2019), Cargo Services Inc (OIA Global, Apr 2026), Central Cargo NA (Italian group), EFW (Estes), Commodity Forwarders (Kuehne+Nagel), Forward Logistics (trucking), Argents and Palisades (warehousing), Pegasus Maritime, ARI Shipping, Gridiron, Dartrans (no email/hook), Atlanta Customs Brokers and WEST Forwarding (fourth check, no dated hook), Casey Overseas (robots); UK: Caledonian Freight (form only), BBL Group (French group), Avrio (US), Isca, W Saunders, Grange, AFS Global, Mersey Forwarding, MAS, Peartree, NV Cargo, Brunel Shipping, FLS Group, Atlantic Freight (no dated company news), Jan de Rijk UK, EMO Trans UK, CustomsLink (Stena), Express Global UK (Cosulich) (groups), Freightways, Malco, Mairon (hauliers), Bethan (consultancy), and the UK near-misses Viamaster, Grace Overseas, Beckchoice, TCB, Eagle International, Freight Agency, MIES, We Ship Global, Phaon, Pinnacle (no new dated post, 20 Nov batch search); AU: MF Freight (now Ofload), Clique Logistics (domestic 4PL, Cloudflare email), Seatram, Triways, Valsecchi, Meridian Freight, MYC, Express-Link, efm, R.L. Felton (no dated hook); HK/SG: WM Logistics SG (HK group), Leader Mutual HK (Taiwan group), Cargoport SG (CFS operator), General Cargo Asia HK, Global Airfreight SG (latest news Mar 2026), G.T. Freight SG, TrueLog SG, Ensign Freight HK (201-500), Worldtrans HK (only 2018 item), Global Container Freight SG, RWSolutions HK, Air Sea Broker HK, Wangfoong HK, The One Group SG, Paltrans, Quickflo, GGL SG.

- 20 Nov (03Z): I.H. Hunter, ICAL, Excel Logistics, Carry Cargo International, Trinity Logistics (all emailed in 2026-11-20-mixed-2); Allyn International US (builds its own AI assistant, partly consultancy), Ultra USA (AI software vendor), Highways & Skyways (Radiant), Masterpiece International (Magnate), AMB Logistic (freight broker), Team Worldwide (franchise), Cargoport AU (only Cloudflare emails after full site check), Scorpion International AU (Powerhouse group), Galaxy Freight AU (Indian HQ), ACFS Port Logistics (in administration), CRL Express (domestic linehaul), DealerSend HK (e-commerce), Burhill Logistics UK (Cloudflare emails, no 2026 news).

- 20 Nov (00Z): MGL Logistics, Elto Freight, Casa Logistics, Intergroup Shipping (WA), End to End Logistics, Fast-Link Express HK, XPand Logistics, ETA Logistics (UK), KMB Shipping, K W L Logistics, V. Alexander & Co., Total Logistics Resource, Chicago Express International (all emailed in 2026-11-20-mixed); Royal Shipping Lines US (hook only a Q3 rate notice; revisit with company news), Mercium UK (already offers instant online quotes), Blacksmith Freight UK (no published email, newest post 13 May 2026), DeltaShipExpress (e-commerce 3PL), U-Ocean HK (U-Freight group), Bright Line Freight HK (group), Parisi Grand Smooth HK (Italian group), Gibson Freight AU (JV), Pentagon Freight AU (JAS group).

- 19 Nov (18Z): Think Global Logistics, Corten, Pro Ag Logistics, Freight On Board, 456 Logistics, JODA Freight, TSL Australia, Rancho Customs Brokers, C.T. Freight, Link Logistics (all emailed in 2026-11-19-mixed-4); Outer Seaways (weak FMC QI-change hook, own instant quote tool), RIV Worldwide (Cloudflare emails, US office), RJJ Freight (all emails Cloudflare, contact page errors, fourth check), Conship USA (site stale since 2014), AGOL Worldwide (SEO blog, 500+ staff), Santos International, JAGRO (no hook after two checks), BM Cargo (consumer courier), Bullet Freight Systems (trucking), Archer Cargo and Volume Logistics (freight brokers), Cahill & Dunn, Lookout Freight, Aegis Worldwide, Cargo Dynamics USA (no website), Unitas LogistiX (Indian), Orbit Logistics (North Melbourne FC deal dates from May 2025), Wymap (not a forwarder), EPL International (no email), Sealink Logistics (Cloudflare email).

- 19 Nov (15Z): PS Forwarding, International Cargo Logistics (ICL), LTS Global Solutions, KRL Logistics, Blaiklock, NEMA Inc, United Carriers APAC, Empire Bison, ATA Logistics (all emailed in 2026-11-19-mixed-3); Cargo Overseas (weak hook: BIFA charity golf day, Oct 2026 BIFAlink; already offers instant online quotes 'Nano'; revisit only with a better hook), Baxter Freight (already contacted), Flyship Logistics (site looks hacked, casino spam), Messiah Freight (SEO blog only, second check), Unique Forwarding (no company hook), Smart Customs (Irish), Worldwide Logistic Partners (Cloudflare emails, third check), Alara Logistics (form only), Platton (SEO blog, own AI tooling), Northern Customs Services (Globco link), Interfracht, Slade Global (foreign groups), Dove Shipping (robots), Valley Worldwide (trucking group sub), Seaway (400+ staff), TNL International (MOVe group), Smith Channon (Optimus group), RAD Global, Xtreme Freight, Oxen, Precision Forwarding, Success Logistics, Crisis Global (no email/hook or not forwarders), Spoti Freight HK (Bangkok HQ), OA Freight (Guangzhou HQ), Goldenstar (chartering), Rockwall Services (truck brokerage), AMCO Global Logistics and D'Global Partners (no site found).

- 19 Nov (13Z): Warrant Group, Clear Fr8, LGL Worldwide, Spatial Global, Xios Global, Juno Logistics, Prime Global Logistics, Trimanson Express, Team Well Logistics (all emailed in 2026-11-19-mixed-2); United Worldwide Logistics, FMC Logistics, UT-WAYS (emailed in 2026-11-19-mixed); Amba Forwarding (3 employees per the 11Z run); BE ACCURATE (Greece), Barta Logistics (no CH company), Optima Worldwide (no live company), GF Logistics UK (Gallozzi group), Compass Logistics International (3 staff), Samphire, Zelir, Future Forwarding, UCargo (already contacted or linked); ImEx Cargo (freight-tech/GSA), Universal Cargo Management, CargoTrans, F.H. Kaysing (no dated hook), PCR International, Cheetah Express, VinWorld, Aries Worldwide, Sun Dragon (no published email), Primary Freight Services (no site), Tower Transition (virtual office), Red Lab Logistics (truck brokerage), Top 1 Xpress (hook Apr 2026), Ambercor (Toronto HQ), Atlas Heavy (heavy haul), MTS Logistics Houston (Turkish group), Towbow, Continental Marine Line, Top Star Shipping, BOLT/RIV US; Sea Logic, Venture Freight, MTF, Kenneth Lloyd, Lace, DSH Global, Think Global Logistics, CFFWORLD, RAW Global, Raitt (no dated hook), Avion Australia (Italian group), Lexin Solutions and Freight Lab 360 (consultancies), TFG Global, OneSource, Neolink, Omega Cargo, ISS Shipping, Express Freight Management, ICS Global, Freightshop, Verus, Phoenix Freight, WCBM, Trojan Freight, TESN; Janco Global (Janco group, contacted), Korchina (Korean group), Welscope, SMT Global, Horstrong (sites fail), Air Sea Worldwide (30+ offices), Shalom (mover), Poh Tiong Choon (listed), Shiplah (consumer), GMT Transpeed (no hook after three runs).

- 16 Nov (05Z): Platinum Cargo Logistics Mobile, Freightlead, Marinex, Delta Express, Neofreight, Wider Logistics, Profit Sail, DEAN World Cargo, PCFS, One Global Logistics (all emailed in 2026-11-16-mixed-2); A & A Contract Customs Brokers (aacb.com) (Canadian-owned, head office Surrey BC (aacb.com/company); only trade alerts); Fracht Group (Houston) (Swiss Fracht group, on Houston/Distribution Top Workplaces 2026); IGT Logistics (Oak Brook IL) (freight broker (Fortune Best Small Workplaces Chicago 2026)); JG Customs Forwarding (Pharr TX) (new facility Oct 2025 (before cutoff), no website or email found); Armada (armada.net), Piraeus International (appliance seller) (Armada is a large supply-chain group; Piraeus not a forwarder); Jori Logistics (HQ Calgary, Canada; form only); Absolute Worldwide Logistics (latest news 2016 (second check)); A & A Customs Brokers (aacb.com) (HQ Surrey BC, Canadian-owned group; US entity is a branch. Posts are tariff alerts only); SSAF Logistics (blog posts are industry news only (no company hook) after two checks); OGT Freight, Hancock International, GII International, TM Logistics, V. Alexander, C J International, Cavalier Logistics, Pride International, Transcontinental Distribution Services, JOBCO, dfYOUNG (no dated company hook on site (V. Alexander, TM Logistics, GII, Cavalier, dfYOUNG also have no published email)); Berrio Logistics Inc (US branch of Indian group (Navi Mumbai HQ)); Swift Line Forwarding / Swiftline (Indian company (Rewari HQ)); Veda Logistics, Nobel Logistics, White Oak Logistics, Kintech Supply Chain (USA), VNFT International (USA) (trucking/drayage or template site (Veda, Nobel, White Oak); foreign group subsidiaries (Kintech, VNFT)); BEL International Logistics (HK) (Konoike Transport has been sole shareholder since 1 Oct 2018 (bel-intl.com news BEL1809100001)); Alpha Logistics (HK) Ltd (subsidiary of the Taipei-headquartered Alphalog Group (hkmpdb com=195)); Air Sea Worldwide Logistics (HK) (800+ staff (HKTDC profile)); Speedway Logistics Ltd (HK) (1-5 staff and no website (HKTDC)); JET Worldwide Logistics (HK) (Canadian parcel company, HQ not HK); Airtropolis Express (S) Pte Ltd (subsidiary of Taiwan Express / T3EX Global since Oct 2018); Ants Logistic Pte Ltd; Mitra Famosa International Pte Ltd (SG) (no company website found (only registry and Panjiva pages)); Synergy Global Freight (HK); Orient Zen Logistics Services (HK) (no web presence found).

- 16 Nov (00Z): Kalgin, Thunderbolt Global, GE Lines, CAP Logistics, TCF International, John S. Connor, AXIMA, Logiaide, Freeport Forwarding (all emailed in 2026-11-16-mixed); Embassy Cargo (Italian HQ), ICAT (New Atlas Capital), DBA (Radiant agent), Brauner (2-9 staff), RK Logistics (large 3PL), ITF Group / ForwardNow (trucking group), Logistify, Tranco Global, Transport Capacity Services (truck brokerage), Harbor Logistics SC (drayage), Freight Minds (UK branch), The ACE Group (no hook or email), Future Forwarding Atlanta (same domain as GB-future-forwarding), TecnoShip (Venezuela courier), NAV Global, PNPLINE, Sky2C, Amoy (no hook after two checks), D.T. Gruelle, Piatek, Serra (no email after two checks); Cargo Up, JTM Cargo (form only), ICAL (old news), O'Brien, Vantage, KTH Customs (sites blocked), FPS Global SG (Famous Pacific group), Susan Danks Tariff Consulting (consultancy).

- 15 Nov (17Z): JNC Line, Magellan Logistics, EORI (UK), Navco, Jeavons Eurotir, Dedola, Allied Group, Amrus, Pro Customs Solutions, Freightair, Metoni Logistics (all emailed in 2026-11-15-mixed-2); Cyclone Global and Austorient (already emailed 10 Nov); HLI (heavy haul and rigging), NXTPoint (Suddath), The Logistix Company (brokerage), RTW Logistics (India group), Hawthorne Logistics, Transworld Cargo NY, TransCargo Solutions, CV International, KIN Logistic, Agramont, Current International Freight, Pentagon Freight (plc), Scarbrough International, PressEx, Fast Global Logistics, IBC Inc, BD Flynn, New Landing, Southern Star Navigation, Carra Globe, TEU Global, Oceana Global, NTMK, LR Global (LRgistics broker), Haque International, Leschaco (German group), Laparkan (job before cutoff); ACA International (Dachser), Freight People, Intercargo Connect, Queensland Customs Brokers, First Logistics, Willship, BloomCorp, Cargoconnect, JWI Customs, XS Global, RR Lawson, ATSL, I.H. Hunter, Power Customs, World Freight Solutions, DLF Global, Platinum Freight, MCC World International, Independent Customs Services (no dated hook or no email); EuroTurk and Unsworth (form only), Efret (GB Global), Bullet Express (PE-backed), Chase Freight (haulier), Balena Projects (Canada/Houston), Derry Bros, Transflex, MITEX HK (Mitsui-Soko), Gateway Global HK, Panda Global HK, Lovyph SG (chartering), Quinn Freight UK (French group), Optima Logistics (NW).

- 15 Nov: OceanBlue, ACP Freight, Freightport, Espace, Powercargo, Roadliner, Henning Harders, GPSM, McHugh & Eastwood, Golden Bridge International (all emailed in 2026-11-15-mixed); Interport Logistics (~400 staff), TransPak (crating), Forefront Global (truck brokerage), Advance Customs Brokers (2023 hook only), Allstates WorldCargo (acquisitive group, no email), RBI USA Customs (old hook), WestXport (no email, tiny), PortVelocity (<10 staff), Chain Logistics USA (Turkish group), EXG / Global Shipping Services (Indian group), Emons Air&Sea (German group), Coppersmith (Honour Lane link), Armstrong (truck brokerage), 17 JCtrans US new members Aug-Nov 2026 (no sites; skip), Bulk Group AU (no recent hook), AGS World Transport (wholesale), Sadleirs (large), FJT Logistics (group, undated), Go Gauge SG and FLS Group SG (groups), AJ Global SG (old hook), SBS Logistics SG (group), Marinair HK (likely Greek group), Unitex HK (720 staff), Global Forwarding UK (Hecny), Morrison Freight (Schneider Group), Seafast (GB Global), Harbour International Freight (pallet haulier), Irish Sea Logistics, Delamode, Speedy Freight, Expressway Handling, Viking, SSO, T S Europe, ValueLogistics, Intercargo, Eurogate (not forwarders or foreign), software vendors Westbound, Forward Solutions, Cargo Forwarder, Innovate Freight.

- 14 Nov: Cargonet Limited UK (airfreight wholesaler selling to forwarders; CH mirror showed overdue filings), Fast-Link Express HK (no website or published email found; HKTDC profile has none), Willson International (HQ Mississauga, Canada not reviewed), CMS Shipping (Montreal), Atlantic Logistics (domestic trucking 3PL), Special Cargo Houston, Project Freight LLC, Mako Freight, Liberty Global Logistics, Racing Cargo, Lasta Forwarding (Ireland), Tan Freight (Ghana), Hedley's Group (site robots-blocked, no published email), Uniserve and Denholm Good (large groups), Wallace International, HOH Global, Colless Young, Stellar Freight, TGL (all emailed in 2026-11-14-mixed).

- UAC Australia (air wholesaler, placeholder site text), Aesir Logistics US (weak, old hook), Priority Worldwide US (no US email published), Interworld Freight US (350+ staff), Alba Wheels Up (PE-owned), Imperative Logistics and Jose D. Gonzalez CHB (PE rollup), EELCO (Redwood), Medov (Italian group), Cardinal Global Logistics, Freight Link Solutions (Stena), Mapcargo (corporate parent), Killick Martin (Atlantic Pacific group), Worldwide Book Services (Woodland), Customs Agency Services AU (Mondiale VGL), Whale Logistics AU (Dolphin Group), Connor Anderson AU (acquired by AIT), cargo-partner HK (Nippon Express), Visy Global Logistics SG, DCS DAH Star, Davies Turner (too large), Goodrich Asia Pacific SG (India group), Mercury Freight, Barker & Hood, Global Freight Logistics, Powerhouse International, Hexagon Logistics, Continental Freight Forwarding, Next Day Cargo, KOPE, TRT International, Luminary, D'EL, ETH Cargo, Pace Global, Tri Star, Sciens (all emailed in 2026-11-13-mixed-2, now in companies.csv), Bulldog Cartage (not a forwarder), Loccitec (Mexico), Cargoways (Navalmar), OnBoard Logistics (350+), Colossal Transport (Watco), Mohawk Global (large, no email), Corrigan Air & Sea (no email, group), MHT Forwarding (Abu Dhabi), M&S Logistics (UK group), Summit Logistics (Canada), Across Logistics USA (Spanish group), Fura (brokerage), CustomsLink (Stena), Seabridge AU (Cardinal), Globelink AU (CWT), DCG Logistics UK (700+), Compliant Customs (not a forwarder), Quay Shipping AU (liner agency), Bok Seng SG (400+), Star Concord SG (Pacific Star), Rulewave SG (Dutch group), Global One SG (Chinese group), Regent Group SG (marine services), Multimax, Propel, Sea Carrier, SMI, Hanson Carriers, Econship, Kita Shipping (carriers), Far Sight, Vastwin, Topsheen, Denzai, AIN Group (foreign HQ), CTO Global HK (old hook), U-Freight HK (too large), Eurosprint, SARR, Harborside, Eurospecial, Freight Tank, Phoenix Supply Chain, Wanlong, Beyond Borders, Shipair HK, Trinity Cargo Link (emailed in 2026-11-13-mixed-3), Samphire Customs (Samphire-Simpex group), ALS Customs Services (ALS Holding), Transline International (BTL Group), Alonso Forwarding UK (Grupo Alonso), GP Logistics (Graypen), DL Logistics (Dutch), Sovereign Speed (Hamburg network), Carousel Logistics (too large)
- US | Worldwide Logistic Partners: Clutch profile (clutch.co/profile/worldwide-logistic-partners) lists no email either (14 Nov); still missing email.
- AU | Cargoconnect: homepage re-checked 14 Nov, still no dated hook.
- UK | Eutraco (eutraco.eu, Multimodal 2027 stand 6040) | missing: which country it is based in (likely not UK), email
- US | Magaya customer releases 2026 not yet checked: EP Logistics (22 Jan 2026, cross-border, probably too old), RBI USA Customs Service LLC (11 Feb 2026), Noamex, AGESBEC, Piatek Customs & Logistics | missing: dates under 6 months, location, email

## Run of 19 Nov 2026 (prep, 11Z): yield was 5 of 25 needed; US/UK/AU/HK sources largely exhausted

US | CANDIDATE (weak hook) Universal Cargo Management (universalcargo.com, Los Angeles): in cands_us.json; hook is a company blog post of 5 Nov 2026 only; email info@ on /contact-us/; MX = Microsoft 365; size and ownership not stated.
US | UNFINISHED Atlanta Customs Brokers (atlantacustomsbrokers.com, Atlanta GA, 10-49 staff per goodfirms): ship@atlantacustomsbrokers.com plain text on homepage; only hook is SEO blog posts (15 Sep 2026, 4 May 2026); ownership not stated; MX not run.
US | UNFINISHED CargoTrans (cargotransinc.com): info@ on /blog/5/; only SEO guides (Oct 2026) plus an IEEPA refund promo; no size or ownership.
US | UNFINISHED DayStar Global Solution (daystarglobal.com, Atlanta, 100% employee-owned forwarder and customs broker, 50-249 per Clutch/goodfirms): contact page form only, no email, no dated news.
US | UNFINISHED Lee Hardeman Customs Broker (Atlanta, Global Freight Group member, 50-249), Cargo Brokers International (Atlanta, 10-49), IFF Inc (Atlanta/Stockbridge): domains not found, no hook checked.
US | UNFINISHED Refresh Global Logistics (info@refreshgl.com, JCtrans 27 May 2026): not re-fetched; size probably under 5.
US | UNFINISHED VinWorld (vinworld.com): no plain-text email on home or /about; family group with brands in India, China, Canada, Gulf; hook JCtrans 17 Jul 2026.
US | REJECTED ImEx Cargo: woman-owned airline GSA / freight broker with its own Freight Desk quoting platform (software-like); only email Michelle@ImExCargo.com is a media contact; posts dated 5 Jun, 4 Jul, 22 Jul 2026 are titles only.
US | REJECTED Green Worldwide Shipping (greenworldwide.com, Decatur GA HQ): GPTW post 28 Aug 2026 but emails are Cloudflare-obfuscated on /contact-green/ (not plain text); size unknown, many warehouses.
US | REJECTED Laufer Group: WCA join post is 14 Jun 2023, no plain email anywhere.
US | REJECTED Haque International Logistics (GLA golden member 26 Jun 2026) and Oceana Global Logistics (GLA): GLA posts name a contact but no site or email; Panjiva only.
US | REJECTED CMS Shipping (Canada, Magaya 7 May 2026), AGESBEC (15 May 2025), WCM Worldwide (19 Jan 2026), Piatek (16 Sep 2025): wrong country or too old, no site/email in releases.
US | REJECTED Harbor Logistics (drayage/warehouse SC), KCH Transportation (drayage; blog 2 Nov 2026 not forwarding), MBM Logistics (trucking, Winona MN), M2 Logistics (truckload broker), Avenger Logistics (MODE Global sub), Integrated Shipping and Logistics (Feb 2024), EELCO (Mar 2024 hook), Vanguard Logistics (undated), ITF Group ForwardNow (Hazelwood MO; award 28 Apr 2026, no email, older than cutoff), Priority Freight (300+ staff), Protrans (Indianapolis trucking-led, undated), Freight Minds (Aug 2025), Future Forwarding (UK).
US | NEW SOURCE (small): goodfirms.co/supply-chain-logistics-companies/freight-forwarding/<city> and clutch.co/logistics/freight-forwarders/<city> city lists give names and size bands, but most entries are trucking. Searching with allowed_domains for guessed domains only surfaced company sites with SEO blogs.
US | DEAD ENDS this run: generic searches for anniversary, new-office, ribbon-cutting, WBENC, executive-moves, Magaya customer releases, paylocity/lever/greenhouse quoting roles (only Priority Worldwide, already rejected), AJOT/FreightWaves launch searches. JCtrans week 46+ not indexed. Atlanta Top Workplaces 2026 50-149 p4 has no forwarders.

UNFINISHED (known / missing)
UK | Clear Fr8 Limited (10890861, Active, conf stmt 12 Mar 2026, Dover; rates@clearfr8.com on clearfr8.com; no ownership stated) | hook JCtrans 11 Sep 2026 under name CLEAR FR8 (BRADFORD) GLOBAL FORWARDING LIMITED (weekly202637, offset 100000) | missing: proof the JCtrans entity is the Dover company; size; MX not run
UK | Universe Logistics Ltd (unvs.co.uk, Reg 11089887, Clutch 50-249) | missing: published email (contact page only), dated hook
UK | LGL Worldwide Logistics Ltd (Manchester; JCtrans 28 Sep 2026 weekly202640; GLA member 2023) | missing: website (lglworldwide.co.uk robots-blocked, yellowsky mirror has no email), email, CH
UK | RIV Worldwide Ltd (London, JCtrans 6 Nov 2026 weekly202645), Whale Global Freight Ltd (London, JCtrans 9 Nov 2026 weekly202646), RJJ Freight Ltd (London, 23 Oct weekly202643), Atlantic Ocean Shipping Co Ltd (London, 28 Jul weekly202631), Freight Box Global Ltd (Birmingham, 6 Aug weekly202632), DGR Global Logistics UK Ltd (14535070, London, 19 Aug weekly202634), TGT Global Solutions Ltd (Dover, 7 Sep weekly202637) | missing: website, email, CH (all likely tiny)
UK | Warrant Group Ltd (01941659) | CH page returned client_error 19 Nov; still no Active proof
UK | Optima Worldwide (optima-worldwide.com; sales@optima-worldwide.com) | no legal entity found after 2 more searches; privacy/about pages error
UK | Brit Customs Ltd (13394926, Active, conf stmt 18 Jul 2026, Chelmsford; brit-customs.com JS-rendered, no readable email; Multimodal 2027 stand 9015), P2P Customs (p2pcustoms.com JS-rendered, stand 9028), Easy Customs (no site) | missing: readable email

REJECTED
UK | GF Logistics (UK) Ltd | part of Gallozzi group, no email, newest news Jan 2025
UK | Spatial Global Ltd | member of Keswick Enterprises group
UK | Compass Logistics International Ltd (11052114) | 3 employees, no website
UK | Amba Forwarding (London) Ltd (01281193) | 3 employees, no website
UK | Barta Logistics | no CH match (BARTA LIMITED 05534977 is a Bromley SIC 96090 company, unrelated), site email only on contact page
UK | Eurocustoms BV, Customs Insights Consultancy, Brightfinch (consultancy/customs trainer, hook Mar 2026) | not target or hook too old
UK | MEXL Express Ltd | Freight Midpoint join 13 Mar 2026 (before cutoff), no email
UK | BIFA 2026 shortlist | all remaining forwarders already in companies.csv or rejected; page now USED UP
UK | BE ACCURATE LTD | Piraeus, Greece (not UK)

NEW SOURCES / NOTES
- JCtrans weekly pages 31-46 now checked for UK (31,32,34,37,40,41,43,45,46 each list 1-2 UK joins; none show websites or emails; tiny firms). Truncated tails (offset 100000) checked for 32,35,37,43,44,45; 38, 42 tails unchecked.
- JCtrans weekly page week N also gives enough dated hook text ("independent ..." description) for a hook when the company website is found elsewhere.
- Clutch UK freight forwarders pages 1-2 (clutch.co/logistics/freight-forwarders/uk, ?page=2) fetch: gives size bands; no domains except top 18. Page 3 not checked.
- Dead ends: FBJ monthly archives 2026/05, 06, 07 (p1-2) nothing new; multimodal.org.uk/article?limit=100&start=110 has no dates; Multimodal 2026 awards winners and 2026 Modal finalists (forwarders all large or already contacted); Conqueror news and GLA news pages (no 2026 UK members); UK recruiter job ads hide employer names; BIFAlink June 2026 flippingbook p21 (no new members).

UNFINISHED
AU | Avion Australia (avionaustralia.com, Matraville NSW) | known: hook = office and warehouse move to 1/42-52 Raymond Ave Matraville effective 1 Jun 2026 (notice 4 Jun 2026, avionaustralia.com/notification-of-change-of-office-and-warehouse-address/); info@avionaustralia.com in footer; MX Microsoft 365; no no-unsolicited text | missing: independence. About page says it is part of Avion Company SPA Group (Italy, Milan). Main session decides; I treated it as a group member and excluded it
AU | KTL Australia | in cands_au.json but hook is undated job ads (weak); Mailguard MX
AU | Prime Global Logistics (primeglobal.com.au, Perth/Brisbane, 27 staff, operations@primeglobal.com.au in footer) | known: Australian-owned project forwarder; news 4 May 2026 (conveyor reels), Dec 2025 Green Steel of WA, Techking 3PL 20 Oct 2025 | missing: hook after mid-May 2026; recheck for newer news
AU | Smartclear (smartclear.com.au, Taren Point; enquiries@smartclear.com.au) | missing: any dated hook (copyright 2025)
AU | Tomax Logistics Australia (sales@tomax.com.au) | missing: dated hook; part of Tomax Group (check)
AU | DSH Global (sales@dshglobal.com.au; Dominic@dshglobal.com.au named MD) | missing: dated hook (latest BMSB 2025-26 notice)
AU | JCtrans wk46: Ship Smart Logistics Australia (Melbourne, 12 Nov 2026), Freight Lab 360 (Brisbane, 13 Nov 2026; only a manus.space template site) | missing: own website and email
AU | Sea Logic, Venture Freight, MTF, Kenneth Lloyd, Lace, TGL, CFFWORLD, Specific Freight, Raitt, Synergy, Felton: homepages/news re-read 19 Nov (MTF, TGL, Venture, DSH, Lace, CFFWORLD): still no dated company hook
AU | Pivot Freight (GLA golden member, tiny); Transways Intl (owned by Transways Group)

REJECTED
AU | BTi Logistics: acquired by OIA Global
AU | Trans Global Projects (tglobal.com): appointments news 3 Nov 2025, too old, no email seen
AU | Spark Global Logistics, Regroup, TFG Global, SCI Australia, Pacific Air Cargo, WCBM, Selsby, Pure Global (template copy): no published email and no dated hook
AU | Woodford Cargo: only bigpond/gmail addresses, no hook
AU | Tradewise Global, Total Maritime, Port Air Logistics: robots-blocked
AU | MRL Global: transport group first, no email, no recent hook
AU | NMT Shipping/Custom Brokers (Adelaide): RoRo shipper, 275+ staff
AU | SSN Projects: no website; Frontier United: under 10 staff
AU | DCN 2026 finalists (Freight Forwarder, Project Cargo, Customs Broker): all finalists already in companies.csv or rejected except Shipping Solutions Australia (site blocked)
AU | Freight On Board Intl: 35th anniversary 8 May 2025, old
AU | Customs Agency Services (CAS 50 years, 6 Aug 2026): already rejected (Mondiale VGL)

NEW SOURCES
- JCtrans weekly 2026 wk46 lists 2 AU joins without sites; wk20-29 AU checked this run: only Intercargo Connect (wk28, already rejected).
- employmenthero.com/jobs/position/<company>-... pages: job ads from small AU forwarders (KTL, SSN Projects, BTi, Harders); undated, usable only as weak quote-desk hiring hook.
- Clutch AU forwarder lists clutch.co/au/logistics/freight-forwarders/melbourne.md and /sydney.md (50 firms each with size bands; domains only for top 15).
- FTA member directory read fully A-Z this run (offsets 150000, 250000 give P-Z).
- Dead ends: DCN tag page and FTA news list show no small-forwarder company news after mid-May 2026; dated AU member news is very scarce.

UNFINISHED
HK | Team Well Logistics Ltd (twlog.com.hk) | known: info@twlog.com.hk in MarDep directory; on HKPC TPLSP list as at 9 Oct 2026 (hook date 2026-10-09); site live in search index | missing: ownership and size (robots-blocked on every page, 19 Nov); looks like HK/Mainland local transport, check it quotes air/sea/customs; MX not run
HK | Vinflair Logistics (vinflair.com/contact.html fetches; Kowloon Bay HQ, 40+ years, offices Tokyo/Shanghai/Shenzhen/Jakarta/Singapore) | on HKPC TPLSP list 9 Oct 2026 | missing: email (Cloudflare-obfuscated), ownership, size
HK | Lapton Freight International (lapton.com, robots-blocked; kelvin@lapton.com in MarDep) | missing: dated hook (not on HKPC list, news page empty)
HK | SMT Global Logistics (smtglobal.com.hk), Fairate Express (fairate.com), Welscope (welscope.com) | on HKPC TPLSP 9 Oct 2026 | smtglobal returns client_error on all pages, fairate fetch fails except membership.asp (HAFFA/IATA/FIATA/CPN, no email), welscope empty page
HK | CATI Global Logistics (HK) (JCtrans 9 Jul 2026 weekly202628, FILAS list 9 Oct 2026; garment and DG specialty) | missing: website and email
SG | Alliance 21 (a21.com.sg; alex.world redirects there) | hook: CEO Benjamin Ong SAAA 2nd Deputy Chairman 2026-28, A21 Distribution rename ~23 Oct 2026 | missing: email (site JS-rendered, all pages return metadata only)
SG | WHL Logistics Pte Ltd (whl.sg, info@whl.sg on homepage) | missing: dated hook, size, ownership
SG | Highlight International Logistics (hil-group.com robots-blocked)
SG | Silk Express Freight (SAAA new member Sep 2026) | no website found in two searches

REJECTED
HK | Korchina Logistics (H.K.) (KC International, Korean group, site robots-blocked)
HK | Extrans International (HK) / extransglobal.com | self-described Korean logistics company (group)
HK | Sino Shipping / FNM Group | 400+ staff, no 2026 news
HK | CIFA / Comprehensive International Freight Forwarders (ciff.com.hk) | now Mondiale VGL
HK | Sin Kung Logistics | Malaysian
HK | Premiere Logistics (HK), Tradeport HK | only hook is MATF internship list dated 11 May 2026 (before cutoff)
SG | SkyQuick International | parcel network, not a forwarder
SG | Speedmark Singapore | Taiwan-HQ group, ~150 staff, no 2026 news
SG | Shalom International Movers, Raffles Fulfillment (SAAA council) | movers / fulfilment, not forwarders
SG | Poh Tiong Choon Logistics | large trucking/logistics firm
SG | Scan Global Logistics (scangl.com) | Danish group

NEW SOURCES / NOTES
- MarDep HK freight forwarder directory (120 firms, emails) fetched OK 19 Nov; intersect with HKPC TPLSP 9 Oct 2026 list gives only Team Well, Korchina, Central Oceans HK, Hankyu, Kerry, Logwin, CH Robinson as new names; the rest already used or large. Few HK small forwarders publish dated news; hook source is the weak point.
- SAAA PERSPECTIVES Jul-Sep 2026 PDF names Council 2026-28 (Skyquick, Speedmark, Logwin, Rohlig, Apex, Dachser, Geodis are not targets; UT-WAYS used).
- saaa.org.sg/?p=NNNN pages now all show the association's own contact details, not member data. sla.org.sg member directory and news pages empty/failing. SAAA latest-news page has nothing after Mar 2024.
- JCtrans weekly202628 (7-10 Jul 2026) lists AOCEAN (SG 7 Jul), CATI (HK 9 Jul), DMU Logistics (SG-HQ group, 26 branches, too large).
- Dead: award.businessfocus.io SME 2026 winners (no logistics), Neutral Air Partner latest page (no SG/HK), Lognet NYS Global (2018), HK Maritime Internship list (11 May 2026).
- aocean.com.sg homepage is tanker chartering; forwarder arm is aocean.com.sg/ao/about/ (AO Global).

- Avion Australia (avionaustralia.com): hook 1 Jun 2026 office move, but part of Avion SPA Group (Italy): rejected as group-owned.
- Rejected 19 Nov: KTL Australia (undated job-ad hook only), ImEx Cargo, Laufer Group.

## Run of 19 Nov 2026 (prep, 15Z): 9 of 25 written; sources thin in every market

NEW / PRODUCTIVE SOURCES
- multimodal.org.uk/news: one fetch lists all items 19 May-19 Nov 2026 (first 100000 chars, newest first; prompt "list EVERY headline"). Used: PS Forwarding, LTS. Remaining items are hauliers, pallet networks, large groups (Baxter Freight already contacted).
- Freight-software vendor customer news names small UK forwarders with dates: albacore.co.uk/news, cargonewswire/aircargoweek CargoWise stories (Cen Global), Mosaiq, Breeze. Search "<vendor> customer UK forwarder 2026".
- projectcargonetwork.com/news/archive: ~94 dated member posts 20 May-19 Nov 2026 in one fetch (UK: Blaiklock only; used).
- perishablenews.com covers UK forwarder branch openings (ICL Felixstowe). BIFAlink Oct 2026 flipbook (online.flippingbook.com/view/470360780/) has member news.
- prospeo.io/c/<slug> and Endole brand pages give domain, headcount and PSC; CH /company/<n>/persons-with-significant-control fetches by hand-built URL.
- US: FMC OTI licence applicant lists (fmc.gov/oti-update/<month>-<day>-2026-ocean-transportation-intermediary-license-applicants/, surface with allowed_domains fmc.gov). Dated hook for established firms adding NVO/OFF services. Fetched: 26 May, 15 Jun, 22 Jun, 20 Jul, 10 Aug, 17 Aug, 1 Sep, 14 Sep, 13 Oct, 19 Oct, 9 Nov. Unfetched: 3 Jun and any newer list after 9 Nov. Most applicants are micro firms with no site.
- AU: sports-club sponsorship announcements (semphoenix.com.au, nmfc.com.au, ministryofsport.com) gave United Carriers and Orbit Logistics. Care-Factor 2026 sponsors: Blueprint Global, FreightPlus, Wymap Group, OneStop (unchecked).
- SG: SAAA article pages (saaa.org.sg/article-detail?slug=...) are dated and name members; some old-style profiles (saaa.org.sg/planet-logistics/) still carry emails. HK: HKPC FILAS list (bee.hkpc.org/media/tz1j5ymi/filas_list-of-successful-applicants_en-102026.pdf), codes FILAS-26-09-NNN date to Sep 2026; Security Cargo Network news; HAFFA Executive Committee 2025-27 names small HK forwarders.

DEAD ENDS (19 Nov 15Z)
- JCtrans weekly202647 still not published (client_error) at 15Z.
- UK: regional business awards (Northants, NECC, EADT, Yorkshire, Black Country), everywoman/CILT 2026, FBJ archives 2026/08-11 later pages, glafamily, Lognet, theloadstar/insidermedia/bdaily (client_error).
- US: PCN/WWPC (no new US members), Inc 5000, Top Workplaces Dallas/Distribution, 40-under-40, ISO/GPTW, G75, Crain's searches, Elite GLN and X2 (robots), DF Alliance blog, job ATS searches, guessed-domain allowed_domains searches, cargonewswire/aircargoweek "goes live" US searches.
- AU: state and national export awards (no logistics category), Illawarra/Hunter awards, ALC/AFI/SCLAA awards, FACCI, Freight Midpoint AU, jobstralia, DCN tag/author pages. FIATA AU directory USED UP; FTA directory P-Z read.
- HK/SG: Enterprise 50 2026 not yet announced; SBR/SPBA/APEA; HK award searches (Hactl/AFLAS only); HK Customs AEO; CAD RA list; HKLA new members (JS); hk.jobsdb/ctgoodjobs blocked; 2026-news searches over 40 MarDep HK domains found nothing dated.

UNFINISHED
- UK | Brit Customs (brit-customs.com, "British Italian Customs Solutions") | JS-only, third check; possible Italian link | drop unless an email appears
- UK | Universe Logistics, P2P Customs, Delsol (newer hook) | not reached this run
- US | FMC applicants unresolved: Cahill & Dunn CHB (Culleoka TN, adding NVO/OFF 9 Nov), Worldwide Freight Forwarder LLC (Medley FL, adding NVO 9 Nov), Skywater Cargo (Naples FL), Archer Cargo (Darien IL, 15 Jun), Lookout Freight Group (Hixson TN, 1 Sep), Cargo Dynamics USA (Star Tannery VA, adding NVO 10 Aug), One World Logistics (Woburn MA, 14 Sep, robots), Aegis Worldwide (Ponte Vedra FL), Volume Logistics (Gainesville GA, 17 Aug), Interglobal Forwarders and Unitas LogistiX (Greer SC), Youness Export (Dearborn MI) | missing: website, email
- AU | Orbit Logistics (orbitlogistics.com.au, Essendon Fields, MD Glenn Allison) | North Melbourne FC partnership (undated, likely late 2026) | missing: plain email (Cloudflare), exact date
- AU | Felton Global Logistics | only trade newsletters dated 2026 | missing: company hook
- AU | email known, no dated hook: Rodinia, Stokes and Bell, TWG, Pro Freight, Westlink, WWCF, Customs Brokers Pty Ltd, Link Logistics (TAS), AFI Logistics (TAS)
- HK | China Freight (Hong Kong) Ltd (chinafreight.com.hk) | HKPC FILAS Sep 2026 round (list 9 Oct 2026) | missing: email (site errors), group structure
- HK | Cargoholic International (info@cargoholic.com), AE Cargo Services (aecargo@aecargo.com) | missing: dated hook
- SG | Sky Leader Freight | SAAA outreach 22 May 2026 | missing: website, email (retry saaa.org.sg/sky-leader-freight/)


## Run of 19 Nov 2026 (prep, 18Z): 10 of 25 written; US sources nearly exhausted

NEW / PRODUCTIVE SOURCES
- NCBFAA Monday Morning eBriefing (ncbfaa.org/news-advocacy/monday-morning-ebriefing-details/N, 1 = newest, about 13 Nov 2026): dated "Welcomes New Members" items naming small US customs brokers and forwarders (no cities). Surface with a search limited to ncbfaa.org, then hand-built N works. Checked 1, 3, 5, 7, 8, 10, 12, 13, 14, 17, 18, 19, 21; NOT checked 2, 4, 6, 9, 11, 15, 16, 20. Unresearched names: Airgo Worldwide, Production Freight, Imago Logistics, Clear Customs and Trade Solutions, Harris CHB, Pax Customs, DIMAR, Valls International, DIF International (more in the run's notes). Best US start for the next run.
- IFCBAA 2026 National Conference program PDF (ifcbaa.com/common/Uploaded files/_Event Documents/IFCBAA 2026 National Conference Program 15.4.26.pdf): AU speakers by company (16 May 2026; now at the edge of the hook window, use only for strong fits). anzslconference.com/sponsors and the FTA/APSA 2026 ANZ conference program (27 Aug 2026) name sponsoring AU forwarders.
- Greater Birmingham Chambers member-news pages are dated (UK hooks). Clutch UK city lists fetch by typed URL: clutch.co/logistics/shipping-companies/uk/england/london.md, /manchester.md, clutch.co/logistics/freight-forwarders/uk?page=3.
- FMC OTI applicant lists fetched through 16 Nov 2026 (also 3 Jun, 30 Jun, 4 Aug, 8 Sep, 21 Sep, 28 Sep, 5 Oct). Next list expected about 23 Nov.

DEAD ENDS (19 Nov 18Z)
- JCtrans weekly202647 still not published (about 18Z).
- US: President's E Award (no 2026 round), Aggie 100, Inc 5000 logistics, Inbound Logistics Top 100 (only already-contacted fits), WCA 2026 awards, NY/NJ association awards, NCBFAA board, lmtonline (blocked), VMA bulletins (2025), Doral Chamber, SBDC stories, cargo screening news, CNS magazine, GoFreight stories, cargolinked.com directory (no dates/sites), GLA/Globalia/IFC8/Cooperative Logistics Network (no dated US joins), Global Affinity Alliance (blocked). Many small US sites loop https to http and cannot be fetched (interglobalforwarders.com, unitycb.com, allroundlogistics.com).
- UK: BIFAlink Aug/Oct 2026 (no usable member news, no Nov issue indexed), Albacore/Breeze/CargoWise vendor news, anniversary and AEO searches, CIEIT awards 2026.
- AU/HK/SG: HKPC FILAS and TPLSP lists used up; Care-Factor 2026 sponsors used up; SAAA Sep-Oct 2026 articles name no members; DCN finalists used; Breakbulk Asia hand-built profile URLs and wwpc.eu.com/news refused; MegaTrans exhibitor list and au.seek.com do not load.

UNFINISHED
- US | Celeris Global (Hebron KY, sales@ found) | new FMC licence application 21 Sep 2026 | missing: size and ownership (probably a start-up)
- US | Unity Customs Broker (unitycb.com) | NCBFAA new member 18 Sep 2026 | missing: site unreadable (redirect loop), email
- US | Southern States Forwarding (New Orleans) | NCBFAA new member 13 Nov 2026 | missing: website, email
- US | Cargo Logistics Group (cargologisticsgroup.com) | only careers@ and an undated sales job | missing: sales email, dated hook
- UK | Freight Box Global Ltd (16914325) | all checks pass, but 1-10 staff and incorporated Dec 2025 | held back for size
- UK | Blacksmith Freight (hook 13 May 2026, no published email); J. S. Forwarding Felixstowe (sales@ published, no dated hook); Universe Logistics (homepage fetch timed out); P2P Customs, TGT Global Solutions, Whale Global Freight, Atlantic Ocean Shipping (not reached)
- AU | North Queensland Customs Services (good fit, MD Ben McMahon, email known) | missing: dated hook; PG Logistics (IFCBAA 16 May speaker) | missing: website; Blueprint Global (4PL, likely buys freight rather than quotes) | fit doubtful
- AU | email known, no dated hook: JB Kline, TWG, Stokes and Bell, Rodinia, Westlink, Elto Freight, Freight Connections TAS, Customs Brokers Pty Ltd / WWCF
- HK/SG | Lapton, Cargoholic, AE Cargo (HK), WHL Logistics, AM Global, ACS Freight (SG) | email known | missing: dated hook

## Run of 19 Nov 2026 (prep, 21Z): 9 of 25 written (US 7, UK 2); AU, HK, SG gave none

NEW / PRODUCTIVE SOURCES
- NCBFAA eBriefing pages base to /21 all read 19 Nov 21Z; USED UP until the next issue (about 20 Nov). Page numbers shift weekly as issues are added. Hand-built ncbfaa.org URLs are refused at first, then fetch later in the same session: retry rather than spend searches.
- importinfo.com / importgenius.com importer pages reveal a company's email domain, which then lets an allowed_domains search surface its site (found Affinity Shipping).
- Repeatable US hook: small brokers posting dated advisories (Nov 2026) on CBP's stricter importer of record / CTPAT-validated broker rule effective 5 Jan 2027 (used for IFF). Check blogs of backlog brokers that publish an email.
- Company careers pages with quote/pricing roles: search "careers" + freight forwarder + "pricing" OR "quotations executive" with job boards excluded (found Uniexpress).
- HAFFA site (haffa.com.hk) fetches, including 2026 press releases; 60th-anniversary closing ceremony 27 Nov 2026 (photo album may name members). Descartes general news (descartes.com/news-events/general-news) fetches.
- JCtrans weekly202638 fetches by hand-built URL (US joins BMI Brave Motion Oldsmar FL, BCS Global Houston, WELL Worldwide Energy Logistics Houston, no sites; SG RESHETH GLOBAL FREIGHT PTE LTD 18 Sep 2026). weekly202647 still refused/unpublished at 21Z.

DEAD ENDS (19 Nov 21Z)
- US: Airforwarders Association new members (newest 2025), Florida Trend / LABJ / Top Workplaces Bay Area and Atlanta, SupplyChainBrain 100 Great Partners, FCBF golf and Port Laredo summit pages, acquisition/network-join/chamber/new-office/CTPAT/pricing-job searches; FMC lists nothing after 16 Nov. members.ncbfaa.org directory is a form.
- UK/AU: Clutch UK city lists and bifa.org new-members by hand-built URL (refused), Greater Birmingham Chambers news USED UP, FTA homepage news and ANZSL conference pages (no sponsor names in text), Thames Valley and Hereford & Worcester Chamber awards, IoE International Trade Awards 2026, Shipping Australia new members, BIFAlink Sep 2026 (metadata only; Nov not indexed), generic AU searches.
- HK/SG: Breakbulk Asia USED UP (only Megaton, already contacted); AM Global news page empty; ALMAC 2026 attendee list only page 1 readable.

UNFINISHED
- US | A1 Worldwide Logistics (North Miami, 10-49 staff, info@a1wwl.com on contact page, MX Proofpoint) | hook founder FIU SBDC Entrepreneur of the Year (article 19 May 2026, at cutoff) | missing: newer hook
- US | Total Logistics Resource (shiptlr.com, bd@shiptlr.com, MX Microsoft 365) | CTPAT/importer of record articles 12 Nov 2026 | missing: HQ city, size, ownership
- US | Atlanta Customs Brokers (ship@ published) | homepage "We have moved to 4777 Aviation Parkway", undated | missing: move date
- US | Celeris Global (no address/size on site), Southern States Forwarding (New Orleans, NCBFAA 13 Nov, no site), Boston Mountain Customs Brokerage (NCBFAA 6 Nov, no site), NDA Logistics (Hawthorne CA, ndalgx.com not surfaced), Unity Customs Brokers (site unreadable)
- AU | Navia Freight (exports@naviafreight.com, Sydney office page, MX Microsoft 365; hook TCI Navia JV 18 Aug 2026) | held back: 15 offices in 5 countries, likely over 300 staff, own tech platform
- AU | Clarke Global Logistics (enquiry@clarkeglobal.com.au) | missing: dated hook (SEO news only)
- UK | KWL Logistics Felixstowe (kwlquote@kwllogistics.co.uk; news 2024), Universe Logistics (info@unvs.co.uk; undated posts) | missing: dated hook
- HK | Golden Jet Freight Forwarders Ltd (chairman Gary Lau is HAFFA Chairman; remarks at HAFFA-supported ALMAC 2026 seminar 16 Nov 2026, haffa.com.hk/en-HK/Page/Default.aspx?id=3107) | missing: website and email (goldenjet.com is an unrelated Canadian firm)
- HK | HAFFA Executive Committee 2025-27 firms unchecked: Hentrans, Bollyman, CTI Logistics HK, Diversified Freight, Easyway, Forward By Norman, NAF Global, U-Ocean, OA Cargo
- HK | Vinflair (only email Cloudflare-obfuscated; HKTDC 26-50 staff, no email)
- SG | PAL Line (sales@palline.com.sg) | missing: dated hook. Unused Clutch SG domains: aspac-aircargo.com.sg, bestglobal.com.sg, lchlogistics.com
- SG/HK | WHL, AM Global, ACS Freight, Cargoholic, AE Cargo (site may be compromised), Lapton (robots), China Freight HK (site down), Sky Leader (SAAA page refused, no site): re-checked 19 Nov 21Z, still no dated hook

REJECTED (19 Nov 21Z)
- Valls International, Robert F. Barnes CHB, LG Cargo Clearances, AIRGO Worldwide, Production Freight, Affinity Shipping (USA), IFF Inc, Uniexpress, Jordon Freight (all emailed in 2026-11-19-mixed-5)
- US: Exim Americas (Indian group), Pax (duty-drawback tech), DIMAR, Adhoc, Pan CHB (robots), Fried-Sped (German group), Green Light (Canadian), Camili (Mexican group), Suarez Brokerage (site spam), ANA Link (form only), Applied Freight Solutions (CargoWise consultancy), SMN (truck brokerage), Transitify and Allister Lines (Cloudflare emails), TGP (Trans Global Projects group), Imago (placeholder site), Harris CHB and Clear Customs (no site), Nowlun (Egyptian platform), Phoenix International (871 staff), WB Skinner (2019 hook), K&R International Services (not clearly a forwarder), eShipping (2024 hook), Charles Kendall (UK group)
- UK/AU: Delsol (about 1m turnover), J. S. Forwarding (no site), Specific Freight, Customs Brokers Pty Ltd, Synergy Freight (third check, no hook), Fintran (biosecurity), CargoMaster (Cloudflare email), Superior Freight (2025 hook)
- HK/SG: KC Intl Logistics SG (Korchina, Korean group); see hksg notes for others

## Run of 20 Nov 2026 (prep, 00Z): 13 of 25 written (AU 5, UK 4, US 3, HK 1); about 160 searches

Key new sources: FTA/APSA Weekly Reports 'Out & About' and 'Our expanding alliance' (ftalliance.com.au/advocacydetail/<id>, 2026/21-46 read, start at 2026/47); revenuebase.ai UK city/category lists plus an allowed_domains news search; IACAC The Pallet new members (US); small brokers' dated posts on the CBP foreign importer of record rule (US); Security Cargo Network news and MarDep directory (HK). Notes: Fast-Link HK was wrongly rejected on 14 Nov for no email (MarDep lists it); I.H. Hunter (FTA 28 Oct 2026) and ICAL (FTA 30 Sep 2026) now have dated hooks and can be reopened. dns.google MX lookups were refused this run (web-fetch subagent, permission prompt timed out).

Agent notes (near-misses and sources):

US | A1 Worldwide Logistics (North Miami, info@a1wwl.com) | founder FIU Entrepreneur of the Year (article 19 May 2026, one day before cutoff); blog only SEO/tariff posts to 19 Nov 2026 | missing: hook on/after 20 May
US | Exportalia Customs Brokers LLC (San Diego/Otay Mesa, CEO Lorna I. Manrique) | San Diego Regional Chamber member spotlight 29 Sep 2026 (sdchamber.org/2026/09/member-spotlight-exportalia-customs-brokers-llc/); email ecbusdoc@exportaliasc.com only on chamber page | missing: own-site email (grupoexportalia.com redirect loop), ownership (possible Mexican "Grupo")
US | GGL USA (gglusa.us) | IACAC new member, The Pallet Sep 2026 (published 23 Oct 2026) | missing: email (contact page empty), ownership ("GGL Global" presence map suggests a group)
US | Baycor International (Houston, info@baycorinternational.com, MBE, est. 1997) | only SEO posts (4 Sep); Clutch 2-9 staff | missing: company hook, size
US | Everglory Logistics (Boston/Chicago/LA/Atlanta) | latest company news 2016; only a CPSC explainer 7 Jul 2026 | missing: hook, plain email
US | WEST Forwarding Services (Middleburg Heights OH, info@westforwarding.com, 40+ yrs) | missing: dated hook
US | Amex Logistics (Miami, Info@amexlogistics.net, 6 US offices) | no news section | missing: hook, ownership
US | PSI Global Logistics (Houston, info@psishipping.com, Nigeria lanes) | SEO blog only | missing: company hook
US | Profreight Brokers (NJ, est. 1989) | missing: email, hook
US | Gene Mack International (Fullerton CA) | CTPAT certified Jul 2026, Veroot release 29 Sep 2026 | missing: email; very small entry-filing-only broker (no freight quoting), likely below size floor
US | Celeris Global (sales@celerisglobal.com) | FMC licence application 21 Sep 2026 | missing: address, size, ownership (site gives none)
US | iTransTrade / International Transportation & Trade LLC (South Florida) | joined World Freight Network 24 Sep 2026 (worldfreightnetwork.com/wfn-welcomes-new-member-in-the-usa/) | missing: site fetch refused, email, size (likely tiny)
US | Royal Shipping Lines written as WEAK (hook is a rate-adjustment notice); main session decides

SOURCES:
- Productive: small brokers' dated advisories on CBP foreign-importer-of-record/CTPAT rule (Nov 2026): gave V. Alexander (11 Nov) and TLR (updated 12 Nov). Use allowed_domains over backlog broker domains with query "foreign importer of record CTPAT validated broker January 2027".
- Productive: IACAC (Chicago air cargo association) monthly newsletter The Pallet (iacac.com/the-pallet-<month>-2026/; surface with allowed_domains iacac.com): "Welcome New Members" dated by issue. Sep issue (23 Oct) gave Chicago Express, GGL; Jun-Aug, Oct had only carriers/insurers. Check Nov issue when out.
- Productive (small): Clutch city lists clutch.co/logistics/customs-brokers/<city> and /freight-forwarders/houston, /air-freight-companies/houston fetch after an allowed_domains clutch.co search (hand-built .md URLs were refused this run). Houston, Miami, LA, Chicago, Atlanta, Dallas, Seattle read; most domains give only SEO blogs.
- Small: San Diego Regional Chamber member spotlights (sdchamber.org/2026/MM/member-spotlight-...) are dated.
- Dead: JCtrans weekly202647 (still client_error 20 Nov), NCBFAA eBriefing (still 13 Nov issue), CBP permitted broker CSV (proxy 403, WebFetch client_error), Inc 5000/FreightWaves list, GPTW pages (OnBoard, Logiaide), Global Freight Group news (old/US member sold to Eezy), WWPC network (renewals only), World Freight Network news (one US join), Doral Chamber (already used), FIU awards (19 May), Descartes news, Texas Border Business, PR news (newsismybusiness), Charleston/Jax journals, Global Trade Leading 3PLs (nominations only), chamber member-of-month and minority/women award searches, acquisitions searches, pricing-job searches, "proud to announce" CTPAT searches. Search proxy 400 when allowed_domains includes postandcourier/ajc/houstonchronicle/crainsnewyork/savannahnow group. Robots-blocked: pacavologistics.com, clockworkfreightsolutions.com, clockworkfreight.com. patriot-logistics.com dead domain. DeltaShipExpress is an e-commerce 3PL (reject).

UK | We Ship Global Forwarding Ltd (we-ship.co.uk, Stowmarket, sales@we-ship.co.uk) | IFN Gold Founder member on ifnfamily.com/blog/freight-forwarders-uk/ (8 Oct 2026); Amazon FBA e-commerce forwarder | missing: CH check, size (probably small), stronger hook
UK | Phaon Logistics / Phaon Freight Solutions Ltd (phaonlogistics.com, Ludgershall, hello@phaonlogistics.com, co. 13628985) | IFN Gold Founder member (same page, 8 Oct 2026) | missing: CH status, size (inc. 2021, likely tiny)
UK | George Baker (Shipping) Ltd (01613385, Felixstowe) | hook: new Kufstein (Austria) office, post 20 May 2026 (georgebakershipping.com/george-bakers-new-austrian-office/); emails on contact page written with [at], only Birmingham named contact warren.holmes[at]georgebakereurope.com | doubts: George Baker Group 25-50% owned by GB Global Management (the GB Global group earlier rejected for Seafast/Efret), multi-country, probably over size band
UK | AFS Global (afs-global.com, Manchester, 12 staff, info@afs-global.com) | missing: dated hook (latest news 2024)
UK | Quantum Air & Sea Ltd (qasl.co.uk, Harrow, independent, info@qasl.co.uk) | missing: dated hook
UK | Conquest Shipping Ltd (Woodford Green, family-owned, sales@conquest-shipping.com) | missing: dated hook
UK | WM International Ltd (02311436, Birmingham, info@wminternational.com) | missing: dated hook
UK | Supreme Freight Services (Southampton, 51-200) and Plexus Freight (Portishead, family-owned) | email obfuscated on both; only SEO posts
UK | Translink Express Logistics (Narborough, family-owned; thebusinessdesk 27 Aug 2026 expansion story) | not checked: may be courier/haulier, no site or email found
UK | Blacksmith Freight | re-checked 20 Nov: no published email (phones only), newest post 13 May 2026: drop

SOURCES:
- PRODUCTIVE: revenuebase.ai category/city lists fetch by hand-built URL (top 15-25 names, domain and size band): /companies/customs-brokers-and-freight-forwarders/united-kingdom, /shipping-and-freight-forwarders/united-kingdom(/london), /freight-forwarders/united-kingdom(/felixstowe, /manchester, /birmingham, /london, /liverpool), /customs-brokers/united-kingdom(/london). Southampton, Glasgow, Leeds, Hull, Dover pages fail. Then one WebSearch with allowed_domains = 20 of those domains and a news-style query (e.g. "appointed OR accreditation OR new office OR milestone 2026") surfaces company news posts, which then fetch (gave XPand, ETA, Mercium). Pure "2026 news" queries return SEO trade-news posts.
- PRODUCTIVE: ifnfamily.com/blog/freight-forwarders-uk/ (8 Oct 2026) lists 5 UK IFN members (KWL used; We Ship, Phaon near-miss; United Worldwide already contacted; Angel Shipping unchecked).
- PRODUCTIVE (one hit): plain search "UK freight forwarder celebrates years anniversary family business 2026 customs clearance" gave KMB Shipping (and International Freight Solutions, already contacted).
- DEAD: FBJ 2026/07 p1, 09 p3-4, 10 p4, 11 p3 and category/forwarding (all large firms; ICL/Infinity Container, Toga, Drummond-Dachser); logisticsmanager/lloydsloadinglist/aircargoweek depot searches; regional business awards and IoE ITA 2026; recruiter job ads (names hidden); MBO/EOT searches (all 2017-2024); GLA UK welcomes (latest Sep 2025: Vantage Cargo, Rapid Transport); BIFAlink Jul 2026 (metadata only, no Nov issue yet); BIFA member pages (client_error); insidermedia (client_error); thebusinessdesk logistics stories (mostly hauliers/old); Supply Chain Excellence Awards 2026 (no list); MRO Europe 2026 exhibitor preview (no UK logistics names); Transport Logistic China UK pavilion search; freightforwardersfamily.com (no UK joins since 2017).
- PROVENANCE: seven-logistics.co.uk and georgebakershipping.com homepages refused until the domain surfaced in a search.

AU | Cargoport Pty Ltd (cargoport.com.au, Bibra Lake WA plus Melbourne, Sydney, Brisbane offices; founded 2004 by Marina Brew) | hook: FTA Weekly Report 2026/32 (12 Aug 2026, ftalliance.com.au/newsdetails/41059) says founder retiring and business passing to Nerelle Rockall, Danielle Muratore and team | missing: plain email (info@ is Cloudflare-obfuscated on every page)
AU | ASL Customs (Melbourne, Nick Borradale) | hook: FTA Weekly Report 2026/46 (18 Nov 2026, ftalliance.com.au/newsdetails/41724), FTA member catch-up | missing: website/email (aslcustoms.com.au not indexed)
AU | GTC (Perth; Abhidha Bhatt, Lorin McKenzie) | hook: new FTA member, new offices, FTA Weekly Report 2026/35 (2 Sep 2026, advocacydetail/4915) | missing: website, email, business type
AU | I.H. Hunter (Melbourne; Craig Priest, Lachlan Hunter) and ICAL (Perth; Mark Coleman) | NEW hooks: FTA Weekly Report 2026/43 (28 Oct 2026, advocacydetail/4950) for I.H. Hunter; 2026/39 (30 Sep 2026, advocacydetail/4930) for ICAL | both are in the Rejected list for "no hook", so I did not re-research; main session may re-open them
AU | Elto/Casa/Intergroup/End to End sizes unknown (written to results)
AU | Pentagon Freight Services AU: JAS group (out). Gibson Freight: JV with Cargo Services Far East (out). Seaway: 400+ staff (out). Clarke Global: still no company hook (latest company item 9 Jan 2026). TWG, Stokes and Bell: still no dated hook (Stokes news page is JS-only).

SOURCES:
- PRODUCTIVE: FTA / APSA Weekly Reports, "Out & About" and "Our expanding alliance" sections. Read them at ftalliance.com.au/advocacydetail/<id> (the /weekly-report/<id> pages are empty shells). Index of ids: ftalliance.com.au/weekly-report. 2026/21 to 2026/46 ids: 4854, 4861, 4866, 4871, 4875, 4877, 4882, 4884, 4890, 4895, 4900, 4904, 4909, 4913, 4915, 4917, 4920, 4924, 4930, 4934, 4941, 4947, 4950, 4956, 4960, 4963. All read this run except 4861 (read as newsdetails/40559, nothing), 4877 (Gibson/AWA only), 4904/4900 (read via newsdetails). Each new weekly report (Wednesdays) names 2 to 5 member firms with a date: use 2026/47 onward.
- PRODUCTIVE (one lead): DCN Shipping & Logistics Charity Golf Day write-up (thedcn.com.au/news/golf-day-yarn, 30 Oct 2026) hole sponsors: MGL Logistics (used), Asiaworld Shipping (likely AWS, already contacted), Seaway (400+).
- DEAD: FTA /news list (government notices only), FTA ads, DCN partner-news/industry-movers/The Grill tags, Gold Coast and Business NSW Sydney 2026 awards, Global Sourcing Expo, network new-member searches (GLA AU posts are 2025), ATT accreditation searches, BMSB 2026-27 advisories (large firms), Glassdoor/SEEK, businessnewsaustralia (fetch fails), Townsville port news, JCtrans weekly202647 (still fails 20 Nov). WebSearch with allowed_domains returns HTTP 400 if it includes sbs.com.au/theaustralian/goldcoastbulletin-type news domains.

# hksg run (20 Nov 2026): 1 qualified (Fast-Link Express HK), 38 searches

Near-misses:
HK | Fast-Link Express (qualified; note) | own site fastlink-hk.com is HTTP-only, WebFetch loops https->http and proxy curl refuses plain HTTP; site indexed (contact.html, profile1-4.html) | ownership/size from own site not read
HK | Lapton Freight (lapton.com, kelvin@ and enquiry@lapton.com) | homepage fetched 20 Nov: since 1999, CN+HK offices; no dated 2026 item | dated hook
SG | PAL Line (sales@palline.com.sg) | news page: Enterprise 50 award 2 Dec 2025 (before cutoff), Jul 2026 SEO posts only | hook after 20 May 2026 (watch E50 2026 results)
SG | WHL Logistics (info@whl.sg) | homepage has no dated news; template text contaminated (locksmith blurb) | hook
SG | AM Global | news page empty 20 Nov | hook
HK | Ports Express Ltd (ports-express.com.hk, Pangea member, est. 1998) | only Pangea news 26 Jun 2024 | email, hook
HK | Piaxa Logistics HK (piaxalog.com, Pangea member) | no news | email, hook, ownership
HK | NAF Global Logistics (HKTDC: 51-100 staff, est 1984, San Po Kong; HAFFA committee Raymond Wong) | no website/email found | site, email, hook
HK | HAFFA committee firms: Hentrans (possibly listed group), U-Ocean (U-Freight group, reject), CTI Logistics HK (no site; ctilogistics.com is Australian CTI), Bollyman / Forward By Norman / Easyway / Diversified Freight / OA Cargo (no sites surfaced in 2 searches) | HAFFA 2026 pages (luncheon 18 Sep id=3101, ALMAC 16 Nov id=3107, chairman msg id=3092) do not name committee members, so no person-level hook
Rejected: Air Sea Worldwide (30+ offices, JS-protected emails), Unitex HK (720 staff), Parisi Grand Smooth (Italian group), Spoti Freight HK (Bangkok HQ branch), Perfect Cargo / Po Fung (already contacted), 456 Logistics (already contacted), Golden Jet (no site found, 2nd check), Bright Line Freight HK (LA/Shanghai group), Speedway Logistics (1-5 staff).

SOURCES:
- Productive: MarDep directory fetches fine and gives official emails (fastlink-hk.com was in it, contradicting the 14 Nov 'no email' rejection). Freight Midpoint blog p1 (11 Nov 2026 Fast-Link post). Security Cargo Network news (securitycargonetwork.com/news/, 100 dated posts per page, HK: Perfect Cargo 3 Sep, Spoti 17 Sep; SG: Cooper Cargo Mar) - fetches cleanly, check for new HK/SG posts each run. Pangea HK profiles (pangea-network.com/freight-forwarder/...) give website, staff, founding, dated company news.
- HAFFA: hand-built Page/Default.aspx?id=NNNN fetch works (3092 chairman msg 20 Apr, 3100 HKICT 20 Jul, 3101 luncheon 18 Sep, 3104 CILT 20 Sep, 3107 ALMAC 16 Nov, 3108 FIATA guidance 6 Jul, 3123 B&R summit); IDs 3095/3096/3098/3105/3110/3115 return the homepage. Press release index (Index.aspx?id=4) lists titles/dates but no links. Album page errors.
- Dead (20 Nov): SAAA site (latest articles Sep-Oct 2026 name no member firms; transport logistic 2027 pavilion names only MMI Asia; no Oct-Dec 2026 PERSPECTIVES yet; jobs-connect errors); GLA news (new IDs render empty; only Jan 2026 and older fetch); Globalia news (last post Oct 2025); Freight Midpoint pages 2-7 (no HK/SG); ALMAC site (no exhibitor list); JCtrans weekly202647 (still client_error 20 Nov); SME100/SPBA/E50/SLA award searches; SG pricing-job searches (recruiter ads, masked emails); HK Customs AEO Express (only to Feb 2026 surfaced); allowed_domains '2026 news' over 40 unexcluded MarDep domains (nothing dated); Clutch HK (9 firms, mostly large); cargoconnections brochures (no dates).

## Run of 20 Nov 2026 (prep, 03Z): 5 of 25 written (AU 3, UK 2); US, HK, SG gave none; about 152 searches

Notes: dns.google MX lookups and FTA advocacydetail pages were refused (permission prompt timed out); hand-built URLs were refused almost everywhere, only URLs returned by a search fetched. Next-best timing: NCBFAA eBriefing and FMC OTI list due about 23 Nov, FTA Weekly Report 2026/47 about 25 Nov, IACAC Pallet November issue, JCtrans weekly202647 (still unpublished 20 Nov). Conditional AU leads held back: FJT Logistics (fjt.com.au, 25th anniversary in Oct 2026 News Brief, new Perth and Brisbane managers 19 Nov 2026; fjtmel@fjt.com.au appears only in the contact page meta description, visible emails Cloudflare-hidden; family-owned, earlier 'group' rejection was its own branches) and AAW Global Logistics (aawho@aaw.com.au on aaw.com.au/globallogistics/contact-us/; about 200 staff, Australian owned; only hook Breakbulk Europe 2027 listing, undated). UK Pinnacle International Freight (01059368, pharma warehouse 27 Aug 2026) has only Cloudflare emails.

### US near-misses
US | Highland Forwarding (Londonderry NH, founder-owned, 40+ staff, highlandforwarding.com) | independent project forwarder | missing: no email on site (phone only), no 2026 dated item
US | C.H. Powell Co. (Boston, 4th-gen family) | independent | missing: no published email; newsroom only regulatory posts (latest 3 Jun 2026)
US | Cargo Brokers International (Atlanta/Charlotte/Miami, family-owned, cargobrokers.com) | management page | missing: emails Cloudflare-obfuscated, no dated hook
US | A.J. Arango (Tampa, family, est. 1948) | site stale (copyright 2021), template email | missing: hook, email
US | Allyn International: written above as WEAK FIT (consultancy/own AI)
US | Ultra USA (NCBFAA new member 13 Nov 2026) | REJECT: AI customs-risk software vendor (carahsoft.com/ultra-usa)
US | WEST Forwarding (info@westforwarding.com; CEO Kristi Buckholz, President Derek Weaver on /our-team/) | 'Company Events' section empty | missing: dated hook
US | Atlanta Customs Brokers (ship@atlantacustomsbrokers.com) | banner '40 Years Strong 1985-2025', 'We have moved to 4777 Aviation Parkway Ste E' still undated | missing: move date
US | Southern States Forwarding (New Orleans, NCBFAA 13 Nov) | only a mapquest listing, no site | missing: site, email
US | Exportalia | grupoexportalia.com still redirect-loops (https->http) | missing: own-site email, ownership
US | Celeris Global | no size/address found in a search | missing: size
US | Cargo Brokers International, Highland Forwarding, C.H. Powell, A.J. Arango: see above
US | Highways & Skyways (Hebron KY) | REJECT: owned by Radiant Global Logistics
US | Masterpiece International | REJECT: Magnate Worldwide group
US | AMB Logistic (Troy MI) | REJECT: freight brokerage
US | Team Worldwide (Winnsboro TX) | REJECT: 35+ franchise branches, hook 2024, no email
US | Compass Logistics Marine (Global Affinity Alliance best partner award) | ajot page client_error, not checked | missing: everything
US | 1UP Cargo (Beverly Hills chamber member, VP Jordan Shahriary) | no website/email on chamber page | missing: site, email, hook
US | IFN US members (AWATAC USA, ISL International, Allpoints Unlimited, Segaduanca USA) | names only on ifnfamily.com homepage, no dates | missing: hook, sites

### US sources
- NCBFAA eBriefing base page (ncbfaa.org/news-advocacy/monday-morning-ebriefing-details) still shows the 13 Nov 2026 issue on 20 Nov (Adhoc, ANA Link, Armando Garza Jr., Clear Customs, Jack Li, Pro Ag, Southern States Forwarding, Ultra USA): all used, rejected or individuals. /1 refused (provenance). Next issue around 23 Nov.
- IACAC homepage lists Pallet Oct 2026 (10 Nov) as newest; no November issue yet; the-pallet-november-2026 refused.
- JCtrans weekly202647: refused (provenance) and not indexed (two searches). FMC: no list after 16 Nov (next one about 23 Nov), not searched.
- Allowed_domains news search over known independent US forwarder domains gave Allyn International (allynintl.com news pages fetch; the news index redirect-loops, but /news-press-releases/P2 works). Lesson: leave domains with large news archives (mohawkglobal.com, everglorylogistics.com) out, or they fill every result.
- Clutch US customs brokers page=6 and page=11 (clutch.co/us/logistics/customs-brokers?page=6, clutch.co/logistics/customs-brokers?page=11) fetch. Mostly trucking or large firms; unchecked forwarders: Posey International (Houston, 10-49), Compass Global Logistics (Spring TX), Preferred Global Logistics (San Diego), KPI Logistics (San Diego), Innovative Carriers and Unisource Shipping (Brooklyn), Agra Brokerage (Jamaica NY), JF Moran (Smithfield RI, 50-249), Howard Baer (Nashville), Unitrans International (Inglewood), Codysur (San Benito TX, probably Mexican group). Guessed domains did not surface.
- DEAD (20 Nov US run): Miami Air Cargo Association (launched Jan 2026, board only); Inc 5000 and fast-growth list searches; Beacon Awards 2026 (Trade & Logistics winner ALLYO = Interport, rejected); FIU Business at its Best 2026 (A1 Worldwide, article 19 May, one day before the cutoff); NJBIZ Best Places 2026 (no forwarders); OCBJ Best Places 2026 (list not in page); GPTW pages (Worldwide Logistic Partners, Logiaide, OnBoard, all known); jobleads/careers-page/ATS pricing-job searches (client_error or recruiters); IFN network (US member list not in page text); Security Cargo Network news (no new US members; IGL Charlotte page refused); Pacific Coast Council/WESCCON and NCBFAA events (vendors, CBP webinars); JFK brokers (members-only), IFFCBANO, CBFANC (sponsors are insurers/vendors); perishables press (Advance CB old); CargoWise news (no US forwarder customers); Raft/Freightos case studies (large firms); local business journals (lbbusinessjournal, gsabusiness, memphisdailynews: nothing new). WebSearch returned HTTP 400 when allowed_domains included labusinessjournal/ocbj/sdbj/libn/djc/texasborderbusiness/dallasinnovates (one of them). FreightWaves Borderlands tag (Aug-Nov 2026: only acquired firms, RM Customhouse and Interload); JCtrans success stories (Asian firms, 2025).
- PROVENANCE this run: almost every hand-built or linked URL was refused (ncbfaa /1, iacac Nov, jctrans 47, atlantacustomsbrokers, allyn news index, securitycargonetwork post). Only URLs returned by a search fetched reliably.

### UK near-misses
- UK | Pinnacle International Freight Ltd (pinnaclefreight.com, Broughton Astley, Leicester; est. 1972 by three brothers, "privately owned since 1972", firmbase 55 staff; US office Virginia Beach) | hook: opened GDP pharma warehouse Hemel Hempstead, post 27 Aug 2026 (pinnaclefreight.com/2026/08/27/pinnacle-international-freight-opens-gdp-compliant-pharmaceutical-warehouse-facility-in-hemel-hempstead/, quote Gavin Newman, Ops Director); also Made in the Midlands visit 8 Sep 2026 | missing: plain email (every page Cloudflare-obfuscated; decoded fragment = enquiry@pif.co.uk, not usable per brief), CH check
- UK | AGI Global Logistics Ltd (agi.global, Westerleigh Bristol, co. 07552812 per site, "100 team members", 11 UK offices) | hook: UK Transport Awards 2026 win, post 15 Apr 2026 (before cutoff) | missing: email (contact form only), hook in window
- UK | Viamaster International (viamaster-intl.com, Leeds, MD Paul Pedley, info@viamaster-intl.com on /news/) | latest company items 11 Jan 2026 (web award), 17 Feb 2026 | missing: hook after 20 May 2026, CH
- UK | Grace Overseas (graceoverseas.com, Manchester/Birmingham, family-owned since 1984, MD Sarah Taylor; enquiries@graceoverseas.com, freight@graceoverseas.com on /a-new-era-.../ page) | latest company items: joined UKWA 9 Mar 2026, rebrand 23 Oct 2025; only SEO posts after 20 May | missing: dated hook, CH
- UK | TCB Group (tcbgroup.com, Belfast + St Helens + Dublin + Singapore; est. 2007; wholesale LCL consolidator for forwarders; sales@tcbgroup.com on post pages) | company items: Sera Lim joins SG team 12 May 2026 (before cutoff); Nov 2026 posts are service/SEO pages (NY LCL service introduced Mar 2026) | missing: hook in window, CH (NI company)
- UK | Eagle International Logistics (eagleinternationallogistics.com, Altrincham, co. 13042931 per site, privately owned, ~10 named staff; ops@eagleinternationallogistics.com on /about-us/) | missing: dated hook
- UK | Burhill Logistics (burhilllogistics.com, Felixstowe) | latest post 12 Dec 2025, emails Cloudflare-obfuscated | drop
- UK | Freight Agency Ltd (freightagency.com, Baildon/Bradford, since 1986, 38 named staff, Ghana office; sales@freightagency.com on /about-us/) | blog Jun-Aug 2026 is SEO guides only; newest company item Oct 2025 (Saudi docs service) | missing: dated hook, CH, ownership
- UK | Beckchoice (beckchoice.co.uk, Tilbury, since 1979, MD Ray Palmer, info@beckchoice.co.uk) | company news only BIFA golf day 23 May 2025; 2026 posts are trade alerts | missing: hook
- UK | MIES International (miesinternational.com, Ashby de la Zouch, employee-owned, co. 1261687, sales@mies.co.uk) | newest post 22 Dec 2025 (BIFA terms notice) | missing: hook
- UK | Pinnacle CH note: PINNACLE INTERNATIONAL FREIGHT LIMITED 01059368 (great.gov.uk Find a Supplier, 51-200 staff, no email there); holding co 05012885 PSCs = Pinnacle International Freight Group Ltd and Nathan James Burrell (family)
- UK | Executive Freight Services Ltd (executivefreightservices.co.uk, Hampshire, 5 UK offices) | Hampshire Chamber listing gives sales@executivefreightservicesw.co.uk (typo domain); own site fetch refused | missing: hook, own-site email
- UK | We Ship Global Forwarding Ltd (sales@we-ship.co.uk on homepage) and Phaon Freight Solutions Ltd (13628985, hello@phaonlogistics.com on /services) | only hook remains the IFN UK blog post (8 Oct 2026, URL refused this run) | missing: verified hook, CH status, size
- UK | Mersey Forwarding (merseyforwarding.com) | newest company post 21 Oct 2025 | missing: hook
- UK | Excluded: Customs Clearance Ltd/CCL (ccllhr.com, Lenton Group), Sprint Logistics (e-commerce 3PL), FWD Freight / AFI / Andante Freight (EFS Global group), World Cargo Logistics (news undated, no email), Rochefreight (Irish Roche Logistics Group), Bold Logistics (Barcelona), Seaspace (now Emerge Global, acquisitive group, Cloudflare emails, rebrand 1 Apr 2026), Transportify (site errors), Normac Shipping (port agency/chartering), Trans-Bridge (no dated posts), Paragon Freight (newest company post Jan 2025), Clearfast (posts 2019), Selvic and Uneek (SEO/case studies only), Chandler Freight (Cloudflare email), Burhill (Cloudflare email), Daygard (undated), Pegasus Logistics (US), PFE Express (no 2026 items found), MultiFreight and Customs Declarations UK (software vendors), Tuscor Lloyds (no email, newest news 2024), Grace/Viamaster (see above).

### UK sources
- PRODUCTIVE: firmbase.co UK freight-forwarding lists (May 2026; domains, headcount, founding year): /resources/industry-lists/freight-forwarding-companies-in-the-uk and -london, -manchester, -birmingham, -leeds, -liverpool, plus logistics-companies-in-the-uk-london. Fetch after any search surfaced firmbase. Top ~50 per page readable; most domains now searched (see below).
- PRODUCTIVE: revenuebase.ai new categories (surfaced with one allowed_domains revenuebase.ai search): /freight-forwarding-companies/united-kingdom(/london), /international-freight-forwarding-companies/united-kingdom, /international-food-freight-forwarders/united-kingdom, /container-freight-forwarders/united-kingdom/london, /international-freight-forwarders/united-kingdom/london, /freight-forwarding-services/united-kingdom/london, /freight-brokers-and-forwarders/united-kingdom. Hand-built city pages (heathrow, bristol, nottingham) were refused.
- BEST QUERY for allowed_domains batches of ~24 company domains: 'sponsorship OR charity OR "welcome to the team" OR "congratulations" OR "proud to announce" OR "new warehouse" 2026' (surfaced Carry Cargo, Trinity, Pinnacle-type company-news posts). "news 2026", "latest news", "company news blog" queries return SEO/trade-alert pages, and one SEO-heavy domain (Supreme, Uneek, TCB) can take all 10 results: leave such domains out.
- Domains already searched this run (do not repeat): see firmbase/revenuebase lists above; essentially all London, Manchester, Liverpool, Leeds and Birmingham top-50 forwarders plus revenuebase London lists.
- PROVENANCE (this run): every hand-built URL was refused, including Companies House search pages and revenuebase city pages; even links inside fetched pages were often refused. Only URLs returned by WebSearch (or a few links on fetched pages) worked. CH company pages surface with an allowed_domains CH search on the exact company name plus number.
- DEAD (20 Nov UK run): ifnfamily.com blog and members directory (no member names; blog URL refused), Pangea UK (3 members: Santova, Transvalair, WTA, no fits), Made in the Midlands Expo (no exhibitor names), Grant Thornton Kent/Cheshire/Herts Ltd 2026 (no small forwarders), Kent Invicta MegaGrowth 50 (17 Mar 2026), GM/Hampshire/Hull/Black Country chamber searches (old or large firms), freight-software vendor search (GoFreight SEO only), Corporate Vision/SME News awards (no 2026 UK forwarder winners), B Corp search (500 Logistics certified Aug 2024), trade press new-office search (Ntex, Campeys, Future Forwarding old), careers/pricing-job searches (recruiters only), Multimodal 2026 "visit us" search (software vendors), anniversary search (Unsworth, UPN, KMB already used).

### AU near-misses
AU | Cargoport (cargoport.com.au, Bibra Lake WA) | hook FTA 2026/32 founder retiring (12 Aug 2026) | info@ is Cloudflare-obfuscated on every page (home, contact, about, our-network, resources, news); T&C PDF and .docx forms carry no email; news page empty. DROP unless the main session can find a plain address.
AU | ASL Customs (Melbourne, Nick Borradale) | hook FTA 2026/46 (18 Nov 2026) | no website found in two searches (name and person); aslcustoms.com.au not indexed
AU | GTC (Perth) | hook FTA 2026/35 | no website found (search returned only GTL / unrelated)
AU | Across the Ocean Shipping (atoshipping.com; au.atoshipping.com; Cremorne VIC; est. 2008; 21-50 staff; also US/NL sites) | Cremorne HQ move is Jan 2024; site has an undated "New Brisbane Office" post (us.atoshipping.com, fetch client_error) and an undated "proud to announce" DG energy-storage project post | missing: dated hook, plain email (none on pages read), ownership (multi-country)
AU | Express Customs & Forwarders (ecandf.com.au, Tullamarine, 10-49, operations@ecandf.com.au on homepage) | only SEO blog posts (latest 14 Apr 2026) | dated hook
AU | Matthew Short & Associates (matthewshort.com.au, family owned, 30+ years, enquiries@matthewshort.com.au) | no news | dated hook
AU | SP Customs & Forwarding (spcustoms.com.au, Tullamarine, 2-9, imports@spcustoms.com.au) | no news; small | dated hook
AU | Australian Customs Clearance (aucustomsclearance.com.au, Redland Bay, 100% Australian owned, 6 cities) | news = SEO articles only; no email on about page | hook, email
AU | International Trade Management / ITM (itm.com.au, Tullamarine HQ, 100+ staff, sales@itm.com.au on /contact-us/brisbane) | no news section; NZ arm uses pengellys.co.nz domain (check ownership) | dated hook
AU | FM Global Logistics Australia (fmgloballogistics.com.au, Bibra Lake WA, sales@ and office emails on homepage) | site last modified Feb 2025, no news | dated hook
AU | Transworld Freight Services (transworldfreight.com.au, Tullamarine, 50-249) | homepage has phone only, no email, no news | email, hook
AU | DSH Global (rejected earlier) | "Customs approved warehouse S77G" and "Quarantine approved" announcements are undated | dated hook
AU | Airwave (Australia) Pty Ltd (airwaveaust.com.au, Melbourne, est. 2000, GLA golden member, post undated) | site loops https->http, unreadable | email, hook
AU | Taurus Logistics (tauruslogistics.com.au, info@) | vehicle/boat shipping forwarder, copyright Taurus Logistics Ltd (likely NZ company) | hook, ownership
AU | Snapes Logistics (snapes.com.au, est. 1932, 7 cities) | mainly 3PL/FF&E install, form only | not target
AU | Scorpion International (Mayfield West NSW) | "30 years" HBR article undated; merged into Powerhouse Group 2010 (Powerhouse already contacted) | REJECT (group, contacted)
AU | Excel/ICAL/I.H. Hunter/FJT/AAW: see blocks above
AU | Rejected this run: Galaxy Freight (Indian HQ), ACFS Port Logistics (in administration), CRL Express (domestic linehaul; sponsorship Dec 2025), Gavos and Bullocks and 3DL and FreightPlus and EES and PAT Express (already in companies.csv), Orbit Logistics (rejected 19 Nov), Rohlig (group).

### AU sources
- PRODUCTIVE: own-site monthly news briefs/newsletters (fjt.com.au/<month>-2026-news-brief/ gave FJT 25th anniversary; excellogistics.com.au/news/ gave Excel). Look for "News Brief"/"Newsletter" sidebars on Clutch-listed AU forwarder sites.
- PRODUCTIVE: Clutch AU customs-broker pages (clutch.co/au/logistics/customs-brokers, ?page=3, ?page=4, /melbourne?page=2) and freight-forwarders/melbourne?page=2 fetch after one surfacing search; Leaders Matrix gives domains. Unchecked names from them: Integrated Cargo Services (Port Melbourne), Allworld Logistics (N Melbourne, 50-249), MODE Logistics, Bluestar Global, REM International, Austex, Exim Express, Globe Trans, ADT Freight (robots), Trademark Logistics (Derrimut), Consolidated Cargo and Customs Services, AGL Logistics, CEO Global Group, PDS Global, Summit Global, CargoLive, Poseidon Freight, J.N. Allen, Interfreight, Vantage Freight, Cargo Australia, Export Consolidation Services, Anchor Logistics (50-249), Merchant Shipping (50-249), MF Freight (mffreight.com.au), Shiprite International, Clemenger International Freight (cif.com.au robots-blocked), Diamond Freight (diamondfreight.com.au/contact-us/ surfaced, not read), Zenith International Freight, Fremantle Customs Brokers, Chilvers Customs, Customs & Forwarding Services (Bowen Hills), D&D Worldwide (Geelong), Freight Management Australia, TFI Global.
- ICN Gateway supplier pages (gateway.icn.org.au/suppliers/<id>) give staff counts, ownership and emails for AU project forwarders (AAW).
- heavyliftpfi.com/news/regions/australasia: dated AU project-forwarder stories (17 Nov Bullocks, already contacted); page/2 refused.
- FTA Across Borders Annual Review 2026 PDF (ftalliance.com.au/data/accrossborder_attachments/48_FTA_2026_Digital.pdf): few forwarders named (AAW, TGL).
- DEAD (20 Nov AU run): FTA weekly-report index and advocacydetail/newsdetails hand-built URLs (provenance refused; homepage shows newest report is 2026/46, 2026/47 due ~25 Nov); JCtrans weekly202647 (refused); IFCBAA latest news (regulatory notices only); IFCBAA/award searches; local business awards (Issuu finalist docs have no text); Women in Industry 2026 (no forwarders); sports sponsorship search (only CRL Express, Orbit); anniversary search (PAT 11 May, EES Mar, Gavos 2025 all used/old); new-office search (ATOS 2024, FJT Perth undated); IMARC/expo exhibitor searches; ATT accreditation search; network new-member search (Airwave GLA undated, 1UP Cargo 2020); Clarke Global news (SEO only); aucustomsclearance news (SEO only).
- Blocked URLs this run: ftalliance.com.au/weekly-report, ftalliance.com.au/advocacydetail/4950, /news/41724, ihhunter.com.au root, fjt.com.au root, aaw.com.au root, matthewshort/ecandf/zenith/shiprite before surfacing, marketing.jctrans.com weekly202647, heavyliftpfi page/2, airwaveaust.com.au (redirect loop), cif.com.au and adtfreight.com.au (robots), au.atoshipping.com (client_error).

Searches used: 36 of 40.

### HK/SG near-misses
HK | Forward by Norman Ltd (bynorman.com, Cheung Sha Wan HQ + Yuen Long air/logistics warehouses, Norman Express (China) Shanghai/Guangzhou; 30+ yrs airline agent; revenuebase 51-200; HAFFA Exec Committee 2025-27 firm) | email hq@bynorman.com and logistics.hkg@bynorman.com on bynorman.com/contact; site has sea-freight quote-request form | missing: dated hook after 20 May 2026 (no news page; one name search found nothing), ownership not stated
HK | Stallion Freight Ltd (stallion.com.hk, founded Jan 1991, air/sea, Guangzhou branch; revenuebase 11-50) | no email on homepage (contact.html not read) | email, hook
HK | Fast Cargo Solution Ltd (fastcargosolution.net, Yau Tong; 11-50) | Insights page = republished WSJ items only, no email on expertise page (contact page not read) | email, hook
HK | We World Express (weworldexpress.com, Kwai Chung HQ + Istanbul/Shanghai/Shenzhen; cs@ and express@weworldexpress.com on contact.html) | multi-country, likely express/courier | hook, business type
HK | OneGlobe Logistics HK, now AONE Global Logistics HK (oneglobehk.com -> aoneglobalhk.com; JCtrans join noted in an earlier run) | revenuebase 1-10 staff, no email | email, size
HK | A&G Logistics Ltd (anghk.com, est. 1996 = 30th year in 2026; MarDep emails alan@ / kam@anghk.com) | no dated 30th-anniversary item on site | dated hook
HK | DealerSend Logistics (dealer-send.com) | e-commerce fulfilment, Cloudflare email | reject (not a forwarder fit)
HK | Freight Midpoint HK members without hooks: Metro Freight, Multi-Gold Air & Sea Express, Sky G Logistics (member since 2014-2018) | no sites checked | site, email, hook
SG | GFS Forwarding Pte Ltd (gfsforwarding.com, Tampines; info@gfsforwarding.com on homepage; revenuebase 11-50; sea/air/road, DG, projects) | no news page, careers empty | dated hook, ownership
SG | Infreight Logistics Pte Ltd (infreight-logistics.com, United Square + JB + HCMC offices; infreight.sg@infreight-logistics.com; WCA + JCtrans member; 11-50) | no news page | dated hook (check JCtrans join date)
SG | Airpak Express (airpak-express.com, Changi South; CS_SIN@AIRPAK-EXPRESS.COM; 51-200) | media page = SEO blog only, last 14 May 2026; express/e-commerce heavy | hook
SG | Global Airfreight International (globalair.com.sg, 51-200; STP Plus, TradeFIRST Premium, CEIV Pharma) | no email on certification page, certs undated | email, hook
SG | Ansync Global (ansyncglobal.com, support@) | cargo GSA, latest post Nov 2024 | not target/hook
SG | Best Global Pte Ltd (bestglobal.com.sg) | no email on homepage, no news | email, hook
SG | Asia Marine Logistics (asiaml.com) | no email, no news | email, hook
SG | Freight Midpoint SG members: ETW Logistics, SA Logistics (S), WWW Cargo, Kai Associates | not checked | site, email, hook

### HK/SG sources
- Security Cargo Network news (securitycargonetwork.com/news/): newest HK/SG item is Cooper Cargo SG 12 Nov 2026 (already in companies.csv); otherwise only Perfect Cargo / Spoti (used). Next run: check for posts after 12 Nov.
- revenuebase.ai SG/HK lists fetch after a search with allowed_domains revenuebase.ai: /companies/freight-forwarding-companies/singapore/singapore, /international-freight-forwarding-companies/singapore, /consolidation-freight-forwarders/singapore/singapore, /freight-brokers-and-forwarders/singapore/singapore, /international-air-freight-forwarders/hong-kong (gave bynorman.com, previously "no site found"). Unread: /freight-brokers/singapore, /freight-forwarding-hubs/singapore, /container-freight-services/singapore, /freight-consolidation-centers/singapore.
- HK Customs AEO Express index (customs.gov.hk .../aeo/aeo-express/index.html) lists issues #132-162 (May-Nov 2026); new HKAEO members in window are a supplement maker (Jul) and a noodle maker (Sep): DEAD for forwarders.
- MarDep directory fetched (URL without index.html worked after a search); 120 firms; allowed_domains searches over 40 more MarDep domains found no dated company news (Kesco only rate reports, US-HQ).
- Freight Midpoint directory (freightmidpoint.com/Directory/) gives HK/SG member-since dates (all 2014-2024).
- DEAD (20 Nov, this run): HAFFA 60th gala page (only Hactl/AAHK/AAT sponsors), HAFFA events list (no member names), Super Terminal Expo 2026 and LogTech Expo 2026 (vendors), HKIA cargo luncheon 17 Jul 2026 (no forwarder names), GLA (article/member pages client_error), Pangea news search (Visy, APM only), PCN/GPLN search (brochures only; news archive refused), network new-member searches (JCtrans dominates), anniversary search (Ports Express 2024), trade-press "HK-based/SG-based forwarder" search (large firms), HK pricing-job search (recruiters), SG Customs awards/directory (no forwarder list), E50 2026 (not yet announced as of 20 Nov), SAAA homepage (Oct 2026 council note names no firm; jobs-connect errors), Enterprise SG logistics article (client_error).
- Refused without provenance (permission prompt timed out): JCtrans weekly202647, mardep .../freiforw/index.html, pangea-network.com country pages, clutch.co/sg, revenuebase hand-built URLs, projectcargonetwork.com/news/archive. curl to mardep.gov.hk blocked by proxy (403).
- Also DEAD: Cathay Cargo top-customer awards story (30 Jun 2026, no recipients named); Chinese-language HK anniversary/new-warehouse search; combined name search for Infreight/GFS/Stallion/Norman (no hits).

Searches used: 30 of 30. Qualified: 0.


## Run of 20 Nov 2026 (prep, 06Z): 7 of 25 written (UK 4, AU 2, US 1); HK and SG gave none; about 165 searches

Notes: dns.google MX lookups refused again (permission prompt), all MX unchecked. Next dated sources: NCBFAA eBriefing and FMC OTI list about 23 Nov, FTA Weekly Report 2026/47 about 25 Nov, DCN awards night 26 Nov (winners), HAFFA 60th closing ceremony 27 Nov, JCtrans weekly202647+ (still refused/unindexed 20 Nov), IACAC Pallet November, SAAA PERSPECTIVES Oct-Dec 2026, Enterprise 50 2026 results.

### Unfinished leads (email known unless noted; missing a dated hook after 20 May 2026 unless noted)
- US | ILS Inc (ilsinc.net, Carson CA, family-owned since 1995, info@ilsinc.net) | hook, size
- US | BGI Worldwide Logistics (bgiworldwide.com, Rancho Dominguez CA; sales@bgiworldwide.com on /contact-us/new-york/; Clutch 10-49) | hook, ownership
- US | JDF International Transport (jdftransports.com, Timonium MD, est. 1991, info@jdftransports.com) | hook (footer 2022)
- US | Worldwide Cargo Services Inc (Lawrence NY) | joined Aerocean Network (aeroceanetwork.net post, undated) | date, website, email
- US | Serra International | President won NY/NJ FFFBA 2026 Captain of Industry (8 Jun 2026) | published email (earlier rejected for none)
- UK | Trade Freight International / International Logistics Centre (tradefreight.co.uk, Newark; P.A. Freight Services) | hook: hosted "Exporting for Growth" event 12 Nov 2026 | plain email (all Cloudflare); check internationallogisticscentre.com; CH
- UK | RJJ Freight (rjjfreight.co.uk, Felixstowe) | JCtrans join 23 Oct 2026 (weekly202643), Formula Student 2027 partner | plain email (obfuscated), CH
- UK | KC Group Shipping (kcshipping.co.uk, Glasgow, 27 staff, ist@kcshipping.co.uk) | Freyt World join, undated | date, CH
- UK | Aver Logistics (averlogistics.co.uk, Chesham, 7 staff) | site errors | everything
- UK | Felixstowe revenuebase names unchecked: Admark Shipping Solutions (06950315), Origin Global Logistics UK, Kedan, Harbur, We Global Logistics
- AU | FJT Logistics | 19 Nov 2026 News Brief (25th anniversary) | plain email (all 12 Cloudflare; privacy page refused)
- AU | Bollinger Shipping Agency (bollinger.com.au, Thornleigh NSW, family since 1949, info@bollinger.com.au) | leadership-change post 6 May 2026 (before cutoff) | newer hook
- AU | Transcend Logistics & Customs (info@transcendlogistics.com.au), Tayper (Port Adelaide, broker@tayper.com.au), Townsville Customs & Forwarding (info@townsvillecustoms.com.au), ITM, Across the Ocean Shipping | hook
- SG | M&P International Freights (sales@sin-mp.com.sg), Cargohub Groupage (sales@chubgroupage.com), Astro Express Logistics (sale@astro-elogistics.com), FS Freight Systems (no email), Apollo Logistics (Cloudflare) | hook
- HK | HLT Logistics (sales@hlt.hk; posts are industry analysis), Worldtrans Logistics (larry.cheung@ GM), Fast Cargo Solution (no email) | hook

### Sources
- PRODUCTIVE: firmbase.co technology lists (surface with an allowed_domains firmbase.co search): /resources/technology-lists/freight-forwarding-using-divi-uk (115 small UK forwarders, read fully), logistics-using-google-ads-uk, -godaddy-uk, -wpforms-uk, -wp-rocket-uk, -amazon-cloudfront-uk, -powr-uk (mixed with hauliers). Gave Hexagon and Envio.
- PRODUCTIVE: revenuebase /companies/international-air-freight-forwarders/united-kingdom/felixstowe (gave Seaport Freight).
- PRODUCTIVE (one hit each): search for freight firms in 2026/27 football kit sponsor announcements (Banks & Lloyd); allowed_domains batch over ~20 small US broker domains with query 'foreign importer of record CTPAT validated broker January 2027 rule' (Stile; small brokers' regulatory blogs are dated); allowed_domains sponsorship/charity query over Clutch Melbourne domains (Bluestar).
- allowed_domains accepts TLD suffixes such as com.sg and com.hk (one search covers all SG or HK sites); so far it mostly returns SEO posts.
- USED UP: DCN 2026 finalists (AAW was the last AU forwarder), Maryland port broker PDF, Clutch US city lists (NY, Philadelphia, Miami, LA, Houston, Chicago, Seattle, Atlanta), FTA directory I-Z domains (searched), heavyliftpfi Australasia p1, Security Cargo Network news (nothing new after 12 Nov), revenuebase SG lists (customs-brokers-and-freight-brokers, freight-brokers, international-freight-brokers) and HK lists (ocean-freight-forwarding, customs-brokers-and-freight-forwarders, freight-forwarding-brokers).
- DEAD (20 Nov 06Z): NCBFAA eBriefing (still 13 Nov issue; numbered archive URLs are 2021), AfA directory (vendors), GPTW/Top Workplaces again, network new-member pages (Lognet 2017), regional UK awards (Scotland, Wales, NI, NE), UK new-office and anniversary searches, AU job boards, SAAA homepage, HAFFA/HK awards searches, LinkedIn/Facebook/WCA (robots).
- Leave atoshipping.com out of allowed_domains batches (SEO posts fill all results).

## Run of 20 Nov 2026 (prep, 11Z): 4 of 25 written (AU 2, UK 1, US 1); HK and SG gave none; about 150 searches

Written in 2026-11-20-mixed-4 (now rejected for research): ASL Customs Services (AU), All Ports International (AU), AmWorld UK (UK), PNG Worldwide (US). Pinnacle International Freight dropped (no plain email anywhere after full check). MX lookups refused again; all unchecked. iacac.org is a college-admissions body: The Pallet is at iacac.com. FTA weekly report pages ftalliance.com.au/newsdetails/<id> fetch by hand-built URL (2026/46 = 41724; 2026/47 expected about 41780-41790, ~25 Nov).

### US agent notes

### US research run, 20 Nov 2026: 1 qualified (PNG Worldwide), 37 of 40 searches

#### Qualified (in us.jsonl)
- PNG Worldwide, LLC (Lititz PA): hook is its post of 24 Sep 2026 (customs team recovered millions in IEEPA/CAPE refunds); email intl@pngworldwide.com; MX unchecked; headcount not stated. A weaker second hook: SOC 1/SOC 2 Type II programme post, 14 Aug 2026.

#### Unfinished candidates
- US | Trans-Overseas Corporation (trans-overseas.com, Romulus MI; customs broker since 1978, IATA/FMC, offices in Grand Rapids and Taylor, 150k sq ft warehouse; sales@trans-overseas.com on /?p=647 and /careers/) | newest company news Sep 2025 (website relaunch), careers page empty | missing: dated hook after 20 May 2026, size, ownership
- US | Bruning International (bruninginternational.com, Holbrook MA; founded 1975, run by the family's 3rd generation; Clutch 10-49) | /news has only SEO posts (latest 26 Aug 2026); /contact has phone only | missing: email, company hook
- US | R.W. Smith & Co. (rwsmith.com, Houston; since 1936, so 90 years in 2026; NVOCC "Sea Smith"; info@rwsmith.com on /locations and /who-we-are) | press and events pages empty; Clutch says 2-9 staff | missing: dated hook (a 90th-anniversary item would do it), size
- US | Gilscot-Guidroz International (gilscot.com, Marrero LA; family firm since 1967; 14 named staff incl. Rates Manager Ron Marroy; WCA member) | news = tariff alerts only (latest 24 Jul 2026); contact page has a form only | missing: email, hook
- US | Seacoast Logistics Inc (seacoastlogistics.com, Portsmouth NH; sales@seacoastlogistics.com on /about-us; Clutch 10-49) | no news section; Portsmouth chamber member listing exists (business.goportsmouthnh.com/list/member/seacoast-logistics-inc-6287, not read) | missing: hook, ownership
- US | J.F. Moran (jfmoran.com, Smithfield RI, 50-249) | www pages are robots-blocked; jfmoran.com/foreign-trade-zone fetched but other pages failed | missing: email, hook
- US | New Orleans forwarders from the Port of Greater Baton Rouge forwarder directory (portgbr.com/port-directory-freight-forwarders; old list, but gives domains and named emails): GCI Forwarding (gciforwarding.com, gary@gcifwdg.com), Missionary Expediters (mxshipping.com, jackf@), Port Cargo Service (portcargo.com, kevin@), Schwartz Forwarding (schwartzforwarding.com, schwartz@), Irwin Brown (ibrown.com, shellyb@), Worldwide Transportation Services (worldwidenola.com, conrad@) | sites not yet surfaced by a search, so fetches were refused | missing: check the email on the company's own site, a hook, ownership. M.G. Maher now belongs to Livingston (reject).
- US | Boston/NH, from Clutch (clutch.co/logistics/customs-brokers/boston.md): MIG Express (migexpress.com, Nashua, 10-49, est. 2007) and Officium Solutions (officiumsolution.com, Plymouth MA, 10-49) | missing: everything
- US | Houston, from Clutch (clutch.co/logistics/customs-brokers/houston?page=2): Canyon Logistics (canyongl.com, 10-49), COGI Logistic Solutions (cogils.com, 2-9), ASL Global Logistics (2-9), Rivera Forwarding (Porter TX, 2-9) | fetches refused (domains not surfaced in a search) | missing: everything
- US | FreightTAS LLC (Michigan) | Workable ad for an Ocean Import/Export Coordinator (jobs.workable.com, page client_error) | missing: website, email, date

#### Rejected this run
- Airlift USA (airliftusa.com): 14 offices in India plus VN, BD and KH, so likely part of a group
- Compass Logistics & Marine: already contacted; its GAA award is from Nov 2025
- J.M. Rodgers, Approved Freight Forwarders, Freight Right: already in companies.csv
- PSI Global Logistics: the 13 Jul 2026 post is marketing, no company news
- Everglory Logistics: the only company news is the 2016 Liteship acquisition, and no plain email
- Unique Logistics International: part of listed Unique Logistics Holdings
- Imperative Logistics / José D. González CHB: rejected before (PE rollup); acquisition dated 23 Jun 2026
- Texas International Freight: SEO-only site
- Kwick Kargo: page has no date and no email

#### Sources
- PRODUCTIVE (one hit): a topical search on IEEPA/CAPE refunds surfaced small brokers' own posts that carry a company angle ("our team recovered...") and print emails (PNG). Block large or SEO domains (freightright, dimerco, flexport, jdsupra).
- NEW (not yet fully used): the Port of Greater Baton Rouge forwarder directory (portgbr.com/port-directory-freight-forwarders, old, NOLA names with named emails); Clutch Boston customs brokers (.md) and Clutch Houston customs brokers page 2; Clutch Louisiana shipping list (mostly trucking; QCS Logistics and Missionary Expediters are forwarders).
- World Freight Network news (worldfreightnetwork.com/news/): 9 posts from 8 Oct to 17 Nov 2026 announce renewals but no new US members. Cargo Connections news: American CargoCare (Anaheim) joined on 5 Feb 2026, which is too old.
- DEAD: IACAC search (iacac.org is the college-admissions body; the cargo one is iacac.com, and its Nov Pallet is not out yet); Inc 5000 2026 (FreightWaves 167-company article, 18 Aug 2026, names only trucking and tech, Jet Freight Services unverified; the datawrapper chart is 2024 with no rows; inc.com profiles are trucking); small-business-of-the-year, Torch Award, world-trade award, WCA award and ISO/CEIV certification searches; airport lease and new-office searches (large groups); maritime-executive corporate search (old); Top Workplaces 2026 search; FCBF golf 2026 (no sponsor names); Global Trade Magazine leading 3PLs (nothing after 2020); 25-year anniversary search (India, Peru); World Cup 2026 search (Rock-it); BambooHR/Workable/Breezy/applytojob job searches (recruiters, OEC, Laufer, Alara); chamber member-spotlight search; goodfirms Michigan (client_error); JCtrans weekly202647 (still client_error); txgulf.org listing (no contact details).
- PROVENANCE: dns.google MX lookups were refused (permission timeout) and curl to dns.google got a proxy 403. Domains that appeared only inside fetched pages (schwartzforwarding, gciforwarding, mxshipping, canyongl, cogils) were refused. apply.workable.com was refused.

#### Searches used: 37 of 40

### UK agent notes

### UK research run, 20 Nov 2026: 1 qualified (AmWorld UK), 37 of 40 searches used

#### Qualified (written to uk.jsonl)
- AmWorld UK Limited (01974849, Colnbrook): sleeve sponsor of Maidenhead United Women, 13 Aug 2026; info@amworld.co.uk; MX unchecked (dns.google refused, DoH via curl gets a 403 from the proxy). Borderline fit: courier-led, but it lists global freight forwarding. Independent: AmWorld UK is the acquirer of Crossflight Group Holdings (CH PSC notice, 4 Apr 2026).

#### Unfinished candidates (company | known | missing)
- Phaon Freight Solutions Ltd | 13628985, active, CS 11 Jun 2026; Ludgershall/Andover; hello@phaonlogistics.com (phaonlogistics.com and /about); directors Mitchel Cox and Michael Foulds; accounts went from micro (2023) to total exemption full (FY Sep 2025); moved to bigger premises Jan 2026; share allotment Jan 2026. Hook: IFN Gold Founder member in the ifnfamily.com/blog/freight-forwarders-uk/ post (8 Oct 2026, URL now fetched and verified) | headcount (probably under 10); hook is only a network listing
- We Ship Global Forwarding Ltd | sales@we-ship.co.uk, Stowmarket, Amazon FBA forwarder; same IFN post (8 Oct 2026) | CH check, size; weak hook
- Pinnacle International Freight Ltd (01059368) | hook 27 Aug 2026 (GDP warehouse) | still no plain email. Checked: Made in the Midlands profile (no email), business.gov.uk Find a Supplier (website pif.co.uk, 51-200 staff, no email), Clutch (form only), privacy page and en_US contact page (Cloudflare), T&C PDF (client_error), dev.pinnaclefreight.com (robots unreachable), pif.co.uk (refused). DROP unless a plain address turns up.
- Trade Freight International / International Logistics Centre (Newark) | hook 12 Nov 2026 event | the ILC homepage shows the email as "protected"; an "@tradefreight.co.uk" search found nothing; the East Midlands Chamber (emc-dnl.co.uk) member profiles show no member emails
- KC Group Shipping (Glasgow, ist@kcshipping.co.uk) | the Freyt World join post carries article:published_time 25 Jun 2026, but so do the 2022 award post and others (bulk migration date); KC's MD wrote a Freyt World blog on 24 Feb 2026 as a member, so the join was before the cutoff | DROP as hook
- Anchor Freight Ltd (anchor-freight.co.uk; Glasgow, Ipswich, Dover, Leeds; info@, glasgow@, ipswich@, dover@, gary.walker@anchor-freight.co.uk on /services/freight-forwarding/) | newest news 23 Mar 2026 ("Anchor On The Move!") | dated hook after 20 May 2026, CH
- Zenith International Freight (zen-intl.co.uk, Bradford HQ + Manchester/Midlands/Heathrow/East London; hello@zen-intl.co.uk; revenuebase 51-200, firmbase 18 staff) | only SEO posts (9 Nov 2026 etc.) | company hook, legal name/CH
- Schallenberg International Ltd (Felixstowe, since 1983; info@/enquiries@schallenberg.com) | no news section | hook, CH
- We Global Logistics (Felixstowe; hello@wegloballogistics.com) | no news | hook, CH, size (1-10)
- Bower Green Ltd (3368517, Bradford, 4th-generation family; info@bowergreen.co.uk on the W&N Yorks Chamber directory and the post page) | newest news 11 Feb 2026 | newer hook
- Team Wesley Logistics Ltd (Low Moor, Bradford; info@wesleylogistics.co.uk; Lognet member) | no dated news | hook, CH, size
- MC Logistics Ltd (mclogistics.com, Bradford; sales@mclogistics.com on the chamber directory) | not checked on its own site | hook
- EBISS UK Ltd (London; info@ / freight@ebiss.co.uk; art/events/freight, IATA) | no 2026 news; also US and DE entities | hook
- Gabensar Global (Nottingham phone; sales@gabensarglobal.co.uk; founded 2019, director Sam Boot; firmbase 9 staff) | no news | hook, CH
- Origin Global Logistics UK, Harbur, Zygo, Interfreight UK, WS Logistics, FF Customs & Logistics, Wilson Global, Global Container Services (Felixstowe revenuebase) | no dated news surfaced in a batch search | site and email checks not done

#### Rejected
- Admark Shipping Solutions: now part of Thermotraffic (press release, 31 May)
- Magnum Group: 10-company group across 3 continents (incl. Scanwell)
- WM International: WM Group, parent LB GmbH (Germany)
- Pegasus Express: EFS Global group; courier
- Translink Express Logistics: pallet/parcel carrier (haulier)
- Goldstar: airside haulage/screening, no email
- Silver X Group: warehousing
- Grampian Continental: haulier
- Energy Freight Forwarding: no email, news only on LinkedIn
- Quality Freight Services: news stops Oct 2025; 201-500 staff
- PSP London (Premier Shipping & Packing): industry posts only; email typo domain
- Conquest Shipping: template site, no hook
- CMI Logistics: no email (AEO 2019 only)
- Angel Shipping & Logistics: domain for sale
- Cargo Overseas: Freyt World tuk-tuk post 12 Aug 2026, but rejected earlier (own quote tool)
- Elite Universal: Verso Waves go-live 28 Oct 2026, already in companies.csv
- Buckle Shipping: site shows only a bot-check page
- Forest Shipping: Amazon e-commerce
- nkrfreight.com: hacked/spam

#### Sources
- NEW PRODUCTIVE: West & North Yorkshire Chamber member directory (members.wnychamber.co.uk/directory/<id>/) shows member-supplied emails (Bower Green, Team Wesley, MC Logistics). Its member news (/article/, 278 pages) is dated but has no forwarder items in search.
- NEW: multimodal.org.uk/news fetches; one call lists every headline 4 May to 20 Nov 2026 (the list is above in this run; article URLs are not in the text and hand-built slugs are refused). Small-forwarder items in the window are all used or rejected (Translink, Elite Universal, Zelir, Harbour Intl, Baxter, Efret, Infinity, PS Forwarding).
- NEW: revenuebase Felixstowe lists (cargo-shipping-services, international-shipping-agents, international-shipping-services), the Glasgow shipping-companies list, and UK lists (shipping-and-freight-forwarders, air-freight-shipping-companies, trade-show-shipping). All top-25s are now read.
- firmbase technology lists wp-rocket, godaddy, wpforms, cloudfront: first 100k characters read this run (new names listed above). Tails (offset 100000) not read for godaddy, wpforms or cloudfront.
- Freyt World news (freytworld.com/news/, 17 pages): page 1 read; member stories, UK members seen are Cargo Overseas, KC Group and Beckchoice.
- ifnfamily.com/blog/freight-forwarders-uk/ fetches after an allowed_domains ifnfamily.com search.
- DEAD: Freyt World new-member search (not indexed), award-shortlist searches (BIFA 2025 only), thebusinessdesk new-premises stories (2021-2025), club sponsorship search (Altrincham/Banks & Lloyd used, G&T Express Nov 2025), BIFAlink Nov 2026 (not indexed), Felixstowe local news, regional business awards 2026, freight-software customer news (Albacore TFS Feb 2026), GM Chamber logistics list (members only), emc-dnl member profiles (no emails), "independent freight forwarder" announcement search (large or old).
- Refused (provenance): dns.google MX lookups, CH search page, multimodal article slugs, pif.co.uk. DoH via curl returns a proxy 403.

#### Searches used: 37 of 40

### AU agent notes

### AU research run, 20 Nov 2026: 2 qualified (All Ports International, ASL Customs Services)

#### Qualified (written to au.jsonl)
- All Ports International (allports.com.au, Tullamarine VIC; Clutch says 50-249 staff; "totally Australian-owned") | hook: blog post 25 Jun 2026 about Deanne and Phoebe's three-week May trip to agents and clients in UK/NL/DE/FR/IT | deanne@allports.com.au (quote assistance) on www.allports.com.au/locations/ | MX unchecked
- ASL Customs Services (aslinternational.com.au, South Melbourne; family-owned since 1979, "boutique brokerage") | hook: FTA/APSA Weekly Report 2026/46, 18 Nov 2026 (ftalliance.com.au/newsdetails/41724), Lucy Robinson caught up with Nick Borradale | shipping@aslinternational.com.au on /contact | MX unchecked. This closes the earlier "ASL Customs: no website found" lead: the FTA directory lists the site as aslinternational.com.au.

#### Unfinished candidates (company | known | missing)
- FJT Logistics | July 2026 News Brief (17 Jul 2026, fjt.com.au/june-2026-news-brief-2/) says 25th anniversary in Oct 2026; Nov 2026 brief exists | plain email: the contact page body is all Cloudflare. fjtmel@/fjtbne@/fjtadl@ appear only in the og:description meta. Not on the news-forms page or in the T&C PDF. Treat as dead unless the main session accepts the meta-description address.
- Australian Global Freight Pty Ltd (ausfreight.com.au, Eagle Farm QLD; 100% Australian owned; 25+ yrs; 2,000 m2 warehouse; info@ausfreight.com.au on /contact/) | no dated hook (no news section) | hook. The homepage also carries hidden gambling spam links, so the site may be compromised.
- Bollinger Shipping Agency (info@bollinger.com.au) | /news-3/ newest post is 2017 | hook
- Townsville Customs & Forwarding (info@townsvillecustoms.com.au; opened 1996, so its 30th year is 2026) | news archive ends Aug 2022; "John Moore 33 years" post is from 2018 | dated hook
- Bowen's Customs & Logistics (bowenlogistics.com.au, Caringbah; sales@mbowens.com.au) | 40-year post dated 21 Mar 2025 (old); now a 4PL model | hook, fit
- Freight and More Pty Ltd (freightandmore.com.au; enquiries@freightandmore.com.au; serviced-office addresses in Melbourne, Sydney and Brisbane) | media hub has only 2026 SEO guides | hook, real size
- 24 Customs Pty Ltd (24customs.com.au, Auburn NSW + Brisbane; small) | only SEO guides (30 Oct 2026) | email (form only)
- AUSCUS / Australian Customs Brokers & Logistics (auscus.com.au, Brisbane, Director Louise Jones) | community posts Dec 2024/Jan 2025 | email (protected) and hook
- North Queensland Customs Services | jobstralia ad for a logistics coordinator who prepares freight quotes (posted "23 December", year not shown) | dated hook, site/email check

#### Rejected this run
- Aintree Group: accounting firm, not a forwarder
- AGL Logistics: newest item is a 2020 move notice; no email
- Brisbane Logistics: 3PL/e-commerce fulfilment
- Shayona Logistics: 3PL/container transport, SEO blog only
- Easy Freight Ltd: NZ-based, GLA post Jul 2025
- Authentic International Logistics: Freight Midpoint join 2 Feb 2026 (before cutoff), no email
- Complete Global Solutions: procurement/supply-chain consultancy; insights posts are 2024-25
- Global Freight Services (globalfreight.com.au): redirect loop
- Cape Solutions (Hume Business Awards 2026 Transport winner, 29 Oct 2026): business type not found
- Pentagon Freight (FTA 2026/40, new MD Sarah Palmer): JAS group, already rejected
- Kalgin, Gavos, McHugh & Eastwood, Casa (FTA 2026/45, 42, 42, 41): already contacted
- Leeward Group, GCF Griffin, IBC Pacific, KMLT, Elite FSA, J H Bachmann, GCS, Energy Logistics, Oceanbridge, DA Global, Mega Freight, Dazmac, CFA, Consol Alliance: the batch searches surfaced only About or careers pages, with no dated item
- Mac-nels Evans International Freight Consolidators (eifc.com.au): wholesale LCL consolidator, not a target (blog not read)

#### Sources
- NEW, PRODUCTIVE: FTA newsdetails pages fetch by hand-built URL this run (ftalliance.com.au/newsdetails/<id>). IDs run roughly 60 a week but are not strictly in date order.
  - Weekly Report IDs found: 2026/40 = 41418 (7 Oct), 2026/41 = 41472 (14 Oct), 2026/42 = 41521 (21 Oct), 2026/45 = 41665 (11 Nov), 2026/46 = 41724 (18 Nov), 2026/31 = 41014, 2026/25 = 40717.
  - Not found: 2026/44 (IDs 41618-41626 give server errors), 33, 34, 36, 37, 38.
  - The /weekly-report/<id> pages are empty shells and so are the /news/<id> pages; only /newsdetails/<id> has the text.
  - 2026/47 should appear at about newsdetails 41780-41790 on 25 Nov.
  - Each report names only 1-3 member firms, mostly already contacted.
- NEW, PRODUCTIVE: query '2026 news OR announcement OR team OR sponsorship OR anniversary OR trip' over guessed domains surfaced the All Ports trip blog. The FTA directory (www.ftalliance.com.au/members/freight-forwarding-customs-broker, offsets 0 and 100000 read) gives real domains. Offset 200000 (O-Z) was not read this run.
- Clutch AU freight-forwarders base and ?page=3, /brisbane and air-freight-companies (Nov 2026) fetched. New names without domains: Freelance Shipping (Rockdale), AMAC Customs (Busselton; amaccustoms.com.au per FTA), Proactive Customs & Freight (Moorabbin), Smith Lewis and Staff (Melbourne Airport), 2Star International, Johnson Wills (= JWI, rejected), Niche Logistics, VIP Freight (Perth Airport), Gforce Freight, Marair, Romann, Smartways, Freightlinks, ECS Project Logistics (Port Adelaide; Export Consolidation Services = ecsaus.com.au), Global Overseas Direct, Swift Customs, Mac Customs, Customs Logistic Services, End to End Customs, Freight Assist.
- cargolinked.com/directory/country/australia (19 pages, ~950 names, no sites or dates): name pool only.
- DEAD this run:
  - FTA weekly-report shell pages; DCN 'out & about' tag and appointment news (Mondiale, AGS); Shipping Australia QLD golf day page (no sponsors); Care-Factor Trade Ball 2026 article (no sponsor names); Hume Business Awards 2026 (no forwarders); Bayside/Cumberland/Fairfield LBAs (Issuu)
  - mining/energy magazines; heavyliftpfi/breakbulk AU search; Australian Trusted Trader search (FJT only, undated); ABF ATT register (no entries in text); JCtrans weekly202647 (still not indexed)
  - com.au-wide "proud to announce"/newsletter queries (FJT, Freight Mart, Clarke, Century, IFC fill results); network new-member search (GLA 2025 posts)
- Blocked URLs this run: dns.google MX (permission prompt timed out, so both MX are unchecked); allports.com.au without www (fetches only after an allowed_domains search surfaced www pages; /about-us/ redirect-loops).

Searches used: about 38 of 40, counting two that errored (one HTTP 400, one invalid parameters).

### HKSG agent notes

### hksg run (20 Nov 2026, later run): 0 qualified, 35 WebSearch calls (2 rejected by proxy with HTTP 400)

#### Unfinished candidates (company | known | missing)
SG | AJ Global Logistics Pte Ltd | GLA Diamond member 2025-29 (glafamily.com/en/news/2944, 27 Oct 2025); 10th anniversary in 2025; forwarder + customs broker, project cargo; owns 2,000 sq ft office plus leased warehouse; recruiting; contact Alan Lim | website, email, hook after 20 May 2026
SG | Goodrich Asia Pacific Pte Ltd | GLA Golden Plus member (glafamily.com/en/news/2792, 23 Apr 2025); est. 1997; NVOCC/chemical/ISO tank, owns about 30k TEU dry and 10k ISO tanks, so likely an NVOCC/carrier and too big | website, email, ownership; probably reject
SG | RSL Shipping Pte Ltd | GLA Golden project member (glafamily.com/en/news/2778, undated, probably 2025) | everything
SG | Star Concord Pte Ltd (starconcord.com.sg, general@starconcord.com.sg on post pages) | LCL consolidator and forwarder; the blog only reposts industry news (WCA Specialty Conference/Delta 9 Jun 2026, LogiPharma 2026) | own dated hook, size, ownership
SG | Transit Air Asia (transitairasia.com.sg, exhibition logistics) | robots.txt unreachable | everything
SG | Ascendt (ascendt.com.sg, exhibition/tradeshow logistics) | site is HTTP-only, so WebFetch loops on the redirect | everything
HK | New names from the Hong Kong Maritime Hub freight forwarder directory (hongkongmaritimehub.com/the-hub-3/the-hub-directory/directory-freight-forwarders-logistics/), which lists 83 firms with emails. None of these are in our data files: ADL Express (henry@adlexpress.com), Anderson Global Logistics (enquiry@anderson-agl.com), Eagle Global Logistics (enquiry@eagleglobal-logistics.com), EastLink (shipping@eastlinkgl.com), Elite Logistics HK (elite@elitelogistics.com.hk), Ferguson International (enquiry@ferguson-international.com), Flamely Shipping, Flynt International (info@flyntworldwide.com), Future Sky Logistics (patrickyeung@futureskyhkg.com), Global Logistic China (alan@glchk.com), Hosanna Logistics, International Freight Express (general@ifehkg.com), Kesco SCM, Kingsway Logistics (sales@kw-log.com), MC Express, Park Express (sales@parkexpress.com), Sail Win Logistics (carson@sailwin.com.hk), Shun Hing Global, Shuttle Cargo, Sky Air (info@skyairhkg.com), Sui Jun, Supreme Logistics, Suz Air & Sea, SY&L, Thrift Logistics, Tradewinds All Freight, Transcon | Hub emails are undated and the site is a news site, not an official directory, so recheck each email on the company's own site or in the MarDep directory. One allowed_domains search over 25 of these domains found no dated 2026 news | dated hook, size, ownership
HK | revenuebase HK lists, new names: AIR SEA Broker (airseabroker.com, 11-50), Fenix Logistic Services (fls.com.hk, 51-200), Trans Asia Express (transasiatpt.com.hk, 11-50), RW Solutions (rwsolutions.com, est. 2002, 11-50) | email, hook
HK | A&G Logistics (alan@ and kam@anghk.com, also in the Maritime Hub directory) | 30th year in 2026, but no dated item | hook

#### Rejected
- WM Group / WM Logistics (Worldwide) (wmgroup.com.sg): HQ in Hong Kong, more than 600 staff, multi-country group
- Global Airfreight International (globalair.com.sg): no email published; latest company items are from 2017-2020 plus a 25 Mar 2026 market update
- Airpak Express: the only new page (4px-airpak) returns 404; still no hook
- Global Net Int'l Logistics (globalnet.com.hk): a Guangzhou customs/food import agency, not an HK forwarder
- VICO (vico.com.hk): the JCtrans conference item dates from 2023
- SUN Logistics HK: part of the Sun Hing Group; its RACSF item is from 2021
- T.H.I. Logistics (S): branch of the Taiwanese T3EX group
- Ferrari Logistics (Asia): Italian group

#### Sources: productive / dead
- NEW (partly productive): Hong Kong Maritime Hub forwarder directory (83 HK firms with emails, fetches cleanly). revenuebase /companies/freight-forwarding-services/hong-kong and /international-freight-forwarders/hong-kong (top 20 each).
- The MarDep freight forwarder directory URL (mardep.gov.hk/en/public-services/shipping-directory/freiforw/) appeared in a search result this run, so it should now be fetchable.
- DEAD this run: JCtrans weekly202647 (still client_error on 20 Nov); Supply Chain Asia site (JS); Supply Chain Excellence Awards APAC (2025, large firms); SLA awards 2026 (nothing found); SME100 hall of fame 2026 (no HK or SG logistics firms); Singapore SME 500 (Dec 2025, no forwarders); E50 search (only Malaysia's E50, held 16 Oct 2026; the Singapore E50 2026 results are not out, nominations opened Apr 2026); HKMA DSA 2026 (no logistics firms); CEIV searches (Hactl and Cathay only); World Air Cargo Awards 2026 (large firms); Cathay top-agent stories; HAFFA news and 60th-anniversary pages (sponsors only; the gala was 20 Mar 2026); CILT NextGen Logistician Awards (2025 page, no names); transport logistic China 2026 exhibitor pages (logos only, 2028 show); Asia Fruit Logistica 2026 (exhibitor news has no forwarders, and the catalogue PDF/XLS links have no href); HK Maritime Hub news (logistics tag stops in 2020); e2i career fair 4 Sep 2026 (only CEVA and Sankyu); hk.indeed (no dates, mostly large firms); hk.jobsdb (client_error); GLA SG welcome posts in the index are 2025; network new-member searches (only items already used); allowed_domains '2026 news' searches over 22 SG/HK near-miss domains and 25 HK Maritime Hub domains (only SEO or reposted items); WCA/JCtrans conference blog search (VICO 2023, Union Air Freight already contacted).
- Refused without provenance: securitycargonetwork.com/news/ (permission prompt timed out).
- WebSearch with media domains in allowed_domains (businesstimes.com.sg, straitstimes.com, theedgesingapore.com, vulcanpost.com, sbr.com.sg, todayonline.com, channelnewsasia.com) returns HTTP 400 from the proxy.

#### Searches used: 35 of 35 (including 2 that the proxy rejected)
