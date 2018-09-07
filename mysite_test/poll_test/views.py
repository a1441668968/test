from django.shortcuts import render


def polls_index(request):
    return render(request, 'polls/poll_test_index.html')
