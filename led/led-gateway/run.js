{
    "transport": [
        "http",
        "xmpp"
    ],
    "transport-xmpp": {
        "xmpp-password": "Bender",
        "xmpp-server": "charmanson.isandlatech.com",
        "xmpp-jid": "bot@charmanson.isandlatech.com",
        "xmpp-port": 5222
    },
    "application-id": "led",
    "transport-http": {
        "http-ipv": 6
    },
    "node": {
        "composition-file": "composition.js",
        "auto-start": true,
        "top-composer": true,
        "use-cache": false,
        "interpreter": "python3",
        "name": "led-gateway",
        "web-admin": 9000,
        "recomposition-delay": 120,
        "shell-admin": 9001
    }
}
