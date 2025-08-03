from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = "input[data-test='username']"
        self.password_input = "input[data-test='password']"
        self.login_button = "input[data-test='login-button']"
        self.products_text = "text=Products"

    def goto(self, base_url):
        self.page.goto(base_url)

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def is_products_visible(self):
        return self.page.is_visible(self.products_text)
