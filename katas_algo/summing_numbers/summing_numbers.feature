Feature: Summing elements of array to find two numbers giving a sum

    Scenario: Finding numbers if they exists
        Given an array of numbers
        And a searched sum result
        When I search for two numbers summing up to result
        Then get an array of pairs summing to result

    Scenario: Getting empty array if no numbers sum-up to result
        Given an array of numbers
        And a searched sum result
        When I search for two numbers summing up to result
        Then get empty array if no sum give the result