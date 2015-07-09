#!/bin/sh

ps | grep cohorte | cut -f 1 -d \ | xargs kill -9
