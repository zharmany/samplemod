# -*- coding: utf-8 -*-
from .helpers import get_answer
from .helpers import BaseClass1, BaseClass2

def get_hmm():
    """Get a thought."""
    return 'hmmm...'

def hmm():
    """Contemplation..."""
    if get_answer():
        print(get_hmm())

BaseClasses = [BaseClass1, BaseClass2]

class MyClass(*BaseClasses):
    """This class relies on BaseClass helper methods."""

    def message(self):
        self.message1()
        self.message2()
