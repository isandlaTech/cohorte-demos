{
    "transport-xmpp": {
        "xmpp-port": 5222,
        "xmpp-password": "Bender",
        "xmpp-jid": "bot@charmanson.isandlatech.com",
        "xmpp-server": "charmanson.isandlatech.com"
    },
    "application-id": "temper",
    "transport": [
        "xmpp",
        "http"
    ],
    "node": {
        "top-composer": true,
        "auto-start": true,
        "shell-admin": 9001,
        "composition-file": "composition.js",
        "name": "gateway-node",
        "web-admin": 9000
    }
}