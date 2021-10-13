from behave import given, when, then
from numpy.testing import assert_equal

link = "https://qavbox.github.io/demo/dragndrop/"
element2_xpath = "//body[1]/form[1]/fieldset[1]/div[1]/div[5]/input[1]"
message_id = "range"
message = "100"


@given(u'the user navigates successfully to the url https://qavbox.github.io/demo/dragndrop/')
def openUrl(context):
    context.dd.the_url(link)


@when(u'he drags the button to the left')
def slider(context):
    context.dd.slider()


@then(u'he must see the slider draged to the end')
def the_message(context):
    message = context.dd.the_message()
    assert_equal(message, "10")
