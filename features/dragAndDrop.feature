@wip

Feature: The user must drag and drop web elements

  Scenario: : dragging and dropping web elements
    Given The user successfully navigates into the url https://qavbox.github.io/demo/dragndrop/
    When he drops the Drag me to my target box on the Dropped box
    Then he must see the message Dropped!