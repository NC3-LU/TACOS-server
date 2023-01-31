

python src/manager.py db_empty
python src/manager.py db_init

# Feed set: Luxembourg Greater Region
python src/manager.py add_feed_set 'Luxembourg Greater Region' 'Feeds proposed by NC3 Luxembourg.' 1
python src/manager.py add_feed 'BEE Secure' 'Bee Secure feed' https://www.bee-secure.lu/de/rss/news de 1
python src/manager.py add_feed 'Silicon Luxembourg' 'Silicon Luxembourg' https://www.siliconluxembourg.lu/tag/cybersecurity/feed/ en 1

# Feed set: World feed
python src/manager.py add_feed_set 'World feed' 'Feeds from all other the world proposed by NC3 Luxembourg.' 2
python src/manager.py add_feed 'Schneier on Security' 'Schneier on Security' https://www.schneier.com/blog/atom.xml en 2
python src/manager.py add_feed 'KrebsOnSecurity' 'KrebsOnSecurity' https://krebsonsecurity.com/feed en 2
python src/manager.py add_feed 'CSO online' 'CSO online' https://www.csoonline.com/index.rss en 2
python src/manager.py add_feed 'SANS Institute Security Awareness Tip of the Day' 'SANS Institute Security Awareness Tip of the Day' https://feeds2.feedburner.com/security-awareness-tip-of-the-day en 2
python src/manager.py add_feed 'Cybersecurity & Digital Privacy Policy (Unit H.2)' 'Cybersecurity & Digital Privacy Policy (Unit H.2)'  'http://ec.europa.eu/information_society/newsroom/cf/generaterss.cfm?tpa_id=16548&sub=1&pr=all' en 2

# Feed set: NC3 feed
python src/manager.py add_feed_set 'NC3 news' 'News about NC3-LU' 3
#python src/manager.py add_feed 'NC3 tools' 'NC3-LU tools' https://open-source-security-software.net/organization/NC3-LU/releases.atom en 3
python src/manager.py add_feed 'NC3 Luxembourg' 'Articles from the NC3 website' https://nc3.lu/feed.xml en 3
python src/manager.py add_feed 'MONARC news' 'News about MONARC' https://www.monarc.lu/feeds/all.atom.xml en 3
