#!/usr/bin/python
#-- Content-Encoding: UTF-8 --
"""
This bundle provides a component that is a simple implementation of the
Dictionary service. It contains some English words.

:authors: Shadi Abras, Thomas Calmant
:copyright: Copyright 2013, isandlaTech
:license:  Apache Software License 2.0
"""

# iPOPO decorators
from pelix.ipopo.decorators import ComponentFactory, Property, Provides, \
    Validate, Invalidate

import logging

_logger = logging.getLogger("spellchecker.spell_dictionary_EN")

# Name the iPOPO component factory
@ComponentFactory("spell_dictionary_en_factory")
# This component provides a dictionary service
@Provides("spell_dictionary_service")
# It is the English dictionary
@Property("_language","language","EN")
class SpellDictionary(object):
    """
    Implementation of a spell dictionary, for French language.
    """
    def __init__(self):
        """
        Declares members, to respect PEP-8.
        """
        self.dictionary = None

    @Validate
    def validate(self, context):
        """
        The component is validated. This method is called right before the
        provided service is registered to the framework.
        """
        _logger.info("SpellDictionary EN validated")
        self.dictionary = {"hello" , "world", "welcome", "to", "the", "ipopo", "tutorial"}

    @Invalidate
    def invalidate(self, context):
        """
        The component has been invalidated. This method is called right after
        the provided service has been removed from the framework.
        """
        self.dictionary = None

    def check_word(self, word):
        """
        Determines if the given word is contained in the dictionary.

        @param word the word to be checked.
        @return True if the word is in the dictionary, False otherwise.
        """
        word = word.lower().strip()
        return not word or word in self.dictionary
