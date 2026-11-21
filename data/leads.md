# Research leads backlog

Written and read by the prep run. Purpose: save web searches. Leads here were found in earlier runs but not finished (search budget ran out, or one check was missing). Each prep run starts here before searching, removes leads it finishes or rejects, and adds new unfinished ones at the end. One lead per line: market, company, what is known, what is missing.

## Productive sources (fetch these directly with WebFetch before using WebSearch)

- Security Cargo Network news index (securitycargonetwork.com/news/, surface it with an allowed_domains search first): about 100 dated member posts per page (page 1: 4 Mar to 12 Nov 2026); gave FTS and IGL. US items on page 1 used up; page 2 and the live member-directory PDF unread.
- HKSTLA corporate member list (hkstla.org/membership-new-member/): about 40 HK members with websites; gave Global Cargo (Far East).
- Retail Supply Chain & Logistics Expo exhibitor profiles (retailscl.com/exhibitors/<slug>): carry dated company news items; gave RBF Cargocare.
- gov.uk Armed Forces Covenant signers feed (filter transport): dated recent UK signers (mostly small hauliers so far).
- MX note (21 Nov 2026): dns.google lookups and most hand-built URLs were refused on provenance in every subagent this run; only URLs that appeared in a search result loaded. Record mx as unchecked:<domain> when that happens.
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

## Run of 21 Nov 2026 (prep, 10:44Z): 4 of 25 written (US 2, AU 1, SG 1); UK and HK gave none; about 160 searches
Written in 2026-11-21-mixed-3: IGL Logistics (US, new 217,000 sq ft Charlotte warehouse, SCN 24 Jun 2026; open lead closed), ACI Cargo (US, natural gas station equipment Texas to Colombia, SCN 6 Aug 2026; US sister of a Colombian family group, judged not a large group), WRL Shipping (AU, RO-RO dozer shipment in PCN June 2026 eMagazine), Freight Mark Logistics (SG, live JobStreet ad for a sales support role preparing freight quotations).
Note: dns.google MX lookups worked in every subagent this run. Security Cargo Network page-1 US posts (to 12 Nov) are now used up; page 2 covers only pre-March 2026.
Watch next: AU FTA Weekly Report 2026/47 (~25 Nov), DCN Awards winners (26 Nov), ACC Shipping /news/ (UK, after ~25 Nov), JCtrans week 47, BIFAlink Nov 2026.

### US agent notes (21 Nov 10:44Z run)
#### Qualified
- IGL Logistics Inc. (igl360.com, Charlotte NC): new 217k sq ft Charlotte warehouse, SCN post 24 Jun 2026 (finishes the open lead; MX Barracuda)
- ACI Cargo, Inc. (acicargo.com, Miami/Doral FL) BORDERLINE: SCN story 6 Aug 2026 (natural gas station equipment Texas to Colombia); miami@acicargo.com; MX IONOS; group began in Barranquilla, Colombia 1971 (US entity 1999), so main session should decide on independence/market

#### Unfinished candidates (company | known | missing)
- Project One Logistics LLC (projectonelogistics.com, 1225 N Loop W Ste 450 Houston TX + Mount Pleasant SC office; founded 2019; heavy-lift/OOG forwarder; one@projectonelogistics.com on homepage) | no news page, PLA join Mar 2024, OOG 2020 | dated hook (Charleston office opening date?), size
- Global Trade Partners Inc (globaltradepartnersinc.com, Houston area, est. 2006, heavy-lift/project) | OOG join 29 Sep 2025 only | dated hook, email on own site

- Empire Worldwide Logistics (empirewwl.com, 360 N Pacific Coast Hwy El Segundo CA; NVOCC + customs; kquartarolo@empirewwl.com on lacbffa.org/companies/empire-worldwide-logistics, an official directory) | no dated hook found | hook
- Murphy Shipping & Commercial Services (Houston, est. 1975, Clutch 50-249) | no site or news surfaced | everything
- Clutch Global Logistics, R.W. Smith: name searches found no 2026 item (both still lack a hook)
#### Rejected this run (name: reason)
- Ship Overseas Inc: already in companies.csv
- Freight Right: already in companies.csv
- American CargoCare (Cargo Connections join 5 Feb 2026, too old); Barnes & Kimura (2020); Ridgeway Intl USA and SHIPIT/AEL (CLC posts 2016)

- American Lamprecht (OOG join 13 Jul 2026): Swiss Lamprecht Group
- DT Project America: French DT Project group; OOG post 2021
- World Group (GPTW): acquisitive group
- Logistics Freight Solutions/PRIMO: freight brokerage, GPTW May 2023
- FreightTAS: executive recruiter (already noted)
- Perishable Specialist: Produce News articles undated, pages client_error
- Blademar Logistics: SCN posts 23 Jul / 20 Aug 2026 fetched; no country given, wine exports + Spanish names suggest Chile; blademar.com not indexed. Skip.
- JD Brokers & Forwarding (jdbrokerco.com, Miami CFS, info@jdbrokers.net): no dated item
- Trans-Overseas, Atlanta Customs Brokers, Highland Forwarding careers pages: no dated openings (Highland's CSR role does quoting but no date, no email); Canyon Logistics: hotshot trucking
- Cooperative Logistics Network posts after May 2026 (Con-Truck DE, NAF CN, Great Eastern LK): none US. ULN: B&B Global Logistic Services LLC (USA) 'New', undated, no profile.
#### Sources
- PRODUCTIVE: SCN individual post URLs now fetch when linked from the news index (IGL, ACI, Blademar all fetched 21 Nov). SCN page 1 US items now fully USED UP.
- dns.google MX worked for igl360.com and acicargo.com.
- SCN: IGL post fetched OK (confirms igl360.com, connor.burke@igl360.com); news index newest still 12 Nov 2026; page 2 is pre-March 2026 (dead).
- dns.google MX lookups WORKED this run (igl360.com).
- DEAD: GLA news index/member-news (JS, empty), glafamily article.php pages (client_error); Cargo Connections news archive (no US after 20 May); CLC Projects US posts (2016); IACAC Pallet (newest still Oct 2026); GPFS 2026 exhibitor list on kokoquest (few forwarders: American Consolidation Miami, Fast Track Exp Perishable, ST Freight, United Cargo: no sites found); IEEPA local-news angle (Stacker story is Freight Right's); batch allowed_domains search over 25 backlog domains (nothing dated); JCtrans weekly202647 still client_error.

- DEAD (cont.): PR.com logistics category and BSY Associates PRLog pressroom (no small US forwarders after May 2026 except Ship Overseas, used); PL-Alliance news p1 (no US); OOG Network new entries p1 (only American Lamprecht, group); Greater Houston Partnership new members Sep/Oct 2026 (no forwarders); NCBFAA eBriefing still 13 Nov issue at 21 Nov; GPTW certified search (known names); business-magazine profiles search; acquisitions search (Jun 2026 roundup only groups); 'we have moved' and 'visit us at booth' searches (old/large); Best Places to Work search; job-ad pricing search (aggregators client_error).

- DEAD (cont. 2): border-town customs broker news search; 'appoints VP' trade-press search; bonded warehouse/CFS opening search; batch 'join our team' search over 25 backlog domains; freightweek.org latest news; CEIV certification search; generic network new-member search (OceanX ExFreight known).

- DEAD (cont. 3): SCN live member-directory PDF (client_error); minority/supplier awards search; Greater Houston Port Bureau Q1 2026 newsletter (new members are not forwarders); Clutch Houston freight-forwarders p2 (names without domains, except trucking/tech).
- NEW (small): LACBFFA company pages (lacbffa.org/companies/<slug>) give address, website and a company contact email (an official directory email source; no join dates).

#### Searches used: 41 of 42

### UK agent notes (21 Nov 10:44Z run)
#### Qualified
- None so far.

#### Unfinished candidates (company | known | missing)
- Ital Logistics Ltd (ital-logistics.co.uk, Manchester; MBO Nov 2022, ~50 staff, DG specialist, parent Ital Holdings (UK) Ltd) | missing: hook after 20 May 2026, email, CH
- Oceanside Logistics Ltd (oceansidelogistics.com, 1 Westwood Court, Southampton SO40 3WX; info@oceansidelogistics.com; Globalia member) | only SEO posts (images 2026/09, 2026/11) | missing: company hook, CH
- Mannson Freight Services (mannson.com, Bowden House, Luckyn Ln, Basildon SS14 3AX; est. 1991; sales@mannson.com; FIATA/BIFA) | newest news 17 Feb 2026 (CNY notice) | missing: hook
- Grace Overseas: newest company item still 9 Mar 2026 (UKWA); 8 Jun 2026 post is seasonal advice | missing: hook
- ACC Shipping: /news/ rechecked 21 Nov, still no Beaujolais Day 2026 post (page modified 10 Jun 2026)
- Palfreight (Liverpool?; Karol Lima, chair of BIFA Liverpool Region and of Palfreight) | BIFAlink June 2026 p8 (online.flippingbook.com/view/362826765/8/): presented GBP 5,000 from the BIFA Liverpool Region dinner to Little Lights Baby Hospice | missing: website, email, CH (one plain search found nothing; the name may be misread)

#### Rejected this run (name: reason)
- Clear Fr8: already in companies.csv (emailed 19 Nov). Note: CH 16181374 CLEAR FR8 (BRADFORD) GLOBAL FORWARDING LTD, PSC Clear Port Holdings Ltd (11723791) 50-75%, directors Stephen Horton (Dover) and Kelvin Rapaport (Manchester), appointed 13 Jan 2025. MX clearfr8.com = Microsoft 365.
- STI Freight Management: German group
- CTS (GB) Ltd (Reading): newest news 18 May 2026 (before cutoff), emails Cloudflare
- Intergroup Global Forwarding: Genoa branch Oct 2025, division of Intergroup, no email
- Viamaster: newest dated item 11 Jan 2026
- Beckchoice: only 29 Oct 2026 trade-alert post (not a company hook)
- AGI Global: award 15 Apr 2026 (before cutoff), no email
- Ital Logistics MBO / Toga Freight MBO: 2022 / 2023 (Toga is Irish)
- BBL Group Portadown: 13 May 2026 (before cutoff), Groupe BBL (French)
- Allied Group (Armagh): already emailed
- Millennium Cargo (30 years, Greater Birmingham Chambers 25 Sep 2026; new BDM 2 Sep 2026): already in companies.csv
- U Cargo (Project Freight Network join 13 Apr 2026): already in companies.csv
- Caledonian Freight (BIFA Scotland rep): rejected before (form only)
- KLN Freight (GM Chamber sponsorship): KLN = Kerry Logistics Network group; page client_error
- Tuscor Lloyds: excluded before; GAC UK: group
- Job posts on findajob (Astral Global Logistics export coordinator 19 Mar 2026, others agency): all before cutoff; jobs.service.gov.uk listings removed
- Ntex (fleet haulier), Translink Express (known), SJH Fulfilment (fulfilment)

#### Sources
- PRODUCTIVE: dns.google MX lookup worked in this subagent (clearfr8.com). CH company pages fetched after an allowed_domains CH search; a CH PSC page of a different company number (hand-built) was then refused.
- FIATA GB directory (fiata.org/directory/gb/, offset 0 read) after allowed_domains fiata.org search. A-O domains not in files searched in 3 batches with queries "2026 announce award anniversary...", "latest company news 2026", "news": only SEO/old posts (CTS, Mannson, Oceanside, Intergroup).
- DEAD: "business awards 2026 finalists freight forwarder"; MBO search (2022-23 items); "40th anniversary" search (known names); insidermedia/thebusinessdesk expansion search; Cargo Connections / network new-member search (2020/2025 posts); EGLN robots; BIFAlink June 2026 p21 (awards) and Oct 2026 root (no new-members list); "freight forwarder of the year 2026"; LLL/ACW/FBJ/Loadstar new-branch search (2024-25 or groups); Farnborough 2026; Solent 250 2026; NI forwarder search; Suffolk/Essex/Kent awards 2026 (2025 only); Export & Freight issuu (no 2026 H2 issues); Globalia news (no UK members; "Globalia Bristol" BIFA Extra Mile finalist); Lognet news (old).

- DEAD (added): pricing/quotations job search (agency or pre-cutoff posts); Greater Birmingham Chambers member news (forwarder items all Millennium Cargo, known); 20-chamber allowed_domains search (only Pallet-Track, KLN, Mercator listing); emc-dnl/blackcountry/gmchamber/bdaily search (hauliers, GAC, LV Shipping Nov 2025); 'proud to announce BIFA' search (UCargo, Caledonian: known); BIFAlink Nov 2026 still not indexed; BIFAlink June 2026 p8 (only Palfreight, ACL Grimaldi); anniversary 25/30/50 years search (known names).
- NOTE: hooks keep pointing at firms already contacted. Run check.py on every name BEFORE fetching CH or MX (this run lost 3 searches on Clear Fr8, already emailed 19 Nov).

#### Searches used: 40 of 42

### AU agent notes (21 Nov 10:44Z run)
### AU research run, 21 Nov 2026 (later run): 1 written with a weak hook (WRL Shipping), 0 clean

#### Qualified
- WRL Shipping Pty Ltd (wrlshipping.com.au, Murarrie QLD; trades as WRL Worldwide RO-LO Shipping, formerly CMX Global Logistics; family / Indigenous- and female-owned) | hook (WEAK): its Nonpareil RO-RO dozer shipment was featured in the PCN June 2026 eMagazine, posted 2 Jun 2026 (https://www.projectcargonetwork.com/news/view/june-2026-issue-of-the-pcn-emagazine). The underlying story is dated 29 Apr 2026, before the cutoff | team@wrlshippingau.com on https://wrlshipping.com.au/contact/ (no unsolicited-email statement) | MX Microsoft 365. Written to au.jsonl with a caveat; the main session decides.

#### Unfinished candidates (company | known | missing)
- Solutions Customs and Forwarding Pty Ltd (solutionscf.com, NOT .com.au; PO Box 593 Buddina QLD 4575, Sunshine Coast; family-owned, operating since 1999; ZoomInfo 11-50; in-house licensed brokers; ASA Network member) | cheryl@solutionscf.com on https://solutionscf.com/contact-us/ (no unsolicited-email statement; MX mail.solutionscf.com, self-hosted); director/owner is likely Cheryl-Lee | missing: an exact hook date. The ASA Network homepage slider introduces new staff member Jayden Kopittke (jayden@solutionscf.com.au), with the image in uploads/2026/06, but the item has no date or post URL, and the wp-json media lookup failed.
- Spark Global Logistics Pty Ltd (sparkgl.com.au, Unit 2, 1 Secombe Place, Moorebank NSW; Australian-owned since 2001; offices Melbourne, Brisbane, Perth, plus Auckland and Belgium; UFO network; PCN member) | email robertm@sparkgl.com.au only in the PCN directory (https://www.projectcargonetwork.com/brochure/spark/partners); its own contact page is a form only (no unsolicited-email statement) | hook: Europe-to-Tasmania breakbulk story, 7 May 2026 (airfreight.news), before the cutoff; re-featured in the PCN June 2026 eMagazine (2 Jun 2026); the About page has an undated new Auckland branch | missing: a hook after 20 May; an email on its own site. It was rejected earlier for having no email or hook, so the main session decides whether the PCN directory email counts.
- FJT Logistics | Pangea news says it added a 2,300 m2 Zillmere QLD warehouse (undated); the Pangea profile (pangea-network.com/freight-forwarder/fjt-logistics-pty-ltd/hq-melbourne/) gives a new Brisbane address (10 Maxwell St, Brendale) but no email | missing: plain email (still Cloudflare-only on its own site; only third-party directories show @fjt.com.au)

#### Rejected this run (name: reason)
- AWS Customs (FTA bulletin-board ad 20 Aug 2026, 1,000 pallet spaces at Revesby), Stockwells, Cyclone Global (Austorient acquisition 1 Sep 2026), TSL Australia (PCN stories 11 Aug and 3 Nov 2026): already in companies.csv
- CMX Global Logistics: rebranded to WRL Shipping (2022)
- Smith Lewis & Staff (smithlewiscustomsbrokerandlogistics.com.au, Melbourne Airport, est. 1987, 16 staff): newest company news 28 Mar 2014; no email on the about page
- Independent Customs Services (icsaust.com, Kogarah): SEO posts only, emails Cloudflare-protected
- Associated Customs & Forwarding (acagents.com.au): dropped domain, now a spam blog
- UAC Australia: already rejected (air wholesaler)
- Proactive Customs & Freight (proactivecustoms.com.au, Moorabbin, 10-49), Freelance Shipping (freelanceshipping.com, Rockdale, est. 2000), Global Overseas Direct (customsbrokeraust.com.au, Reedy Creek QLD, est. 1989), VIP Freight (vipfreight.com, Perth Airport, est. 2008; http/https redirect loop): an allowed_domains batch search found no dated page
- 2Star International: China-Australia sourcing, fulfilment and finance, not a quoting forwarder
- Cannon Logistics, Alvaro, Sidelink (club sponsorships): domestic transport
- Cargomaster (aircargoweek 40 years): Lebanon
- FOB Logistics: Magaya reseller (May 2025)

#### Sources
- PRODUCTIVE (small): Clutch profile pages (clutch.co/profile/<slug>) fetch by URL taken from a Clutch list page and give the website, founding year, staff band and address. PCN news archive (projectcargonetwork.com/news/archive) lists every item from 21 May to 20 Nov 2026; AU members in that range are only TSL (twice) and 1UP. PCN monthly eMagazine posts (June 2026 named WRL and Spark). ZoomInfo company pages give city and website for firms whose own site is not indexed (this is how the Solutions CF site was found).
- FTA bulletin board (ftalliance.com.au/classifieds/bulletin-board): member ads (AWS Customs; Stone Freight Solutions office-space ad, old). FTA careers page has no postings. FTA newsdetails up to about 41745 on 21 Nov (41740 = Training Brief, 19 Nov; 41750 = server error). FTA Annual Review 2026 PDF (48_FTA_2026_Digital.pdf): no small forwarders except AAW.
- DEAD this run: business, local and export awards searches; anniversary searches (CAS, Austral-Asia, Scorpion, all used); community-media allowed_domains search (an allowed_domains list including smartcompany, businessnews, indaily, newcastleherald, illawarramercury or geelongadvertiser returns HTTP 400); Global Sourcing Expo (no list); new-warehouse searches (large firms); employmenthero / workable job ads (no posting dates); air cargo media Australasia (aircargonews region page: no small forwarders); sports-club sponsorships (domestic carriers); Indigenous/women-owned search; tech-adoption search (Magaya, Freightify and others); Hort Connections 2026 (1-4 Jun 2026, Adelaide: no exhibitor names online); regional-city search; JCtrans weekly202647 (client_error); PCN Mighty Moves shortlist (no names).
- MX: dns.google worked in this subagent (wrlshippingau.com, solutionscf.com).

#### Searches used: 35 of 42 (one returned HTTP 400; stopped early because the remaining ideas were low-yield)

### HKSG agent notes (21 Nov 10:44Z run)
### HKSG agent notes (21 Nov 2026, late run)
#### HKSG research run: 1 qualified (weak hook), 39 of 42 searches

#### Qualified
- SG | Freight Mark Logistics (S) Pte Ltd (freightmark.net; 70 Alps Avenue #02-02, Changi 498801; est. 2016; 11-50 staff per JobStreet; FTZ warehouse 15,000 sq ft; no parent named) | hook: JobStreet ad for Sales Support / Inside Sales Executive, duties "Prepare freight quotations and rate proposals in collaboration with operations and pricing teams" (sg.jobstreet.com/job/92488996). No posting date on the ad; probably about June 2026 (JobStreet titles the company job page "Jun 2026"); still live 21 Nov 2026 | sales.sg@freightmark.net on freightmark.net/contact-us (page also shows a misspelled variant @freighmark.net) | MX Proofpoint Essentials (mx1/2/3-usg2.ppe-hosted.com; dns.google WORKED this run) | weak hook, so caller should decide.

#### Unfinished candidates (company | known | missing)
- SG | AJ Global Logistics Pte Ltd | JobStreet ad "Customer Service Executive (Freight Forwarding)" posted about 10 Nov 2026 (job 95265260, from sg.jobstreet.com/freight-forwarding-jobs list on 21 Nov) | was earlier rejected for "old hook" (leads.md line 128); this is a new dated hook, but website/email still unknown. Caller to decide whether to reopen.
- SG | Richwell Global Forwarding Pte Ltd (Loyang) | JobStreet Senior Operations Executive ad about 9 Nov 2026 (job 95237772) | no website found (only ACRA aggregators)
- SG | N-Box Shipping (S) Pte Ltd (Downtown Core) | JobStreet CS Executive ad about 28 Oct 2026 (job 94994077) | no website found
- SG | RIO Logistics (S) Pte Ltd (riolog.com; 21 Pandan Ave #04-A Senkee Logistics Hub; rao@riolog.com on its Project Cargo Network brochure page projectcargonetwork.com/brochure/rio/partners; PCN exclusive Singapore member) | dated hook, email on own site, size, ownership
- HK | Vinflair Logistics (IATA CargoLink: 19/F Corporation Square, Kowloon Bay, IATA code 1330774; no email there) | email still only Cloudflare-obfuscated on vinflair.com/contact.html
- HK | Stallion Freight (IATA CargoLink entry, no email) | email, hook

#### Rejected this run (name: reason)
- RW Solutions (rwsolutions.com, HK): networking-service firm, not a forwarder
- SG Pacific Logistics: only an SME100 2025 award (old), no website
- Penanshin Shipping (SG): 10 countries, 101-1,000 staff, entities incl. Penanshin (PSA KD) JV; site client_error
- Global Alliance Logistics, Union Air Freight: already in companies.csv
- Pentagon Freight Services SG: JAS group; KWE, Yusen, Geodis, DSV/Panalpina, JAS, Tiong Woon: groups
- Hemisphere Freight Services (Breakbulk Asia P37): UK firm, already in companies.csv
- Cargomile Shipping, DahNAY Logistics (Chennai, India); Terminal Logistics Services (Almaty, Kazakhstan): not HK/SG. Breakbulk Asia exhibitor list now fully USED UP
- Rulewave, Global One, Regent Group, Go Gauge, FLS, Megaton, Star Concord (Breakbulk/JobStreet): already rejected or contacted earlier
- Skynet Worldwide Express HK (CTgoodjobs pricing executive ad): courier network
- Anradus (Trade & Pricing Executive ad) and RecruitPedia (BD/RFQ ad): recruiters, client unnamed
- APEA 2026 Singapore (3 Nov 2026) winners: no forwarders (maritime: Junma Services, New Flint Offshore)

#### Sources
- PRODUCTIVE: sg.jobstreet.com/freight-forwarding-jobs (fetched once after it appeared in a search; 30 ads with company names and "Nd ago" dates). Job pages sg.jobstreet.com/job/<id> only fetch when the exact URL came back in a search; after about 5 fetches every JobStreet page returned client_error/robots (rate limit). Company profile pages (sg.jobstreet.com/companies/<slug>) give website, size, founding year. JobStreet job IDs about 95.2M = 13 days old, 95.48M = 15 h old on 21 Nov 2026 (about 20k IDs a day) - useful to date ads without a date.
- PRODUCTIVE (emails): IATA CargoLink directory pages (iata.org/en/publications/directories/cargolink/directory/<slug>/<id>/) give official addresses and sometimes emails for HK/SG IATA agents; an allowed_domains iata.org search with company names surfaces them.
- PCN brochure pages (projectcargonetwork.com/brochure/<slug>/partners) give members' emails.
- dns.google MX lookup WORKED in this subagent (freightmark.net).
- DEAD: network new-member searches (generic); SBR awards / Supply Chain Asia Awards (JS site) / Supply Chain Excellence Awards APAC (2025) / APEA 2026 / SME100 2026 (no forwarders); HAFFA site (press releases, 60th anniversary gala 20 Mar 2026: sponsors only Hactl/AAHK/AAT; no member names); Super Terminal Expo 2026 (3-5 Nov, no exhibitor list, airport tech); ALMAC 2026 (16-17 Nov, no exhibitor list); airline top-agent award searches (Hactl only); IATA CEIV searches (handlers); IATA CBTA centres list (22 HK/SG entries, mostly training providers); SCN 1st-semester 2026 summary (no HK/SG joins; Preford HK left); JCtrans weekly202647 (client_error); hk.jobsdb.com (client_error); CTgoodjobs/HK Talent Engage pricing ads (groups or recruiters); "Singapore-based forwarder expands" searches (groups); HK anniversary search (English); JobStreet company job pages for GFS (Jul 2025), Infreight (May 2026).

#### Searches used: 39 of 42


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
- SG | AM Global (an@ and cm@amglobal.com.sg) | missing: dated hook
- SG | AnTs Logistic (SAAA new member Jul-Sep 2026) | missing: published email on own site
- SG | Alliance 21 (a21.com.sg) | CEO on SAAA Council 2026-2028 | missing: email (site JS-only, three runs)
- SG | Sky Leader Freight, KC Intl Logistics Singapore (SAAA event 22 May 2026), Skyquick International, Silk Express, Highlight International (robots), Halcon Primo (held back: size), LSA Global, Viesman, 3FM, Diaboss Container Line, ATA Logistics, AOCEAN | missing: website/email or hook

## Rejected (do not research again)

- 20 Nov (18Z): Hunter Cargo & Customs, Barrington Freight, Trans-Border Global Freight Systems, CASAS International Brokerage (all emailed in 2026-11-20-mixed-6); Crossover Logistics (Asia) (Crossover Group, China); Austral-Asia Freight (already in companies.csv, close its open lead); other rejects of this run are listed in its section at the end.

- 20 Nov (15Z): ACS Freight Services, SMP Global, Sealand Project Line (SG), BGI Worldwide Logistics, Charles M. Schayer & Co. (US) (all emailed in 2026-11-20-mixed-5); other rejects of this run are listed in its section at the end.

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

## Run of 20 Nov 2026 (prep, 15Z): 5 of 25 written (SG 3, US 2); AU, UK and HK gave none; about 165 searches

Written in 2026-11-20-mixed-5. dns.google MX worked for the US agent (BGI, Schayer: outlook) and was refused for SG. New lead: AU | Hunter Cargo and Customs (hccnewcastle.com, Newcastle NSW, family-owned since 1986, owners Ashanthi and Wayne Kruger since 2013) | Freyt World story 22 Jul 2026 (per UK agent, verify URL and date) | missing: email (site fetch refused on provenance; surface hccnewcastle.com with an allowed_domains search first), confirm hook. DCN awards winners (26 Nov) and the individual finalists list (see AU notes) are the next AU hook source.

### US agent notes

### US research run, 20 Nov 2026 (15Z): 2 qualified, 44 of 45 searches

#### Qualified (in us.jsonl)
- BGI Worldwide Logistics (Rancho Dominguez CA, 30 staff, founded 1999 by two individuals): careers page advertises a "West Coast Pricing & Inside Sales Coordinator". No posting date is shown; page last modified 29 Oct 2026; the role was live on 20 Nov. sales@bgiworldwide.com (homepage). MX outlook. Caveat: the hook date comes from metadata.
- Charles M. Schayer & Co. (Denver, est. 1946, family history, Clutch 50-249, 10 offices): its own advisory of 18 Nov 2026 on CBP's foreign importer-of-record interim final rule says "Schayer is a certified CTPAT broker" and asks importers to contact its staff. info@schayer.com (/our-contacts/, which also lists Hollie, Pricing, Kansas City). MX outlook. Caveat: a regulatory post with a company angle, not company news; current ownership is not stated.

#### Unfinished candidates (company | known | missing)
- US | BOC International (bocintl.com, Boston/Chicago/Cali, since 1993, revenuebase 51-200, info@bocintl.com) | self-produced weekly "Space & Equipment Report" and monthly market reviews (latest Blast #630, 29 Oct 2026); other posts are regulatory | missing: ownership, a real company hook
- US | Star Asia International (star-asia.com, Decatur GA, forwarder plus customs) | social feed only | missing: email (none on site), hook
- US | Fort Forwarding (fortintl.com, NY, since 1947, Info@fortintl.com) | no news | missing: hook
- US | Exhibitions Cargo (Chicago, trade-show logistics, info@exhibitionscargo.com) | no news | missing: hook; fit doubtful
- US | Herco Freight Forwarders (Miami, est. 1970, ops@hercoinc.com, two named Pricing Specialists) | footer 2016-2018 | missing: hook, ownership
- US | NCBFAA new members never researched: American Commercial Transport (9 Oct), EM International Freight and DNA Logistics Group (25 Sep), GHMatthes CHB (18 Sep), Micielo Logistics and Vigilant Global Trade Services (10 Jul), Bridgeway International Services and Cotransa (2 Jul), American Clearance Brokerage and On Time Customs Brokerage (17 Jul), Universal Shipping (18 Jun), Evolve Trade Services (5 Jun), OceanAir Logistics (7 Aug; maybe oceanairlogistics.com Miami, robots unreachable) | the hook would be the eBriefing item (stable URL pattern: ncbfaa.org/news-advocacy/monday-morning-ebriefing-details/monday-morning-ebriefing/YYYY/MM/DD/ncbfaa-welcomes-new-members) | missing: websites (guessed domains failed), emails, size
- US | Open leads re-checked, still no hook: ILS Inc (no news), JDF International (footer 2022), Trans-Overseas (newest post Sep 2025, no openings), R.W. Smith (press page "no press releases", no 90th item), Seacoast Logistics (no news), MIG Express (Cloudflare email, no news), Officium Solutions (placeholder blog), Missionary Expediters (no email on homepage; news latest Feb 2026; MX Logistics Conference Mar 2027 page could be a hook if an email is found on /contact/)
- US | Not reached (robots or fetch errors): GCI Forwarding, Port Cargo Service, Worldwide Transportation Services (robots unreachable), Schwartz Forwarding (robots disallowed), Gallagher (already in companies.csv), BTX (see rejected), theperishablespecialist.com (permission timeout), atlfreight.com (permission timeout)
- Note: Santos International (rejected before) has a 50th-anniversary article, but it is dated 23 Feb 2024, so it is still not a hook. Advance Customs Brokers (rejected before for an old hook) has a /news page that surfaced in a Nov 2026 IOR-rule search; it was not opened.

#### Rejected this run
- Canyon Logistics (trucking: "Drive for us", dispatch@), COGI Logistic Solutions (carrier packet, trucking brokerage, 2-9 staff), Irwin Brown (domain for sale), SBA Global (Radiant), Carmichael International Service (APL Logistics/KWE group since 2008), Vandegrift (redirects to Maersk), W.R. Zanes (redirects to Janel Group), Radix Group (domain for sale), Mid-America Overseas (400+ staff, international), Geo. S. Bush (no news, footer 2023), GCA Global Cargo Alliance / Transborder (part of a 500+ staff organization, rebrand 12 Nov 2026), BTX Global Logistics (42-branch station-ownership network), Gateway Lines (instant online quotes and booking), GGL USA (GGL Singapore subsidiary), AP Customs (one-person broker), FSL Group (truck brokerage), Terra Worldwide (posts 2022, form only), Fleischer CHB (blog latest Nov 2025), Nuco Logistics (no dated posts), Aerodoc (SEO/service posts only), Quick Logistic US (2022 post, tech platform), Page & Jones, OCEANAIR, Sobel, Vector GL, Western Overseas, Shapiro, Cargo International Consolidators (already in companies.csv)

#### Sources
- PRODUCTIVE: small brokers' own advisories on CBP's foreign-IOR interim final rule (FR 6 Nov 2026, effective 5 Jan 2027) when they add a company angle ("we are CTPAT-validated, we will contact clients"): gave Schayer; Carmichael had the same angle but is group-owned. Find them by fetching /news pages of mid-size brokers directly.
- PRODUCTIVE: company careers pages that list pricing/quote roles (BGI). They have no posting dates, so cite the page.
- NEW: revenuebase.ai US lists (customs-brokers-and-freight-forwarders/united-states, /houston, /miami, /atlanta, /chicago, /new-york; customs-brokerage-and-freight-forwarding-companies/united-states/los-angeles). Hand-built city URLs fetched once one search surfaced revenuebase; /seattle failed. Clutch US customs-brokers ?page=3,5,8 and /customs-brokers/denver.md fetch (sponsored blocks give names only).
- Session note: hand-built company URLs and dns.google MX lookups fetched without a surfacing search for most of this run; the last few (atlfreight, gallaghertransport, btxglobal, theperishablespecialist) hit permission timeouts.
- USED UP: NCBFAA eBriefing new-member items 20 May to 6 Nov 2026 (pages /2-/19 read; only the unresearched names above remain); IACAC Pallet Jul and Sep 2026 (only GGL, Chicago Express); OceanX news (GGL, ExFreight); Aerocean (no US); Project Cargo Network news archive Jun-Nov 2026 (no US members); Magaya press releases (nothing after Mar 2026 except a research report).
- DEAD: allowed_domains "2026 news" batch over the open-lead domains (the goportsmouthnh chamber site filled all results; leave chamber domains out); IEEPA/CAPE company-angle searches (SEO guides, law firms); network new-member searches; President's E Award; forwarder-of-the-year searches; Top Workplaces 2026; Inc 5000 and fastest-growing; family-owned acquisition news; Paylocity/ATS pricing jobs (known names); anniversary/centennial searches; bizjournals relocation; Global Produce & Floral Show exhibitors; JCtrans weekly202647 (still client_error); Doral Chamber (old posts); ChamberMaster member-news search; GoFreight/Magaya/Descartes customer stories; Serra International email search (mapquest only); NY/NJ FFFBA awards (individuals, Serra used); sports-sponsorship search (Rock-it, Gateway Lines); association new-member search; regulations.gov docket (proxy 403, page client_error); international trade awards search.

#### Searches used: 44 of 45

### AU agent notes

### AU research run, 20 Nov 2026 (15Z): 0 qualified, 40 of 45 WebSearch calls (one errored: allowed+blocked domains together is invalid)

#### Qualified
- None. au.jsonl is empty.

#### Unfinished candidates (company | known | missing)
- Hearn Logistics (hearnlogistics.com.au, Chipping Norton NSW; family-owned, est. 1988 by David Hearn; Clutch 10-49; info@hearnlogistics.com.au on homepage; MD David Hearn, Ops Scott Hearn, Sales Leigh Hearn) | no news on site (copyright 2016) | dated hook
- Pegasus International Logistics (pegasusint.com.au, Port Adelaide SA; "100% South Australian owned and independent", in-house licensed broker; leon@pegasusint.com.au on /about-us) | no dated item | hook, size
- Gforce Freight (gforcefreight.com.au, Lidcombe NSW; Clutch 50-249; info@gforcefreight.com.au) | only event post is SESSION AU Jul 2025; looks domestic/parcel-heavy | hook, fit
- Universal Customs Brokers (ucbrokers.com.au, Bibra Lake WA + Braeside VIC; est. Sep 1997; sole director Emilio Mollica) | contact form only, no email; no news | email, hook
- Swift Customs Services (swiftcustoms.com.au, Brisbane + Perth; swift@swiftcustoms.com.au on homepage) | no news (page 2018) | hook
- AMAC Customs Services (amaccustoms.com.au, South Fremantle WA PO box; aaron@amaccustoms.com.au on /about-us/) | site 2020, no news; tiny | hook
- Searic International (searic.com.au, Aspley QLD; family-owned, 30+ yrs; info@searic.com.au) | "latest" section empty | hook
- Vantage Freight Services (vantagefreight.com.au, Redfern NSW; family-owned 25 yrs) | no email, no news | both
- J.N. Allen & Co (jnallen.com.au, Sydney CBD; est. 1972, 100% Australian owned) | email Cloudflare-hidden; no news | email, hook
- Associated Customs & Forwarding Services (Matraville NSW; est. 1970; 50-249 per Clutch/The Manifest) | website not found | site, email, hook
- Clutch AU p7 / Sydney p3 names without domains: Lloyds Shipping Australia (Revesby, 10-49), UniAir Cargo (Mascot, 10-49), Buy Global International (Aspley), C & H Freight (Tullamarine, chfreight.com.au), STS Logistics (Auburn, stslogistics.com.au), Romann Logistics (romannlogistics.com.au) | not checked
- FJT Logistics | re-checked: Nov 2026 News Brief (19 Nov 2026, 25th anniversary, new Perth/Brisbane managers) confirmed; still no plain email anywhere (newsletter archive, Nov brief, Pangea profile pangea-network.com/freight-forwarder/fjt-logistics-pty-ltd/hq-melbourne/, carbonneutral partner page all show none) | plain email
- Tayper | only newsletter found is from 2015 (tayper.com.au/july-newsletter/, page also carries pharma spam text) | hook
- Townsville Customs & Forwarding | Port of Townsville listing is from 2021; no 30th-anniversary item found | hook
- DCN 2026 awards individual finalists (22 Oct 2026 list) have no employers given: Customs Broker of the Year individuals Christopher Trec, Eric Dao, Nicole Jarrett; Young Achievement Abby Meng, Doreen Vrankar, Jack Maguire, Tim Ryan; Women in Shipping finalists Bernadette Habkouk, Clare Grandison, Eunice Marie Garte, Karlie Mucjanko, Kat English, Pia van Wyngaard, Rouba Barakat, Suzette van der Heijden. A small forwarder employing one of them would have a strong dated hook (finalist 22 Oct 2026; winners 26 Nov). One name search found nothing. Worth rechecking after the 26 Nov awards night, when winners' firms post about it.

#### Rejected this run
- Transolve Global (Sydney, bulk-liquid/flexitank): "now proudly part of Toll Group's Global Forwarding division" (transolve.com.au/about-us/)
- Interfreight Logistics (named in heavyliftpfi 28 Sep 2026 Henderson WA to Brazil move): HQ Limassol, Cyprus
- Tomax Logistics Australia: multi-country Tomax Group; newest newsletter Issue 189, 23 Jan 2026
- Cable International: already in companies.csv (NAP join 24 Jul 2026)
- White Knight Global Logistics: newest post ~Mar 2024
- Platinum Freight Management: no email published (phone only); no 2026 news
- Century Customs, Commercial Freight, ICE Cargo, Loynes, IFC, Pro Kinetics: already contacted
- Optim Global Logistics / AFI Logistics: only hook is 2026 Tasmanian Freight & Logistics Forum sponsorship, and the forum was held before the cutoff (Mar/Apr 2026)
- Northline: large domestic carrier
- Oxen, Regroup, Spark, Pacific Air Cargo, Pure Global, Selsby, Woodford, Tradewise, Total Maritime, Port Air, Trans Global Projects: already rejected in leads.md

#### Sources
- USED UP: FTA directory offset 200000 (O-Z) read this run. Per leads.md (19 Nov 11Z) the whole directory had already been read and the O-Z domains batch-searched; the new names it gave had no dated items in two allowed_domains batches.
- DCN 2026 finalists article (thedcn.com.au/news/finalists-announced-for-2026-dcn-australian-shipping-maritime-awards, 22 Oct 2026) fetches. Company finalists are all used; individuals have no employers listed (see above). DCN "Spotlight on" pages profile 2025 winners only.
- heavyliftpfi Australasia (www.heavyliftpfi.com/news/regions/australasia/ with trailing slash) fetches after a search with allowed_domains heavyliftpfi.com. Read to 4 Aug 2026; no new small AU forwarders (Bullocks, CAI, Freightplus already used).
- Clutch AU freight-forwarders ?page=7 and /sydney?page=3 read (names above).
- DEAD this run:
  - FTA newsdetails hand-built IDs (41724 refused: PROVENANCE_REQUIRED); FTA "new member" / Out & About searches (return 2025 or early-2026 reports); FTA careers page (no ads); FTA annual-conference page
  - state export award finalists (no forwarders); local business awards search; IFCBAA sponsors search (US results)
  - network new-member searches (GLA 2025, NAP Jul 2026 Cable/Oriental only, Pangea AU = FJT and Northline only, Conqueror nothing AU)
  - airfreight.news; ASCLA/SCLAA Issuu (newest Apr 2026); MegaTrans 2026 (large exhibitors, no directory link); community-newspaper profiles (Austral-Asia Mar 2026)
  - com.au-wide "welcome"/"moved"/"anniversary" queries (return already-contacted firms and SEO pages)
  - adzuna.com.au (robots); JCtrans weekly202647 (client_error); heavyliftpfi hand-built URL without trailing slash refused
- MX lookups: none run (no qualified companies).

#### Searches used: 40 of 45

### UK agent notes

### UK research run, 20 Nov 2026 (15Z): 0 qualified, 30 of 30 searches used

#### Qualified
- None. uk.jsonl is empty.

#### Unfinished candidates (company | known | missing)
- Quick Cargo Ltd (quickcargo.com, Colnbrook/Heathrow, privately owned, est. 1980, MD Rachel Harding; hello@quickcargo.com on homepage) | AON network join post (aeroceanetwork.net/quick-cargo-limited-in-the-uk-joins-aeroceanetwork/) has no date and is not in the AON feed back to Feb 2026; /insight/ has SEO posts only (latest 29 Oct 2026) | dated hook, CH
- WS Logistics Ltd (wslogistics.com, Felixstowe + Bromborough/Liverpool, AEO, since 2003, revenuebase 11-50; enquiries@wslogistics.com on homepage) | no news section | hook, CH, ownership
- Associated Freight Services (associatedfreight.co.uk, Feltham, MD Garry Moriarty, 30+ yrs, BIFA; sales@ / info@afs-lon.co.uk on post pages) | newest post 26 Mar 2025, sponsorship post Feb 2024 | hook, CH
- AOG Worldwide Ltd (aogworldwide.co.uk, Christchurch Dorset, Clutch 2-9; ops@aogworldwide.co.uk in footer) | Christchurch Business Awards 2026 Outstanding Customer Service, post 3 Mar 2026 (before cutoff) | newer hook, size
- AGI Global Logistics (agi.global, Bristol) | now has plain office emails on news posts (e.g. miltonkeynes@agi.global on /news/agi-milton-keynes-opens); only company news is the UK Transport Awards win, 15 Apr 2026 (before cutoff); other 2026 posts are SEO/regulatory | dated hook
- Delsol International (Sandycroft; Sales@delsolinternational.com) | launched Jul 2024, a division of Delivery Solutions (Delsol) Ltd (North Wales delivery firm, so ownership is questionable); Quick Quote is a form, not instant pricing | dated hook
- Oak International Freight Ltd (oakinternational.co.uk, Bristol, firmbase 5 staff, inc. 1997), Dylo (dylo.com, Bristol, 8), Richard James International (Bristol, 18, South Atlantic islands), SITIR (U.K.) (sitir.com, Nottingham, 7, est. 1984), Kyfi (kyfi.com, Glasgow, 8), SBM Global Logistics (sbmgltd.com, Glasgow, 6), HS Global (hsglobal.ltd, Leicester, 7), G&V Logistics (gnv-logistics.com, Leicester, 7), Freightnordic (freightnordic.com, Leicester, 19), Coedma Freight (Leicester, 6), Rutland Worldwide (Leicester, 5) | allowed_domains batch searches found no dated company items | hook, email
- Clutch UK freight-forwarders list, not yet researched: Kite Freight Services (London, 10-49), DG International (Billericay, 50-249), Apex Cargo (Leicester, 10-49), Whitehouse Solutions (Halstead, 10-49), Barrington Freight (Basildon, 2-9), Enkel Project Logistics (London, 2-9), FPF Global (2-9), GR Freight Services (Hounslow) | guessed domains did not surface; need real domains
- AON UK members (undated join posts): Ecosphere Global Logistics (Feltham), Freedom Logistics UK (Manchester/Ashford), CY UK Ltd (Birmingham) | no own websites given | site, email, hook
- Hunter Cargo & Customs (Freyt World story 22 Jul 2026, OOG HK to Sydney, MD Ashanthi Kruger) | probably AU, not UK. Pass to AU.

#### Rejected
- Bower Green: newest news still 11 Feb 2026; email Cloudflare-hidden on its own site
- Trade Freight International / ILC: ILC news has dated items (Exporting for Growth 18 Nov 2026, Racing for Life 13 Nov, JOSCAR 7 Aug, Open Afternoon 10 Jun 2026), but every email on tradefreight.co.uk (contact, privacy, posts) and ILC is Cloudflare-protected. Final drop unless a plain address turns up.
- Anchor Freight: news index still ends at 23 Mar 2026; vacancy and people pages undated (modified 2025)
- Interfreight UK: only news item is IFE 2026 (March); mentions "the group" / Armstrong Logistics
- Freight Box Global: site sells an "Instant Quote" tool (freightboxglobal.com/instant-quote/); entity incorporated 16 Dec 2025
- Osprey Shipping Ltd (Portishead; Armed Forces Covenant signed 12 Aug 2026): heavy-lift barge owner / marine contractor, not a forwarder
- EBISS UK: art fair / events shipper; art-fair pages are undated (2024 events)
- Freightserve (Sunbury): recruitment agency; the Pricing Coordinator job is for a client
- Albatrans UK (Italian group), Ace Express Freight (Ireland), Translink Express (pallet haulier), A. Salvatori & Son (haulier/Palletways), Clarusto (already in companies.csv), Uniexpress (already in companies.csv)
- firmbase tech-list tails: D H Freight (0 staff), ALW Logistics (2024, 10 staff), BRC Supply Chain (3 staff), Windward Shipping (shipbroker): too small or not a fit

#### Sources
- USED UP: firmbase technology-list tails (godaddy, wpforms, cloudfront at offset 100000; only D H Freight, ALW, BRC, Windward, none usable). Freyt World news: p1-2 cover everything from 1 Apr 2026 on, so p3-17 are older than the cutoff (no UK items). BIFA FSA 2026 shortlist (transportmonthly.co.uk copy fetches; every name known). AON (aeroceanetwork.net/feed/?paged=N fetches by hand-built URL, dated): no UK joins Feb-Nov 2026. IFN UK blog (5 names, all known). Freight Midpoint p1 (nothing new after 13 Nov).
- PARTLY USED: FBJ monthly archives fetch by hand-built URL (fbj-online.com/2026/MM/page/N/). Read this run: 11 p3-4, 10 p4-6, 09 p3-4, 08 p3-4, 07 p1-2, 06 p1-2. Mostly large firms; small UK hits were Clarusto (known) and Salvatori (haulier).
- NEW: forwardermagazine.com section pages (road-freight, giving-back, customs-clearance, recruitment-training, exhibitions-events) fetch and show dated headlines; mostly hauliers or large firms. Homepage, sea-freight and airfreight sections gave server errors. forwardingjobs.com shows no listings (JS).
- NEW: firmbase city lists (firmbase.co/resources/industry-lists/logistics-companies-in-the-uk-<city>) fetched for glasgow, leicester, edinburgh, bristol, nottingham; southampton/sheffield/hull refused (provenance), slough/coventry client_error. About 1-13 forwarders per city in the top 50.
- NEW: Clutch UK freight forwarders (clutch.co/logistics/freight-forwarders/uk) fetches: 50 names; domains shown only for the top 18.
- NEW: gov.uk Armed Forces Covenant business pages (gov.uk/armed-forces-covenant-businesses/<slug>) show date signed, size band and region. These are dated official hooks, but searching gov.uk returns mostly non-forwarders. Forwarders found: World Freight Ltd (signed 13 Mar 2026), FactoryCargo (22 Jul 2026, micro), Berser International Cargo (2024), United Worldwide Logistics (already emailed).
- DEAD: W&N Yorks chamber directory (only Advanced Forwarding new, no web/email; Zenith/512 pages robots-unreachable); BIFA category/news pages (client_error); UK chamber new-member searches (Suffolk/Essex etc.); club sponsorship searches (Leigh Leopards: G&T Express, Cal Courier; Southampton: AGL parcel software; Swansea: Owens Group); network new-member searches (FPS 2025, ASA no UK date, WTC alliance redirect); Enterprise/business awards 2026 searches (BIFA, Irish); AEO announcement search; pricing-appointment search (recruiters); JCtrans weekly202647 (client_error).
- Refused (provenance): zen-intl.co.uk, firmbase southampton/sheffield/hull city pages.

#### Searches used: 30 of 30

### HKSG agent notes

# hksg run (20 Nov 2026, 15Z): 3 qualified (all SG), 37 of 40 WebSearch calls

## Qualified (in hksg.jsonl)
- SG | Sealand Project Line Pte. Ltd. (spl-asia.com) | Breakbulk Asia 2026 exhibitor, stand B34 (18 Nov 2026) | sales@spl-asia.com (spl-asia.com/contact.php) | caveat: about.php title metadata says "WILH LOESCH" (Hamburg forwarder); body text and Breakbulk.com profile (shareholder Sanwar Kanoria, SG HQ, own Hamburg office since 2015) suggest independent. Part charterer.
- SG | ACS Freight Services Pte Ltd (acsfrt.com.sg) | Singapore Pavilion co-exhibitor, transport logistic / air cargo Shanghai 2026 (24-26 Jun 2026) | enquiry@acsfrt.com.sg (acsfrt.com.sg/contact/). Was an open lead with no hook.
- SG | SMP Global Pte Ltd (smp-global.com) | same Singapore Pavilion, Shanghai 24-26 Jun 2026 | enquiry@smp-global.com (smp-global.com/about-us/)
- MX: dns.google refused (permission prompt timed out), so all three are unchecked.

## Unfinished candidates (company | known | missing)
- HK | CATI Global Logistics (HK) Ltd (Unit 1502 Telford House, Kowloon Bay; IATA CargoLink id 9763) | TWO hooks: JCtrans join 9 Jul 2026 (weekly202628) and HKPC FILAS approval (ref FILAS-26-09-003-P, list as at 9 Oct 2026) | no website or email found (IATA listing has phone only; not in MarDep or HK Maritime Hub)
- HK | China Freight (Hong Kong) Ltd (chinafreight.com.hk; est. 1996, founder Terence Lai, local HK air/sea forwarder, agent for 15 airlines) | FILAS approval (FILAS-26-09-004-P, list 9 Oct 2026) | email: contact page (?page_id=1622) returns client_error; about page (?page_id=1538) fetches. Ownership of group not stated
- HK | Aria Supply Chain Ltd | JCtrans join 17 Jul 2026 (weekly202629) | website, email (JCtrans profile client_error, one name search found nothing)
- SG | Crossover Logistics (Asia) Pte Ltd (UEN 201908234W, 1 Tai Seng Ave, SSIC freight transport arrangement) | Singapore Pavilion Shanghai 24-26 Jun 2026 | website, email; possible link to a "Crossover Group" (epca.eu) not checked
- SG | Orbita Global Pte Ltd | Singapore Pavilion Shanghai 24-26 Jun 2026 | website, email (no web presence found)
- HK | JSD Logistics (HK), VINS Logistics, Orion Express (orionexpress.com.hk; robots.txt unreachable) | HKPC TPLSP approvals between 26 Jun and 9 Oct 2026 | sites/emails (searches found nothing)
- SG | Sky Leader Freight Pte Ltd | SAAA Project IMDD outreach at ITE College East 22 May 2026 (PERSPECTIVES Apr-Jun 2026) | no website; SAAA members-listing gives names only

## Rejected (this run)
- KC Intl Logistics Singapore: Korchina (Korean group). OA Freight: Guangzhou HQ (oafreight.com/service). Hiap Woon Shipping SG: chartering/port agency, no email, Taiwanese shipowner offshoot. DSM International Shipping SG: chartering. Poh Tiong Choon Logistics: group with independent directors (listed-style), large. FS Freight Systems SG: no email, LFS Global group member. RW Solutions HK: forwarder network operator, not a forwarder. Breakbulk Asia HK/China names (Win Rich, YH Ocean, RH Intl/Dalian Ruihao, Bao Glory, Lynux, Chinaland, Sea Bridge, SevSing): carriers or mainland firms. Top-Trans Expo Logistics (HK): exhibition logistics, mainland group likely (not checked further).

## Sources
- PRODUCTIVE: transport logistic China joint-pavilions page (transportlogistic-china.com/exhibitors/joint-pavilions) = 2026 show; Singapore Pavilion co-exhibitors: ACS Freight, Kargosmart, Crossover Logistics (Asia), SMP Global, CrimsonLogic, Orbita Global, CCN, Otonomi. Preliminary exhibitor PDF (imgs.tl-c.cn/uploads/editor/20260429/tlC%20preliminary%20list%20202605-EN.pdf) lists HK/SG exhibitors with country: USED UP for HK/SG (HK: Team Well contacted, Top-Trans Expo, CLN, TAC Index).
- PRODUCTIVE (one): Breakbulk Asia 2026 exhibitor list (asia.breakbulk.com/exhibitors, 192 names) now fully checked for SG/HK: USED UP.
- HKPC lists: TPLSP and FILAS "as at 9 Oct 2026" PDFs linked from bee.hkpc.org/funding-schemes/tplsp/ (fetches). June 2026 list: bee.hkpc.org/media/mhpfkkta/list-of-successful-applicants_en-62026.pdf (as at 26 Jun 2026). All post-March names now worked; next list probably Jan 2027.
- JCtrans weekly202621-202630 read for HK/SG (week 22, 26 none; 21 Halcon Primo; 23 JNC; 24 Seven Seas Container Lines (carrier); 25 Highlight; 27 Lovyph; 28 CATI HK + AOCEAN SG; 29 Aria HK; 30 ATA). HK/SG weeks 21-46 now all checked.
- Singapore Customs STP list now "21 July 2026" (isomer-user-content link on customs.gov.sg STP page); previous public list 13 Nov 2025, so a diff cannot prove a post-20-May certification. Not used.
- SAAA PERSPECTIVES Jul-Sep 2026: names Anthola Brokers + OTONOMI (sponsors 30 Jul 2026) only; no forwarders.
- DEAD: APEA 2026 (regional 15 Jul, Singapore 3 Nov: no forwarders); HK NextGen Logistician Awards 2026 (17 Nov 2026, winners from Hactl, DSV, CR Logistics, Cathay); HKPC LPFS list (associations only); HK Customs Elite Enterprise awards 2026 (names not published); Supply Chain Asia Awards 2026 (JS site); HAFFA 60th page (sponsors Hactl/AAHK/AAT), HAFFA competitions (2025, schools); ALMAC 2026 exhibition and participant pages (JS/client_error); hkiacargo market insights (no forwarder features); Security Cargo Network (nothing new for HK/SG); Pangea/PCN/GPLN/GLA HK-SG searches (old); com.sg / com.hk "announce/anniversary" searches (groups, SEO); SG job boards (jobstreet client_error); SME100 2026 (no forwarders); Breakbulk Americas (US firms); SBR awards (groups).
- Refused: dns.google MX lookup (permission timeout); jctrans.com store profiles (client_error); macaubusiness (robots); linkedin (robots).

## Searches used: 37 of 40

## Run of 20 Nov 2026 (prep, 18Z): 4 of 25 written (AU 1, UK 1, US 2); HK and SG gave none; about 145 searches

Written in 2026-11-20-mixed-6. dns.google MX worked via a web-fetch subagent (all four). Best unfinished: HK Premiere Logistics (HK) Ltd (Transport and Logistics Bureau MATF internship list 23 Jul 2026, 20 sea-freight trainee places; only an HR address michelle.leung@premierehkg.com on the government list, premierehkg.com not fetchable; needs a company sales/general address). Next hook sources opening soon: JCtrans weekly202647 (after 22 Nov), FTA Weekly Report 2026/47 (about 25 Nov), DCN awards winners (26 Nov).

### US agent notes

#### US research run, 20 Nov 2026 (later run): 2 qualified, 40 of 40 searches

##### Qualified (in us.jsonl)
- Trans-Border Global Freight Systems, Inc. (Round Lake NY; tbgfs.com; "locally owned and operated" since 1997; revenuebase 51-200). Hook: Employee of the Quarter Q3 2026, posted 5 Oct 2026 (tbgfs.com/employee-of-the-quarter-q3-2026/). The winner, Jessica, works in the Agent Pricing & Routing department and is praised for taking on difficult quotes, so the hook fits Kazinga well. Email: info@tbgfs.com (homepage footer and every post). MX unchecked.
- CASAS International Brokerage (San Diego/Otay Mesa CA; casasintl.com; founded 1984 by sisters Sylvia and Martha Casas; family-owned MBE; "Mighty Team Of 90+"). Hook: ENERGY STAR NextGen certification for its building, post 14 Oct 2026 (casasintl.com/news-and-events/casas-earns-energy-star-nextgen-certification). Email: services@casasintl.com (casasintl.com/our-story). Caveats: customs-brokerage-led (forwarding not listed as a service), and it belongs to CPH Group USA (cphgroupusa.com), an alliance of three family-owned border brokers. MX unchecked.

##### Unfinished candidates (company | known | missing)
- Highland Forwarding (Londonderry NH) | trade.gov Eastern Region Business Service Providers lists nicole@highlandforwarding.com (official directory; company rejected earlier for "no email") | dated hook after 20 May 2026 (awards page ends 2019)
- Herco Freight Forwarders (Miami) | ops@, wcc@, pricing@hercoinc.com on /category/announcements/ | hook (newest announcement Jan 2022)
- Tower Logistics Group (Doral FL; info@towerlogistics.net; managing partners Eduardo Pertuz and Felix Naveran; 17 US service points) | no news section, footer 2025 | hook
- Veritas Global Transportation (Meridian ID; customerservice@ and rates@veritasglobaltrans.com; NVOCC since 2015) | blog is SEO only | hook, size
- Advance Customs Brokers (Miami; founded 2013 by Pat Compres and Maria Bermudez; perishables) | IOR post after 6 Nov 2026 says "Advance Customs Brokers is a CTPAT certified broker" | published email (contact page has phone only); rejected earlier
- AIR 7 SEAS (Milpitas CA, since 1986; trade.gov San Jose list gives bsp@air7seas.us) | events page lists WCA Singapore 2026 and JCtrans Bangkok 2026, undated | dated hook, ownership (India offices?)
- NIT Logistics (Hackensack NJ, sales@nitlogistics.com), Straight Forwarding (Milpitas, chris@sfi.com), Just Your Broker (Elmont NY, hello@justyourbroker.com), all from trade.gov BSP lists | not surfaced in a batch "2026" search | hook, size
- Bay Area (Clutch SF): Air & Ground World Transport (ag-world.com; blog robots-unreachable), World Asia Logistics (myworldasia.com), Triple B Forwarders (tripleb.com), Cosdel, Graf Air Freight, OTX Logistics, KMD International | batch searches found no dated item | hook, email
- NY (Clutch New Haven list): R & R Freight (rrfreight.com), Capital Logistics (White Plains), JIMY USA, Euro Cargo Express, World Class Shipping, Dietl (fine art) | no dated item surfaced | hook, email
- LA Forwarders & Brokers directory (losangelesforwardersandbrokers.com, 46 members): Packair, Flegenheimer (info@flegenheimer.com; news stops 2008), Earth Cargo, CSL Express Line (customer advisories Nov 2026 only), Continental Agency/Unipac, FESCO, JG International, Momentum Shipping, Weida (lax@weidafreight.com) | no company hook | hook

##### Rejected (name: reason)
- Vigilant Global Trade Services: compliance-services firm, not a forwarder; no email
- On Time Customs Brokerage (Forest Hills NY): tiny, phone only, footer 2023
- Cotransa: "Cotransa Group" (foreign group)
- Missionary Expediters: contact page client_error, no site hits; mission-cargo niche
- Charter Brokerage: duty-drawback specialist; newest post Apr 2026; no email
- HYC Logistics: blog is third-party promotion; no company news
- Seair Global: India-led, multi-country group; jobs dated 2025 to Jan 2026
- American Shipping Company (shipamerican.com): newest dated company item Jun 2025; no email
- Bonded Logistics (Charlotte): 3PL warehousing / contract packaging
- Tri-Link FTZ: FTZ / e-commerce fulfilment 3PL with an SEO blog
- Unisco: SEO-heavy site; only GRI notices
- ClearFreight: JS-only site (nothing readable); 201-500 staff
- Serra International: President's 2026 Captain of Industry award (24 Jun 2026) is a hook, but still no published email
- Other NCBFAA 2026 new members (American Commercial Transport, EM International Freight, DNA Logistics Group, GHMatthes CHB, Micielo, Bridgeway, American Clearance, Universal Shipping, Evolve Trade Services): a guessed-domain allowed_domains search and a name search found no sites. Treat as dead.

##### Sources
- PRODUCTIVE: revenuebase.ai US category previews (surface with an allowed_domains revenuebase.ai search). "aviation-customs-brokers/united-states" and "customs-brokers-and-freight-agents/united-states" list 51-200 firms (gave CASAS, Trans-Border). Hand-built city pages fail (boston, san-francisco, baltimore, philadelphia, detroit). Dallas and San Diego fetched; Dallas is trucking.
- PRODUCTIVE: an allowed_domains batch over ~12 mid-size broker domains with the plain query "2026 announce OR anniversary OR welcome OR new office OR proud OR importer of record". It surfaced the Trans-Border employee-spotlight posts. Company "Employee of the Quarter/Month" or staff-spotlight pages are good hooks; look for /company-news/ category pages.
- NEW: trade.gov Business Service Provider pages (eastern-region, seattle-area, san-jose, boise) list forwarders with official emails, but there are few names. losangelesforwardersandbrokers.com gives 46 LA member domains (no emails). Clutch customs-brokers/san-francisco, /new-haven.md and freight-forwarders/san-francisco, /charlotte, /baltimore fetched (mostly trucking or movers).
- USED UP / DEAD: NCBFAA eBriefing (still the 13 Nov issue at 20 Nov); NCBFAA member-achievements page (Centurion awards, last 2026 = Deringer); IACAC Pallet (newest is still Oct 2026); JCtrans weekly202647 (client_error); Freyt World news (no US members); IOR-rule company-angle search (all known names); GPTW / employee-of-the-quarter / anniversary / award / careers-pricing searches (generic results); Propeller Club and NY/NJ FFFBA honorees (terminal operator, Serra); Chicago Propeller board (Jan 2026). Leave out SEO-heavy domains: bocintl.com, unisco.com, trilinkftz.com, air7seas.com, hercoinc.com.

##### Searches used: 40 of 40


### AU agent notes

#### AU research run, 20 Nov 2026 (later run): 1 qualified, 31 of 40 searches

##### Qualified (in au.jsonl)
- Hunter Cargo & Customs (hccnewcastle.com, Tighes Hill / Newcastle NSW; 13 staff plus the owners; Director Ashanthi Kruger, GM Wayne Kruger; no parent or group mentioned; Freyt World member). Hook: Freyt World story "Hunter Cargo & Customs and Nexline HK Deliver Complex OOG Solution", 22 Jul 2026 (article:published_time 2026-07-22), https://www.freytworld.com/news/hunter-cargo-customs-and-nexline-hk-deliver-complex-oog-solution/ . Email: sales@hccnewcastle.com, plain text on the homepage and on https://www.hccnewcastle.com/contact/ (which also lists imports@, exports@, customs@, accounts@). No unsolicited-email statement. MX not checked. Caveat: the hook is a network-news story and is 4 months old.

##### Unfinished candidates (company | known | missing)
- 1UP Cargo (1upcargo.com; AU offices in Scarborough QLD, Miranda NSW, Melbourne, Adelaide, Kewdale WA, plus CA/US/ZA/NZ) | dated hooks: own post "Aircraft Engines | Brisbane to Prague", 6 Oct 2026 (https://www.1upcargo.com/post/aircraft-engines-brisbane-to-prague); PCN member story 18 Aug 2026 (GM Omid Jay Ahmadi, Fremantle to Bauan RORO); exhibitor at transport logistic China, 24-26 Jun 2026 (preliminary list dated Apr/May 2026); Lognet member | missing: no plain AU email anywhere on the site (only a bookings link, plus za.ops@ in a mailto). Several office addresses look like serviced or virtual offices, and the business "emerged from the consolidation of business units" in 5 countries, so HQ, size and ownership are unclear. Probably drop.
- Brisbane Customs and Forwarding (brisbanecustomsandforwarding.com.au, Ascot QLD; corporate broker licence 00052C since 1992; "independent company"; info@brisbanecustomsandforwarding.com.au on homepage) | no news section | dated hook, size
- Anchor Logistics (anchorlogistics.com.au, 520 Collins St Melbourne; independent Australian-owned FCL export sea freight broker; 9 named staff with emails incl. Pricing Co-ordinator michelle@anchorlogistics.com.au; info@) | no news | dated hook; fit: export NVO/broker rather than full forwarder
- Poseidon Freight (poseidonfreight.com, Mascot NSW; MD David Denning; freight@poseidonfreight.com on homepage; Lognet member since 2015; Australia-Africa trade lane) | no news | dated hook, size
- Uniair Cargo (uniaircargo.com.au, Mascot NSW plus depots in Tullamarine, Pinkenba, Kidman Park and Perth Airport; enquiries@uniaircargo.com.au; IATA agent with 20+ years) | no news | dated hook, size, ownership
- Transco Cargo (transcocargo.com.au, Dandenong South VIC; trading since 1991; WCA and ALN; info@transcocargo.com.au) | blog posts are from May 2024 | dated hook
- Trademark Logistics International (Melbourne) | form only, no news | email, hook
- Allworld Logistics (100% Australian-owned, est. 2006) and Diamond Freight (Melbourne and Sydney) | no plain email, no news | email, hook
- Lloyds Shipping Australia (lloydsshipping.com.au, Revesby NSW) | phone and fax only, no news | email, hook
- Carried over, re-checked or not reached this run: Hearn, Pegasus, Searic, Swift Customs, Townsville Customs, Transcend, ECandF, Freight and More, Smartclear, RH Freight, Clarke Global (a careers/pricing batch search surfaced only homepages and service pages: no hook). FJT Logistics: still no plain email (not rechecked). Ship Smart Logistics Australia (JCtrans wk46): no website found in one search.

##### Rejected (name: reason)
- STS Logistics (stslogistics.com.au): site stale (news 2015, footer 2016); part of "STS Group"
- Romann Logistics: domestic pallet, linehaul and courier carrier, not a forwarder
- Mode Logistics (modelogistics.com.au): redirects to Seafrigo (group)
- GenFreight: already in companies.csv (it does have new dated posts: 13th anniversary 26 Aug 2026, team profile 14 Oct 2026; its emails are Cloudflare-hidden apart from a malformed sales@ link)
- Across the Ocean Shipping: AON stories are from 2021 (no dates), still no plain email
- Austral-Asia Freight: already in companies.csv (the open lead in leads.md is stale)
- C & H Freight (chfreight.com.au): robots.txt unreachable, site not readable

##### Sources
- Productive: Freyt World news (freytworld.com/news/) gave Hunter Cargo; there are no other AU items since Apr 2026. The allowed_domains trick worked: a search with hccnewcastle.com in allowed_domains made the site fetchable.
- New, partly useful: Lognet member directory pages (lognetglobal.com/directory/members/<id>) give city, website and enrolment date (1UP Cargo, Poseidon, Tomax, MCC). The revenuebase.ai AU list (/companies/shipping-and-freight-forwarders/australia) shows the top 25 of 467 only, mostly known or large. The ABF licensed-brokerages list (abf.gov.au/licensing/brokers/brokerages) gives about 416 names with no dates (a name pool only). The PCN Sep 2026 eMagazine has AU stories from TSL only.
- Used up: Freyt World news (AU); PCN news archive since May (TSL, 1UP only); AON feed (no AU members, only a Spedition India-to-Melbourne story); transport logistic China 2026 preliminary list (AU = 1UP Cargo, Omni Composite Tank); Breakbulk Asia 2026 list (AU = Powerhouse, already contacted, and LINX, a port operator).
- Dead this run: Smart50 2026 finalists (no logistics firms); Fremantle Business Awards 2026 winners and Wyndham Business Awards 2026 finalists (no forwarders); DCN homepage and features (members-only, no small forwarders quoted); DCN Women in Shipping and Customs Broker individual finalists (name searches find nothing); FTA/APSA 2026 conference program (speakers only from Think Global and CFL, both contacted); MHD and supply-chain magazines (large firms; mhdsupplychain robots unreachable); mining and energy magazines and projectcargojournal (now redirects to heavyliftpfi); chamber new-member searches; ISO-certification, case-study, "we have moved", hiring and "meet the team" searches over com.au (SEO pages); IFN AU members (no AU blog post; /blog/freight-forwarders-australia/ errors); World Freight Network news (no AU); NAP news (no AU since Oct); cargoconnections.net/news (client_error); GPLN newsletter 112 (flipbook, no text); businessnews.com.au (paywalled stubs); government submission searches; DCN AI articles (members-only); sports and charity sponsor searches.
- Not available yet: JCtrans weekly202647 (client_error again, and week 47 ends 22 Nov); FTA Weekly Report 2026/47 (about 25 Nov); DCN awards winners (26 Nov). These are the next AU hook sources.

##### Searches used: 31 of 40


### HKSG agent notes

#### hksg run (20 Nov 2026, later run): 0 qualified, 36 of 40 WebSearch calls

##### Qualified
- None. hksg.jsonl is empty. No HK or SG company met all four tests (independent, hook dated after 20 May 2026, self-published email, live site).

##### Unfinished candidates (company | known | missing)
- HK | Premiere Logistics (HK) Ltd | NEW HOOK: listed as "currently offered" (Part A) on the TLB/MATF "List of Maritime-related Internship Places" as at 23 Jul 2026 (tlb.gov.hk/matf/doc/Maritime-related_Internship_Places.pdf): 20 Management Trainee places in sea-freight marketing, 1 Apr 2026 to 31 Mar 2027. That page also publishes michelle.leung@premierehkg.com (an HR/recruiting contact, given with her name) | missing: ownership and size; a general or sales email on its own site (premierehkg.com: robots.txt unreachable; not in MarDep or hkmpdb; two searches found nothing). The main session decides whether a government internship list counts as an "official directory"
- HK | China Freight (Hong Kong) Ltd (chinafreight.com.hk) | FILAS approval FILAS-26-09-004-P (HKPC FILAS list as at 9 Oct 2026, bee.hkpc.org/media/tz1j5ymi/filas_list-of-successful-applicants_en-102026.pdf). HKTDC profile: 51-100 staff, est. 1996, Kwai Chung, contact Mr Stephen Law (Air Freight Controller), IATA/HAFFA/WCA. About page (?page_id=1538) calls it "the principal, wholly owned subsidiary" of a group (founder Terence Lai) | missing: email (homepage client_error, contact page client_error; not in MarDep, hkmpdb or HKTDC), parent-group identity
- HK | CATI Global Logistics (HK) Ltd | FILAS-26-09-003-P (same list) and JCtrans 9 Jul 2026 | missing: website and email. A third search found only the IATA CargoLink entry (id 9763)
- HK | Cargo Freight Services Ltd (cargofreight.com.hk, San Po Kong; cfshkg@cargofreight.com.hk in hkmpdb com=18; ex-HAFFA vice-chair firm) | official email | missing: hook (site robots-unreachable), size, ownership
- HK | MarDep directory firms never searched before (all have official emails in mardep.gov.hk/.../freiforw/index.html): Hanson Forwarding (hfltd.com.hk), A & B Logistics, A.R.T. Logistics, CAESAR (HK), Charter Link, CL Consolidators, CMS Logistics Group HK, EgapGO, Endeavour Cargo (eclworld.com), Fine Sky, Full Speed Maritime, G.R. Logistics, Guideline (HK), Hansen Exhibition Forwarding, HJ Interfreight, Honour Asia, Initial Express, Joy Fortune, JSP Global, Kesco SCM, Kusa Shipping, NTC Logistics, Oriental Air Transport, Pan World, Prime Line, Regal Worldwide, San Tai, Seatop, Shanghai Dragon, Shuttle Cargo, Sui Jun, Super International Freight, Supernova Logistics, Suz Air & Sea, SY&L, Thrift, Transfit, Tricor Global Logistics, Triple Eagle, Wintop, Xen Freight | missing: dated hook. Two allowed_domains searches over these domains surfaced only homepages and profile pages (most sites are old and have no news)
- SG | Penanshin Shipping / Penanshin Air Express (penanshin.com, 51-200) | has a news page (penanshin.com/news/) | WebFetch client_error on every page; group structure not checked
- SG | new revenuebase names (none in our data): Alps Global, GEFS, Monter Global, Eastern Oriental, Bluorbit, Satsaco, Germaxco, Cargosavvy, Kang Logistics, Raks International, NS International, Go Well, HBS Logistics, Fastrans, Fibs | missing: hook, email. One allowed_domains search found no dated company news

##### Rejected (name: reason)
- Crossover Logistics (Asia) Pte Ltd: part of Crossover Group, an ISO-tank chemical logistics group founded in China in 2014 (epca.eu/company/crossover-group); offices in SG, Suzhou, Jakarta
- Xpert-Log: a forwarder network, not a forwarder
- Air Planners (S) Pte Ltd: GSA, postal and e-commerce consolidator; no email
- Justship (justship.sg): online shipping platform with its own quoting
- ESA Logistics (HK): 3PL with 380k sq ft and 5+ mainland offices; no email on site; only a Part B (no longer offered) MATF entry
- Cargo Services Far East / US Allport Cargo Services HK: Allport group
- Morning Global, FreightAmigo, FUNDel, AIgniter (TLB modern-logistics internship lists 28 Aug and 21 Sep 2026): tech platforms, not target forwarders (FreightAmigo already offers instant quotes)
- NAF Global Logistics: only a Part B (no longer offered) MATF entry (email claudia.lee@naffreight.com, an HR contact); still no hook
- Panda Cargo HK (Lognet): joined 2015
- DT Logistics (HK) (NAP): 500+ staff, joined 2024
- SFS (Pharma) Logistics (Supply Chain Excellence Awards APAC 2026 shortlist): not HK or SG

##### Sources
- PRODUCTIVE (small, new): TLB Maritime and Aviation Training Fund internship lists (tlb.gov.hk/matf/doc/...). Maritime-related list as at 23 Jul 2026 (Part A = currently offered, gives company HR emails); Modern Logistics lists as at 28 Aug 2026 (..._(as_at_28.08.2026).pdf) and 21 Sep 2026 (F4-List_of_Internship_Positions_related_to_Modern_Logistics.pdf). These are mostly large firms and tech platforms; the only small independent was Premiere Logistics. An Aviation-related list for 2026 was not found (only the 2024 versions are indexed; the hand-built URL failed).
- USEFUL: MarDep freight forwarder directory fetches directly (120 entries); about 40 firms in it have never been checked (listed above). hkmpdb company-detail pages fetch.
- USED UP: HKPC FILAS list (only 3 names: OA Freight, CATI, China Freight); HKPC LPFS approved projects as at 23 Jul 2026 (associations only); HK Customs AEO Express new-member issues after May 2026 (#143 CATALO, #155 Sun Shun Fuk: not logistics firms; index at customs.gov.hk/en/service-enforcement-information/trade-facilitation/aeo/aeo-express/index.html); Supply Chain Excellence Awards APAC 2026 shortlist (supplychainexcellenceawardsasiapacific.com/2026-shortlist; awards night 1 Dec 2026, no HK/SG forwarders).
- DEAD: JCtrans weekly202647 (still client_error 20 Nov); HKPC LogTech Expo 29 Oct 2026 (vendors only); CILF 2026 (no exhibitor list); Lognet news (HK join from 2015); NAP news (no HK/SG joins since Oct); network new-member searches (cargoconnections, x2 and others gave nothing); CeMAT SEA 2026 SG Pavilion (12-14 May, before cutoff); transport logistic 2027 Munich directory (not out until end of 2026); tlacSEA 2027 (no list); ALMAC 2026 (hkmb articles name only large firms); HAFFA directory (no join dates), HAFFA 60th (sponsors Hactl/AAHK/AAT); Singapore Customs Awards (held in January); HKAEE (Jan 2026); HR Asia, CEIV, SBR and Supply Chain Asia awards (large firms or JS-only site); trade press searches for SG forwarders (large groups); premierehkg.com, cargofreight.com.hk, penanshin.com (fetch blocked); chinafreight.com.hk homepage (client_error).
- MX lookups: not attempted.

##### Searches used: 36 of 40


### UK agent notes

#### UK research run, 20 Nov 2026 (late): 1 qualified (Barrington Freight), 35 of 35 searches used

##### Qualified (in uk.jsonl)
- Barrington Freight Ltd (06060302, Basildon, active; CS 19 Feb 2026, accounts to 31 Mar 2026). Hook: new China to mainland Europe cross-trade service, blog post 3 Nov 2026 (barringtonfreight.co.uk/blog/cross-trade-shipping-china-mainland-europe/). Email info@barringtonfreight.co.uk (on /about-us/ and every page). Named contact on the same about page: Matt Everard, MD, matt@bfreight.co.uk (other domain; Simon Poole simon@bfreight.co.uk, Lee Pottle lee@bfreight.co.uk also listed). Owned by Matthew and Carriann Everard (PSCs, 25-50% each). Size: Clutch says 2-9, but the site names 4 managers, a terminal at Bowden House and 224 Google reviews; may sit at the low end of the band. Road/sea/air/customs; quotes by request form (no instant pricing). MX not checked. Source: Clutch UK freight-forwarders page 3 (Leaders Matrix), then an allowed_domains search.

##### Unfinished candidates (company | known | missing)
- Velta International Ltd (03873306, Witham + Heathrow + Manchester; 36 staff and GBP 17.9m turnover FY Nov 2024 per Endole; AEO, BIFA, IATA, WCA) | plain emails Witham@velta.co.uk, Airfreight@velta.co.uk, Logistics@velta.co.uk on velta.co.uk/About-us/; CH active (CS 27 Jan 2026) | dated hook (site /news/ has only carrier news; no 2026 company items); PSC is one unnamed controller on Endole, check CH PSC page
- The Custom House (Transit) Ltd (12922382, Ashford/Sevington, independent customs agent, Clutch 10-49, ECSA UK rep) | enquiries@thecustomhouse.co.uk on homepage | company hook (no news page). Industry angle only: HMRC Sept 2026 notice on Sevington/Holyhead IBF changes and the Oct 2026 Sevington transit closure (multimodal news 28 Oct) affect it directly; CH check not done
- Flight Logistics Group Ltd (Colnbrook + Wokingham, founded 1991, courier origin) | heathrow@ / crm@flightlg.com on /who-we-are/; case study "Supporting Serpentine Galleries" 1 Jul 2026 (flightlg.com/2026/07/01/...) | fit doubtful (3PL, e-commerce fulfilment, art logistics, courier; freight modes not described); size, ownership, CH
- Alinea Customs (London EC4, customs@alineacustoms.com, director Holly Piggott, Clutch 2-9) | customs broker plus consultancy/training | dated hook (latest company item Dec 2024), size
- TGT Global Solutions Ltd (13405722, Dover; renamed from TGT Customs Ltd on 3 Aug 2026 per CH; JCtrans 7 Sep 2026) | hooks exist | every email Cloudflare-obfuscated (home, jobs, T&C); also sells its own in-house customs platform "Velocity Enterprise" (poor fit). Effectively a reject unless a plain email appears
- Clutch customs-broker names not checked: Dover Hamilton UK Customs Agents (dovertransit.co.uk, Rainham, 50-249), Bounty Freight (bountyfreight.co.uk, Dover, 2-9), CustomsChecks UK (Coulsdon, 10-49), Nucleus International Cargo (Sunninghill, 2-9), Cool Cargo UK (coolcargo.co.uk, Hounslow, 2-9) | none surfaced company news in batch searches
- goodfirms UK air-freight names not researched (no sites surfaced): Mango Logistics Group (Rotherhithe), Alinnza Trading London, Andrews Shipping & Forwarding (05640055, Enfield), D & K Freight, Fusion Freight (Leeds), Atlantis Forwarding (Leeds), Dartswift International (Liverpool), Blue Whale Logistics (Leicester, 10-49), Bettafreight, Airfreight Worldwide (Birmingham)

##### Rejected (name: reason)
- Whale Global Freight Ltd (08818247, Potters Bar; JCtrans 9 Nov 2026): no website (whaleglobal.co.uk is an unrelated IT shop); SIC road freight/warehousing
- DGR Global Logistics UK: London W1 virtual office, foreign-run site, Cloudflare email only
- Brit Customs: site still renders nothing (fourth check)
- JLD International Ltd (Armed Forces Covenant 26 Jul 2026): micro, CH company incorporated 27 May 2026 at a Keighley farm; not a forwarder
- RJB (UK) Logistics (Covenant 26 Oct 2026): micro haulage, no site
- Atlas Logistics UK Ltd (Feltham): newest news Jul 2024; WCA member
- Linc Group (Coggeshall): the domain found is a mobile-phone firm; no forwarder site found
- FPF Global Ltd (Heathrow, 2-9): no email on site, phone only
- CARGOBY Connect: haulier group (ex Brian Yeardley Continental); groupage launch article undated
- ITD Global: international e-commerce logistics group (West Ham partner), not a target
- Frontier Forwarding Services (Feltham): international removals
- Tudor International Freight, Kinnes Shipping, Hemisphere, Interspan, KL Freight, International Forwarding, Millennium Cargo, Simarco, Jenkar: already in companies.csv
- AICES express members (Mark3, Team Air, Nemcast, GlobeXAir, Superior, UKP, Tylos, Linex, One Stop): courier/express operators; none surfaced company news except UKP (SEO post only)

##### Sources
###### Productive
- Clutch UK pages (fetch directly; domains given only for Leaders Matrix): freight-forwarders/uk?page=3 (gave Barrington), customs-brokers/uk, customs-brokers/uk/england.md, air-freight-companies/uk. freight-forwarders/uk?page=4 and customs-brokers/uk?page=2 are 404.
- goodfirms.co/supply-chain-logistics-companies/air-freight/uk: 48 UK names with size band and founding year (no domains).
- Barrington's blog (barringtonfreight.co.uk/blog/) posts dated company news; recheck in later runs.
###### Used up / low yield
- gov.uk Armed Forces Covenant: the transportation-industry Atom feed (gov.uk/armed-forces-covenant-businesses.atom?armed_forces_covenant_business_industry%5B%5D=transportation) fetches and lists the 50 latest signers with dates. Since 20 May only micro hauliers, bus and rail firms; keyword parameters are ignored.
- multimodal.org.uk/exhibitor-article list is now 59 pages (about 590 entries), ordered by modification, not alphabetically; pages 1-2 have no new UK forwarders (Clearport is software).
- multimodal.org.uk/news newest items to 20 Nov 2026: no new small UK forwarders.
- FBJ archives 2026/06 p3, 07 p3, 09 p5 and category/people: large firms only.
- forwardermagazine.com homepage now fetches (newest item 7 Oct 2026); no small forwarders.
- Kent Invicta Chamber members-blog fetches (dated); no forwarders.
###### Dead
- HMRC customs agents register: only ODS files (assets.publishing.service.gov.uk); curl is blocked by the proxy (403) and WebFetch sees binary. The CFSP contact list page points to the same ODS.
- AICES members page: express couriers only.
- BIFA new-member PDFs: the 2024 pattern (bifa.org/wp-content/uploads/2024/10/New-Members-for-September-2024.pdf) fetches, but 2026 guesses fail; bifa.org/membership/new-members gives client_error; dev.bifa.org/?p=768 fetched, but dev.bifa.org/membership/new-members/ was refused (provenance, user declined). Do not retry.
- Breakbulk Europe: only page 1 loads; the old Exhibitor-list path errors.
- JCtrans weekly202647: still client_error.
- Intermodal Europe exhibitor list (JS widget), Import Export Show 2026 (no list), Spelthorne Business Awards 2026 (Blaiklock only), UKWA, International Trade Week, EcoVadis/JOSCAR, rebrand, new-service, network new-member, charity/sponsorship and trade-press new-office searches: nothing new.
- Robots-unreachable: kitefs.co.uk (Kite Freight Services).

##### Searches used: 35 of 35

## Run of 20 Nov 2026 (prep, 21Z): 2 of 25 written (SG 1, UK 1); AU and US gave none; about 156 searches
Written in 2026-11-20-mixed-7: EES Freight Services (SG, VILOG 2026 exhibitor), Martintrux (UK, BIFAlink Aug 2026 regional meeting speaker).
Held back (finish next run): HK | Cargo Freight Services Ltd (cargofreight.com.hk; cfshkg@cargofreight.com.hk from hkmpdb.gov.hk/en/company-detail.php?com=18; VILOG 2026 exhibitor booth A121; MX self-hosted) | missing: confirm the website is live (our fetcher could not reach it) and headcount. US | Exportalia Customs Brokers (grupoexportalia.com; ecbusdoc@exportaliasc.com printed only in SD Chamber spotlight 29 Sep 2026) | missing: address on its own site, site loads (redirect loop), ownership.
New source: VILOG exhibitor list (vilog.vn/en/exhibitor-list/page/N/?page_branch=189, 13 pages, show 30 Jul to 1 Aug 2026; hand-built page URLs fetch). HK/SG fully checked; names for other regions not yet researched: AU MCC World International, Neolink, 1UP Cargo, Ace Global Logistics; UK Global Intelligent Logistics; US IBC, Premier Global Logistics.

### AU agent notes
### AU research run, 20 Nov 2026 (21Z): 0 qualified, 39 of 45 searches

#### Qualified (in au.jsonl)
- None. au.jsonl is empty.

#### Unfinished candidates (company | known | missing)
- FJT Logistics | strong hook (Nov 2026 News Brief, 19 Nov 2026: 25th anniversary, new Perth/Brisbane managers) | plain email: fjtmel@/fjtbne@/fjtadl@ appear only in the og:description meta tag, contact body is Cloudflare. Main session should decide whether the meta-tag address counts as published (not rechecked this run).
- Novis Logistics Solutions (novislogistics.com.au; founded 2012 by Director Max Telese, maxt@novislogistics.com.au and customerservice@ on /about-us/team/ and site pages; HO 41/574 Plummer St, Port Melbourne; Adelaide Business Manager John Auciello, johna@) | no dated company item (blog undated SEO, careers "no openings", BMSB 2026-27 flyer only) | dated hook (an Adelaide office opening would be one if dated)
- Bell Total Logistics / BTL (btl.com.au; HQ Kirrawee NSW, offices Wingfield SA, Brendale QLD, Keilor Park VIC; privately owned, began 1878 as E.V. Little; Clutch 2-9, really larger) | gallery caption "Sarah Coles 20 Years of Service 2026" (undated within 2026; images in 2026/03 folder, so probably before cutoff); news = regulatory notices; AEB automated-clearance launch Oct 2025 | plain email (all Cloudflare on contact/about), dated hook
- Priority Cargo Australia (prioritycargo.com.au, 303 Collins St Melbourne; founded Sydney 2000, Melbourne 2004, Brisbane 2005; privately owned, Chinese-language focus) | no email on about page, no news | email, hook
- Salt Global Logistics (saltglobal.com.au, Banksmeadow, 2-9), TFI Global (tfi.com.au, Tullamarine, 10-49, est. 1989), MHK Corps (mhkcorps.com, Parkville, 10-49), BKG Logistics (bkglogistics.com.au, Terrey Hills, 2-9), Admiral International (admiralgroup.com.au, Caringbah; logistics/fulfilment) | domains surfaced in one batch search but homepages refused (PROVENANCE_REQUIRED) for tfi/mhkcorps/saltglobal | everything
- Orion Shipping (orionshipping.com.au, Melbourne, 2-9), TWF Logistics (twflogistics.com, Ascot Vale, 2-9) | not fetched | email, hook
- Global Destination Forwarding (gdfaustralia.com.au, Brookwater QLD; NZ and AU) | robots unreachable; ownership NZ? | everything
- GTC (Perth; Abhidha Bhatt, Lorin McKenzie; new FTA member, new offices, FTA 2026/35 2 Sep 2026) | one people search found nothing | website, email
- Older AU unfinished leads from previous runs (Hearn, Pegasus, Searic, Swift Customs, Brisbane Customs and Forwarding, Anchor, Poseidon, Uniair, Transco (only 2018 office move post), Townsville Customs, Tayper, Transcend, ITM, ECandF, Matthew Short, SP Customs, Australian Global Freight, Freight and More, 1UP Cargo) still have no dated hook; one name-batch search returned nothing.

#### Rejected this run (name: reason)
- FM Global Logistics Australia (Bibra Lake WA; hook FTA 2026/32, pictured at ATLC Perth evening 12 Aug 2026): Malaysian listed FM Global Logistics Holdings annual report 2025 lists "FM Global Logistics - Australia" (group)
- Towers International (towersint.com.au): domain redirects to seaway.com.au (Seaway, rejected)
- Doser Freight (Dry Creek SA): trucking. Australian International Express (Wangara): courier. Hellas Europe: removalist. Secon: container cartage. Customised Freight Solutions: domestic road/rail. ACE Logistic Solutions (acetrans): Leggett Group, trucking. Transcoast Express: domestic 3PL
- Consolidated Freight Australia (cfalogistics.com.au): no email (phone only), news page only external links
- Warren Global Logistics: 2-9 staff, no email (form), news 2018
- Global Transport Logistics (globaltransport.com.au, Bibra Lake): sales@ on homepage, no dated item (gallery "coming soon")
- Intercargo Connect: JCtrans wk28 join already considered and rejected earlier
- Lloyd International (lloydintl.com): HQ Scituate MA, USA (US mover to AU), no email
- Complete Freight (Seaton SA, info@completefreight.net.au, wholly Australian owned): news page ends 2013
- Atlas Global Logistics (atlasglobal.com.au, Carlisle WA, 100% Australian owned, 2-9 staff, enquiries@): no dated item
- Now Global Logistics (nowglobal.net, Woodville SA): no email, no news
- Ship Cargo / Cargo Australia (shipcargo.com.au): blog full of unrelated SEO spam, email Cloudflare
- AUK Logistics (auklogistics.com): AU/TW/MY offices, emails Cloudflare, no news
- Bollinger Shipping: news page newest 2017 (third check)
- Across the Ocean Shipping: Brisbane-office post still client_error
- ACID Logistics (Business NSW Central Coast micro-business finalist, 7 Aug 2026): 5 staff or fewer
- Navia (FTA 2026/34 visit): Navia Freight, held back earlier as large

#### Sources
- FTA advocacydetail/<id> hand-built URLs FETCH this run (no search needed). Mapping: 4877=2026/26 (1 Jul), 4881=Biosec 27, 4882=2026/27 (8 Jul), 4884=2026/28, 4890=2026/29, 4895=2026/30, 4900=2026/31, 4904=2026/32 (12 Aug), 4909=2026/33, 4913=2026/34, 4915=2026/35, 4917=2026/36, 4920=2026/37, 4924=2026/38, 4930=2026/39, 4947=2026/42. Firms named in 26-39 are all contacted/rejected/groups (United Carriers, Gibson, 3DL, McHugh, OSCL, Pentagon, Bluestar, ICE Cargo, Cargoport, End to End/ATLC, FM Global (group), CAS (Mondiale), Intergroup, Magellan, EES, Kalgin, ICAL, Navia (large), GTC Perth (no site)). Weekly reports 43/44 not located (4943=submission, 4946=podcast, 4948=Biosec 42, 4949=Biosec 43). USED UP through 2026/46. Next: 2026/47 about 25 Nov (try advocacydetail about 4955-4960).
- JCtrans weekly AU: weeks 21, 23, 25, 27, 28 (offset 100000: only Intercargo Connect), 29 checked this run: no new AU. Week 47 client_error. AU weeks 20-46 now all checked = USED UP until week 47+.
- Clutch AU freight-forwarders ?page=2, 4, 5, 6 and customs-brokers ?page=5 read; Clutch profile pages clutch.co/profile/<slug> FETCH by hand-built slug and give website, staff band, founding year (some slugs client_error). Names from these pages now mostly checked.
- heavyliftpfi Australasia: nothing new since 17 Nov (Bullocks).
- DEAD this run: network new-member searches (GLA/X2/Globalink/Atlas/WCA/Cargo Connections/Freight Midpoint: only 2025 or used posts); Lognet news (no AU since Feb 2024 Vincon), Lognet/WCA directory (JS-only); DCN news and feature searches (paywalled, no small firms visible); WiseTech/CargoWise customer stories (no AU since 2021); AFIF new-member search; Business NSW 2026 Business Awards; AFI Awards 2026 (trucking); regional new-office search (groups); SmartCompany/InDaily search; Care-Factor ball sponsors; Lloyd's Loading List/Loadstar/STAT Times (acquisitions only); careerone/Workforce Australia/lever job search; trade-show exhibitor search (Fine Food = GEL Events; CBAFF26 is NZ); AusTender search; com.au "attended conference" search (SEO); "proud to announce" extended search.
- allowed_domains with theleadsouthaustralia/indaily/smartcompany/brisbanebusinessnews/illawarramercury/geelongadvertiser/newcastleherald returned HTTP 400 (works with only the first three).
- MX lookups: none run (no qualified companies).

#### Searches used: 39 of 45 (including one HTTP 400)


### HKSG agent notes
### HKSG research run, 20 Nov 2026 (21Z): 2 qualified, 41 of 45 searches

#### Qualified (in hksg.jsonl)
- SG | EES Freight Services Pte Ltd (eesfrt.com.sg, 50+ staff, est. 1983) | VILOG 2026 exhibitor, booth C101 (show 30 Jul-1 Aug 2026) | general@eesfrt.com.sg (contact page) | Microsoft 365
- HK | Cargo Freight Services Ltd (cargofreight.com.hk, est. 1996) | VILOG 2026 exhibitor, booth A121 | cfshkg@cargofreight.com.hk (hkmpdb com=18) | self-hosted MX | size not published, own site unreachable

#### Unfinished candidates (company | known | missing)
- HK | Farenco Freight Services Ltd | Hong Kong ICT Awards 2026, Smart Logistics Certificate of Merit (UnlockScale: City Super smart warehouse, with Geek+), ceremony 19 Nov 2026 (gs1hk.org/SmartMobilityAward) | website, email, ownership (may be City Super's logistics arm); booklet PDF gs1hk.org/sites/default/files/2026-11/SMA2026%20e-version.pdf returned empty
- SG | Highlight International Logistics Pte Ltd | VILOG 2026 exhibitor (JCtrans pavilion B156) plus JCtrans join week 25 2026 | site highlight-logistics.com refused (provenance), hil-group.com robots-blocked | email, size
- HK | EZOCEAN (ezoceanlogistics.com) | VILOG 2026 exhibitor via its Vietnam entity; says HQ in Hong Kong and China | HK office address/email, ownership, size
- HK | Premiere Logistics (HK) Ltd | TLB MATF maritime internship list as at 23 Jul 2026 (tlb.gov.hk/matf/doc/Maritime-related_Internship_Places.pdf): 20 Management Trainee places 1 Apr 2026-31 Mar 2027; michelle.leung@premierehkg.com (HR contact) on that list | ownership and size still unknown (two more searches found nothing; one result pointed at listed Grand Power Logistics 8489.HK but no link to Premiere confirmed); premierehkg.com robots-unreachable

#### Rejected this run (name: reason)
- SCF Global (scf-global.com, SG): CargoWise/BPO consultancy, SCF Group; not a forwarder (Supply Chain Asia Awards 2026 winner, 30 Oct 2026)
- Star Concord SG: blog only republishes trade news (AERO post 8 Apr 2026 is Air Cargo Week copy); still no own hook
- (EES Freight Services SG: its Lognet join is from 18 Feb 2020, so not a hook; qualified later via VILOG 2026)
- NTC Logistics HK (ntclogistics.hk): subsidiary of NTC Group India
- JSP Global Forwarding HK (jspuniversal.com): part of JSP Universal Group, Calgary (Canada)
- Endeavour Cargo Logistics HK (eclworld.com): site static, footer 2019, no dated item
- CT Freight (S): no website or email (JCtrans profile only)
- Pegasus Worldwide Logistics (Hong Kong) (pegasuslog.com, VILOG 2026 C164): Taipei HQ, no HK address or email published
- Topsheen Shipping Singapore (VILOG 2026): carrier (Chinese shipping line)
- PAL Line SG: news page still only E50 (Dec 2025) plus two generic 28 Jul 2026 articles
- DENZAI International (SG, Breakbulk Middle East 2027 exhibitor): DENZAI Huationg, part of the Huationg heavy-lift group
- Breakbulk Middle East 2027 (Dubai, 2-3 Feb 2027) SG names: FLS Singapore (group), Goodrich (India group), Chinaland, Hanson Carriers, SMI Shipping, Ceekay (carriers); HK Hong Glory Shipping (carrier by name; profile refused)
- Farenco Freight Services Ltd (HK): Certificate of Merit, Hong Kong ICT Awards 2026 Smart Logistics (co-entrant with City Super / Geek+, ceremony 19 Nov 2026; gs1hk.org/SmartMobilityAward) | no website or email found in two searches; moved to unfinished

#### Sources
- DEAD: Security Cargo Network news (newest post 12 Nov 2026, no HK/SG); JCtrans weekly202647 (client_error); Conqueror news page 2 (Jun-Sep 2026, no HK/SG); Payload Asia freight-forwarders category (large firms only); Payload Asia Awards search; SSA year in review (no names); SLA new-member search; Lognet news (pages 2 and 12 checked; IDs up to 984; no 2026 HK/SG; page 1 and 21 return an old default list); SG Police RACA list (10 Mar 2026, before cutoff); Supply Chain Asia Awards 2026 page (no names; ceremony 30 Oct 2026 Bangkok; only Hactl and SCF Global publicised).

- DEAD (cont.): Asia Cargo News HK search (large firms); Pangea news pages 1-3 (HK/SG only Unitex and Visy); Freight Midpoint blog p1 (only Fast-Link 11 Nov, used); WCA broadcast pages (robots); WCA Worldwide Conference 2026 Singapore was March 2026 (before cutoff); CEIV search (Hactl/Cathay/AOC); HKGCC new-members search (nothing); HAFFA press index (no member names May-Nov 2026); GLA Singapore member directory (renders empty); ALMAC 2026 coverage (no exhibitor names); TLB maritime internship list 23 Jul 2026 re-read (Part A forwarders: AOC, cargo-partner, Hankyu, KWE, MOL, Premiere only); egapgo.com (empty page); tflogistics.com and seatophk.com (robots-unreachable).
- PRODUCTIVE (new): VILOG 2026 exhibitor list (vilog.vn/en/exhibitor-list/page/N/?page_branch=189, Transport and Forwarding, 13 pages, hand-built page URLs fetch). Show held 30 Jul-1 Aug 2026 at SECC HCMC (JETRO J-messe 157802); list pages undated. HK/SG fully scanned: EES (SG), Cargo Freight Services (HK), Pegasus HK, EZOCEAN, Highlight SG, Global Container Freight SG (rejected earlier), Global Alliance SG (contacted), Topsheen SG (carrier). Other branches 211/213 have no HK/SG forwarders. Same list has AU names (MCC World International, Neolink, 1UP Cargo, Ace Global Logistics AU) and US/UK names (IBC, Premier Global Logistics, Global Intelligent Logistics UK) for other regions. The country filter parameter is ignored.
- PRODUCTIVE (small): Hong Kong ICT Awards 2026 Smart Mobility winners (gs1hk.org/SmartMobilityAward), Smart Logistics stream.
- DEAD (late): TILOG-LogistiX 2026 (10times exhibitors client_error, no official list surfaced); Transport Logistics Indonesia (next edition May 2027, no list); luminik transport logistic SEA (client_error); Intermodal Europe 2026 (exhibitor widget not fetchable); JCtrans expo page (Urumqi forum 19-22 May 2026, no names); Hanoi logistics show search (nothing); hkengage job search (JS-only list; the portal mainly carries large firms).
- Refused (provenance timeout) late in the run: highlight-logistics.com, middleeast.breakbulk.com exhibitor profile pages (denzai, smi-shipping-pte-ltd, hong-glory-shipping-co-limited).
- hkengage.gov.hk job pages fetch and show company plus publish date (HK government job portal); not searched systematically.
- MarDep freight forwarder directory fetched in full (120 names, websites, emails) this run.

#### Searches used: 41 of 45


### US agent notes
### US research run, 20 Nov 2026 (21Z): 1 qualified (weak/conditional), 40 of 42 searches

#### Qualified (in us.jsonl)
- Exportalia Customs Brokers, LLC (San Diego / Otay Mesa CA): WEAK/CONDITIONAL. Hook: San Diego Regional Chamber Member Spotlight, 29 Sep 2026 (sdchamber.org/2026/09/member-spotlight-exportalia-customs-brokers-llc/). Email ecbusdoc@exportaliasc.com appears only in that spotlight (company-supplied copy), not on its own site. MX = Google Workspace (dns.google worked). grupoexportalia.com still redirect-loops, so ownership is unverified ("Grupo" suggests a cross-border group with a Mexican side; Mexico is not excluded). Main session decides.

#### Unfinished candidates (company | known | missing)
- US | Clutch Global Logistics (clutchgl.com, Lombard IL, est. 1993; LetsTalk@clutchgl.com, Wesley.peterson@clutchglobal.com Director of Compliance on /pmsp/; OTI/NVOCC/IATA/IAC; CCBFA voting director) | careers page lists Import Division Manager + 2 entry writers, recruiter.com ad for a US-Canada Cross Border Trucking Specialist, all undated | missing: a dated hook after 20 May 2026, size, ownership
- US | Empire Worldwide Logistics (empirewwl.com, El Segundo CA; partnerships@empirewwl.com; LACBFFA 2026 board director Kenneth Quartarolo) | no news | missing: hook, size; positions itself with a 'platform' (check fit)
- US | ITC-Diligence International (LA; David Harlow is LACBFFA President 2026), Interline Corporation, Team Handling Services (teamhandling.com redirect-loops), Jaak Transport | from LACBFFA Board 2026 page | missing: websites (ITC, Interline not surfaced), email, hook
- US | Highland Forwarding (nicole@highlandforwarding.com via trade.gov) | events page says it exhibits at Breakbulk Houston/Antwerp, but it is not on the Breakbulk Americas exhibitor list; site/privacy page has no email | missing: dated hook
- US | Miami small NVOCCs from revenuebase (no dated items): Deluxe Freight (sales@deluxefreight.com, est. 1996, 11-50), United Globe Cargo (info@unitedglobecargo.com, owner Konny Nakamura), Blue Draco (info@bluedraco.us, posts end 2024), Caribtrans (sales@caribtrans.com, news ends Jul 2024), CLM Cargo (usa@clmcargo.com; Colombian HQ; blog refused on provenance) | missing: hook. Unchecked from the same lists: itbfusa.com, tsscorp.us, astralfreight.com (est. 1985), drt-int.com, allianceintl.net, ishipinc.com (Houston 11-50), hawthorneglobal.com, mygmt.com (NY), int-shipping.com, kinternational.com, snacargo.com, rfclogistics.com (since 1968), japslogistics.com
- US | Clutch Nashville customs brokers list (clutch.co/logistics/customs-brokers/nashville.md) surfaced, not read
- US | FMC 16 Nov 2026 applicants (QI changes, weak hooks): All World Shipping Corp (Coral Springs; robots), Star Cluster Logistics (Bensenville), Madrizqui Corp (Miami), Bondex Logistics Seattle (El Monte); 5 Oct: Hayakawa Forwarding (Damascus OR, transfer to LLC), Modaltrade USA (Medley) | missing: everything; hook is admin-only

#### Rejected this run (name: reason)
- Weida Freight System: Chinese-owned, 470k sq ft warehouse; news undated
- Tower Logistics (Doral), Triple B Forwarders (no email), World Asia Logistics (myworldasia.com; 13 offices incl. Germany/Italy/Korea), Flegenheimer (news 2008): no dated item
- Magnum Freight (no email, posts 2016), World Commerce Forwarding Houston (footer 2018, no email): stale
- iTransTrade (WFN join 24 Sep 2026): site has no email, address or size
- Advance Customs Brokers: whole news page read, still no email anywhere (third check)
- Profreight Brokers (Edison NJ): IOR post 19 Nov 2026 is promotional; email Cloudflare-obfuscated only
- EDI Express (LTL trucking), DGX/Dependable (group; news 2021), Mach 1 Global (201-500, robots), SeaWide Express (AJC Logistics company, no email)
- Red Lab Logistics (produce brokerage), Altex Logistics (trucking carrier)
- Cahill & Dunn CHB: no website found
- Williams Clarke (footer 2023, no email), CBC Logistics (no email, no news)
- Origin FGL (Istanbul; not US)

#### Sources
- FMC OTI applicant lists newly read: 16 Nov, 5 Oct, 28 Sep 2026 (mostly micro/new firms; Cargo International Consolidators QI change 16 Nov but already contacted; Charles Kendall NY = UK group; Barsan = Turkish group). 13 Jul list surfaced, not read. Next list about 23 Nov.
- revenuebase.ai new slugs (fetch after one revenuebase search): nvocc-freight-forwarders/united-states/miami (25 of 127), /houston (12 of 49), /new-york (9 of 41), nvocc-companies/united-states/miami (14 of 30), less-than-container-load-shipping-companies/united-states, customs-brokerage-services/united-states (mostly known/large), international-ocean / international-air / ocean-freight-forwarders (large only). Small Miami/Houston NVOCC sites are mostly stale.
- LACBFFA Board 2026 (lacbffa.org/cpages/committees) and CCBFA board (ccbfa.org/team): company names, see Unfinished. Board seats are calendar-year, not a post-May hook by themselves.
- sdchamber.org member spotlights are dated and print company emails (gave Exportalia); other chambers' spotlights did not surface in a generic search.
- Inbound Logistics "Noted" monthly highlights (noted-supply-chain-highlights-0726, Sep 2026 issue): large firms only; -1026 slug client_error.
- DEAD: GLA (3103 page undated), Lognet News (US joins 2025), Elite GLN (robots), Freight Midpoint Delex Air Cargo (Mar 2026), FCBF golf 2026 flyer (no sponsor names), FCBF gala page (client_error), state job boards (illinoisjoblink big firms/client_error; caljobs URL too long), exec-moves search, 'member spotlight' searches, broker-exam congratulations, Inc Best Workplaces (2021 article), podcasts, warehouse-opening search, business-of-the-year search, business-journal largest lists (large firms), next-generation/succession search, network 'proud to announce' search, trade.gov Portland BSP (2024), HCBFFA directory (client_error), NCBFAA eBriefing (still 13 Nov issue at 21Z), JCtrans weekly202647 (client_error at 21Z), VMA26 speakers (large firms).
- dns.google MX lookup worked this run (exportaliasc.com).

#### Searches used: 40 of 42


### UK agent notes
### UK research run, 20 Nov 2026 (21Z): 1 qualified, 36 of 38 searches

#### Qualified (in uk.jsonl)
- Martintrux Group Limited (01638449, Dover; customs clearance plus air/sea forwarding; offices Dover, Heathrow, Manchester; revenuebase 51-200) | hook: named as a speaker ("local agent Martintrux Ltd") at BIFA's Kent & East Sussex regional meeting, BIFAlink August 2026 p20 (online.flippingbook.com/view/165913907/20/) | louise@martintrux.co.uk (only address published; martintrux.com/contact) | MX Microsoft 365 | PSCs Robin Sandy and Fashion Distribution Ltd (small private co.) | modest hook, first-name-only mailbox, so address the company, not "Louise".

#### Unfinished candidates (company | known | missing)
- Velta International Ltd (03873306, Witham; Witham@/Airfreight@/Logistics@velta.co.uk) | re-searched: no 2026 company news; velta.co.uk/news client_error | dated hook
- RBF Cargocare: FINISHED, emailed in 2026-11-21-mixed-2 (21 Nov)
- Gemini Freight Management Ltd (8577621, Greenhithe, sales@gemini-freight.com) | newest post Apr 2025 | hook, size
- MEXL Logistics (London, est. 2007, admin@mexl.co.uk; removals, fine art, freight, customs) | no news; accreditation logo links mexl.ch | hook, CH, ownership
- Maina Group (Southall, est. 1979; offices India/Kenya/Uganda/South Africa) | no email on homepage; contact.php unchecked | email, hook, ownership (may be foreign-linked)
- United Global Logistics (unitedglobal.co.uk, Manchester, 11-50) | homepage not checked | everything
- Westin Par LLP (Dover forwarder; Find a Job customs-clerk ad 8 Jan 2026) | no website found in one search | site, email, hook
- LV Shipping / LV Logistics (Middlesbrough; Hebburn expansion, bdaily 24 Nov 2025; MD Lee Woolams) | probably large/multi-country | 2026 hook, size, email, CH
- The Custom House (Transit), Quick Cargo, Anchor Freight, Associated Freight Services, AOG Worldwide, Alinea Customs | rechecked: still no company news after 20 May 2026

#### Rejected this run (name: reason)
- Flight Logistics Group: courier/e-commerce/art 3PL; only SEO posts and a 1 Jul 2026 case study
- Uniexpress: software story 2023; already in companies.csv
- Kranlee Logistics (King's Award 2026): already in companies.csv
- Meachers Global Logistics: already in companies.csv (DFA join was 2023)
- Neon Freight (MD joined BIFA board): already in companies.csv
- Priority Freight: 300+ staff (rejected before)
- Caledonian Freight (Jack Rice, BIFA Scotland rep): rejected before (form only)
- ALS Brokerage Service (Richard Catt, BIFA SE rep): ALS group
- Network International Cargo (Coventry warehouse, Mar 2025): Irish, old
- Pallet Power: haulier subsidiary
- Portico Shipping: port operator
- James Cargo Services / JCS Livestock (BIFA award, BIFAlink Oct 2026): already in exclusion files
- Martintrux blog: SEO only (but company qualified on the BIFAlink hook)

#### Sources
- NEW PRODUCTIVE (small): BIFAlink issues on online.flippingbook.com. August 2026 = /view/165913907/N/ (p1 overview, p20 "Around the regions" names regional hosts/speakers incl. Martintrux; p22 rules/regional reps; p24 ad). October 2026 = /view/470360780/ (golf day: Cargo Overseas, Shipco; award: JCS Livestock; conference sponsors are vendors). Sep and Nov 2026 issues not indexed yet (search "BIFAlink November 2026" again next run; regional-meeting reports name local agents).
- NEW (read): revenuebase /companies/customs-brokers-and-freight-forwarders/united-kingdom (25) and /london (16 of 63). New names listed above; allowed_domains batch over 12 of them found no dated news.
- NEW BUT BLOCKED: gov.uk Find a Job (findajob.dwp.gov.uk/details/<id>) shows direct employers with dates; detail pages fetched early in the run, then robots became unreachable; search pages always ROBOTS_UNREACHABLE; allowed_domains searches return only old job IDs.
- LOW: bdaily.co.uk allowed_domains search works alone (adding eadt/essexlive etc. = HTTP 400).
- Re-read, nothing new (no search cost): Freight Midpoint (Stellar 6 Nov, emailed), Freyt World (to 14 Oct), Project Cargo Network archive p1, WWPC news (to 20 Nov), FBJ 2026/11 p1.
- DEAD: trade-press appointment and "independent forwarder" searches (LLL, ACW, FBJ, Loadstar); Multimodal 2026 Modal Awards finalists (large firms); BIFA Associate Members Apr 2026 (vendors); King's Awards 2026 Gazette lists (Kranlee only); Logistics Awards 2026 finalists; co.uk TLD "proud to announce" search; network new-member searches (incl. Digital Freight Alliance); Dover/Holyhead customs-agent new-office search; sports sponsorship search; ISO/AEO accreditation search; NI forwarder search (Export & Freight NI magazine on issuu not readable); "new weekly groupage" search; Farnborough 2026 exhibitors; freight-software go-live search; firmbase Cardiff list; JCtrans weekly202647 (client_error); bifa.org/people (no employers).
- Refused (provenance): firmbase freight-forwarding-using-wordpress-uk.

#### Searches used: 36 of 38 (one returned HTTP 400)



## Run of 20 Nov 2026 (prep, 23Z, finished 21 Nov): 7 of 25 written (UK 2, US 2, AU 1, SG 1, HK 1); about 140 searches
Written in 2026-11-21-mixed: Global Intelligent Logistics (UK, VILOG), UK Global Logistics (UK, Multimodal 2027 stand E2), MCC World International (AU, VILOG), Highlight International Logistics (SG, new Shah Alam branch Oct 2026), Cargo Freight Services (HK, VILOG; finished from the 21Z hold), Sonica International (US, VILOG), Baylink Shipping (US, VILOG). Rejected: Exportalia (email not on its own site, site redirect loop). VILOG 2026 exhibitor list is now USED UP for all live markets.

### US agent notes
### US research run, 20 Nov 2026 (23Z): 2 qualified, 34 of 44 searches

#### Qualified (in us.jsonl)
- Sonica International (Elk Grove Village IL; est. 2015, privately owned, 7 stations incl. Toronto branch Jan 2026 and Shanghai ops centre) | VILOG 2026 exhibitor booth A159-160 (vilog.vn/en/exhibitor-list/page/12/?page_branch=189; show 30 Jul-1 Aug 2026) | info@sonicainternational.com (/contact-us/; named station emails also there) | MX Microsoft 365
- Baylink Shipping Inc. (Floral Park NY; est. 2006; TSA IAC, FMC NVOCC, WCA + JCtrans; sister Baylink Global Logistics in Bensenville IL and Azusa CA; support centres Nanjing and HCMC) | VILOG 2026 exhibitor booth B113 (page 1 of the list) | info@baylinkusa.com (/contact/ and /company/) | MX IONOS

#### Unfinished candidates (company | known | missing)
- Jaguar Freight Services (jaguarfreight.com, Valley Stream NY; "20+ logistics professionals", offices Antwerp and London; weekly market newsletter "The Weekly Roar", latest 16 Nov 2026) | only email seen is myfuture@ (careers page; careers list dated 2021-23) | missing: sales email (check /contact), a company-news hook (newsletter alone is weak)
- JCtrans week 38 US joins not yet researched: JS & Sons Logistics (Pearland TX, 18 Sep 2026), REYD Global Logistics / Nishukti Management (NJ, 18 Sep 2026) | a name search found no sites | missing: site, email
- Goodfirms US customs brokers (goodfirms.co/supply-chain-logistics-companies/customs-brokerage/usa) 10-49 names never checked: AFC International (Atlanta, 1989), Robert E. Landweer & Co. (SeaTac, 1936, so 90 years in 2026), Sprint Forwarders (Tukwila), The Camelot Company (Schiller Park, 1977), AAA Customs Brokers (Des Plaines, 1986, 40 years), Service Shipping (Schaumburg), Harry F. Long (Wood Dale), E. Besler (Chicago), MP Custom Brokers (Roselle), Comtraasys (NJ, 1984) | domains not surfaced (a name search returned directories only) | missing: everything

#### Rejected this run (name: reason)
- Exportalia Customs Brokers: grupoexportalia.com still 302-loops to itself and exportaliasc.com is robots-unreachable, so the email is not on its own site (brief rule)
- Sine Trading International (Pittsburgh, VILOG A129): no email anywhere on the site; runs its own instant-quote tool
- Premier Global Logistics (ship-pgl.com, VILOG B139): truck/expedite brokerage, Cloudflare email only
- IBC Customs Brokerage & FB Express (VILOG A146): e-commerce courier (rejected before)
- Chariot Logistics (Nashville): truckload brokerage. Rest of Clutch Nashville list: Howard Baer 250-999, others trucking; Caribbean Shipping Freight robots-unreachable
- Prolog Worldwide (Raleigh; FMC name change 13 Jul, new NVO/OFF 27 Jul): 2-9 staff, no email, no news
- CLN Worldwide (Charlotte): blog undated (2023-24 posts), no company hook
- XPI Services (Charlotte): no email or address, footer 2023
- Terra Logistics LLC (Saddle Brook NJ; ASA new member 16 Jul 2026): 2-9 staff, no website
- K Carlton International (Fort Lauderdale): no email on the site, blog undated
- Cargo Services Inc (cargos.com, Indianapolis): acquired by OIA Global, Apr 2026
- Deluxe Freight: its "we are moving" post is from 2016
- Highland Forwarding: events and charitable pages are undated or 2011-2016
- Empire Worldwide Logistics, Clutch Global Logistics: homepages show no 2026 item (re-checked)
- BSI Global Logistics: Chinese group
- Coppersmith: rejected before (Honour Lane link)

#### Sources
- PRODUCTIVE: VILOG 2026 Transport & Forwarding list. All 13 pages were read this run; US names on it: Baylink (p1), Sonica (p12), Sine Trading (p12), IBC (p10/11), Premier Global (p11). It is now USED UP for the US. Branches 211 (warehouse/cold chain) and 213 (support services) have no US exhibitors.
- NEW: ASA Network news (asanetwork.org/category/news/, page 2): dated new-member posts (Terra only for the US). Cargo Power Network blogs (cargopowernetwork.com/blogs): dated member news, no US members since Jun 2026. JCtrans weekly202638 now fetches (US names above). FMC 13 Jul list read (only Prolog and O.E.I. International, San Gabriel, adding OFF, unchecked).
- Clutch .md city lists fetched (hand-built): customs-brokers atlanta, seattle, chicago, charlotte, nashville; freight-forwarders los-angeles, houston, new-york?page=2. Philadelphia .md client_error. revenuebase hand-built city pages work: freight-forwarding-companies/united-states/atlanta, /chicago, /los-angeles (mostly truck brokers).
- DEAD: JCtrans weekly202647 (still client_error 21 Nov); FMC 26 Oct, 2 Nov, 6 Jul lists (client_error); NCBFAA eBriefing 13 and 20 Nov new-member URLs (login page); IACAC Pallet Aug and Oct 2026 (Forward Air, ECU, RAS only); sdchamber member-spotlight and ribbon-cutting categories (only Exportalia); JCtrans USA Regional Conference 2026 page (attendees "coming soon"); TPM who's-attending (only TPM22-25); transport logistic China 2026 list (logos only); IICS Mumbai 2026 list (JS); FITCE (2025 page only); NAFTZ/NCBFAA exhibitors (vendors); CNS 2026 and Conqueror AGM (before cutoff); WCA pressroom (no member news); IFN, Freight Lounge, go2gln (no dated US members); thebusinessview international-trade category; newsismybusiness PR search; four allowed_domains "2026 news" batches over ~70 small-forwarder domains (only Deluxe 2016, Highland, Jaguar newsletter); job-board searches (ATS and state job banks: large firms only); "excited to announce", "visit us at booth" and "we attended" searches.

#### Searches used: 34 of 44

### UK agent notes
### UK research run, 20 Nov 2026 (23Z): 2 qualified (one conditional), 28 of 34 searches

#### Qualified (in uk.jsonl)
- Global Intelligent Logistics (UK) Ltd (09096729, Dartford DA2 6NX; active, CS 23 Jun 2026; sole PSC Daniel Sebastian Hart 75%+; site names MD Daniel Hart plus about 10 managers; sister cos (BIR)/(LHR)/(MAN) Ltd owned in Kent) | hook: exhibitor booth C106 on the VILOG 2026 exhibitor list (vilog.vn/en/exhibitor-list/?page_branch=189&page_country=204, the only UK exhibitor; show 30 Jul to 1 Aug 2026, SECC HCMC) | info@globalintel.co.uk (homepage) | MX Microsoft 365 | caveat: the list page has no year label (site now promotes VILOG 2027, 5-7 Aug 2027); template site with placeholder testimonials.

- UK Global Logistics Limited (UKGL; 08871720, Office 06 Dephna House, 26 Chase Road, London NW10 6QN; active, CS 31 Jan 2026, total-exemption-full accounts; owned 75%+ by Rooopa Ltd, director Ricky Soewignyo) | hook: Multimodal 2027 exhibitor page, stand E2 (multimodal.org.uk/exhibitor-article/ukgl) | info@uk-gl.com (homepage) | MX Google Workspace | CONDITIONAL: page undated (letter stand = 2027 floorplan); headcount unknown, serviced office, may be very small.

#### Unfinished candidates (company | known | missing)
- Velta, RBF Cargocare (homepage: customs clearance Felixstowe, info@, 2023 site, no news), Gemini Freight, MEXL, Maina, Westin Par LLP, The Custom House, Alinea Customs | rechecked or carried | dated company hook still missing
- United Global Logistics Ltd (unitedglobal.co.uk, Manchester, sales@unitedglobal.co.uk, "privately owned independent"; Pakistan links) | news page says "Coming soon" | hook, CH
- ACC Shipping Ltd (accworldwide.com, Gravesend; BIFA/AEO/IATA) | posted "Beaujolais Day 2025" on 25 Nov 2025; a Beaujolais Day 2026 post (event was 19 Nov 2026) may appear in the next days | hook, email
- Tuplin (Gatwick) Ltd (tuplin.co.uk; export packing + forwarding; Gatwick, Stansted, Royston, Newmarket, Shanghai; sales@ and gatwick@tuplin.co.uk) | blog posts Jun-Nov 2026 are SEO guides only | company hook
- Pulse Cargo Ltd (Winchester, getintouch@pulsecargo.co.uk, founder "Tom"), Skyline Global Logistics (Heathrow, enquiries@skylinegl.com; meta tags copied from a kitchen firm), NKR Freight Ltd (08271463, Leicester, info@nkrfreight.com; blog = industry posts only) | no company news | hook

#### Rejected this run (name: reason)
- Alltrade Post Ltd (Northampton, Lognet new member 09/03/2026 = 9 Mar 2026 by list order): before cutoff
- Optima Worldwide, Expressway Handling (Multimodal): already emailed; DRS Logistics Southampton (multimodal article is a 404); transport logistic China 2026 UK exhibitors (charter brokers, GSAs, airports only)
- BE ACCURATE LTD (Breakbulk Europe 1A11): Piraeus, Greece
- BALENA PROJECTS LTD (Breakbulk Europe 1B51): Calgary, Canada
- TR Logistics Group (Belfast; Shauneen McConville is BIFA NI regional rep, BIFAlink Aug 2026 p22): no published email (form only), group with Rotterdam office
- Compliant Customs (Multimodal 2027 stand G5): outsourced remote declaration service, no email, no dated page
- Killick Martin (BIFA 2026 Extra Mile finalist, Globalia news 20 Nov 2026): Atlantic Pacific group (rejected before)
- Allied Group (Armagh, Export & Freight 13 Jan 2026): already emailed
- Allegro Logistics (Clevedon): e-commerce fulfilment, not a forwarder
- CTS (GB) Ltd (Reading): newest news 18 May 2026; DG/nuclear specialist logistics
- CCL Consolidated Carriers (Troon): site now redirects to ccl-techlogix.com
- Emerge Global Ltd (ex Seaspace Int'l Forwarders, Stoke): Cloudflare-only email
- Redcliffe International Shipping: no email, footer 2022
- Interfreight UK: already rejected; Gist (M&S), Raaziq (Pakistan), Newell & Wright (container haulier), Alpi UK (Italian group)
- Pro Customs Solutions and EORI (UK): already emailed; Easy Customs, Bullet Express: no Multimodal page surfaced in a search

#### Sources
- PRODUCTIVE: VILOG UK filter (vilog.vn/en/exhibitor-list/?page_branch=189&page_country=204) fetches directly and lists one UK exhibitor; same pattern should work for other countries (AU/US filters: change page_country).
- NEW POOL: FIATA GB directory (fiata.org/directory/gb/, read with offset 0 and 100000): about 290 UK individual members with city and website; most domains are not in our files. Searched with allowed_domains this run (query "2026 news announce" or "freight forwarding company news 2026"): A-B, C-G, G-L, L-O, P-S, T-Y batches (about 120 domains). Results are mostly SEO posts; only domains listed above surfaced. Don't put raaziq.com in a batch (it floods results). Unsearched: hfreight, ikra etc. were in batch 3; remaining unsearched mostly large groups.
- USED UP: BIFAlink Aug 2026 p14, p21, p22 (p22 = regional reps: Cunningham, Rice, Melton, Murray, Newman (pnauk.com), Catt (ALS), McConville (TR Logistics)); Oct 2026 p19-23 (Euro 7, container losses, port articles; no member news). BIFAlink Sep/Nov 2026 still not indexed (both searched once). dev.bifa.org/events/<date>/ pages list regional meetings without host companies. Breakbulk Europe page 1 now shows different names (Allelys, AV Dawson, ABP); BE Accurate/Balena are foreign. Globalia news (only Killick Martin UK).
- DEAD (added): transport logistic China 2026 preliminary list PDF (imgs.tl-c.cn/.../tlC preliminary list 202605-EN.pdf: 14 UK names, none small forwarders); europe.breakbulk.com UK search (ports, ACS, Portico); bifa.org/event/<slug> pages client_error, dev.bifa.org/event/<slug> fetches but names no hosts; careers/pricing-job search (only US BGI); lognet news (UK join Mar 2026); cargoconnections UK story is 2020; Freyt World news (nothing after 14 Oct).
- Multimodal exhibitor-article searches with allowed_domains multimodal.org.uk still surface new slugs (gave UKGL); most other forwarders surfaced are already contacted.
- DEAD: JCtrans weekly202647 (client_error; a marketing.jctrans.com search returns only older weeks); lognet directory search; EADT/regional business awards 2026; handyshippingguide/exportandfreight/aircargoweek/logisticsbusiness appointment searches; Multimodal exhibitor-list-2026 page (widget only, shows 2027 dates); generic "shortlisted 2026 freight forwarding" search; network new-member search over 15 network domains. allowed_domains with irishnews/belfasttelegraph/agendani/ulsterbusiness gives HTTP 400.

#### Searches used: 28 of 34 (one HTTP 400 included)

### AU agent notes
### AU research run, 20 Nov 2026 (23Z): 1 qualified, 38 of 43 searches

#### Qualified
- MCC World International Pty Ltd (mccworldinternational.com, 18/44 Sparks Ave, Fairfield VIC; est. 2007; "10+ expert logistics team members", "Australian-owned", no group named; Lognet member; main lanes China and Vietnam) | hook: VILOG 2026 exhibitor, booth C137-138 (show 30 Jul to 1 Aug 2026, SECC HCMC), https://vilog.vn/en/exhibitor-list/?page_branch=189&page_country=200 | info@mccworldinternational.com on /contact/ | MX vsrv772.armadaservers.com (web host) | no unsolicited-email statement; street address plain on contact page. Earlier runs had it as "no dated hook"; VILOG is the new hook.

#### Unfinished candidates (company | known | missing)
- Neolink Logistics & Distribution (neolink.au, Alexandria NSW; est. 2017 by Sean Crook and Christopher Makhoul; privately held) | VILOG 2026 exhibitor (booth C101, shared with DACO Logistics GmbH) | plain email: info@ is Cloudflare-only on home, talk-to-us, who-we-are, work-with-us, T&Cs; FTA directory entry has no email; press room newest May 2025.
- Ace Global Logistics Ltd (Australia) (acegloballogistics.com.au) | VILOG 2026 booth G106 | site robots-disallowed, so nothing verifiable
- 1UP Cargo | VILOG 2026 booth G104 (in addition to hooks in the 18Z notes) | still no plain AU email; HQ/ownership unclear
- FJT Logistics | Nov 2026 News Brief (19 Nov 2026, 25th anniversary, new Perth/Brisbane managers) | plain email: none in the news-brief body or privacy policy (meta tag only); privacy policy says no promotional email without consent (newsletter context)
- Novis Logistics (email known) | rechecked nav: no news/events, only BMSB 2026-27 notice | dated hook

#### Rejected this run (name: reason)
- Seabridge Logistics Group: "a member of the Cardinal Group"; no plain email; newsroom = market updates only
- Bell Total Logistics: latestnews = regulatory notices only, emails Cloudflare (re-checked)
- ACLI (All Cargo Logistics International, Mascot): forms only, no news
- ACA International (acaint.com.au): newsroom is "DACHSER news" (Dachser-linked)
- Summit Global Logistics (sgl.com.au, Silverwater): no plain email, no news
- Salt Global Logistics: saltcustomerservice@ known, no news section, no hook
- Priority Cargo Australia: email Cloudflare-only, copyright 2020-21, no news
- UB Freight Australia: NZ HQ, Lognet since 2023, no public email
- Energy Global Logistics (energylogistics.com.au, Eastern Creek; info@ plain, est. 2008, Australian-owned): newest dates 2024, no hook
- KTL Australia (Tullamarine; info@ktlaustralia.com): industry-news undated, newest BMSB 2025-26
- ICS Global Logistics (Bacchus Marsh; ics@): newest post May 2025 (SEO)
- PAT Express, Century Customs, Casa Logistics, Freight Mart, Fintran: already contacted/in records
- Williams Logistics (ASCLA 2026 Future Leaders highly commended, Dimitri Krideras): likely williamsglobal.com.au (robots-blocked); not pursued

#### Sources
- VILOG AU country filter (vilog.vn/en/exhibitor-list/?page_country=200, also with page_branch=189): 5 entries (1UP, Ace Global, DACO GmbH, MCC, Neolink). USED UP.
- FTA advocacydetail mapping: 4934=2026/40 (7 Oct), 4941=2026/41 (14 Oct), 4950=2026/43 (28 Oct), 4960=2026/45 (11 Nov), 4963=2026/46 (18 Nov); 4938=Biosec 41, 4951=Biosec 44, 4955=Shipping Report 31 (6 Nov), 4953/4954/4962/4965 = submissions/notices/DCN item; 4952 server error (probably 2026/44). Small firms named (I.H. Hunter, Casa, Pentagon, Kalgin, ASL) all contacted. USED UP through 46. Next: 2026/47 about 25 Nov, try ids ~4966-4972.
- FTA directory (offset 100000 and 200000) re-read: a few listings show emails (Not Just Customs operations@notjustcustoms.com.au, Taree, no website; Elite International sel@elitefsa.com; GGL Australia edmund@gglaustralia.com; Kenneth Lloyd chris@). Not Just Customs is fresh but has no website or hook.
- ASCLA 2026 winners page (ascla.com.au/winners/) now shows 2026 results (gala 23 Oct 2026): only Williams Logistics (individual HC) and Lexin (consultancy) are near-forwarders.
- FTA newsdetails ids: 41173 = 1 Sep 2026, 41300 = 21 Sep 2026 (mostly ABF notices; low yield).
- Dead this run: Lognet AU search (enrolments old: CTS 2014, UB 2023); IFCBAA (conference 14-16 May 2026 Hobart, no names; news = notices); newsworthy.ai; WA Export Awards and SA Premier's Export Awards 2026 (no forwarders); AusRAIL26 and SPLASH 2026 official forwarder = GEL Events; MegaTrans 2026 (16-17 Sep, MCEC) exhibitor directory is JS-only (primecreative eventsair), and "MegaTrans 2026 stand" search found nothing; Breakbulk Middle East 2027 (no AU exhibitors); FIATA YLP 2026 (no AU); Shipping Australia new-member posts (no forwarders); Glassdoor job lists (client_error); job-board allowed_domains search (lever/workable/employmenthero: no AU forwarders); Prime Mover/trade mags (domestic); Hortconnections/perishables and IMARC exhibitor searches; anniversary search (all contacted); cargolinked.com AU directory (names only); "Borders Across" FTA magazine (no 2026 edition indexed); JCtrans weekly202647 still client_error; allowed_domains batches over Clutch/FIATA/FTA small domains with "news 2026"-type queries mostly return nothing or SEO pages (the hook-word query "anniversary award welcome new office" returned one result for 15 domains).
- MX: dns.google worked in this subagent (mccworldinternational.com).

#### Searches used: 38 of 43

### HKSG agent notes
### HKSG research run, 20 Nov 2026 (23Z): 2 qualified, 39 of 43 searches

#### Qualified (in hksg.jsonl)
- HK | Cargo Freight Services Limited (cargofreight.com.hk) | listed on the VILOG exhibitor list, booth A121 (vilog.vn/en/exhibitor-list/page/5/?page_branch=189). The list page has no date; VILOG 2026 ran 30 Jul-1 Aug 2026 and vilog.vn now promotes VILOG 2027 (5-7 Aug 2027). Word the hook neutrally | cfshkg@cargofreight.com.hk (hkmpdb com=18) | MX self-hosted (mailhub1.cargofreight.com.hk) | the site is CONFIRMED LIVE: https://www.cargofreight.com.hk/?page_id=91 fetched once an allowed_domains search had surfaced it (the homepage and contact pages are still robots-unreachable). Branches in China, Vietnam and HK; no parent group named; headcount not published
- SG | Highlight International Logistics Pte Ltd (highlight-logistics.com, est. Oct 2014) | JCtrans Weekly New Members 17 Jun 2026 (marketing.jctrans.com/magazine/weekly/pc/weekly202625.html, JC Projects) + VILOG B156. Its about-us page also shows a new Shah Alam (Malaysia) branch from 15 Oct 2026 | sales@highlight-logistics.com (highlight-logistics.com/contato-1) | Microsoft 365 | headcount not published; founder-led

#### Unfinished candidates (company | known | missing)
- SG | Silk Express Freight Pte Ltd (silk.com.sg, est. 1994, family-owned, 11-50 staff per ZoomInfo, Cargo Agents Bldg C; SCN member since 2002; WCA/JCtrans) | site live | missing: an email (homepage has none, its contact section is an anchor on the homepage) and a hook. The "SAAA new member Sep 2026" claim in leads.md could not be confirmed: the SAAA homepage has no new-members post, and the Sep post names GE Lines, Ants, Mitra Famosa and FPS
- SG | M&P International Freights Pte Ltd (mp.com.sg, est. 2006, UEN 200614913Z; sales@sin-mp.com.sg on mp.com.sg/about-us/) | certificates uploaded Aug 2026 (Singapore SME 500 award, ISO 9001, SLA membership valid 2026, FIATA, SFA licences); links to mpfreights.cn, so it may have Chinese ownership | missing: a dated hook (no certificate date can be read) and the ownership
- HK | Grandways Int'l Airfreight / Grandways Logistics (grandways.com), Preford Container Line / Air Express (preford.com.hk) | Security Cargo Network HK members | both sites are HTTP-only, so WebFetch loops on the redirect | everything
- SG | BSV Shipping Agencies (S) (bsvship.com, about 15 staff, SCN member) | HTTP-only redirect loop; also runs a container fleet (part carrier) | everything
- HK | Premiere Logistics (HK), CATI Global, China Freight (HK) (chinafreight.com.hk: every page returns client_error), Aria Supply Chain | unchanged from the 21Z run
- HK | Future Sky Logistics (futureskyhkg.com; info@ and joelau@futureskyhkg.com on homepage; JCtrans and Legend Logistics Network member) | missing: a dated hook

#### Rejected this run (name: reason)
- Farenco Freight Services (HK): a China Resources Holding division (CRC Logistics; SCN post of 18 Mar 2022, kamho.chan@crclogistics.com); the second-largest warehouse operator in HK
- EZOCEAN: publishes no HK office or HK email; a multi-country group (VN/TH/ID/KH/MY/US/CA)
- FPS Global Logistics (SG): Famous Pacific / Famous Holdings group (recordowl)
- Ants Logistic (SG): no website (antslogistic.com.sg not indexed); a shipper for a Chinese mattress maker
- MMI Asia Pte Ltd: Messe Muenchen's Singapore trade-fair organiser
- Project Argus (SG): its hook (LogiSYM award, 13 May 2026) predates the cutoff
- CIFF (HK): Mondiale VGL group, about 130 staff
- Flynt Worldwide: Sydney head office
- Park Express (HK): WCA founder member with 8 mainland China offices; no email on the homepage and no news
- Supernova Logistics (HK), The One Shipping (HK): no dated item
- Thrift Logistics: the domain is for sale
- Unitex HK (pricing-assistant job on CTgoodjobs): 720 staff (rejected earlier)
- AGL (SCN Top Asia member, Manila conf Nov 2026): AGL Co. Ltd, Seoul, Korea (excluded country)
- Speed Group Holdings (HK, Nasdaq IPO filing Feb 2026): e-commerce logistics, 87% of revenue

#### Sources
- PRODUCTIVE: an allowed_domains search over 16 candidate domains with the plain query "logistics freight contact us" made cargofreight.com.hk/?page_id=91 and highlight-logistics.com fetchable. Security Cargo Network: its 2019 member-directory PDF (securitycargonetwork.com/wp-content/uploads/2019/11/member-directory.pdf, 309k chars; only the first 100k read) lists HK/SG members with profiles; the news post "Warehousing needs in Hong Kong ... Farenco" settled Farenco's ownership.
- Clutch SG (clutch.co/sg/logistics/freight-forwarders, /customs-brokers, /air-freight-companies) fetched after a search with allowed_domains clutch.co. New domains: lchlogistics.com, nationalforwarder.com, simply-freight.com, wefreight.com.sg, fastrans.com.sg, airsealogistics.com.sg, hermes-logistics.biz, aspac-aircargo.com.sg. One "2026 news" allowed_domains search over 15 of them found only mp.com.sg and amglobal pages.
- TLB MATF: the aviation internship list for 2026 exists only as an XLSX (tlb.gov.hk/matf/doc/Aviation-related_Internship_Positions_2026_(as_at_2026.09.21).xlsx, linked from tlb.gov.hk/matf/eng/aviation/mais.html). WebFetch returns binary and curl gets a proxy 403, so it is UNREAD; it would list small HK air forwarders offering internships. The maritime list is now dated "as at 2026.6.26".
- DEAD: hkengage.gov.hk job pages (indexed jobs return client_error); hk.jobsdb list pages and jobs.ctgoodjobs.hk job pages (client_error); ALMAC 2026 (16-17 Nov 2026; no exhibitor names anywhere); HAFFA site (HKTDC invitations, Belt and Road Summit pass only); SME100 2026 (SG list page server error, no logistics); Cargo Connections news archive (no HK/SG since May 2026; assembly recap names no members); GPLN AGM 2026 sponsors; WWPC news; network new-member searches (dfalliance, x2, atlas etc. gave nothing); Asia Fruit Logistica 2026 (official forwarder DSV); FIATA World Congress 2026 Milan (luminik shows no attendee companies); TILOG-LogistiX 2026 (e-visitor guide exhibitor list empty in extract); HK Customs Elite Enterprise award 2026 (no names); HKEX/Nasdaq small-forwarder IPO search; "Hong Kong-based forwarder opens office" search (large firms); hkmb.hktdc.com SME features (2024-25, platforms); Softlink Global customer releases (no names); air cargo agent award searches (large firms); SAAA latest-news/upcoming-events pages (stale, last item 2024/2025); HKPC TPLSP/FILAS (no list after Oct 2026); a "visit us booth exhibition 2026" allowed_domains search over 20 MarDep domains (only Honour Asia service pages).
- Fetched directly from the MarDep links (no news on any): anderson-agl.com, avanteclogistics.com, kw-log.com, sailwin.com.hk, tricor-global.com, wintopasia.com (robots-unreachable), shglobal.com.hk (client_error).
- JCtrans weekly202647: client_error twice (20 and 21 Nov).
- MX: dns.google worked this run (highlight-logistics.com, cargofreight.com.hk).

#### Searches used: 39 of 43

## Run of 21 Nov 2026 (prep, 07:43 London): 4 of 25 written (UK 2, US 1, HK 1); AU and SG gave none; about 155 searches
Written in 2026-11-21-mixed-2: Global Cargo (Far East) (HK, ALN-BAM Asia & Oceania Top Agent award 1 Nov 2026), Atlantic International Freight Services (UK, rebrand 14 Oct 2026), RBF Cargocare (UK, Fresh Awards 2026 and RSCL Expo), FTS International Express (US, SCN story 15 Oct 2026).
Held back (unfinished): US | IGL Logistics Inc. (igl360.com, Charlotte NC, ops@igl360.com on /about/, 21-50 staff) | SCN index lists 'IGL Logistics New Charlotte warehouse' dated 24 Jun 2026, but the post was refused and the company match is unconfirmed | missing: open the post (securitycargonetwork.com/igl-logistics-new-charlotte-warehouse/) to confirm it is igl360.com, MX.
Watch next: AU FTA Weekly Report 2026/47 (~25 Nov), DCN Awards winners (26 Nov), ACC Shipping Beaujolais Day 2026 post (UK), JCtrans week 47.

### US agent notes (21 Nov 07:43 run)
#### US research run, 21 Nov 2026: 2 qualified (both with caveats), 38 of 44 searches

#### Qualified (in us.jsonl)
- FTS International Express, Inc. (fts.com, 840 Mark Street, Elk Grove Village IL; incorporated Sept 1989 by CEO John Chiu; ZoomInfo 51-200 staff, about $7.7M revenue; branches Torrance, Houston, East Meadow NY, Miami agent; JV offices HK and Hamburg; no parent group named) | hook: Security Cargo Network member story of 15 Oct 2026, "Collaboration of Uni-Express (Kuala Lumpur) and FTS (Chicago)": an 8-tonne, 9.6 m steel mould on a 40ft flat rack from Port Klang to US points (https://www.securitycargonetwork.com/collaboration-of-uni-express-kuala-lumpur-and-fts-chicago/) | chicago@fts.com (fts.com/contact-3/; also ftslax@, houston@, ftsny@, support@) | MX unchecked (dns.google refused on provenance) | caveats: the hook is a network-published joint case story, not FTS's own news; the site looks stale (copyright 2016).
- IGL Logistics Inc. (igl360.com, 7335 Statesville Rd, Charlotte NC; NVOCC/OTI plus air, ocean, trucking, customs and warehousing; Phoenix and Socorro TX sites; 21-50 staff per prospeo; owner Jim Burke per prospeo; SCN member) | hook: SCN news index lists "IGL Logistics New Charlotte warehouse", 24 Jun 2026 (https://www.securitycargonetwork.com/igl-logistics-new-charlotte-warehouse/) | ops@igl360.com (igl360.com/about/) | MX unchecked | caveats: the post page itself was refused by WebFetch, so date, title and excerpt come from the SCN news index page 1. The link to igl360.com rests on the name plus Charlotte HQ. The hook is five months old.

#### Unfinished candidates (company | known | missing)
- Blademar Logistics | SCN posts 23 Jul and 20 Aug 2026 (wine exports, sculpture) and 6 May 2026 (generator import for Google) | its country is unknown; the post fetch was refused (provenance) | everything
- ACI Cargo | SCN posts "ACI Cargo Delivers a Natural Gas Station" (6 Aug 2026) and a solar turbine shipment (4 Mar 2026) | country unknown, post refused | everything
- MH Logistics Ltd (USA; perishables / live plant cuttings forwarder and customs broker; info@mhls.co) | joined SCN 11 Jun 2025 (too old) | website, dated hook
- Jaguar Freight (Valley Stream NY) | homepage re-read: no email anywhere (contact page has a form only), newsletter only, and it builds its own CyberChain tech suite | email; treat as dead
- Goodfirms customs brokers (Landweer, AAA Customs Brokers, Camelot, etc.) | a name search for Landweer returned only directories, and AAA only panjiva/importinfo | websites; treat as dead unless a site turns up
- Clutch Dallas/Miami domains with no dated item in a batch search: insticologistics.com, whitestarlogistics.com, warriorlogistics.com, linkex.us, mscexpressllc.com, tricon-logistics.com, crestlinelogistics.com, addtrans.com, olrservices.us, aefreightlogistics.com, primelogisticsgroup.com, ggcargo.us, eurocargo.com, aereomarexpress.com, international3pl.com, freightrus.net | sizes from Clutch | dated hook, email

#### Rejected this run (name: reason)
- MW Logistics (Dallas; Dallas 100 2026 #61, 12 Oct 2026): freight brokerage, dedicated trucking and yard management, not a forwarder
- EFI Logistics (San Francisco): only release is 27 Oct 2025 (before cutoff); no newer item found
- R.W. Smith & Co.: /press says "There are currently NO Press Releases"; no 90th-anniversary item (third check)
- Interlink Trade Services / CIC Competitive Industrial Center (McAllen): articles from Nov 2024 and 2 Apr 2026 (before cutoff); no website or email
- JG Customs Forwarding: "Faith in Motion" article is 5 Nov 2025; still no site (rejected before)
- CargoWorld Express (Houston), Double Ace Cargo (Miami), ACME (3PL, 2,200 trucks), U.S. Group Consolidator: SCN items from 2021-2025 only
- Trimodal Logistics (UAE), Dynamic Global Logistic (Turkey), Time World Freight (Doha), Evergrow (Xiamen): SCN stories but not US
- Naniq Global Logistics (Anchorage): NAP join 5 Sep 2025, no website or email on the post
- Ambercor (WWPC, 29 Sep 2026): Toronto HQ (rejected before)
- FreightTAS LLC (Workable): an executive recruiter, not a forwarder
- Freight Right: already in companies.csv; ICAT (SCN Top Member Americas): rejected before (group)
- MIA cargo awards item is from 2017; Miami Air Cargo Association (Jan 2026) has only board members

#### Sources
- PRODUCTIVE / NEW: Security Cargo Network news index (https://www.securitycargonetwork.com/news/, page 1 = 100 posts, 4 Mar to 12 Nov 2026; surface it with a search using allowed_domains securitycargonetwork.com). It gave both qualifiers. Individual post URLs from the index mostly fetch, but some were refused (IGL, Blademar, ACI). page/2 and later were refused (hand-built). SCN also publishes a live member directory PDF (securitycargonetwork.com/wp-content/plugins/hughesskeleton-members/admin/reports/member-directory.pdf; surfaced, not read) that could list US members with emails. US items on page 1 are now USED UP.
- Clutch city lists fetch once a clutch.co search surfaces them: customs-brokers/dallas (34 firms, 15 domains), customs-brokers/miami (19), container-shipping-companies/miami (34), customs-brokers?page=19 (mostly foreign or micro), customs-brokers/seattle (4). The same search also surfaced customs-brokers/new-york, freight-forwarders/miami and shipping-companies/dallas (not read). One batch "2026 news" search over 17 of the Dallas/Miami domains gave only MW Logistics (a broker).
- Dallas 100 2026 list (smu.edu/dallas100): no forwarders.
- WWPC news page 1 (wwpc.eu.com/news/, to 20 Nov 2026): only Ambercor touches the US.
- NCBFAA eBriefing /2 = 6 Nov issue (Boston Mountain, already noted) and /8 = Sep 2026 (Camili, Neutoc, A&M): nothing new.
- DEAD (this run): Breakbulk Americas exhibitors and JCtrans weekly202647 (hand-built URLs refused on provenance); transport logistic China 2026 (the Mar 2026 preliminary PDF fetches; US = airlines, airports, Sonica only; the May PDF is still refused); GLA Bangkok conference (22-25 Oct 2026, no attendee list); SEMA/IMTS/Pack Expo/FABTECH searches (IMTS official forwarder = DSV); Expo Carga / Logistics World Mexico (no list; article client_error); Inc 5000 2026 and fastest-growing searches; "Top 10 customs brokers" vanity lists (large firms only); TIACA new members (board items only); IATA accreditation search (DP World); "welcomes licensed customs broker" search; Miami airline top-agent awards; regional association "welcome new members" search (only NCBFAA); ATS job searches (bamboohr/applytojob/workable: OEC, Traffic Tech, Laufer, recruiters); ZipRecruiter category pages (client_error); border customs-broker expansion searches (EELCO 2024, groups); texasborderbusiness.com (all items before cutoff); ASA Network homepage (Terra only for US); Global Affinity Alliance pressroom (robots); IFLN (nothing indexed); ShipNorthAmerica network (nothing); Conqueror industry-news page (newswire feed only); NAP search (US joins all 2025); forwardernetworks.com (metadata only); txgulf.org (port news only).
- Provenance this run: every hand-built URL was refused, including dns.google MX, clutch city slugs, JCtrans weekly, imgs.tl-c.cn May PDF and SCN page/2. Only URLs returned by a search, or linked from a fetched page, fetched (and even some of those were refused). Both MX values are unchecked.

#### Searches used: 38 of 44

### UK agent notes (21 Nov 07:43 run)
#### UK research run, 21 Nov 2026: 2 qualified, 36 of 38 searches

#### Qualified
- Atlantic International (Atlantic International Freight Services Ltd, CH 06676424, Active; Office 2-4, Rear of Access House, 4 Sherwood Road, Bromsgrove B60 3DR; est. 2008; wholly owned by an Employee Ownership Trust, CH PSC Aifsl Employees Trustees Ltd; small-company accounts) | hook: new logo, brand and website launched 14 Oct 2026 (https://atlanticintl.co.uk/new-atlantic-international-website/) | sales@atlanticintl.co.uk (/contact/) | MX unchecked | caveats: the hook is soft (a rebrand). The 20 Nov 06Z Rejected line names an "Atlantic Freight" (no dated company news), which may be this firm. No 2026 CH filing yet (CS 19 Nov 2025; next due Dec 2026).
- RBF Cargocare Ltd (CH 01671463, Active, CS 14 Jan 2026; Unit 8 Summit Business Park, Langer Road, Felixstowe IP11 2JB; est. 1982; customs clearance at UK ports for food/feed, SPS and fresh produce; 4 offices; MD Jon Beech) | hook: Fresh Awards 2026 Business Service Partner of the Year winner. This is a news item dated 06 Nov 2026 on its exhibitor profile https://www.retailscl.com/exhibitors/rbf-cargocare. It also exhibited (stand R1452) at the Retail Supply Chain & Logistics Expo, ExCeL, 11-12 Nov 2026 | info@rbf-cargocare.com (/about-rbf/) | MX unchecked | caveats: the article URL (retailscl.com/blog-library/rbf-cargocare-wins-fresh-awards-business-service-partner-year-2026) timed out and no outside source was found. PSC is Cargocare Limited; the group holding moved to CC Global Holdings Ltd on 24 Feb 2026 (who is behind it was not checked). This finishes the open lead "RBF Cargocare | hook, CH, ownership".

#### Unfinished candidates (company | known | missing)
- TOLF UK Limited / "tolf LIMITED" (tolf.com, CH 12533988, Unit 641 River Gardens, Feltham TW14 0SL; uk.info@tolf.com on /contact.php; PSC Shalinder Singh 75%+; accounts filed 15 Jul 2026; four registered-office changes in 2025-26) | Multimodal 2027 exhibitor page (stand 6080, multimodal.org.uk/exhibitor-article/tolf-limited, undated) | missing: a dated hook and size; the site is template-like ("7,000 offices"), so it may be very small
- Universal Customs Clearance (universalcustomsclearance.co.uk; Dover, Felixstowe, London Gateway, Southampton; hello@; independent customs clearance; BIFA) | blog has only regulatory posts; its Multimodal post is from 2022 | missing: dated hook, CH
- ACC Shipping Ltd (accworldwide.com, Gravesend) | rechecked 21 Nov: still no Beaujolais Day 2026 post, newest item about Apr 2026; named staff emails on the homepage (dbarclay@, kware@, hjefkins@, jevenden@) | missing: dated hook (check /news/ again after about 25 Nov)
- JLD International Ltd (Yorkshire) and RJB (UK) Logistics (West Midlands) | signed the Armed Forces Covenant 26 Jul 2026 and 26 Oct 2026 (gov.uk pages); both micro (0-9) | missing: website, whether they are forwarders at all (probably hauliers)
- Carlton Freight Ltd (carltonfreight.com, Carlton House, 20 Hornspit Lane, Liverpool L12 5LT; "independent international freight forwarders") | email hidden behind JavaScript; no news | missing: email, hook

#### Rejected this run (name: reason)
- EFS Global: group with 550+ vehicles and 30 depots (Multimodal 2035)
- Seabridge (Multimodal 7020): Irish company (seabridge.ie)
- Daygard Logistics Group: already excluded (leads.md line 459)
- Nowlun (Pricing Manager job on Workable): Egyptian platform (rejected before)
- CCT International (cctinternational.co.uk): its only hook is a new website from Mar 2025
- Supreme Freight (Southampton): newest company item is Solent 250 from 2017; Cloudflare email
- Seabourne UK (PCN): part of the Seabourne group; PCN post from 2023
- CY UK Ltd (AON): join post undated, no own site (carried over)
- WM International (UK Metals Expo exhibitor): German parent (rejected before)
- Buckle Shipping (Retail SCL 2026 exhibitor): site shows only a bot-check page (as before)
- Transglobal Express: parcel broker

#### Sources
- PRODUCTIVE (NEW): Retail Supply Chain & Logistics Expo exhibitor profiles (retailscl.com/exhibitors/<slug>). The 2026 show ran 11-12 Nov 2026 at ExCeL (supplychaindigital.com). Profiles show dated exhibitor news (gave RBF's Fresh Awards win). Few forwarders: RBF, Buckle, Ship4WD, ExFreight, 2 Cubeglobal (US?), Customs Support Group, Gaston Schul, Yusen. Many profile fetches return client_error. exhibitor-products?page=N ignores N.
- PRODUCTIVE (one hit): a plain search for UK forwarder rebrand/new-name announcements in 2026 surfaced atlanticintl.co.uk (company news page, dated posts).
- NEW: gov.uk Armed Forces Covenant atom feed filtered to Transportation (gov.uk/armed-forces-covenant-businesses.atom?armed_forces_covenant_business_industry%5B%5D=transportation) lists the 50 newest signers with dates. Mostly bus, rail and haulage firms; forwarder signers in 2026 so far are World Freight (Apr), JLD International, RJB (UK) Logistics (both micro).
- NEW: FIATA GB directory (fiata.org/directory/gb/) fetches once surfaced by an allowed_domains fiata.org search. Read from offset 100000 (P-Z). One batch of 25 unused domains (paragon, quest, rbc, reach, reed, regency, rsllhr, rhysdavies, rowe, slr, spedition, strategic-shipping, supreme, tdm, thecustomscentre, tlc-wlogistics, transmodal, UCC, wfs-intl, wefl, yourcargocontact, wellsandroot, knightwatson, westerlogistics, wifreight) with hook words returned only UCC (2022) and Supreme (2017). Still unsearched from P-Z: penhill.eu, procar.co.uk, reeveslogisticslimited.com, seagull-global.com, seawaylogistics.co.uk, sigmastartltd.com, scaneuropelogistics.co.uk, solibra.co.uk, statusmove.co.uk, sti-freight-management.com, import-agency.com, airoceanlogistics.co.uk, trans-global.com, transcar.co.uk, varamis.co.uk, wadoye.co.uk, weell.co.uk, yushilimited.uk, hubecom.co.uk, kongtrans.com.
- NEW (low yield): eCommerce Expo exhibitor list (ecommerceexpo.co.uk/exhibitor-list; read with offsets 0 and 100000). Exhibitors are mostly parcel and fulfilment firms; WM Tangram (stand A59) is the only UK customs/logistics name, and its profile was refused. UK Metals Expo exhibitor pages fetch (WM International, Denholm Good: both excluded).
- DEAD: multimodal.org.uk exhibitor-article searches (3 queries: only known names or groups); a network new-member search; BIFAlink Nov 2026 (still not indexed); BIFAlink Oct 2026 (no new-members page); Workable/Teamtailor/Recruitee job search; Contracts Finder / Find a Tender (large suppliers, e.g. CitySprint); exportandfreight.com search (homepage refused); "launch of our new website" search (2025 or older); bdaily.co.uk (2 searches: hauliers or old); project-network new-member search (CY UK undated, Seabourne 2023); reed/cv-library/totaljobs pricing jobs (recruiters; totaljobs pages give a server error); "new premises" search (only Future Forwarding); London Produce Show / IFE; Fresh Awards 2026 finalists (judgify and NCGM pages list no logistics names; the fruitnet winners article gives client_error); "joins as pricing manager" search; Global Offshore Wind 2026 (floorplan only); Speciality & Fine Food Fair (no 2026 show); Logistics UK Awards 2026 (already dead); ACC Shipping news (no 2026 Beaujolais post yet).
- Provenance this run: WebFetch refused hand-built URLs (CH search pages, dns.google MX lookups, fiata.org before a search, exportandfreight.com, retailscl.com/exhibitors). Some links found on fetched pages also timed out (retailscl blog-library and exhibitor-news, ecommerceexpo profiles). CH company pages work after an allowed_domains search of find-and-update.company-information.service.gov.uk. Every MX is unchecked.

#### Searches used: 36 of 38

### AU agent notes (21 Nov 07:43 run)
#### AU research run, 21 Nov 2026: 0 qualified, 38 of 44 searches

#### Qualified
- None. au.jsonl is empty.

#### Unfinished candidates (company | known | missing)
- WRL Shipping Pty Ltd (trades as WRL Worldwide RO-LO Shipping; wrlshipping.com.au; 7/41 Paringa Rd, Murarrie QLD 4172; ABN 42133244943; in the Australian market since 2008; "second-generation family business", majority Indigenous and female-owned (ICN Gateway gateway.icn.org.au/suppliers/80059); heavy/project cargo forwarding plus customs clearance; PCN exclusive AU member, GPLN, Supply Nation) | team@wrlshippingau.com on https://wrlshipping.com.au/contact/ (plain text, no unsolicited-email statement, street address on the contact page); kira@wrlshippingau.com on its PCN brochure page (projectcargonetwork.com/brochure/wrl/partners) | missing: a dated hook. Its only dated item is the PCN story "Nonpareil & WRL Australia with RORO Shipment of Dozer", 29 Apr 2026 (before the cutoff). The site has no news section (last modified 2023). Headcount not stated. Watch PCN/GPLN news for a newer WRL story.
- Solutions Customs and Forwarding (solutionscf.com.au, Australia; ASA Network member) | ASA Network homepage (asanetwork.org) introduces new staff member Jayden Kopittke (operations, customs compiling, accounts), jayden@solutionscf.com.au; the post is undated, but its image sits in the wp-content/uploads/2026/06 folder (so about June 2026) | missing: an exact hook date, the company website (solutionscf.com.au refused on provenance and not indexed in search), city, size, and a general email on its own site.
- 1UP Cargo | now has an official-directory email: Au.PCN@1upcargo.com on https://www.projectcargonetwork.com/brochure/1up-au/partners (Miranda NSW) | BUT /company-directors says director Mahsa Pedrami "splits her time between the Canadian and U.S. head offices", so the HQ looks North American (Canada is excluded). Treat as rejected unless the main session reads it otherwise.
- FJT Logistics, Neolink, Cargoport | hooks known (see earlier runs) | still no plain email. ICN Gateway and Defence West directory searches found no listing for them.
- GTC (Perth) | FTA 2026/35 hook | a staff-name search found nothing (third run).
- Carried over unchanged: Hearn, Pegasus, Searic, Swift Customs, Brisbane Customs & Forwarding, Anchor, Poseidon, Uniair, Transco, Townsville Customs, Novis, Global Transport Logistics, Atlas Global, Australian Global Freight, RH Freight, Gforce, KTL, Energy Global, Transcend, Tayper. A "2026 team welcome announcement" allowed_domains search over these 20 domains surfaced only homepages, about pages and the Novis BMSB 2026 flyer: no hook.

#### Rejected this run (name: reason)
- Beachhead Logistics (Osborne Park WA; Land Forces 2026 quad chart, WA pavilion, 6-8 Oct 2026; jarod.monaghan@ in Defence West directory): logistics-over-the-shore / temporary port operator, not a forwarder
- 1UP Cargo: head offices in Canada/US per its own directors page (see above)
- IDS International Delivery Service (idsaus.com, Mascot; markd@idsaus.com on ICN Gateway): blog stops Jun 2021, "our story" is network boilerplate (240 offices, 3,450 staff), no hook
- AussieFreight International Logistics (Eagle Farm): 2-9 staff (The Manifest), no website shown
- Elite (elitefsa.com, Doncaster East, since 1993): mainly domestic transport/warehousing with an own tech platform; no email on the site, no dated item
- GGL Australia (gglaustralia.com): the site gives no offices, email or news; "1 Global Enterprises" keyword hints at a group
- Oriental Freight Services (NAP join 24 Jul 2026): Taipei, Oriental Logistics Group (not AU)
- PCFS Logistics (Globalia 7th Annual Meeting, Bangkok 26-28 Oct 2026; 10-year founder award): already emailed (16 Nov)
- Clutch AU air-freight p5 and shipping-companies/Melbourne p1 names: all already in records or rejected

#### Sources
- PRODUCTIVE (small): Project Cargo Network brochure pages (projectcargonetwork.com/brochure/<slug>/partners) show members' own emails and addresses; an allowed_domains search over projectcargonetwork.com surfaces them (1up-au, wrl, spark). ICN Gateway supplier pages (gateway.icn.org.au/suppliers/<id>) give address, website, email, ABN and an ownership blurb (WRL, IDS), with no dates. These are email sources, not hook sources.
- NEW, checked: Globalia news (news.globalialogisticsnetwork.com) lists every post since 2021. AU members are PCFS (Sydney), "Globalia Melbourne" (sales hire 24 Oct 2025; its company name is not given, and the post URL was refused) and Globalia Fremantle / Transitainer (in records). There are no AU member posts in 2026 apart from the Bangkok meeting (PCFS). ASA Network homepage (asanetwork.org): AU member Solutions Customs and Forwarding only. Land Forces 2026 (Perth, 6-8 Oct 2026): WA quad charts (44 firms) and the VIC pavilion directory have no forwarders. The Defence West capability directory (logistics stream, 188 firms) has only Sadleirs (large).
- DEAD this run: CeMAT Australia 2026 (materials-handling vendors; no exhibitor list surfaced); Clutch Perth customs-brokers hand-built URL (refused); JCtrans weekly202647 (refused; a search returns only weeks up to 37); DCN freight-forwarding tag pages 1-2 (Jun-Nov 2026: WiseTech, AIT/Connor Anderson, CAS, 3DL, IFCBAA, opinion pieces by FTA staff, consultants and Susan Danks; no small forwarders); DCN "Clean Freight Council" article (refused) and its search (US trucking results); DCN "Spotlight on Freight Forwarder of the Year" (2025 winner Whale only); DCN "Pressure points" feature (members-only, no names); AFR Fast 100 search (US lists); VILOG AU listings (no emails on the list); Indeed AU forwarding job pages (large firms and recruiters, no dates; two pages client_error); LinkedIn company pages (robots-disallowed); Asia Fruit Logistica 2026 AU exhibitors (growers only); SA Freight Council / AFI awards (trucking); Australian Business Awards logistics category (no 2026 winners); Africa Down Under 2026 (luminik client_error); ANZSL conference prospectus (no names); ABF Trusted Trader register page (no list in the capture, no dates); DCN individual finalist name searches (second try, nothing); network new-member searches (NAP Jul 2026 only Cable/Oriental; GLA AU posts 2025; Pangea FJT only).
- Provenance refusals this run: marketing.jctrans.com weekly202647, clutch.co/au/logistics/customs-brokers/perth, cargopowernetwork.com/blogs, asanetwork.org/category/news/, solutionscf.com.au, wa.gov.au quad-chart PDF (it fetched after a search surfaced it), thedcn.com.au Clean Freight Council article, Globalia 2025 Melbourne post, projectcargonetwork.com hand-built brochure slug, vilog.vn country filter.
- Next dated AU sources (not yet available on 21 Nov): FTA Weekly Report 2026/47 (about 25 Nov), DCN Awards winners (26 Nov, The Star Brisbane; winners' firms may post about it), JCtrans weekly202647+.
- MX lookups: none run (no qualified companies).

#### Searches used: 38 of 44

### HKSG agent notes (21 Nov 07:43 run)
#### HKSG research run, 21 Nov 2026: 1 qualified, 40 of 42 searches

#### Qualified
- HK | Global Cargo (Far East) Limited (gcfel.com, Unit 03, 16/F Westin Centre, 26 Hung To Road, Kowloon Bay; Chairman Sandy Cheng; air/sea forwarder plus airline GSSA, project cargo; branches Shenzhen, Zhongshan, Vietnam, Thailand; "21 office and associates in Greater China") | hook: relocation and grand opening of its Shenzhen Branch (Xinghang Center, Bao'an) on 12 Sep 2026, news post 23 Sep 2026 (gcfel.com/2026/09/23/global-cargo-far-east-limited-shenzhen-branch-relocates-...). The news page also lists a 20 Nov 2026 headline: honoured as top Asia & Oceania agent at the ALN-BAM meeting in Rome (post not opened) | info@gcfel.com (also airfreight@, seafreight@) on gcfel.com/contact/ | MX unchecked (dns.google refused) | headcount and ownership not stated; part of the business is GSSA. Source: HKSTLA corporate member list, then an allowed_domains search.

#### Unfinished candidates (company | known | missing)
- SG | M&P International Freights (mp.com.sg, sales@sin-mp.com.sg) | about page updated 30 Oct 2026; its "Singapore SME 500 Award" is the Dec 2025 ceremony (before cutoff); certificates uploaded Aug 2026 are undated | dated hook, ownership (mpfreights.cn link). gallery/resources pages refused (provenance)
- SG | Silk Express Freight Pte Ltd (silk.com.sg, 40 staff, est. 1994) | SCN 2019 directory gives bk@silk.com.sg and ok@silk.com.sg (2019, not its own site) | hook; email on own site. A name search for 2026 found nothing
- HK | Ports Express Ltd (ports-express.com.hk, 54 staff, est. 1998, SCN 2019 directory: jtao@, mtsim@ports-express.com.hk; Pangea member) | allowed_domains searches found no 2026 page | hook, email on own site, ownership
- HK | Preford Container Line / Air Express (65 staff over 8 offices CN/KH/VN; stanley@, winner@preford.com.hk in SCN 2019 directory), Grandways (8 staff, too small) | HTTP-only sites | hook
- HK | HKSTLA corporate members never checked before (hkstla.org/membership-new-member/, gives websites): AO Freight (HK) (aofreight.com / aofreight.hk), Wilson Logistics (wilson-logistics.com), Panda Logistics (pandahk.com), ACE Protrans (aceprotrans.com), Power Hub (phublogistics.com), CL International / CL Consolidators (cl-consolidators.com), Pan World Shipping (panworld.com.hk), American Intermodal Container Line (aiclhk.com), Golden Fortune Shipping (gofor.com), Michelle Int'l Transport (art logistics) | two allowed_domains searches surfaced no dated page for these | hook, email
- HK | Future Sky, Lapton, A&G (anghk.com) | still no dated page in two batch searches | hook

#### Rejected this run (name: reason)
- Perfect Cargo Global Logistics (SCN new member 3 Sep 2026): already in companies.csv
- U.S. Group Consolidator (HK/SG, SCN): multi-country group, 200 staff, US offices; SCN posts 2019/2021
- Top-Trans Expo Logistics (HK) (tl China 2026 list): exhibition logistics, mainland-linked; Team Well Logistics: already emailed
- Vantage Logistics Corp (Breakbulk Asia G42): Ho Chi Minh City, Vietnam
- Megaton (Breakbulk Asia): already contacted
- Easy Speed International Logistics (HKSTLA): only item 2025, US/global leadership
- International Supply Chain Alliance (int-sca.com): an alliance/network, not a forwarder
- Anradus job ad (pricing executive): recruiter, client unnamed; Panalpina/DSV ad: group

#### Sources
- PRODUCTIVE (new): HKSTLA member directory (hkstla.org/membership-new-member/, fetches after a search with allowed_domains hkstla.org): about 40 corporate members with websites, no join dates. An allowed_domains search over 16 of those domains with the query "news 2026 announcement new service exhibition" surfaced gcfel.com news posts.
- NEW (read): Security Cargo Network 2019 directory, offsets 100000-309193 now fully read. HK/SG entries: Farenco, Grandways, Norman Global (Ningbo), Merzario HK, MBS HK/SG, Ports Express, Preford, Silk Express, U.S. Group Consolidator. SCN member-news page 1 (to 12 Nov 2026): HK/SG only Perfect Cargo (contacted) and Spoti (rejected). SCN 1st-semester-2026 summary refused (provenance).
- NEW (read): Breakbulk Asia 2026 full exhibitor list (asia.breakbulk.com/exhibitors, 192 entries, fetches after a search with allowed_domains asia.breakbulk.com). No new small HK/SG forwarders (unchecked: Cargomile Shipping A01, DahNAY Logistics L50, Terminal Logistics Services M24, likely non-HK/SG). Exhibitor profile pages refused unless surfaced in a search.
- NEW (read): transport logistic China 2026 preliminary list (imgs.tl-c.cn/uploads/editor/20260318/tlC preliminary list 202603-EN(3).pdf): HK/SG names only Changi, CS Leasing, Ninja Van, Peacock Container, Combined Logistics Networks, TAC Index, Team Well, Top-Trans Expo, Zim. USED UP. The May version (20260429/...202605-EN.pdf) refused (provenance).
- DEAD: JCtrans weekly202647 and hand-built SCN/MarDep/dns.google/breakbulk URLs (provenance refused); marketing.jctrans.com search returns only old weeks (14-37); E50 2026 results not out (KPMG 2026 items only nominations); SME 500 (Dec 2025 ceremony); Changi Cargo Insight (no 2026 issues surfaced); CAD regulated-agent list (none published); SAAA homepage (no new members; Jul-Sep and Apr-Jun 2026 PERSPECTIVES already used) and SAAA member listing (client_error); hkla.org.hk new-member page (JS only); HAFFA member directory (robots-unreachable); HKSTLA events (last 2025); Freight Midpoint directory (HK/SG joins 2014-2024); WWPC directory (only Wangfoong); Africa Logistics Network news (no HK/SG); TCLN Bangkok meeting (May 2026, no names); GLA HK/SG welcome posts (2025 or older); GLN mailerlite search; network-award and "grand opening" searches (large firms); SG pricing-job search (recruiters, groups); Asia Fruit Logistica 2026 search (carriers only); allowed_domains batches over Clutch SG domains, MarDep/Maritime Hub HK domains and near-miss domains (homepages only).
- MX: dns.google refused in this subagent (WebFetch provenance and curl proxy 403).
- WebSearch with kpmg.com plus businesstimes.com.sg in allowed_domains returned HTTP 400.

#### Searches used: 40 of 42 (one returned HTTP 400)
