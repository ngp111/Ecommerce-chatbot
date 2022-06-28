import json

data = {
  "richContent": [
    [
      {
        "text": "YES",
        "icon": {
          "color": "#878fac"
        },
        "type": "button",
        "event": {
          "parameters": {
            "category": "Mobiles"
          },
          "name": "GET_mobile1",
          "languageCode": "en"
        }
      },
      {
        "icon": {
          "color": "#878fac"
        },
        "event": {
          "name": "GET_mobile2",
          "languageCode": "en",
          "parameters": {
            "category": "Mobiles"
          }
        },
        "type": "button",
        "text": "NO"
      }
    ]
  ]
}
mobile_features_continue = json.dumps(data)
data = {
  "richContent": [
    [
      {
        "type": "button",
        "text": "YES",
        "event": {
          "languageCode": "en",
          "name": "GET_recom",
          "parameters": {
            "category": "Mobiles"
          }
        },
        "icon": {
          "color": "#878fac"
        }
      },
      {
        "text": "NO",
        "icon": {
          "color": "#878fac"
        },
        "event": {
          "name": "GET_top5",
          "parameters": {
            "category": "Mobiles"
          },
          "languageCode": "en"
        },
        "type": "button"
      }
    ]
  ]
}
satisfied_mobile = json.dumps(data)
data = {
  "richContent": [
    [
      {
        "icon": {
          "color": "#878fac"
        },
        "event": {
          "parameters": {
            "category": "Mobiles"
          },
          "languageCode": "en",
          "name": "GET_recom"
        },
        "type": "button",
        "text": "YES"
      },
      {
        "event": {
          "name": "GET_recom",
          "parameters": {
            "category": "Mobiles"
          },
          "languageCode": "en"
        },
        "type": "button",
        "text": "NO",
        "icon": {
          "color": "#878fac"
        }
      }
    ]
  ]
}
bestsellers_display = json.dumps(data)
data = {
  "richContent": [
    [
      {
        "type": "button",
        "text": "YES",
        "icon": {
          "color": "#878fac"
        },
        "event": {
          "parameters": {
            "category": "Tablets"
          },
          "languageCode": "en",
          "name": "GET_tablet1"
        }
      },
      {
        "type": "button",
        "event": {
          "parameters": {
            "category": "Tablets"
          },
          "languageCode": "en",
          "name": "GET_tablet2"
        },
        "text": "NO",
        "icon": {
          "color": "#878fac"
        }
      }
    ]
  ]
}
tablet_features_continue = json.dumps(data)
data = {
  "richContent": [
    [
      {
        "event": {
          "name": "GET_recom",
          "parameters": {
            "category": "Tablets"
          },
          "languageCode": "en"
        },
        "type": "button",
        "text": "YES",
        "icon": {
          "color": "#878fac"
        }
      },
      {
        "icon": {
          "color": "#878fac"
        },
        "text": "NO",
        "event": {
          "parameters": {
            "category": "Tablets"
          },
          "name": "GET_top5",
          "languageCode": "en"
        },
        "type": "button"
      }
    ]
  ]
}
satisfied_tablet = json.dumps(data)
data = {
  "richContent": [
    [
      {
        "event": {
          "parameters": {
            "category": "YES"
          },
          "languageCode": "en",
          "name": "GET_power1"
        },
        "text": "YES",
        "type": "button",
        "icon": {
          "color": "#878fac"
        }
      },
      {
        "icon": {
          "color": "#878fac"
        },
        "type": "button",
        "event": {
          "name": "GET_power2",
          "languageCode": "en",
          "parameters": {
            "category": "NO"
          }
        },
        "text": "NO"
      }
    ]
  ]
}
powerbank_features_continue = json.dumps(data)
data = {
  "richContent": [
    [
      {
        "event": {
          "name": "GET_recom",
          "parameters": {
            "category": "Powerbanks"
          },
          "languageCode": "en"
        },
        "type": "button",
        "text": "YES",
        "icon": {
          "color": "#878fac"
        }
      },
      {
        "icon": {
          "color": "#878fac"
        },
        "text": "NO",
        "event": {
          "parameters": {
            "category": "Powerbanks"
          },
          "name": "GET_top5",
          "languageCode": "en"
        },
        "type": "button"
      }
    ]
  ]
}
satisfied_powerbank = json.dumps(data)
data = {
  "richContent": [
    [
      {
        "text": "YES",
        "event": {
          "name": "GET_desktop1",
          "parameters": {
            "category": "Desktops"
          },
          "languageCode": "en"
        },
        "icon": {
          "color": "#878fac"
        },
        "type": "button"
      },
      {
        "event": {
          "parameters": {
            "category": "Desktops"
          },
          "name": "GET_desktop2",
          "languageCode": "en"
        },
        "icon": {
          "color": "#878fac"
        },
        "text": "NO",
        "type": "button"
      }
    ]
  ]
}
desktop_features_continue = json.dumps(data)
data = {
  "richContent": [
    [
      {
        "text": "YES",
        "type": "button",
        "icon": {
          "color": "#878fac"
        },
        "event": {
          "name": "GET_recom",
          "parameters": {
            "category": "Desktops"
          },
          "languageCode": "en"
        }
      },
      {
        "text": "NO",
        "icon": {
          "color": "#878fac"
        },
        "event": {
          "parameters": {
            "category": "Desktops"
          },
          "name": "GET_top5",
          "languageCode": "en"
        },
        "type": "button"
      }
    ]
  ]
}
satisfied_desktop = json.dumps(data)
data = {
  "richContent": [
    [
      {
        "text": "YES",
        "type": "button",
        "event": {
          "name": "GET_laptop1",
          "languageCode": "en",
          "parameters": {
            "category": "Laptops"
          }
        },
        "icon": {
          "color": "#878fac"
        }
      },
      {
        "type": "button",
        "text": "NO",
        "icon": {
          "color": "#878fac"
        },
        "event": {
          "name": "GET_laptop2",
          "languageCode": "en",
          "parameters": {
            "category": "Laptops"
          }
        }
      }
    ]
  ]
}
laptop_features_continue = json.dumps(data)
data = {
  "richContent": [
    [
      {
        "event": {
          "languageCode": "en",
          "parameters": {
            "category": "Laptops"
          },
          "name": "GET_rec"
        },
        "text": "YES",
        "type": "button",
        "icon": {
          "color": "#878fac"
        }
      },
      {
        "icon": {
          "color": "#878fac"
        },
        "event": {
          "languageCode": "en",
          "parameters": {
            "category": "Laptops"
          },
          "name": "GET_top5"
        },
        "text": "NO",
        "type": "button"
      }
    ]
  ]
}
satisfied_laptop = json.dumps(data)
data = {
  "richContent": [
    [
      {
        "event": {
          "parameters": {
            "category": "Smart Watches"
          },
          "languageCode": "en",
          "name": "GET_wear1"
        },
        "text": "YES",
        "icon": {
          "color": "#878fac"
        },
        "type": "button"
      },
      {
        "type": "button",
        "event": {
          "name": "GET_wear2",
          "languageCode": "en",
          "parameters": {
            "category": "Smart Watches"
          }
        },
        "text": "NO",
        "icon": {
          "color": "#878fac"
        }
      }
    ]
  ]
}
watch_features_continue = json.dumps(data)
data = {
  "richContent": [
    [
      {
        "type": "button",
        "icon": {
          "color": "#878fac"
        },
        "event": {
          "languageCode": "en",
          "parameters": {
            "category": "Drives/Storage"
          },
          "name": "GET_drive1"
        },
        "text": "YES"
      },
      {
        "event": {
          "name": "GET_drive2",
          "parameters": {
            "category": "Drives/Storage"
          },
          "languageCode": "en"
        },
        "text": "NO",
        "icon": {
          "color": "#878fac"
        },
        "type": "button"
      }
    ]
  ]
}
drive_features_continue = json.dumps(data)
data = {
  "richContent": [
    [
      {
        "event": {
          "parameters": {
            "category": "Drives/Storage"
          },
          "languageCode": "en",
          "name": "GET_recom"
        },
        "type": "button",
        "icon": {
          "color": "#878fac"
        },
        "text": "YES"
      },
      {
        "text": "NO",
        "event": {
          "languageCode": "en",
          "parameters": {
            "category": "Drives/Storage"
          },
          "name": "GET_top5"
        },
        "icon": {
          "color": "#878fac"
        },
        "type": "button"
      }
    ]
  ]
}
satisfied_drive = json.dumps(data)
data = {
  "richContent": [
    [
      {
        "event": {
          "name": "GET_recom",
          "languageCode": "en",
          "parameters": {
            "category": "Smart Watches"
          }
        },
        "text": "YES",
        "type": "button",
        "icon": {
          "color": "#878fac"
        }
      },
      {
        "type": "button",
        "event": {
          "languageCode": "en",
          "name": "GET_top5",
          "parameters": {
            "category": "Smart Watches"
          }
        },
        "icon": {
          "color": "#878fac"
        },
        "text": "NO"
      }
    ]
  ]
}
satisfied_watch = json.dumps(data)
data = {
  "richContent": [
    [
      {
        "options": [
          {
            "image": {
              "src": {
                "rawUrl": "https://static.digit.in/product/97036a3ef3b60f99a34cf0e16fb867896146a6e2.jpeg?tr=w-1200"
              }
            },
            "text": "Mobile,Tablets & more   "
          },
          {
            "text": "Computers & Accessories",
            "image": {
              "src": {
                "rawUrl": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Desktop_computer_clipart_-_Yellow_theme.svg/1200px-Desktop_computer_clipart_-_Yellow_theme.svg.png"
              }
            }
          },
          {
            "text": "Cameras ",
            "image": {
              "src": {
                "rawUrl": "https://static.bhphoto.com/images/images1000x1000/1536120359_1433711.jpg"
              }
            }
          },
          {
            "text": "TV, Audio, Musical Instruments",
            "image": {
              "src": {
                "rawUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT82n-GhpWR-d_-KHvHLYyLVBR5dJtof0jEEA&usqp=CAU"
              }
            }
          }
        ],
        "type": "chips"
      }
    ]
  ]
}
main = json.dumps(data)
data = {
  "richContent": [
    [
      {
        "options": [
          {
            "image": {
              "src": {
                "rawUrl": "https://www.pngitem.com/pimgs/m/256-2567281_main-menu-button-png-transparent-png.png"
              }
            },
            "text": "Main menu"
          }
        ],
        "type": "chips"
      }
    ]
  ]
}
main_redirect = json.dumps(data)
data = {
  "richContent": [
    [
      {
        "type": "chips",
        "options": [
          {
            "image": {
              "src": {
                "rawUrl": "https://i.pinimg.com/originals/32/3e/3b/323e3b47f07fa1fb0a4b2ecb03b2c965.png"
              }
            },
            "text": "It was not good"
          },
          {
            "image": {
              "src": {
                "rawUrl": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Emoji_u263a.svg/1200px-Emoji_u263a.svg.png"
              }
            },
            "text": "It was nice"
          },
          {
            "text": "It was great",
            "image": {
              "src": {
                "rawUrl": "https://media-assets-03.thedrum.com/cache/images/thedrum-prod/public-news-tmp-980-emoji--default--600.png"
              }
            }
          }
        ]
      }
    ]
  ]
}
feedback = json.dumps(data)
