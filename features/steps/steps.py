import random
from behave import *
from twentyone import *


@given("a dealer")
def step_impl(context):
    context.dealer = Dealer()


@when("the round starts")
def step_impl(context):
    context.dealer.new_round()


@then("the dealer gives itself two cards")
def step_impl(context):
    assert (len(context.dealer.hand) == 2)


_cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


def _next_card():
    return random.choice(_cards)
