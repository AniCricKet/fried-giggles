import uuid, string, random
from words import wordlist


sessions = {}

def generate_gamestate(word, guesses):
    output = ""
    for character in word:
        if character in guesses:
            output += character
        else:
            output+= ("_ ")
    return (output)

def format_output(session):
    session = dict(session)
    session.pop('word')
    return session


def newSession():
    localID = str(uuid.uuid4())
    word = random.choice(list(wordlist.keys()))
    definition = wordlist[word]
    correctguesses = []
    incorrectguesses = []
    gamestate = generate_gamestate(word, correctguesses)

    bodyparts = 0
    session = { 'context': localID, 'word': word, 'definition': definition, 'gamestate': gamestate, 'correctguesses': correctguesses, 
                'incorrectguesses': incorrectguesses, 'bodyparts': bodyparts, 'status': 'OK', 'reason': 'Game in progress'}

    sessions[localID] = session
    return(format_output(session))

def keypress(context, key):
    session = sessions.get(context)
    key = key.lower()
    if (session == None):
        return {"status": 'ERR', "reason": "Invalid Session"}
    print("Session = " + str(session))
    print("Key = " + key)
    if ((len(key) != 1) or (key not in string.ascii_lowercase)):
        err = {"status": 'ERR', "reason": "Invalid Key (Single lowercase character only"}
        session.update(err)
        return(format_output(session)) 
    if ((key in session['correctguesses']) or (key in session['incorrectguesses'])):
        err = {"status": 'ERR', "reason": "Letter already guessed"}
        session.update(err)
        return(format_output(session))
    if key in session['word']:
        # Letter correctly guessed
        session['correctguesses'].append(key)
        session['status'] = 'OK'
        session['reason'] = 'Game in progress'
        session['gamestate'] = generate_gamestate(session['word'], session['correctguesses'])
        if (session['gamestate'] == session['word']):
            session['status'] = 'WIN'
            session['reason'] = 'Congratulations! You have won!'
    else:
        session['bodyparts'] += 1
        session['incorrectguesses'].append(key)
        if (session['bodyparts'] <= 5):
            session['status'] = 'OK'
            session['reason'] = 'Game in progress'
        else:
            session['status'] = 'END'
            session['reason'] = 'You lose! The correct word was ' + session['word'] + '.'
    print("Session = " + str(session))
    return(format_output(session))
