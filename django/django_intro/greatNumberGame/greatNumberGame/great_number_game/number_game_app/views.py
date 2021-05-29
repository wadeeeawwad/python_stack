from django.shortcuts import render, redirect
from random import randint

title = "Great Number Game"
max_guesses = 5
high_scores = [
	{ 'name': '---', 'num_guesses': 999},
	{ 'name': '---', 'num_guesses': 999},
	{ 'name': '---', 'num_guesses': 999},
	{ 'name': '---', 'num_guesses': 999},
	{ 'name': '---', 'num_guesses': 999},
	{ 'name': '---', 'num_guesses': 999},
	{ 'name': '---', 'num_guesses': 999},
	{ 'name': '---', 'num_guesses': 999},
	{ 'name': '---', 'num_guesses': 999},
	{ 'name': '---', 'num_guesses': 999}
]

def index(request):
	if not ('goal' in request.session and 'guess_count' in request.session and 'context' in request.session and request.session['goal'] > 0):
		print('***redirecting to /start')
		return redirect('/start')
	else:
		context = request.session['context']
		print(f"goal = {request.session['goal']}")
		print(f"guess_count = {request.session['guess_count']}")
		print(f"context = {request.session['context']}")
		print("***rendering index.html ...")
		return render(request, 'index.html', context)

def start(request):
	request.session['goal'] = randint(1, 100)
	request.session['guess_count'] = 0
	request.session['context'] = {
		'title': title,
		'alertColor': '',
		'alertVisibility': 'd-none',
		'alertHeader': '',
		'alertMessage': '',
		'paBtnVisibility': 'd-none',
		'addLeaderFormVisibility': 'd-none',
		'guessFormVisibility': 'd-block'
	}
	if not 'highScores' in request.session:
		request.session['highScores'] = high_scores
	request.session.save()
	print('***redirecting back to /')
	return redirect('/')

def process(request):
	request.session['guess_val'] = int(request.POST['guessVal'])
	request.session['guess_count'] += 1
	if request.session['guess_val'] == request.session['goal']:
		print('***redirecting to /correct')
		return redirect('/correct')
	else:
		print('***redirecting to /incorrect')
		return redirect('/incorrect')

def correct(request):
	request.session['context'] = {
		'title': title,
		'alertColor': 'alert-success',
		'alertVisibility': 'd-block py-4',
		'alertHeader': f"{str(request.session['goal'])} was the number!",
		'alertMessage': f"Number of guesses: {str(request.session['guess_count'])}",
		'paBtnVisibility': 'd-block',
		'addFormVisibility': 'd-none',
		'guessFormVisibility': 'd-none'
	}
	for element in request.session['highScores']:
		if element['num_guesses'] > request.session['guess_val']:
			request.session['context']['paBtnVisibility'] = 'd-none'
			request.session['context']['addLeaderFormVisibility'] = 'd-block'
			break
	request.session.save()
	print('***redirecting back to /')
	return redirect('/')

def incorrect(request):
	if int(request.session['guess_count']) >= max_guesses:
		request.session['context'] = {
			'title': title,
			'alertColor': 'alert-danger',
			'alertVisibility': 'd-block py-4',
			'alertHeader': 'You Lose!',
			'alertMessage': f"You reached the maximum number of guesses ({max_guesses}).",
			'paBtnVisibility': 'd-block',
			'addLeaderFormVisibility': 'd-none',
			'guessFormVisibility': 'd-none'
		}
	else:
		if request.session['guess_val'] < request.session['goal']:
			request.session['context'] = {
				'title': title,
				'alertColor': 'alert-danger',
				'alertVisibility': 'd-block py-5',
				'alertHeader': 'Too low!',
				'alertMessage': f"Number of guesses: {str(request.session['guess_count'])}",
				'paBtnVisibility': 'd-none',
				'addLeaderFormVisibility': 'd-none',
				'guessFormVisibility': 'd-block'
			}
		elif request.session['guess_val'] > request.session['goal']:
			request.session['context'] = {
				'title': title,
				'alertColor': 'alert-danger',
				'alertVisibility': 'd-block py-5',
				'alertHeader': 'Too high!',
				'alertMessage': f"Number of guesses: {str(request.session['guess_count'])}",
				'paBtnVisibility': 'd-none',
				'addLeaderFormVisibility': 'd-none',
				'guessFormVisibility': 'd-block'
			}
	request.session.save()
	print('***redirecting back to /')
	return redirect('/')

def play_again(request):
	del request.session['goal']
	del request.session['guess_count']
	del request.session['context']
	print('***redirecting back to /')
	return redirect('/')

def add_high_score(request):
	temp = { 'name': request.POST['name'], 'num_guesses': request.session['guess_count'] }
	x = len(request.session['highScores']) - 1
	while x >= 0:
		if request.session['highScores'][x]['num_guesses'] < temp['num_guesses']:
			break
		x -= 1
	x += 1
	if x >= 0 and x < len(request.session['highScores']):
		print(f"inserting {temp['name']}'s high score at index {x}")
		request.session['highScores'].insert(x, temp)
		request.session['context']['paBtnVisibility'] = 'd-block'
		request.session['context']['addLeaderFormVisibility'] = 'd-none'
	if len(request.session['highScores']) > 10:
		request.session['highScores'].pop()
	request.session.save()
	print('***redirecting to /leaderboard')
	return redirect('/leaderboard')

def leaderboard(request):
	context = {
		'title': title
	}
	print(f"highScores = {request.session['highScores']}")
	print('***rendering leaderboard.html')
	return render(request, 'leaderboard.html', context)

def reset(request):
	print('***RESETTING SESSION - calling flush()')
	request.session.flush()
	print('***redirecting back to /')
	return redirect('/')