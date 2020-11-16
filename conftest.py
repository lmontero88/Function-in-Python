import sys, os, json
if os.path.isdir("./.venv/lib/"):
    sys.path.append('null/site-packages')

def pytest_addoption(parser):
    parser.addoption("--stdin", action="append", default=[],
        help="json with the stdin to pass to test functions")

def pytest_generate_tests(metafunc):
    if 'stdin' in metafunc.fixturenames:
        metafunc.parametrize("stdin",metafunc.config.getoption('stdin'))

    if 'app' in metafunc.fixturenames:
        try:
          sys.path.append('.learn/dist')
          import cached_app
          metafunc.parametrize("app",[cached_app.execute_app])
        except SyntaxError:
          metafunc.parametrize("app",[lambda : None])
        except ImportError:
          metafunc.parametrize("app",[cached_app])
        except AttributeError:
          metafunc.parametrize("app",[cached_app])

    if 'config' in metafunc.fixturenames:
        metafunc.parametrize("config", [json.loads('{"port":3000,"address":"https://accf384e-bce7-479d-8f07-ca85705630e8.ws-us02.gitpod.io","editor":"gitpod","configPath":{"config":"bc.json","base":".learn","exercises":"./exercises","output":".learn/dist"},"outputPath":"./.learn/dist","publicPath":"/preview","grading":"isolated","ignoreRegex":null,"webpack_template":null,"disable_grading":false,"onCompilerSuccess":null,"language":"python3","compiler":"python3","tester":"pytest","actions":["run","test","reset"],"title":"Learn Python Functions Interactively","repository":"https://github.com/4GeeksAcademy/python-functions-programming-exercises","preview":"https://github.com/4GeeksAcademy/python-functions-programming-exercises/blob/master/preview.gif?raw=true","description":"Learn and master functional programing by doing auto-graded interactive exercises.","duration":10,"difficulty":"easy","video-solutions":false,"graded":true,"session":178411343948841060,"exercises":[{"slug":"01-hello-world","title":"01-hello-world","done":false,"path":"exercises/01-hello-world","translations":["es","us"],"graded":false},{"slug":"02-Hello-World","title":"02-Hello-World","done":true,"path":"exercises/02-Hello-World","translations":["es","us"],"graded":true},{"slug":"03-What-is-a-function","title":"03-What-is-a-function","done":true,"path":"exercises/03-What-is-a-function","translations":["es","us"],"graded":true},{"slug":"04-Call-a-function","title":"04-Call-a-function","done":true,"path":"exercises/04-Call-a-function","translations":["es","us"],"graded":true},{"slug":"05-Defining-vs-Calling-a-function","title":"05-Defining-vs-Calling-a-function","done":false,"path":"exercises/05-Defining-vs-Calling-a-function","translations":["es","us"],"graded":true},{"slug":"06-lambda-functions","title":"06-lambda-functions","done":false,"path":"exercises/06-lambda-functions","translations":["es","us"],"graded":true},{"slug":"07-lambda-function-two","title":"07-lambda-function-two","done":true,"path":"exercises/07-lambda-function-two","translations":["es","us"],"graded":true},{"slug":"08-Function-that-returns","title":"08-Function-that-returns","done":true,"path":"exercises/08-Function-that-returns","translations":["es","us"],"graded":true},{"slug":"09-Function-parameters","title":"09-Function-parameters","done":true,"path":"exercises/09-Function-parameters","translations":["es","us"],"graded":true},{"slug":"10-Array-Methods","title":"10-Array-Methods","done":false,"path":"exercises/10-Array-Methods","translations":["es","us"],"graded":true}]}')])
