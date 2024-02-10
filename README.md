This code was fixed by adding route that handles /api/v1/status and retuns OK
to test this code cd to status_server/api/v1


the run the server by typing python -m api.v1.app

use an other terminal or the browser to test

curl -XGET http://0.0.0.0:5000/api/v1/status

