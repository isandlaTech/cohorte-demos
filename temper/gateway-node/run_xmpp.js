{
    "node": {                
        "name": "gateway-node",           
        "top-composer": true,
        "composition-file": "composition.js",
        "web-admin": 9000,     
        "shell-admin": 9001
    },
    "transport": [
        "xmpp"
    ],
    "transport-xmpp": {
      "xmpp-server": "charmanson.isandlatech.com",
      "xmpp-user-jid" : "bot@charmanson.isandlatech.com",
      "xmpp-user-password" : "Bender",
      "xmpp-port": 5222
    }
}
