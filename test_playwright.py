from src.browser.browser import Browser


browser = Browser()

page = browser.new_page()

page.goto(
    "https://www.croma.com/samsung-galaxy-s25-ultra-5g-12gb-ram-256gb-titanium-black-/p/313339",
    wait_until="networkidle"
)

print(page.title())

input("Press Enter...")

browser.close()