
@one
Feature: making a slide

  Scenario: sliding the button to 100%
    Given the user navigates successfully to the url https://qavbox.github.io/demo/dragndrop/
    When he drags the button to the left
    Then he must see the slider draged to the end