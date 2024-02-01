import asyncio
from playwright.async_api import async_playwright

from personalurl import Personnal

SBR_WS_CDP = Personnal.url_scrapp_brow


async def run(pw):
    print('Connecting to Scraping Browser...')
    browser = await pw.chromium.connect_over_cdp(SBR_WS_CDP)
    try:
        page = await browser.new_page()
        print('Connected! Navigating to https://example.com...')
        await page.goto('https://example.com')
        # CAPTCHA handling: If you're expecting a CAPTCHA on the target page, use the following code snippet to check the status of Scraping Browser's automatic CAPTCHA solver
        # client = await page.context.new_cdp_session(page)
        # print('Waiting captcha to solve...')
        # solve_res = await client.send('Captcha.waitForSolve', {
        #     'detectTimeout': 10000,
        # })
        # print('Captcha solve status:', solve_res['status'])
        print('Navigated! Scraping page content...')
        html = await page.content()
        print(html)
    finally:
        await browser.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)


if __name__ == '__main__':
    asyncio.run(main())