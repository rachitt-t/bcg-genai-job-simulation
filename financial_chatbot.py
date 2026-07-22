def simple_chatbot(user_query):
    query = user_query.lower()

    if "microsoft revenue" in query:
        return "Microsoft's total revenue in 2025 was 281,724 million USD."

    elif "apple revenue" in query:
        return "Apple's total revenue in 2025 was 416,161 million USD."

    elif "tesla revenue" in query:
        return "Tesla's total revenue in 2025 was 94,827 million USD."

    elif "microsoft net income" in query:
        return "Microsoft's net income in 2025 was 101,832 million USD."

    elif "apple net income" in query:
        return "Apple's net income in 2025 was 112,010 million USD."

    elif "tesla net income" in query:
        return "Tesla's net income in 2025 was 3,855 million USD."

    elif "best revenue" in query:
        return "Apple generated the highest revenue among the three companies in 2025."

    elif "operating cash flow" in query:
        return (
            "Operating Cash Flow (2025):\n"
            "Microsoft: 136,162 million USD\n"
            "Apple: 111,482 million USD\n"
            "Tesla: 14,747 million USD"
        )

    else:
        return "Sorry, I can only answer predefined financial questions."


print("Financial Chatbot")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    print("Bot:", simple_chatbot(user_input))