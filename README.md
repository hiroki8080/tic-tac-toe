# tic-tac-toe

This is a serverless little game sample.
You can play games with two players via different browsers.
It uses that the temporary data is held within the time-out period.

# How to use it?

Set up a simple Lambda function and API Gateway and access the GET URL.

## Game Start
- Player A accesses the API URL in the browser.
- Player B accesses the API URL in the browser.
- To reset the data, check the Reset check box and click the Submit button.

## Game play procedure
- Player A checks one of the squares and clicks the submit button.
- Player B will redraw the screen by clicking the Submit button.
- Player B checks one of the squares and clicks the submit button.
- Player A will redraw the screen by clicking the Submit button.
- Repeat the above steps.

## Notes

Since this game is a sample of serverless game, there is no processing such as winning / losing judgment.

# License

MIT License (MIT)