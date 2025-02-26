import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()

    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.goto("https://probable-disco-5567x7577w4c4rw-5173.app.github.dev/")
    # page.get_by_role("link", name="Об университете").click()
    # page.get_by_role("link", name="Поступающим").click()
    # page.get_by_role("link", name="О целевом обучении").click()
    # page.get_by_role("link", name="Правила приёма на 2025/2026г").click()

    context.tracing.stop(path="trace.zip")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)