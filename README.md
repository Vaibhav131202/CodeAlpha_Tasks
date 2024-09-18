# CodeAlpha_Tasks
Task 1 - Hangman Game

Overview
This Python script implements a simple command-line version of the classic Hangman game. The player has 6 attempts to guess a randomly chosen word, letter by letter. Correct guesses reveal the letters in the word, while incorrect guesses reduce the number of remaining attempts. The game ends when the player successfully guesses the word or runs out of attempts.

Features:
1. Random Word Selection: The script randomly selects a word from a predefined list (python, JavaScript, HTML, CSS).
2. Letter Guessing: The player guesses one letter at a time.
3. Attempts Limit: The player starts with 6 attempts to guess the word.
4. Word Display: The word is displayed with underscores for unguessed letters and the correctly guessed letters filled in.
5. Game Over Conditions:
    Win: The player successfully guesses all letters of the word.
    Loss: The player uses up all 6 attempts without guessing the word.

How It Works:
1. Random Word Selection: A word is randomly chosen from a list of words.
2. Displaying Word: The word is displayed as underscores _ for unguessed letters, and correctly guessed letters are shown in their 
   positions.
3. User Input: The user guesses one letter per turn.
4. Guess Validation:
    If the letter has already been guessed, the user is informed.
    If the letter is in the word, it's added to the list of guessed letters.
    If the letter is not in the word, the number of attempts is reduced.
5. End Game: The game ends when the player guesses the word or runs out of attempts.


Task 2 - Stock PortFolio Tracker

Overview
This Python script provides a simple StockPortfolio class that allows users to manage a portfolio of stocks. Users can add, remove, and view stocks in their portfolio, as well as calculate the total value of the portfolio based on real-time stock prices retrieved from an API (dummy URL for demonstration).

Features:
1. Add Stocks: Add a stock and specify the number of shares.
2. Remove Stocks: Remove a specified number of shares or delete the stock entirely from the portfolio if all shares are sold.
3. View Portfolio: View the current portfolio, listing all stocks and the number of shares held.
4. Fetch Real-Time Stock Prices: Get the current stock price using an API.
5. Calculate Portfolio Value: Calculate the total value of the portfolio based on current stock prices.

How It Works:
1.Add Stock: Adds a stock symbol (e.g., 'AAPL') and the number of shares to the portfolio.
2. Remove Stock: Removes a specific number of shares of a given stock from the portfolio. If the number of shares removed equals the 
   total in the portfolio, the stock is removed entirely.
3. View Portfolio: Displays all stock symbols and the number of shares held.
4. Fetch Stock Price: Retrieves the stock price from a dummy API (needs to be replaced with a real stock price API).
5. Calculate Total Value: The total portfolio value is calculated by multiplying the current stock price by the number of shares held for each stock.


Task 3 - Basic ChatBot

Overview
This Python script demonstrates a basic chatbot using the nltk library's Chat module. The chatbot is capable of responding to simple predefined input patterns, such as greetings and questions about its name or state of being. It's a simple, rule-based chatbot that responds to specific keywords or phrases using regular expressions.

Features:
1. Predefined Responses: The chatbot responds to simple greetings and common conversational questions using predefined responses.
2. Pattern Matching: Uses regular expressions to identify specific user inputs and provide appropriate responses.
3. Conversation Mode: The chatbot remains in conversation mode until the user types "bye."

How It Works:
1. Pairs: The chatbot's responses are defined in pairs, a list of input patterns and their corresponding responses.
   Example: If the user types "hi" or "hello", the chatbot will respond with either "Hello!" or "Hi there!"
2. Reflections: The reflections dictionary from the nltk.chat.util module is used to map pronouns (e.g., "I" -> "you") in conversations 
   to make responses more natural.
3. Chat Instance: A Chat object is created with the defined pairs and reflections, which enables the chatbot to respond to user input.
