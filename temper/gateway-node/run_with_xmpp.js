{
    "node": {                
        "name": "gateway-node",           
        "composition-file": "composition.js",
        "web-admin": 9000,     
        "shell-admin": 9001
    },
    "transport": [
        "xmpp", "http"
    ],
    "transport-xmpp": {
        "xmpp-server": "charmanson.isandlatech.com",
        "xmpp-port": 5222,
        "xmpp-password": "Bender",
        "xmpp-jid": "bot@charmanson.isandlatech.com"
    },
}