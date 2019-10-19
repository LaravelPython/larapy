from Chamak.Foundation.app import Application
from Chamak.view.view import View


class HomeController:

    def index(self):
        return View().view('welcome')
