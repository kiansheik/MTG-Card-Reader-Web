from bottle import route, run, debug, template, request, static_file
import os

# Self Defined Matching Package which relies on cv2 and numpy
import matching

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


##################################################################################


# # Accept Request for Set Load
# @route('/load_set', method='POST')
# def load_set():
#     setBytes = request.body.read()  # has form of bytestring
#     setcode = setBytes.decode('utf-8')
#     return "load_set not fully implemented yet"

# Accept Request for Card Match
@route('/match_card', method='POST')
def match_card():
    #Read Image and Setcode from Request Form
    cam_png_uri = request.forms.get('png')
    setcode     = request.forms.get('setcode')
    card_name,card_url = matching.match(cam_png_uri,setcode)
    card_both = card_name+'$'+card_url
    return card_both

# Accept Request for List of Set Codes
@route('/set_list')
def set_list():
    setcodes = matching.setList()
    setstr = '$'.join(setcodes)
    return setstr


##################################################################################


# Serve Main Page
@route('/')
def index():
    return template('index.html', request=request)

# Serve Static Files
@route('/<filepath:path>')
def send_static(filepath):
    return static_file(filepath, root='.')


##################################################################################


run(host='localhost', port=8000, debug=True)
