{
    "node": {
        "name": "raspberry-pi",
        "composition-file": "composition.js",
        "auto-start": true,
        "top-composer": false
    },
    "application-id": "temper",
    "transport-xmpp": {
        "xmpp-server": "charmanson.isandlatech.com",
        "xmpp-port": 5222,
        "xmpp-jid": "",
        "xmpp-password": ""
    },
    "transport": [
        "xmpp"
    ]
}
