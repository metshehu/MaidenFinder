import json

import httpx

client = httpx.Client(
    headers={
        # this is internal ID of an instegram backend app. It doesn't change often.
        "x-ig-app-id": "936619743392459",
        # use browser-like features
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9,ru;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
    }
)


def scrape_user(username: str):
    """Scrape Instagram user's data"""
    ur = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={
        username}"

    print(ur)
    result = client.get(ur)
    return result


print(scrape_user("orindaakrasniqi"))
#    data = json.loads(result.content)
#    return data["data"]["user"]


# print(scrape_user("orindaakrasniqi"))

# print(scrape_user("orindaakrasniqi"))
# a = 0
# thumbnail_src = (
#     "https://instagram.fprn13-1.fna.fbcdn.net/v/t51.29350-15/459031563_857466203161089_9130304129139129556_n.jpg?stp=c0.180.1440.1440a_dst-jpg_e35_s640x640_sh0.08\u0026_nc_ht=instagram.fprn13-1.fna.fbcdn.net\u0026_nc_cat=109\u0026_nc_ohc=lQ9vfp7w9j4Q7kNvgGRKij2\u0026_nc_gid=45ffe1011ae04c21b7ffebccc9743b6c\u0026edm=AOQ1c0wBAAAA\u0026ccb=7-5\u0026oh=00_AYBwsUWo6ET02L6XH03J2vonUCY9gsF1r9U0B-JKIvRPxQ\u0026oe=671320B3\u0026_nc_sid=8b3546",
# )
# thumbnail_resources = [
#     {
#         "src": "https://instagram.fprn13-1.fna.fbcdn.net/v/t51.29350-15/459031563_857466203161089_9130304129139129556_n.jpg?stp=c0.180.1440.1440a_dst-jpg_e35_s150x150\u0026efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE4MDAuc2RyLmYyOTM1MC5kZWZhdWx0X2ltYWdlIn0\u0026_nc_ht=instagram.fprn13-1.fna.fbcdn.net\u0026_nc_cat=109\u0026_nc_ohc=lQ9vfp7w9j4Q7kNvgGRKij2\u0026_nc_gid=45ffe1011ae04c21b7ffebccc9743b6c\u0026edm=AOQ1c0wBAAAA\u0026ccb=7-5\u0026oh=00_AYDxZL4v25Khx_OBS8BwWXQtI658lWSbU6BE4E0ejWvcig\u0026oe=671320B3\u0026_nc_sid=8b3546",
#         "config_width": 150,
#         "config_height": 150,
#     },
#     {
#         "src": "https://instagram.fprn13-1.fna.fbcdn.net/v/t51.29350-15/459031563_857466203161089_9130304129139129556_n.jpg?stp=c0.180.1440.1440a_dst-jpg_e35_s240x240\u0026efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE4MDAuc2RyLmYyOTM1MC5kZWZhdWx0X2ltYWdlIn0\u0026_nc_ht=instagram.fprn13-1.fna.fbcdn.net\u0026_nc_cat=109\u0026_nc_ohc=lQ9vfp7w9j4Q7kNvgGRKij2\u0026_nc_gid=45ffe1011ae04c21b7ffebccc9743b6c\u0026edm=AOQ1c0wBAAAA\u0026ccb=7-5\u0026oh=00_AYAOBr5pOPmUu7qS7D0-GrbsEE7iYUXJyew7fp7EeYiYBg\u0026oe=671320B3\u0026_nc_sid=8b3546",
#         "config_width": 240,
#         "config_height": 240,
#     },
#     {
#         "src": "https://instagram.fprn13-1.fna.fbcdn.net/v/t51.29350-15/459031563_857466203161089_9130304129139129556_n.jpg?stp=c0.180.1440.1440a_dst-jpg_e35_s320x320\u0026efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE4MDAuc2RyLmYyOTM1MC5kZWZhdWx0X2ltYWdlIn0\u0026_nc_ht=instagram.fprn13-1.fna.fbcdn.net\u0026_nc_cat=109\u0026_nc_ohc=lQ9vfp7w9j4Q7kNvgGRKij2\u0026_nc_gid=45ffe1011ae04c21b7ffebccc9743b6c\u0026edm=AOQ1c0wBAAAA\u0026ccb=7-5\u0026oh=00_AYC_TYx6hhACi1zT6b8CFPs4Jb8_r_aVoUn_lZpbmx09tg\u0026oe=671320B3\u0026_nc_sid=8b3546",
#         "config_width": 320,
#         "config_height": 320,
#     },
#     {
#         "src": "https://instagram.fprn13-1.fna.fbcdn.net/v/t51.29350-15/459031563_857466203161089_9130304129139129556_n.jpg?stp=c0.180.1440.1440a_dst-jpg_e35_s480x480\u0026efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE4MDAuc2RyLmYyOTM1MC5kZWZhdWx0X2ltYWdlIn0\u0026_nc_ht=instagram.fprn13-1.fna.fbcdn.net\u0026_nc_cat=109\u0026_nc_ohc=lQ9vfp7w9j4Q7kNvgGRKij2\u0026_nc_gid=45ffe1011ae04c21b7ffebccc9743b6c\u0026edm=AOQ1c0wBAAAA\u0026ccb=7-5\u0026oh=00_AYAU3z7Qwb7TVkcEKdtCcnLu6io4VAJ4sAbXXC2c8NUIOQ\u0026oe=671320B3\u0026_nc_sid=8b3546",
#         "config_width": 480,
#         "config_height": 480,
#     },
#     {
#         "src": "https://instagram.fprn13-1.fna.fbcdn.net/v/t51.29350-15/459031563_857466203161089_9130304129139129556_n.jpg?stp=c0.180.1440.1440a_dst-jpg_e35_s640x640_sh0.08\u0026efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE4MDAuc2RyLmYyOTM1MC5kZWZhdWx0X2ltYWdlIn0\u0026_nc_ht=instagram.fprn13-1.fna.fbcdn.net\u0026_nc_cat=109\u0026_nc_ohc=lQ9vfp7w9j4Q7kNvgGRKij2\u0026_nc_gid=45ffe1011ae04c21b7ffebccc9743b6c\u0026edm=AOQ1c0wBAAAA\u0026ccb=7-5\u0026oh=00_AYBwsUWo6ET02L6XH03J2vonUCY9gsF1r9U0B-JKIvRPxQ\u0026oe=671320B3\u0026_nc_sid=8b3546",
#         "config_width": 640,
#         "config_height": 640,
#     },
# ]
# for thumbnail in thumbnail_resources:
#     # Replace escaped characters
#     src = thumbnail["src"].replace("\\u0026", "&")
#     print(src + "\n")
