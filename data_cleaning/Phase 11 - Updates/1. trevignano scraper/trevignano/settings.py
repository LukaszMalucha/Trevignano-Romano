# -*- coding: utf-8 -*-

BOT_NAME = 'trevignano'

SPIDER_MODULES = ['trevignano.spiders']
NEWSPIDER_MODULE = 'trevignano.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False


HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 24 * 60 * 60

