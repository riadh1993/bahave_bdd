from behave import given, when, then
from numpy.testing import assert_equal

link = "https://qavbox.github.io/demo/dragndrop/"
element1_id = "draggable"
text_id = "dropText"
expected_message = "Dropped!"


@given('The user successfully navigates into the url https://qavbox.github.io/demo/dragndrop/')
def openUrl(context):
    context.dd.the_url(link)


@when('he drops the Drag me to my target box on the Dropped box')
def dragElement(context):
    context.dd.drag()


@then('he must see the message Dropped!')
def verifyMessage(context):
    text = context.dd.message()
    assert_equal(text, "Dro!")
