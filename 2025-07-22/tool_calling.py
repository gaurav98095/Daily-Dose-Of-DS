import yfinance as yf
import ollama


def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    return stock.history(period='1d')['Close'].iloc[-1]



response = ollama.chat(
    'deepseek-r1:1.5b',
    messages=[{'role': 'user', 'content': 'What is the stock price of Apple?'}],
    tools=[get_stock_price],
)


available_functions = {
    'get_stock_price': get_stock_price,
}

for tool in response.message.tool_calls or []:
    function_to_call = available_functions.get(tool.function.name)

    if function_to_call:
        print('Arguments:', tool.function.arguments)
        print('Function output:', function_to_call(**tool.function.arguments))
    else:
        print('Function not found:', tool.function.name)
