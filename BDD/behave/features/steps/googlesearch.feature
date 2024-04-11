Feature: login as a direct user
  Scenario: login page
Given User is on the Login page of CM
And Enter a  username in the Username textbox
And Enter a password in the Password textbox
And Click on the 'Sign In' button
Then Verify the User gets successfully logged into the platform and the Dashboard page is displayed