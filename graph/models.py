# import json
# from requests import get
# from urllib import request
#
# from flatten_dict import flatten
#
# okyanus = {"id": "אוקיינוס",
#            "type": "mainos",
#            "children": [
#                {
#                    "id": "רשתות חברתיות",
#                    "collapsed": "true",
#                    "children": [
#                        {
#                            "id": "Facebook",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "FB Lookup ID", "link": "https://lookup-id.com/", "info": "קבלת מזהה משם משתמש"},
#                                {"id": "Facebook Video Downloader", "link": "https://fbdown.net/",
#                                 "info": "הורדת סרטונים מפייסבוק"},
#                                {"id": "Ad Library",
#                                 "link": "https://www.facebook.com/ads/library/?active_status=all&ad_type=political_and_issue_ads&country=IL&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped",
#                                 "info": "חיפוש פרסומות בפייסבוק"},
#                                {"id": "Facebook Geo Pages", "link": "https://www.osintcombine.com/facebook-geo-pages",
#                                 "info": "חיפוש דפים לפי נ.צ ורדיוס"}
#                            ]
#                        },
#                        {
#                            "id": "Instagram",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "Pici Go", "link": "https://picigo.com/",
#                                 "info": "חיפוש לפי משתמשים ותגיות, אפשרות צפייה והורדה של Stories וסטטיסיקה לגבי משתמשים"},
#                                {"id": "Explore Locations", "link": "https://www.instagram.com/explore/locations",
#                                 "info": "אינדקס מיקומים של אינסטגרם - ניתן לראות תמונות שתויגו במקום"},
#                                {"id": "Yooing", "link": "https://www.yooying.com/",
#                                 "info": "חיפוש משתמשים ותגיות, הורדת תמונות וסרטונים"},
#                                {"id": "Search my bio", "link": "https://www.searchmy.bio/",
#                                 "info": "חיפוש בBio של כל המשתמשים הציבוריים"},
#                                {"id": "Osintcombine - Insta",
#                                 "link": "https://www.osintcombine.com/instagram-explorer/",
#                                 "info": "חיפוש תמונות לפי תאריך ותיוג למקום"},
#                                {"id": "Searchusers", "link": "https://searchusers.com/",
#                                 "info": "חיפוש משתמשים, הצגת כל התמונות של המשתמש (אם המשתמש לא נעול) ועוד"},
#                                {"id": "Downloadgram", "link": "https://downloadgram.com/",
#                                 "info": "הורדה של תמונות וסרטונים באינסטגרם - יש צורך בקישור של של הפוסט"},
#                                {"id": "Imginn", "link": "https://imginn.com/",
#                                 "info": "צפייה בפרופילים, תגיות, ואפשרות הורדה של Stories"},
#                                {"id": "izuum", "link": "https://izuum.com/",
#                                 "info": "אפשרות לקבל תמונת פרופיל ברזולוציה גבוהה, גם אם הפרופיל סגור"}
#                            ]
#                        },
#                        {
#                            "id": "Twitter",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "Twitter Date Search ",
#                                 "link": "https://twitter.com/search?q=SearchTerm%20since:2016-03-01%20until:2016-03-02",
#                                 "info": "חיפוש ציוצים לפי תאריך ציוץ"},
#                                {"id": "Twitter User Directory", "link": "https://twitter.com/i/directory/profiles/",
#                                 "info": "ספריית פרופילים, מסודרת לפי אותיות"},
#                                {"id": "First Tweet", "link": "http://ctrlq.org/first/",
#                                 "info": "כלי ניתוח לטוויטר, חיפוש בזמן אמת של ציוצים וטרנדים  (יש צורך בחשבון של טוויטר)"},
#                                {"id": "Twitterfall", "link": "https://twitterfall.com/",
#                                 "info": "כלי ניתוח לטוויטר, חיפוש בזמן אמת של ציוצים וטרנדים  (יש צורך בחשבון של טוויטר)"},
#                                {"id": "Profile Search", "link": "https://followerwonk.com/bio/?q=zero%20day&l=us",
#                                 "info": "חיפוש מילות תוכן בפרופילים באופן כללי, אפשר לחפש גם לפי מיקום, שם, וכתובת URL"},
#                                {"id": "Twoogel Search Engine", "link": "http://twoogel.com/",
#                                 "info": "מנוע חיפוש מותאם לגוגל - מחפש תוצאות רק ברשת טוויטר"},
#                                {"id": "Followerwonk Analyze", "link": "https://followerwonk.com/analyze",
#                                 "info": "סטטיסטיקות אודות משתמשים וטרנדים"},
#                                {"id": "Twitter Analytics", "link": "https://foller.me/",
#                                 "info": "סטטיסיקה אודות משתמש"},
#                                {"id": "Mentionmapp Analytics", "link": "https://mentionmapp.com/",
#                                 "info": "מציאת קשרים בין פרופילים ברשת הטוויטר - מוגבל ל300 חיפושים בחודש (יש צורך בחשבון של טוויטר)"},
#                                {"id": "Sleeping Time", "link": "https://socialbearing.com/",
#                                 "info": "בדיקת זמני הדדמה של פרופיל טוויטר  (יש צורך בחשבון של טוויטר)"},
#                                {"id": "Trendsmap", "link": "https://www.trendsmap.com/",
#                                 "info": "מפת טרנדים לפי איזור גיאוגרפי"},
#                                {"id": "Tinfoleak", "link": "https://tinfoleak.com/",
#                                 "info": "יוצר דוח מפורט אודות משתמש - יש צורך בכתובת מייל (יש לברר לגבי רישום כתובת IP)"},
#                                {"id": "Tweets Map ", "link": "https://www.omnisci.com/demos/tweetmap",
#                                 "info": "מפת ציוצים לפי איזור, שפה, ותגיות"},
#                                {"id": "One Million Tweet Map ", "link": "https://onemilliontweetmap.com/",
#                                 "info": "מפת ציוצים של ה24 שעות האחרונות, לפי איזור וסיווג הפוסט האם הוא חיובי, שלילי או ניטרלי"},
#                                {"id": "Burrrd – Twitter Account Analytics ", "link": "https://burrrd.com/",
#                                 "info": "סטטיסיקה אודות משתמש"},
#                                {"id": "Get Twitter ID ", "link": "https://commentpicker.com",
#                                 "info": "קבלת מזהה משם משתמש"},
#                                {"id": "Twitter Audit – Real Followers", "link": "https://www.twitteraudit.com/",
#                                 "info": "בודק את הסבירות לאמינות המשתמש (מוגבל לחיפוש אחד לפי כתובת IP)"}
#                            ]
#                        },
#                        {
#                            "id": "Tiktok",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "TiktokOff", "link": "https://tiktokoff.com/en",
#                                 "info": "הורדת סרטונים על ידי לינק"},
#                                {"id": "Osintcombine - Tiktok",
#                                 "link": "https://www.osintcombine.com/tiktok-quick-search",
#                                 "info": " חיפוש משתמשים ותגיות וצפייה בפרטים אודות המשמתמש"},
#                                {"id": "Find TikTok User ID",
#                                 "link": "https://www.instafollowers.co/find-tiktok-user-id",
#                                 "info": "הוצאת מזהה משם המשתמש"}
#                            ]
#                        },
#                        {
#                            "id": "Telegram",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "Buzz", "link": "https://search.buzz.im/", "info": "חיפוש הודעות בקבוצות פתוחות"},
#                                {"id": "Telegram Channels", "link": "https://telegramchannels.me/",
#                                 "info": "חיפוש ערוצים, קבוצות ובוטים"},
#                                {"id": "Channels", "link": "https://tlgrm.eu/channels",
#                                 "info": "אינדקס ערוצים לפי קטגוריות"},
#                                {"id": "Xtea", "link": "https://xtea.io/ts_en.html",
#                                 "info": "חיפוש ערוצים, קבוצות ובוטים"},
#                                {"id": "Telegram Analytics", "link": "https://tgstat.ru/en/search",
#                                 "info": "חיפוש מתקדם בטלגרם"},
#                                {"id": "Telegago",
#                                 "link": "https://cse.google.com/cse?cx=006368593537057042503:efxu7xprihg#gsc.tab=0",
#                                 "info": "חיפוש בערוצים, קבוצות, בוטים ובפרטי המשתמש"}
#                            ]
#                        },
#                        {
#                            "id": "Snapchat",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "Snapchat Map", "link": "https://map.snapchat.com/",
#                                 "info": "מפת סטורי לפי מיקום"},
#                                {"id": "Snapchat Story", "link": "https://story.snapchat.com/",
#                                 "info": "חיפוש משתמשים וצפייה בסטורי -ניתן גם לצפות בסטורי של משתמש מסויים על ידי הוספת /s/username ללינק"}
#                            ]
#                        },
#
#                        {
#                            "id": "Linkedin",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "LinkedIn Xray Search", "link": "https://recruitmentgeek.com/tools/linkedin",
#                                 "info": "חיפוש לפי כישורים או מיקום"}
#
#                            ]
#                        },
#                        {
#                            "id": "VKontakte",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "Snradar", "link": "http://snradar.azurewebsites.net/",
#                                 "info": "מציאת תמונות שצולמו לפי מיקום ותאריך"},
#                                {"id": "vk communities", "link": "https://vk.com/communities",
#                                 "info": "חיפוש קהילות ברשת VK"},
#                                {"id": "vk peoples", "link": "https://vk.com/people", "info": "חיפוש משתמשים ברשת VK"}
#
#                            ]
#                        },
#                        {
#                            "id": "Youtube",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "Extract Metadata", "link": "https://citizenevidence.amnestyusa.org/",
#                                 "info": "הצגת מידע על סרטון, כולל אפשרות חיפוש של קטעי תמונה מהוידאו באינטרנט"},
#                                {"id": "Yout", "link": "https://yout.com/",
#                                 "info": "הורדת סרטונים בפורמט אודיו או וידיאו, ואפשרות חיתוך לפי מקטע"},
#                                {"id": "Watchframebyframe", "link": "http://www.watchframebyframe.com/",
#                                 "info": "מאפשר צפייה בסרטון בהילוך איטי"},
#                                {"id": "Savefrom", "link": "https://en.savefrom.net/18/",
#                                 "info": "הורדת סרטונים מפלטורמות שונות"}
#                            ]
#                        },
#                        {
#                            "id": "Pinterest",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "Expert PHP",
#                                 "link": "https://www.expertsphp.com/pinterest-photo-downloader.html",
#                                 "info": "הורדת אלבומים"},
#                                {"id": "Pingroupie", "link": "https://pingroupie.com/", "info": "חיפוש קבוצות"}
#                            ]
#                        },
#                        {
#                            "id": "Github",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "Coderstats", "link": "https://coderstats.net/", "info": "חיפוש משתמשים"},
#                                {"id": "Github Id", "link": "https://caius.github.io/github_id/",
#                                 "info": "מציאת ID לפי שם משתמש"},
#                                {"id": "Awesome Lists", "link": "http://awesomelists.top/",
#                                 "info": "רשימות של מקורות לפי קטגוריה"}
#                            ]
#                        },
#                        {
#                            "id": "רשתות חברתיות נוספות",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "Tumblr", "link": "https://tumblr.com"},
#                                {"id": "Discord", "link": "http://www.discord.com/"},
#                                {"id": "Ok.ru", "link": "https://ok.ru"},
#                                {"id": "Quora", "link": "https://quora.com"},
#                                {
#                                    "id": "Twitch",
#                                    "collapsed": "true",
#                                    "children": [
#                                        {"id": "Twitch Website", "link": "https://www.twitch.tv/"},
#                                        {"id": "Twitch Tracker", "link": "https://twitchtracker.com/",
#                                         "info": "חיפוש משתמשים וערוצים"}
#                                    ]
#                                }
#                            ]
#                        }
#                    ]
#                },
#
#                {
#                    "id": "דואר אלקטרוני",
#                    "collapsed": "true",
#                    "children": [
#                        {
#                            "id": "פורנזיקה",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "Email Dossier", "link": "https://centralops.net/co/emaildossier.aspx",
#                                 "info": "תחקור כתובת מייל"},
#                                {"id": "Email Header Analysis",
#                                 "link": "https://www.iptrackeronline.com/email-header-analysis.php",
#                                 "info": "בדיקת Header של כתובת מייל"},
#                                {"id": "Mxtoolbox", "link": "https://mxtoolbox.com/",
#                                 "info": "בדיקת כתובת MX של כתובת מייל"}
#                            ]
#                        },
#                        {
#                            "id": "חיפוש",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "Hunter", "link": "https://hunter.io/",
#                                 "info": "חיפוש כתובות מייל נוספות הקשורות לדומיין"},
#                                {"id": "Haveibeenpwned", "link": "https://haveibeenpwned.com/",
#                                 "info": "בדיקה האם כתובת המייל נמצאת במאגרים של חשבונות פרוצים"},
#                                {"id": "EmailHippo", "link": "https://tools.verifyemailaddress.io/",
#                                 "info": "חיפוש כתובות מייל נוספות הקשורות לדומיין"},
#                                {"id": "Emailrep", "link": "https://emailrep.io/",
#                                 "info": "חיפוש כתובות מייל נוספות הקשורות לדומיין"}
#                            ]
#                        },
#                        {
#                            "id": "Gmail",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "Epieos", "link": "https://tools.epieos.com/google-account.php",
#                                 "info": "מחזיר פרטים לגבי משתמש גוגל"}
#                            ]
#                        }
#                    ]
#                },
#
#                {
#                    "id": "ניתוח כתובות IP ודומיין",
#                    "collapsed": "true",
#                    "children": [
#                        {
#                            "id": "כתובות דומיין",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "DomainTools", "link": "https://whois.domaintools.com/",
#                                 "info": "בדיקת רישום דומיין"},
#                                {"id": "crt.sh", "link": "https://crt.sh/?q=",
#                                 "info": "תחקור תעודות SSL - ניתן לתחקר דומיין או כתובת Hash"},
#                                {"id": "Similarweb", "link": "https://www.similarweb.com/",
#                                 "info": "בדיקת פופלריות של דומיין"},
#                                {"id": "Bulk whois lookup",
#                                 "link": "https://whois.whoisxmlapi.com/bulk-whois-lookup/?mc=circled",
#                                 "info": "תחקור של עד 500 דומיינים בשאילתה אחת"},
#                                {"id": "Leads Finder Online", "link": "https://omail.io/leads/",
#                                 "info": "הוצאת כתובות מייל וטלפונים מדומיינים"},
#                                {
#                                    "id": "סאב דומיין",
#                                    "collapsed": "true",
#                                    "children": [
#                                        {"id": "Dnsdumpster", "link": "https://dnsdumpster.com/",
#                                         "info": "חיפוש רקורסיבי של רשומות DNS"},
#                                        {"id": "Pentest tools - Subdomains",
#                                         "link": "https://pentest-tools.com/information-gathering/find-subdomains-of-domain#",
#                                         "info": "סריקת סאב דומיינים אפשריים לכתובת דומיין"}
#                                    ]
#                                }
#                            ]
#                        },
#                        {
#                            "id": "כתובות IP",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "IPinfo", "link": "https://ipinfo.io/", "info": "מספק מידע אודות כתובת IP"},
#                                {"id": "IPdata", "link": "https://ipdata.co/?ref=iplocation",
#                                 "info": " מידע מפורט אודות כתובת IP"},
#                                {"id": "FireHOL IP Lists", "link": "http://iplists.firehol.org/",
#                                 "info": "מאגר דיווחים אודות כתובות IP"}
#                            ]
#                        },
#                        {
#                            "id": "IP + דומיין",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "Censys", "link": "https://censys.io/ipv4",
#                                 "info": "חקירה מעמיקה של דומיינים וכתובות IP"},
#                                {"id": "Shodan", "link": "https://www.shodan.io/",
#                                 "info": "חקירה מעמיקה של דומיינים וכתובות IP"},
#                                {"id": "Zoomeye", "link": "https://www.zoomeye.org/",
#                                 "info": "מנוע חיפוש מתקדם לכתובות IP ודומיינים"},
#                                {"id": "Threatcrowd", "link": "https://www.threatcrowd.org/",
#                                 "info": "תחקור וויזאולי של כתובות דומיין וIP"},
#                                {"id": "Spyse", "link": "https://spyse.com/tools/ip-lookup",
#                                 "info": "מספק אודות כתובת IP - פורטים, דומיינים קשורים לכתובת, תעודות SSL, שרתי DNS - יש צורך בהרשמה על מנת לקבל את כל המידע"},
#                                {"id": "Urlscan", "link": "https://urlscan.io/search/#*",
#                                 "info": "מידע נרחב אודות כתובת IP וכתובות הדומיין המקושרות לכתובת"},
#                                {"id": "Onyphe", "link": "https://www.onyphe.io/",
#                                 "info": "בדיקת IP מול מאגרי כתובות IP המקושרות לשימוש לא חוקי"},
#                                {"id": "Packet Total", "link": "https://www.packettotal.com/",
#                                 "info": "מאגר קבצי pcapp - אפשרות חיפוש כתובת IP / דומיין בקבצי הלוג"},
#                                {"id": "IPVOID", "link": "https://www.ipvoid.com/",
#                                 "info": "מאגר לבדיקת כתובת IP בכלים שונים"},
#                                {"id": "IP2Location", "link": "https://www.ip2location.com/demo",
#                                 "info": "מספק מידע אודות כתובת IP"},
#                                {"id": "Central Ops", "link": "https://centralops.net/co/",
#                                 "info": "חקירת כתובות IP או דומיינים"}
#                            ]
#                        }
#                    ]
#                },
#
#                {
#                    "id": "פורנזיקה דיגיטאלית",
#                    "collapsed": "true",
#                    "children": [
#                        {
#                            "id": "ניתוח תמונה",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "Fotoforensics", "link": "http://fotoforensics.com/",
#                                 "info": "אנאליזה של קובץ תמונה"},
#                                {"id": "Photo-forensics", "link": "https://29a.ch/photo-forensics/#forensic-magnifier",
#                                 "info": "אנאליזה מתקדמת של קובץ תמונה"}
#
#                            ]
#                        },
#                        {
#                            "id": "ניתוח וידאו",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "Extractmetadata", "link": "http://www.extractmetadata.com/",
#                                 "info": "ניתוח וידאו"},
#                                {"id": "MediaInfo", "link": "https://mediaarea.net/en/MediaInfo", "info": "ניתוח וידאו"},
#                                {"id": "Youtube-metadata", "link": "https://mattw.io/youtube-metadata",
#                                 "info": "ניתוח וידאו ביוטיוב"}
#
#                            ]
#                        },
#                        {
#                            "id": "שמירה ותיעוד אתרים",
#                            "collapsed": "true",
#                            "children": [
#
#                            ]
#                        },
#
#                        {"id": "Unfurl", "link": "https://dfir.blog/unfurl/", "info": "ניתוח כתובת אינטרנט"},
#                        {"id": "Ddownr", "link": "https://ddownr.com/", "info": "הורדת וידאו מיוטיוב"},
#                        {"id": "Twitter video downloader", "link": "https://botdownloader.com/twitter-video-downloader",
#                         "info": "הורדת וידאו מטוויטר"},
#                        {"id": "Facebook video downloader",
#                         "link": "https://botdownloader.com/facebook-video-downloader",
#                         "info": "הורדת וידאו מפייסבוק"},
#                        {"id": "Tiktok video downloader",
#                         "link": "https://www.expertsphp.com/tiktok-video-downloader.html",
#                         "info": "הורדת וידאו מטיק טוק"}
#                    ]
#                },
#
#                {
#                    "id": "שם משתמש",
#                    "collapsed": "true",
#                    "children": [
#                        {"id": "knowem", "link": "https://knowem.com/",
#                         "info": "בודק זמינות לשמות משתמשים, דומיין וסימון מסחרי וחיפוש שמות משתמשים ב- 500 רשתות חברתיות"},
#                        {"id": "Checkusernames", "link": "https://checkusernames.com/",
#                         "info": "חיפוש שם משתמש ב300 רשתות חברתיות"},
#                        {"id": "Namechk", "link": "https://namechk.com/",
#                         "info": "חיפוש שם משתמש ברשתות חברתיות מובילות"},
#                        {"id": "namecheckup", "link": "https://namecheckup.com/", "info": "בודק זמינות לשמות משתמשים"},
#                        {"id": "namecheckr", "link": "https://www.namecheckr.com/",
#                         "info": "בודק זמינות דומיין ושם משתמש חברתי במספר רשתות"},
#                        {"id": "usersearch", "link": "https://usersearch.org/",
#                         "info": "בודק זמינות לשמות משתמשים כולל אפשרות לצפייה בפרופיל"},
#                        {"id": "Whatsmyname", "link": "https://whatsmyname.app/", "info": "חיפוש מקיף של שם משתמש"},
#                        {"id": "instantusername", "link": "https://instantusername.com/",
#                         "info": "בודק זמינות מהיר לשמות משתמשים"}
#                    ]
#                },
#
#                {
#                    "id": "אתרי הכרויות",
#                    "collapsed": "true",
#                    "children": [
#                        {
#                            "id": "היכרויות - חברתי",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "Tinder", "link": "https://tinder.com/?lang=he"},
#                                {"id": "OkCupid", "link": "https://www.okcupid.com"},
#                                {"id": "Lovely", "link": "https://www.lovely.co.il/"},
#                                {"id": "DATELAND", "link": "http://dateland.co.il"},
#                                {"id": "LoveMe", "link": "https://www.loveme.co.il/he/"},
#                                {"id": "rusDate", "link": "https://rusdate.co.il"},
#                                {"id": "החצי השני", "link": "https://www.onlyu.co.il/"},
#                                {"id": "שליש גן עדן", "link": "https://www.date4dos.co.il"},
#                                {"id": "LoveAble", "link": "https://www.loveable.co.il/"},
#                                {"id": "שניים שהם אחד", "link": "https://www.2become1.co.il/join"},
#                                {"id": "Jdate", "link": "https://www.jdate.com"},
#                                {"id": "אלפא", "link": "https://www.alpha.co.il"},
#                                {"id": "Date50+", "link": "https://date50plus.co.il/"},
#                                {"id": "DateMyAge", "link": "https://www.datemyage.com"},
#                                {"id": "bumble", "link": "https://bumble.com/"},
#                                {"id": "Badoo", "link": "https://badoo.com/he/"}
#                            ]
#                        },
#                        {
#                            "id": "הכרויות - אחר",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "ריצ'דייט", "link": "https://www.richdate.co.il"},
#                                {"id": "שוגר דדי", "link": "https://sugardaddy.co.il"},
#                                {"id": "בוגדות", "link": "https://bogdot.co.il/"},
#                                {"id": "ASHLEY MADDISON", "link": "https://www.ashleymadison.com"}
#                            ]
#                        }
#                    ]
#                },
#
#                {
#                    "id": "מספרי טלפון",
#                    "collapsed": "true",
#                    "children": [
#                        {"id": "number way", "link": "https://www.numberway.com/",
#                         "info": "אתר המציע קישוריות לספרי טלפונים בכל העולם"},
#                        {"id": "truecaller", "link": "https://www.truecaller.com/", "info": "חיפוש הפוך של מספרי טלפון"},
#                        {"id": "synapsint", "link": "https://synapsint.com/", "info": "חיפוש הפוך של מספרי טלפון"},
#                        {"id": "emobiletracker", "link": "https://www.emobiletracker.com/free-trace-world-phone.html",
#                         "info": "חיפוש הפוך של מספרי טלפון"},
#                        {"id": "IntelligenceX", "link": "https://intelx.io/tools?tab=telephone",
#                         "info": "חיפוש הפוך של מספרי טלפון, ארה''ב ובין לאומי בלבד"},
#                        {"id": "How to Call Abroad", "link": "https://www.howtocallabroad.com/",
#                         "info": "חיפוש קוד קידומת עולמי, כולל חיפוש הפוך"},
#                        {"id": "countrycode", "link": "https://countrycode.org/",
#                         "info": "חיפוש קוד קידומת עולמי, כולל קוד עיר"},
#                        {"id": "imei24", "link": "https://imei24.com/",
#                         "info": "מידע על טלפונים סלולריים ע''פ IMEI, כולל רשימה שחורה"},
#                        {"id": "numberingplans", "link": "https://www.numberingplans.com/",
#                         "info": "כלי חיפוש ומאגר מידע, כולל חיפוש IMSI/IMEI"},
#                        {"id": "441il", "link": "https://441il.com/reverse_lookup/phone_number/israel.html",
#                         "info": "חיפוש הפוך של מספרי טלפון, ישראל בלבד (חלקי)"},
#                        {"id": "b144", "link": "https://www.b144.co.il/", "info": "חיפוש אנשים ועסקים בישראל"},
#                        {"id": "pelephone",
#                         "link": "https://www.pelephone.co.il/digitalsite/heb/support/general_info/find-number/",
#                         "info": "חיפוש מספר טלפון ללקוחות פלפון (שם ישוב נדרש)"},
#                        {"id": "partner", "link": "https://www.partner.co.il/selfservice/144",
#                         "info": "חיפוש מספר טלפון ללקוחות פרטנר (שם פרטי לא נדרש)"},
#                        {"id": "hot", "link": "https://www.hot.net.il/heb/Phone/info/#",
#                         "info": "חיפוש מספר טלפון ללקוחות הוט (כולל עסקים)"},
#                        {"id": "Phone Account Finder", "link": "https://tools.epieos.com/phone.php",
#                         "info": "חיפוש מספר טלפון בכמה פלטפורמות חברתיות"},
#                        {"id": "012mobile", "link": "https://www.012mobile.co.il/144",
#                         "info": "חיפוש מספר טלפון ללקוחות 012"}
#                    ]
#                },
#
#                {
#                    "id": "רשת",
#                    "collapsed": "true",
#                    "children": [
#                        {
#                            "id": "מאגרי מידע פרוצים",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "Pastebin", "link": "https://pastebin.com",
#                                 "info": "מאגר מידע טקסטואלי - המכיל הדלפות"},
#                                {"id": "Offshore", "link": "https://offshoreleaks.icij.org/",
#                                 "info": "חיפוש עסקים במאגרי מידע מודלפים"}
#                            ]
#                        },
#                        {
#                            "id": "ארכיון הרשת",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "Wayback Machine", "link": "https://archive.org/web/",
#                                 "info": "ארכיון גדול לאתרי אינטרנט"},
#                                {"id": "Archive.is", "link": "https://archive.is/",
#                                 "info": "ארכיון אתרי אינטרנט, כולל גם שמירה של פרופילים ברשתות חברתיות"},
#                                {"id": "Cachedview", "link": "https://cachedview.com/",
#                                 "info": "גישה למטמון של גוגל לכל כתובת דומיין"}
#                            ]
#                        }
#
#                    ]
#                },
#
#                {
#                    "id": "מפות / כלים גיאוגרפיים",
#                    "collapsed": "true",
#                    "children": [
#                        {
#                            "id": "מפות עולמיות",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "Google Maps", "link": "https://www.google.com/maps/",
#                                 "info": "מפה דינמית כולל צילומי לוויין, הדמיה תלת ממדית, תצלומים, מראה מהרחוב ועוד"},
#                                {"id": "OpenStreetMap", "link": "http://www.openstreetmap.org/#map=5/40.614/-100.679",
#                                 "info": "מפה חופשית"},
#                                {"id": "Google Earth",
#                                 "link": "https://earth.google.com/web/@0,0,0a,22251752.77375655d,35y,0h,0t,0r",
#                                 "info": "מפה הכוללת הדמיה תלת ממדית, מראה מהרחוב, מדידת מרחק וסימולטור טיסה"},
#                                {"id": "Dual Maps", "link": "http://data.mashedworld.com/dualmaps/map.htm",
#                                 "info": "מפה דינמית כולל צילומי לווין ומראה מהרחוב, כולל אפשרות לצפייה במספר מפות במקביל"}
#                            ]
#                        },
#                        {
#                            "id": "מפות נושאיות",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "demo.f4map", "link": "https://demo.f4map.com/#camera.theta=0.9",
#                                 "info": "מפה בהדמייה תלת ממדית של מבנים, תשתיות וטפוגרפיה"},
#                                {"id": "simplex", "link": "https://www.simplex-mapping.com/meymad",
#                                 "info": "הדמייה תלת ממדית מדוייקת של מס' ערים בישראל"},
#                                {"id": "phorio.com", "link": "https://en.phorio.com/",
#                                 "info": "מידע על פרויקטים ומבנים ברחבי העולם"},
#                                {"id": "mapchecking", "link": "http://mapchecking.com",
#                                 "info": "כלי לחישוב צפיפות אנושית ביחס לשטח נתון במפה"}
#
#                            ]
#                        },
#                        {
#                            "id": "כלים גיאוגרפיים",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "mapillary", "link": "https://www.mapillary.com/",
#                                 "info": "אתר ליצירת מפות הכוללות נתוני תשתיות באמצעות צילום במצלמות דרך"},
#                                {"id": "Maphub", "link": "https://maphub.net/",
#                                 "info": "כלי ליצירת פוליגון/ מפה דינמית"},
#                                {"id": "mapbox", "link": "https://www.mapbox.com/",
#                                 "info": "כלי לבניית מפות דינמיות וניווט"},
#                                {"id": "thetimezoneconverter", "link": "https://www.thetimezoneconverter.com/",
#                                 "info": "ממיר שעה לאיזורי זמן אחרים"},
#                                {"id": "openstreetcam", "link": "https://www.openstreetcam.org/",
#                                 "info": "מפה חופשית של צילומי נסיעה (מראה מהרחוב), בעיקר כבישים ראשיים בישראל"}
#
#                            ]
#                        },
#                        {
#                            "id": "מצלמות - שידור ישיר",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "earthcam", "link": "https://earthcam.com/",
#                                 "info": "מפת מצלמות רשת ברחבי העולם"},
#                                {"id": "earthcam", "link": "https://www.windy.com/",
#                                 "info": "מפת מצלמות רשת ברחבי העולם"},
#                                {"id": "earthcam", "link": "https://worldcam.eu/webcams/asia/israel",
#                                 "info": "מפת מצלמות חופים ברחבי העולם"}
#
#                            ]
#                        },
#                        {"id": "Wayback Imagery", "link": "https://livingatlas.arcgis.com/wayback/",
#                         "info": "חיפוש צילומי לוויין היסטוריים"},
#                        {"id": "govmap", "link": "https://www.govmap.gov.il/?c=204000,595000&z=0",
#                         "info": "אתר המפות הרשמי של ישראל כולל פריסת מחוזות המשטרה, חיפוש והזמנת צלומי אויר"},
#                        {"id": "overpass-turbo", "link": "https://overpass-turbo.eu/",
#                         "info": "אתר להרצת שאילתות לחיפוש במפה כולל אשף המסייע ביצירת שאילתות"},
#                        {"id": "mc.bbbike", "link": "https://mc.bbbike.org/mc",
#                         "info": "צפייה בשלוש מפות במקביל לשם השוואה"}
#                    ]
#                },
#
#                {
#                    "id": "מנועי חיפוש",
#                    "collapsed": "true",
#                    "children": [
#                        {
#                            "id": "חיפוש כללי",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "Google", "link": "https://www.google.com/"},
#                                {"id": "Bing", "link": "https://www.bing.com/"},
#                                {"id": "Yahoo", "link": "https://www.yahoo.com/"},
#                                {"id": "Yandex", "link": "https://yandex.com/", "info": "מנוע חיפוש - רוסיה"},
#                                {"id": "Infospace", "link": "https://infospace.com/"},
#                                {"id": "Lycos", "link": "https://www.lycos.com/"},
#                                {"id": "Exalead", "link": "https://www.exalead.com/search/"},
#                                {"id": "ASK", "link": "https://www.search.ask.com/"},
#                                {"id": "Ecosia", "link": "https://www.ecosia.org/"},
#                                {"id": "entireweb", "link": "https://www.osintcombine.com/tiktok-quick-search"},
#                                {"id": "teoma", "link": "https://www.teoma.com/"},
#                                {"id": "yippy", "link": "https://www.yippy.com/"},
#                                {"id": "I Search From", "link": "http://isearchfrom.com/",
#                                 "info": "מדמה שימוש בחיפוש במנוע החיפוש Google ממיקום אחר או מכשיר אחר וכו'"},
#                                {"id": "millionshort", "link": "https://millionshort.com/",
#                                 "info": "מאפשר להסיר את תוצאות החיפוש העליונות "},
#                                {"id": "Dogpile", "link": "https://www.dogpile.com/",
#                                 "info": "תוצאות משולבות מ- Google ו- Yahoo"},
#                                {"id": "Goofram", "link": "http://www.goofram.com/",
#                                 "info": "תוצאות משולבות מ- Google ו- Wolfram Alpha"},
#                                {"id": "iZito", "link": "https://www.izito.com/",
#                                 "info": "Yahoo, Microsoft Bing, YouTube, Wikipedia, Entireweb תוצאות משולבות מ"},
#                                {"id": "Mail.ru", "link": "https://go.mail.ru/search_social?",
#                                 "info": "מנוע חיפוש רוסי, בין היתר מאפשר חיפוש ברשתות חברתיות"},
#                                {"id": "WebCrawler", "link": "https://www.webcrawler.com/",
#                                 "info": "תוצאות משולבות מ- Google ו- Yahoo"}
#                            ]
#                        },
#
#                        {
#                            "id": "מנועי חיפוש אנונימיים",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "DuckDuckGo", "link": "https://duckduckgo.com/", "info": "מנוע חיפוש אנונימי"},
#                                {"id": "Startpage", "link": "https://www.startpage.com/",
#                                 "info": " קבלת תוצאת מ-Google מבלי לעקוב אחר המשתמש"},
#                                {"id": "Peekier", "link": "https://peekier.com/",
#                                 "info": "מנוע חיפוש ששומר על פרטיות המשתמש"},
#                                {"id": "Qwant", "link": "https://www.qwant.com/",
#                                 "info": "מנוע חיפש מטה-דאטה באנונימיות"}
#                            ]
#                        },
#                        {
#                            "id": "חיפוש תמונות",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "Google image search", "link": "https://images.google.com/"},
#                                {"id": "Bing image search",
#                                 "link": "https://www.bing.com/?scope=images&nr=1&FORM=NOFORM"},
#                                {"id": "Yahoo images", "link": "https://images.search.yahoo.com/"},
#                                {"id": "Yandex images", "link": "https://yandex.com/images/"},
#                                {"id": "Baidu images", "link": "https://image.baidu.com/"},
#                                {"id": "Imgur", "link": "https://imgur.com/"},
#                                {"id": "Picsearch", "link": "https://www.picsearch.com/"}
#                            ]
#                        },
#                        {
#                            "id": "חיפוש אנשים",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "FaceSearch", "link": "http://www.facesaerch.com/",
#                                 "info": "חיפוש תמונות פנים של ישות"},
#                                {"id": "IdCrawl", "link": "https://www.idcrawl.com/",
#                                 "info": "חיפוש אנשים ברשתות חברתיות"},
#                                {"id": "מאגר בעלויות כלבים", "link": "https://www.moag.gov.il/Pages/DogSearch.aspx",
#                                 "info": "הצגת תעודת זהות ומספרי פלאפון של בעלי כלבים בישראל"},
#                                {"id": "אבלים", "link": "https://www.avelim.co.il/", "info": "מודעות אבל"}
#                            ]
#                        },
#                        {
#                            "id": "חיפוש חברות",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "B144", "link": "https://www.b144.co.il/", "info": "חיפוש עסקים ישראלים"},
#                                {"id": "דפי זהב", "link": "https://www.d.co.il/", "info": "חיפוש עסקים ישראלים"},
#                                {"id": "Occrp", "link": "https://aleph.occrp.org/",
#                                 "info": "מאגר מידע גלובלי מפורט על חברות"},
#                                {"id": "Offshore leaks", "link": "https://offshoreleaks.icij.org/",
#                                 "info": "חיפוש עסקים במאגרי מידע מודלפים"},
#                                {"id": "Crunchbase", "link": "https://www.crunchbase.com/",
#                                 "info": "מידע על עסקים - בינלואמי"},
#                                {"id": "Aihitdata", "link": "https://www.aihitdata.com/",
#                                 "info": "חיפוש חברות בינלאומיות"}
#                            ]
#                        },
#                        {
#                            "id": "חיפוש - אחר",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "Docketalarm", "link": "https://www.docketalarm.com/",
#                                 "info": "חיפוש תיקים משפטיים"}
#                            ]
#                        }
#
#                    ]
#                },
#
#                {
#                    "id": "פורומים / קהילות",
#                    "collapsed": "true",
#                    "children": [
#                        {
#                            "id": "פורומים ישראלים",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "FXP", "link": "https://fxp.co.il"},
#                                {"id": "Tapuz", "link": "https://tapuz.co.il"},
#                                {"id": "Stips", "link": "https://stips.co.il"},
#                                {"id": "AskPeople", "link": "https://www.askp.co.il"},
#                                {"id": "Rotter", "link": "https://rotter.net"},
#                                {"id": "Atraf", "link": "https://www.atraf.co.il/dating/"}
#
#                            ]
#                        },
#                        {
#                            "id": "פורומים בינלאומיים",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "Voat", "link": "https://voat.co/"},
#                                {
#                                    "id": "Reddit",
#                                    "collapsed": "true",
#                                    "children": [
#                                        {"id": "f5bot", "link": "https://f5bot.com/",
#                                         "info": "התראות לגבי מילות מפתח שמפורסמות בזמן אמת"},
#                                        {"id": "Imagoid", "link": "http://www.imagoid.com/",
#                                         "info": "חיפוש תמונות ברדיט לפי נושא"},
#                                        {"id": "Karmadecay", "link": "http://karmadecay.com/",
#                                         "info": "חיפוש לפי תמונה"},
#                                        {"id": "Comment Search", "link": "https://redditcommentsearch.com/",
#                                         "info": "חיפוש תגובות לפי משתמש"},
#                                        {"id": "Reddit Investigator ", "link": "https://www.redditinvestigator.com/",
#                                         "info": "מידע סטטיסטי מפורט על שם משתמש"},
#                                        {"id": "Reddit Search", "link": "https://camas.github.io/reddit-search/",
#                                         "info": "חיפוש פוסטים לפי טווח תאריכים"},
#                                        {"id": "Resavr", "link": "https://www.resavr.com/",
#                                         "info": "חיפוש פוסטים שנמחקו"},
#                                        {"id": "SearchReddit", "link": "https://searchreddit.blogspot.com/",
#                                         "info": "חיפוש פוסטים לפי מילות מפתח"},
#                                        {"id": "Simpleddit", "link": "http://www.simpleddit.com/",
#                                         "info": "חיפוש פורום לפי נושא בהתאמה אישית"},
#                                        {"id": "Tidder", "link": "http://tidder.xyz/", "info": "חיפוש תמונה ברדיט"},
#                                        {"id": "Wisdomfreddit", "link": "https://wisdomofreddit.com/",
#                                         "info": "חיפוש ברדיט לפי מילות מפתח"}
#                                    ]
#                                },
#                                {
#                                    "id": "Github",
#                                    "collapsed": "true",
#                                    "children": [
#                                        {"id": "Coderstats", "link": "https://coderstats.net/", "info": "חיפוש משתמשים"},
#                                        {"id": "Github Id", "link": "https://caius.github.io/github_id/",
#                                         "info": "מציאת ID לפי שם משתמש"},
#                                        {"id": "Awesome Lists", "link": "http://awesomelists.top/",
#                                         "info": "רשימות של מקורות לפי קטגוריה"}
#                                    ]
#                                }
#
#                            ]
#                        }
#                    ]
#                },
#
#                {
#                    "id": "דארקנט",
#                    "collapsed": "true",
#                    "children": [
#                        {
#                            "id": "אתרי Onion",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "PwnDB", "link": "http://pwndb2am4tzkvold.onion/",
#                                 "info": "מספק סיסמאות או כתובות מייל ממאגרים שנפרצו"},
#                                {"id": "Torch Search Engine", "link": "http://cnkj6nippubgycuj.onion/",
#                                 "info": "מנוע חיפוש ברשת הדארקנט"},
#                                {"id": "Not Evil", "link": "http://hss3uro2hsxfogfq.onion/",
#                                 "info": "מנוע חיפוש ברשת הדארקנט"},
#                                {"id": "Tordex", "link": "http://tordex7iie7z2wcg.onion/",
#                                 "info": "מנוע חיפוש ברשת הדארקנט"},
#                                {"id": "Haystak", "link": "http://haystakvxad7wbk5.onion/",
#                                 "info": "מנוע חיפוש ברשת הדארקנט"},
#                                {"id": "Torch",
#                                 "link": "http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/cgi-bin/omega/omega",
#                                 "info": "מנוע חיפוש ברשת הדארקנט"},
#                                {"id": "The Hidden Wiki",
#                                 "link": "http://zqktlwi4fecvo6ri.onion/wiki/index.php/Main_Page",
#                                 "info": "אינדקס שירותים ברשת הדארקנט"}
#
#                            ]
#                        },
#                        {"id": "Darksearch", "link": "https://darksearch.io/", "info": "מנוע חיפוש לרשת הדארקנט"},
#                        {"id": "Deeponionweb", "link": "https://www.deeponionweb.com/",
#                         "info": "אינדקס שירותים ברשת הדארקנט"},
#                        {"id": "ExoneraTor", "link": "https://metrics.torproject.org/exonerator.html",
#                         "info": "בדיקה האם כתובת IP הייתה מעורבת ברשת הTOR בתאריך מסויים"},
#                        {"id": "Ahmia", "link": "https://ahmia.fi/", "info": "מנוע חיפוש לרשת הדארקנט"},
#                        {"id": "Dark.fail", "link": "https://dark.fail/", "info": "אינדקס שירותים לרשת הדארקנט"},
#                        {"id": "Tor - Wiki", "link": "https://en.wikipedia.org/wiki/List_of_Tor_onion_services",
#                         "info": "ערך בוויקיפדיה המכיל שירותים ברשת הדארקנט"},
#                        {"id": "OnionLand", "link": "https://onionlandsearchengine.com/",
#                         "info": "מנוע חיפוש לרשת הדארקנט"}
#                    ]
#                },
#                {
#                    "id": "לוחות מכירה",
#                    "collapsed": "true",
#                    "children": [
#                        {
#                            "id": "לוחות כלליים",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "יד 2", "link": "https://www.yad2.co.il/",
#                                 "info": "פלטפורמה למסחר וחיפוש עבודה ולימודים (ניתן לחפש זהויות ע''פ שם, למעט דירות)"},
#                                {"id": "HappySale",
#                                 "link": "https://play.google.com/store/apps/details?id=com.happysale",
#                                 "info": "מסחר במוצרים משומשים כולל פרסום ברשתות חברתיות"},
#                                {"id": "הפורום הישראלי להסברה", "link": "https://www.metalindx.com/he/dboards.aspx?p=1",
#                                 "info": "פורטל הכולל לוח יד שנייה "},
#                                {"id": "תרי זוזי", "link": "https://www.zuze.co.il/index.php",
#                                 "info": "פלפורמה למסחר ואינדקס עסקים, גמ''חים, דרושים ועוד (מיועדת לציבור החרדי)"},
#                                {"id": "שטריימל", "link": "http://www.shtraymel.co.il/",
#                                 "info": "פלפורמה למסחר ואינדקס עסקים, גמ''חים, דרושים ועוד (מיועדת לציבור החרדי), ניתן לחפש זהויות ע''פ שם"},
#                                {"id": "לוח365", "link": "http://www.luach365.co.il/", "info": "חיקוי של יד 2"},
#                                {"id": "bipbip", "link": "https://www.bipbip.co.il/", "info": "חיקוי של יד 2"},
#                                {"id": "madas", "link": "https://www.madas.co.il/", "info": "חיקוי של יד 2"},
#                                {"id": "לוח אחד", "link": "https://www.luah1.co.il/", "info": "חיקוי של יד 2"},
#                                {"id": "telebuy", "link": "https://www.telebuy.co.il/",
#                                 "info": "חיקוי של יד 2 (ישנם גם קבוצות מסחר מקבילות בפייסבוק)"},
#                                {"id": "הומלס", "link": "https://www.homeless.co.il/",
#                                 "info": "חיקוי של יד 2 (ניתן לחפש זהויות ע''פ שם)"},
#                                {"id": "ad ", "link": "https://www.ad.co.il/",
#                                 "info": "חיקוי של יד 2 כולל ארכיון מודעות (ניתן לחפש זהויות ע''פ שם או מס''ט)"},
#                                {"id": "ג'וב מאסטר", "link": "https://www.jobmaster.co.il/",
#                                 "info": "לוח דרושים הכולל חיפש זהויות ע''פ שם וקורות חיים"},
#                                {"id": "תעשיה.קום", "link": "https://www.taasiya.co.il/",
#                                 "info": "לוח דרושים הכולל לוחות מכירה, השכרה, דרושים, לימודים ועוד"},
#                                {"id": "הכל", "link": "http://akol.co.il/icbaapp/bboard/", "info": "לוח מודעות"}
#                            ]
#                        },
#                        {
#                            "id": "לוחות בינלאומיים",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "קרייגליסט", "link": "https://craigslist.org/",
#                                 "info": "לוח מודעות בינלאומי למגוון תחומים (ניתן לחפש זהויות לפי שם וטלפון)"},
#                                {"id": "אמזון", "link": "https://www.amazon.com/-/he/ref=nav_logo",
#                                 "info": "חנות ופלטפורמה למסחר בינלאומית למגוון תחומים (ניתן לצפות בפרטי מוכרים חיצוניים)"},
#                                {"id": "אטסי", "link": "https://www.etsy.com/il-en/?ref=lgo",
#                                 "info": "פלטפורמה למסחר בחפצי אומנות ומלאכות יד (ניתן לצפות במיקום ותמונת המוכר)"}
#                            ]
#                        },
#                        {
#                            "id": "לוחות נושאיים",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "אקט מוסיקלי", "link": "https://www.act.co.il/bazaar/",
#                                 "info": "אתר בנושאי טכנולוגיות במוסיקה הכולל לוח יד שנייה (ניתן לחפש זהויות ע''פ שם) "},
#                                {"id": "hwzone", "link": "https://hwzone.co.il/community/classifieds/",
#                                 "info": "אתר בנושאי מחשבים ודיגיטל הכולל לוח יד שנייה"},
#                                {"id": "eway", "link": "https://www.eway.co.il/second-hand/",
#                                 "info": "אתר בנושאי רכיבה על אופניים הכולל לוח יד שנייה"},
#                                {"id": "דוקטור אונליין", "link": "https://doctoronline.co.il/",
#                                 "info": "אתר בנושאי רפואה הכולל לוח דרושים ויד שנייה"},
#                                {"id": "לימודים בישראל",
#                                 "link": "https://student.universities-colleges.org.il/%D7%A1%D7%A4%D7%A8%D7%99%D7%9D-%D7%9E%D7%A9%D7%95%D7%9E%D7%A9%D7%99%D7%9D/",
#                                 "info": "אתר הכולל פלטפורמה למסחר בספרי לימוד משומשים"},
#                                {"id": "groopy", "link": "http://www.groopy.co.il/secondhand.aspx",
#                                 "info": "אתר לרוכבי אופנים הכולל לוח מכירות"},
#                                {"id": "archijob", "link": "http://www.archijob.co.il/archilist/board.aspx?id=8",
#                                 "info": "פורטל לאדריכלות, עיצוב ותכנון הכולל לוח מחפשי עבודה "},
#                                {"id": "all bikes", "link": "https://www.allbikes.co.il/userAd?Category=1",
#                                 "info": "פלטפורמה למסחר באופניים ואביזרים נלווים"},
#                                {"id": "מרמלדה מרקט", "link": "https://market.marmelada.co.il/",
#                                 "info": "פלטפורמה למסחר במוצרי טיפוח, עיצוב, פנאי ומלאכת יד "},
#                                {"id": "משומש", "link": "https://www.meshoomash.co.il/",
#                                 "info": "פלטפורמה למסחר בציוד תעשייתי משומש"},
#                                {"id": "לוח פוקוס", "link": "https://www.focusnet.co.il/",
#                                 "info": "פלטפורמה למסחר ברכבים מכל הסוגים וכלי שיט"},
#                                {"id": "תתניע", "link": "https://www.tatnia.co.il/",
#                                 "info": "פלטפורמה למסחר ברכבים מכל הסוגים וכלי שיט"}
#                            ]
#                        },
#                        {
#                            "id": "לוחות מקומיים",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "לוטם",
#                                 "link": "http://www.lotem.org.il/ViewPage.asp?pagesCatID=3905&siteName=lotem&myMsg=2",
#                                 "info": "אתר מקומי הכולל לוח מודעות"},
#                                {"id": "מועצה איזורית בנימין", "link": "https://www.binyamin.org.il/boards/",
#                                 "info": "אתר מקומי הכולל לוח מודעות"},
#                                {"id": "משגב", "link": "https://www.misgav.org.il/boards/",
#                                 "info": "אתר מקומי הכולל לוח מודעות"},
#                                {"id": "חגלאי", "link": "http://moshavhogla.com/hogla-bulletin",
#                                 "info": "אתר מקומי הכולל לוח מודעות"},
#                                {"id": "הערבה התיכונה", "link": "https://www.arava.co.il/boards/",
#                                 "info": "אתר מקומי הכולל לוח מודעות"},
#                                {"id": "מולדת",
#                                 "link": "http://www.m-moledet.org.il/ViewPage.asp?pagesCatID=22300&siteName=moledet",
#                                 "info": "אתר מקומי הכולל לוח מודעות"},
#                                {"id": "שהם", "link": "https://www.shoham.muni.il/boards/",
#                                 "info": "אתר מקומי הכולל לוח מודעות"},
#                                {"id": "קדימה לעבודה", "link": "https://www.job-hr.co.il/",
#                                 "info": "אתר מקומי הכולל לוח מודעות"}
#                            ]
#                        },
#                        {
#                            "id": "לוחות בערבית",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "עסקים בישראל",
#                                 "link": "http://www.findglocal.com/IL/Jerusalem/765270063531420/%D9%85%D8%B7%D9%84%D9%88%D8%A8-%D9%84%D9%84%D8%B9%D9%85%D9%84.-%D9%81%D8%B1%D8%B5%D8%A9-%D8%B9%D9%85%D9%84.-%D9%88%D8%B8%D8%A7%D8%A6%D9%81-%D8%B4%D8%A7%D8%BA%D8%B1%D8%A9?__cf_chl_jschl_tk__=05f7624bd81239872b6b99bc002ad0af9b0867ad-1606043853-0-AZ6Q0NlDO7raUkFQ5DYz4R-yL3xAo5zdYITmzmlHJNz35TOpFx3OroXyxE16y_7aTfQSGkn2gB1el6SMckumWU-UtdoQITOeIOOgTXEfsr3N2vVD1ExD-sbtNjGxAmAMyQXzvMH53s3ZYxKtSq0gngZLbwbrbUhP0fbs0GUhOtdzdbuKJmc_Ao7OxS5qhcuBoFlGPLyAoiHrbdli3dNG3-4nmNsZ4Xe1pGSkJrlS6EoIWUfhwe2Oiv-KUV5H7SdGUlmbn-xoOiSB16ne8tsbYnXjmCHlTzGp3xn7zijIk0c51Gt8azbrqyyGQkDaUYKdUpd4C9ia6bZHhxEkfdaaQ8k_Ob2WQfOY8k_6nTZmPJO0dE8thWdjnGwJXSXd0mtNnNHqB0LEP6ZJxYr7hp8l2HH6X6lg6K0ujt7fkMvmnM6MixijVjQL2_yfQzl9LzoFESl4jf48a8_xB_YRiSwB1SMF5PHNpHTaaDjEOWQXBt6Qy1lzRbPr7f0FgjUs7j1ZXv7NMMB8R2iP1Vs0xSAawrLnph8WZyH7VGz2SOeBq_brYNcqNKmEueOo2t_trpwuvd4ajghLbEIUpuGgDOhPzWZouy7yM_ku1429G8auURXjfVY7lRBFc4ZYnZ-eer0YrQ",
#                                 "info": "אינדקס עסקים בישראל הכולל לוח דרושים"},
#                                {"id": "albaazar", "link": "http://albaazar.com/",
#                                 "info": "פלטפורמה למסחר חיפוש עבודה ולימודים"},
#                                {"id": "albaladsouq", "link": "http://www.albaladsouq.com/",
#                                 "info": "פלטפורמה למסחר חיפוש עבודה ולימודים"},
#                                {"id": "shobiddak", "link": "https://shobiddak.com/stuffs/315459",
#                                 "info": "פלטפורמה למסחר חיפוש עבודה ולימודים"},
#                                {"id": "opensooq", "link": "https://ps.opensooq.com/ar",
#                                 "info": "פלטפורמה למסחר חיפוש עבודה ולימודים"},
#                                {"id": "משומש - למכירה - ירושלים",
#                                 "link": "https://www.facebook.com/pages/category/Company/%D9%85%D8%B3%D8%AA%D8%B9%D9%85%D9%84-%D9%84%D9%84%D8%A8%D9%8A%D8%B9-%D8%A7%D9%84%D9%82%D8%AF%D8%B3-1465158007104458/",
#                                 "info": "קבוצת פייסבוק למסחר במוצרים משומשים"},
#                                {"id": "מכוניות מתוך ישראל למכירה", "link": "https://ar-ar.facebook.com/bycar.khalel/",
#                                 "info": "קבוצת פייסבוק למסחר ברכבים משומשים"},
#                                {"id": "מכוניות למכירה", "link": "https://he-il.facebook.com/groups/232971943564365/",
#                                 "info": "קבוצת פייסבוק למסחר ברכבים משומשים"}
#                            ]
#                        },
#                        {
#                            "id": "לוחות ברוסית",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "דוסקה", "link": "http://doska.co.il/",
#                                 "info": "פלטפורמה למסחר, חיפוש עבודה ולימודים"},
#                                {"id": "russiandoska",
#                                 "link": "https://www.russiandoska.ru/cat/0-692/izrail-vse-razdely.html",
#                                 "info": "פלטפורמה למסחר, חיפוש עבודה ולימודים"},
#                                {"id": "il4ru", "link": "https://il4ru.com/",
#                                 "info": "פלטפורמה למסחר, חיפוש עבודה ולימודים"},
#                                {"id": "ישראל סייל", "link": "https://isra.sale/",
#                                 "info": "פלטפורמה למסחר, חיפוש עבודה ולימודים"},
#                                {"id": "מועצת ההודעות לישראל", "link": "https://doska.orbita.co.il/",
#                                 "info": "פלטפורמה למסחר, חיפוש עבודה ולימודים"},
#                                {"id": "israelinfo", "link": "https://israelinfo.co.il/",
#                                 "info": "פלטפורמה למסחר, חיפוש עבודה ולימודים (ניתן לחפש זהויות)"},
#                                {"id": "סנטרו", "link": "https://centro.co.il/",
#                                 "info": "פלפורמה למסחר בכלי תחבורה משומשים"},
#                                {"id": "rabota-il", "link": "http://www.rabota-il.com/",
#                                 "info": "לוח דרושים הכולל הכולל קורות חיים"},
#                                {"id": "souz", "link": "https://souz.co.il/index.html", "info": "צריך לפתוח"},
#                                {"id": "jobisrael", "link": "https://he-il.facebook.com/groups/jobisrael/",
#                                 "info": "קבוצת פייסבוק לחיפוש עבודה"},
#                                {"id": "קנו מכוניות משומשות בישראל",
#                                 "link": "https://www.facebook.com/pages/category/Automotive-Dealership/%D0%9A%D1%83%D0%BF%D0%B8%D1%82%D1%8C-%D0%90%D0%B2%D1%82%D0%BE%D0%BC%D0%BE%D0%B1%D0%B8%D0%BB%D0%B8-%D0%B2-%D0%98%D0%B7%D1%80%D0%B0%D0%B8%D0%BB%D0%B5-%D0%91%D1%83-1624382111161840/",
#                                 "info": "קבוצת פייסבוק למסחר ברכבים משומשים"},
#                                {"id": "autoisrael", "link": "https://www.facebook.com/groups/autoisrael/",
#                                 "info": "קבוצת פייסבוק למסחר ברכבים משומשים"},
#                                {"id": "work_israel", "link": "https://vk.com/work_israel",
#                                 "info": "קבוצת VK לחיפוש עבודה"}
#                            ]
#                        },
#                        {
#                            "id": "לוחות מכירה - פייסבוק",
#                            "collapsed": "true",
#                            "children": [
#                                {"id": "פשפשוק", "link": "https://www.facebook.com/groups/pishpeshuk",
#                                 "info": " קבוצת פייסבוק למסחר במגוון תחומים"},
#                                {"id": "פשפשוק - יד שניה", "link": "https://www.facebook.com/groups/268799249931777",
#                                 "info": "מכירות של מוצרים יד שניה במגוון תחומים"},
#                                {"id": "פשפשוק - רכבים", "link": "https://www.facebook.com/groups/pishpeshuk.cars",
#                                 "info": "פרסום רכבים למכירה"},
#                                {"id": "פשפשוק - למסירה", "link": "https://www.facebook.com/groups/Pishpeshuk.Handover/",
#                                 "info": "פרסום מוצרים למסירה"},
#                                {"id": "פשפשוק - סלולר",
#                                 "link": "https://www.facebook.com/groups/1555004694768144/?ref=ts&fref=ts",
#                                 "info": "מכירות של מכשירי סלולר"},
#                                {"id": "לוח מכירה וקניה", "link": "https://www.facebook.com/groups/1279479825439685",
#                                 "info": "קניה ומכירה של מוצרים"},
#                                {"id": "למכירה - לוח מכירה חינמי",
#                                 "link": "https://www.facebook.com/groups/1558952784334779",
#                                 "info": "פרסום מוצרים למכירה"},
#                                {"id": "נתקעתי עם", "link": "https://www.facebook.com/groups/stuckwith",
#                                 "info": "פרסום מוצרים שונים למכירה"}
#                            ]
#                        }
#
#                    ]
#                },
#                {
#                    "id": "דואר ומשלוחים",
#                    "collapsed": "true",
#                    "children": [
#                        {"id": "flightradar24", "link": "https://www.flightradar24.com/",
#                         "info": "מעקב בזמן אמת אחר תעבורת מטוסים ושדות תעופה"},
#                        {"id": "planefinder", "link": "https://planefinder.net/",
#                         "info": "מעקב בזמן אמת אחר תעבורת מטוסים ושדות תעופה "},
#                        {"id": "planemapper", "link": "http://www.planemapper.com/aircrafts",
#                         "info": "מאגר מידע בנושא תעבורה אווירית (כולל מעקב בזמן אמת)"},
#                        {"id": "marinetraffic", "link": "https://www.marinetraffic.com/",
#                         "info": "מעקב בזמן אמת אחר תעבורה ימית"},
#                        {"id": "vesselfinder", "link": "https://www.vesselfinder.com/",
#                         "info": "מעקב בזמן אמת אחר תעבורה ימית"},
#                        {"id": "cruisemapper", "link": "http://www.cruisemapper.com/",
#                         "info": "מאגר מידע בנושא שייט ימי (כולל לוחות זמנים ויעדי נסיעה מתוכננים)"},
#                        {"id": "shipfinder", "link": "http://shipfinder.co/", "info": "מעקב בזמן אמת אחר תעבורה ימית"},
#                        {"id": "aftership", "link": "https://www.aftership.com/couriers",
#                         "info": "מעקב אחר חבילות דואר ומשלוחים"},
#                        {"id": "packagetrackr", "link": "https://www.packagetrackr.com/",
#                         "info": "מעקב אחר חבילות דואר ומשלוחים כולל הדמיית מסלול בגוגל מפות"},
#                        {"id": "דואר ישראל", "link": "https://mypost.israelpost.co.il/",
#                         "info": "מעקב משלוחים של דואר ישראל"},
#                        {"id": "prefixlist", "link": "http://www.prefixlist.com/", "info": "מאגר מידע על מכולות"},
#                        {"id": "bic-code", "link": "https://www.bic-code.org/bic-codes/", "info": "מאגר מידע על מכולות"}
#                    ]
#                },
#
#                {
#                    "id": "מטבעות וירטואליים",
#                    "collapsed": "true",
#                    "children": [
#                        {"id": "Blockchain", "link": "https://blockchain.info/",
#                         "info": "אזור סחר בו ניתן לחפש עסקאות, כתובות, בלוקים"},
#                        {"id": "BTC.com", "link": "https://btc.com", "info": "סייר עבור מגוון מטבעות"},
#                        {"id": "BlockCypher", "link": "https://live.blockcypher.com", "info": "סייר עבור מגוון מטבעות."},
#                        {"id": "BitRef", "link": "https://bitref.com/", "info": "בדיקת יתרת ארנק לפי כתובת"},
#                        {"id": "Wallet Explorer", "link": "https://www.walletexplorer.com/",
#                         "info": "סייר עבור ביטקויין בלבד"},
#                        {"id": "OXT", "link": "https://oxt.me",
#                         "info": "סייר עבור ביטקויין בלבד הכולל אפשרות לחיפוש עסקאות לפי תאריך וסכום"},
#                        {"id": "Bitcoin Abuse", "link": "https://www.bitcoinabuse.com",
#                         "info": "מעקב אחר כתובות ביטקוין המשמשות תוכנות כופר, סוחטים, רמאים וכדומה"},
#                        {"id": "Bitcoin Who's Who", "link": "https://bitcoinwhoswho.com/",
#                         "info": "סייר עבור ביטקויין כולל אינדיקציה על הימצאות ברשימה השחורה"},
#                        {"id": "addresschecker.eu", "link": "http://addresschecker.eu",
#                         "info": "סייר ביטקויין המאפשר לבדוק מס' ארנקים במקביל"},
#                        {"id": "Etherscan", "link": "https://etherscan.io/", "info": "סייר עבור אתריום בלבד"},
#                        {"id": "XMRChain.net", "link": "https://xmrchain.net/", "info": "סייר אנונימי עבור מונרו בלבד"},
#                        {"id": "Monero Blocks", "link": "http://moneroblocks.info/", "info": "סייר עבור מונרו בלבד"},
#                        {"id": "Coin ATM Radar", "link": "https://coinatmradar.com",
#                         "info": "איתור כספומט (ATM) למטבעות ווירטואליים"},
#                        {"id": "Crypto Scam Checker", "link": "https://fried.com/crypto-scam-checker",
#                         "info": "בדיקת מהימנות של אתרים למסחר במטבעות וירטואליים"}
#                    ]
#                }
#
#            ]
#            }
#
#
# # def update_node(path: str, object_to_update):
#     # path_list = path.split('/')
#     # if path_list[0] == 'okyanus':
#     #     path_list.pop(0)
#     # if path_list[-1] == '':
#     #     path_list.pop(-1)
#     # print(path_list)
#     # for num, slice_of_path in enumerate(path_list, start=0):
#     #     if slice_of_path.isnumeric():
#     #         path_list[num] = int(slice_of_path)
#     # print(path_list)
#     # okyanus = json.load(open('data.json'))
#     # node = okyanus
#     # for slice_of_path in path_list:
#     #     node = node[slice_of_path]
#     # node[slice_of_path] = object_to_update
#     # print(node[slice_of_path])
#
#
# def create_path(path: str):
#     path_list = path.split('/')
#     if path_list[0] == 'okyanus':
#         path_list.pop(0)
#     if path_list[-1] == '':
#         path_list.pop(-1)
#     new_path = ''
#     for slice_of_path in path_list:
#         if not slice_of_path.isnumeric():
#             slice_of_path = "'{}'".format(slice_of_path)
#         new_path = '''{}[{}]'''.format(new_path, slice_of_path)
#     return '''{}'''.format(new_path)
#
#
# def add_node(path: str, object_to_add):
#     okyanus = json.load(open('data.json'))
#     path_to_eval = create_path(path)
#     requested_node = eval('okyanus' + path_to_eval)
#
#     # okyanus[eval('''['test']''')]
#     # okyanus['test']=object_to_add
#     print(okyanus)
#     # print(okyanus[eval('''['children']''')])
#     # new_path = create_path(path)
#     # okyanus[eval('''['children']''')]=object_to_add
#     # new_node =object_to_add
#     # # print(okyanus)
#
#
# def get_node(path: str):
#     path_to_eval = create_path(path)
#     okyanus = json.load(open('data.json'))
#     requested_node = eval('okyanus' + path_to_eval)
#     return requested_node
#     # print(requested_node)
#     # print(requested_node)
#     # okyanus[requested_node] = {'test': 'test'}
#     # json.dump(okyanus, open('data.json', "w"))
#     # print(okyanus)
#     # return okyanus[requested_node]
#
#
# # def recurse(node,location_in_list:int,path_list:list,object_to_add):
# #     if location_in_list == len(path_list)-1:
# #         node = object_to_add
# #     else:
# #         recurse(node[location_in_list+1],location_in_list+1,path_list,object_to_add)
#
# def test(node):
#     pass
#     # print(okyanus['children'][0])
#
#
#     # node = {'test':'test'}
#     # print(node)
#     # print(okyanus["children"])
#     # seri = json.dump(okyanus, open('data.json', "w"))
#     # blah = json.load(open('data.json'))
#     #
#     # st = '''['children']'''
#     # eval('''st={}''')
#     # test = (eval('''blah['children']'''))
#     # test ={}
#
#
#     # print(blah)
#
# blah = json.load(open('data.json'))
# test(blah['children'])
# # update_node('okyanus/children/0/children/0/children/0/',{'test','test'})
# # add_node('okyanus/test/', {'test', 'test'})
# # print(get_node('okyanus/children/'))
# # test()
# # get_node('okyanus/children/0/')
# # add_node('okyanus/children/0/', {'test': 'test'})
# # r = get('https://fire-base-crud-project-default-rtdb.europe-west1.firebasedatabase.app/okyanus/.json')
# # print(r.text)
# # with open('okyanusa.json', 'w') as f:
# #     json.dump(r.json(), f)
#
# # data = request.urlopen(
# #     'https://fire-base-crud-project-default-rtdb.europe-west1.firebasedatabase.app/okyanus/.json').read().decode(
# #     'utf-8')
# # blah = json.loads(data)
# # dump = json.dumps(blah, ensure_ascii=False).encode('utf8')
# #
# # # with open('okyanus.json') as f:
# # #     c = json.load(f)
# #
# # print(type(dump.decode()))
# # # print(dump.decode())
