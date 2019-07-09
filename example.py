#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from instabot_py import InstaBot

bot = InstaBot(
        login="",
        password="",
        like_per_day=7019,
        comments_per_day=197,
        tag_list=["aviation", "sky", "avgeek", "aviationlovers", "boeing", "aircraft", "pilot", "airplane" ,"plane" ,"fly" ,"travel","flight","airport" ,"aviationphotography", "instagramaviation"
         ,"airbus"  ,"pilotlife", "flying", "instaaviation" ,"aviationgeek", "planespotting"
          ,"aviationdaily" ,"photography", "instaplane", "instagood", "planes", "love", "bhfyp","jet", "crewlife" ,"photooftheday" ,"clouds", "b", "cabincrew" ,"follow" ,"megaplane", "airline" ,"instagram"
           ,"lovers" , "landing" ,"pilots", "cessna", "airforce", "takeoff", "beautiful" ,"avporn" ,"planespotter" ,"military", "usa" , "sun", "crew", "boeinglovers", "picoftheday","flightattendant" ,"instatravel"
           , "avgeek", "aviation", "aircraft", "airplane", "boeing", "avporn", "instaplane", "pilot", "megaplane", "plane", "instaaviation", "airport", "airbus", "aviationlovers", "planeporn", "planespotting", "flying", "aviationphotography", "boeinglovers","pilotlife"
           , "flight", "aviationgeek", "planespotter", "fly", "crewlife","sky", "spotting", "travel", "planes", "instapilot"],
        tag_blacklist=['rain', 'thunderstorm'],
        user_blacklist={},
        max_like_for_one_tag=50,
        follow_per_day=402,
        follow_time=1 * 30,
        unfollow_per_day=402,
        unfollow_break_min=5,
        unfollow_break_max=20,
        log_mod=0,
        proxy='',
        # List of list of words, each of which will be used to generate comment
        # For example: "This shot feels wow!"
        comment_list=[["🤞","🙏","✌️"],
                      ['❤️','💜','💚','💙',"🧡","💛"]
                      ],
    # Use unwanted_username_list to block usernames containing a string
    # Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
    # 'free_followers' will be blocked because it contains 'free'
    unwanted_username_list=[
        "second",
        "stuff",
        "art",
        "project",
        "love",
        "life",
        "food",
        "blog",
        "free",
        "keren",
        "graphy",
        "indo",
        "art",
        "shop",
        "store",
        "sex",
        "toko",
        "jual",
        "online",
        "murah",
        "jam",
        "kaos",
        "case",
        "baju",
        "fashion",
        "corp",
        "tas",
        "butik",
        "grosir",
        "karpet",
        "sosis",
        "salon",
        "skin",
        "care",
        "cloth",
        "tech",
        "rental",
        "kamera",
        "beauty",
        "express",
        "kredit",
        "collection",
        "impor",
        "preloved",
        "follow",
        "follower",
        "gain",
        ".id",
        "_id",
        "bags",
    ],
    unfollow_whitelist=["example_user_1", "example_user_2"],
    # Enable the following to schedule the bot. Uses 24H
    # end_at_h = 23, # Hour you want the bot to stop
    # end_at_m = 30, # Minute you want the bot stop, in this example 23:30
    # start_at_h = 9, # Hour you want the bot to start
    # start_at_m = 10, # Minute you want the bot to start, in this example 9:10 (am).
)

bot.mainloop()
