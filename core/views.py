# core/views.py

from django.http import JsonResponse

def fibonacci(request, n):
    try:
        n = int(n)
        if n < 0:
            return JsonResponse({'error': 'Please provide a non-negative integer.'})
        
        fib_sequence = [0, 1]
        for i in range(2, n+1):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        
        return JsonResponse({'fibonacci_sequence': fib_sequence[:n+1]})
    except ValueError:
        return JsonResponse({'error': 'Please provide a valid integer.'})

def hello_hovo(request):
    return JsonResponse({'message': 'Hello Hovo!'})

def word_definition(request, word):
    # Replace with your actual word definition logic
    definitions = {
        'django': 'A high-level Python web framework that encourages rapid development and clean, pragmatic design.',
        'python': 'An interpreted, high-level, general-purpose programming language.',
        # Add more word definitions as needed
    }
    
    if word in definitions:
        return JsonResponse({'word': word, 'definition': definitions[word]})
    else:
        return JsonResponse({'error': 'Word not found in dictionary.'})
