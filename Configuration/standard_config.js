[
  {
    "module": "updatenotification",
    "position": "top_bar"
  },
  {
    "module": "clock",
    "position": "top_left"
  },
  {
    "module": "calendar",
    "header": "US Holidays",
    "position": "top_left",
    "config": {
      "calendars": [
        {
          "symbol": "calendar-check",
          "url": "webcal://www.calendarlabs.com/ical-calendar/ics/76/US_Holidays.ics"
        }
      ]
    }
  },
  {
    "module": "compliments",
    "position": "lower_third"
  },
  {
    "module": "newsfeed",
    "position": "bottom_bar",
    "config": {
      "feeds": [
        {
          "title": "New York Times",
          "url": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
        }
      ],
      "showSourceTitle": true,
      "showPublishDate": true,
      "broadcastNewsFeeds": true,
      "broadcastNewsUpdates": true
    }
  }
]