const puppeteer = require('puppeteer');
const fs = require('fs');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  const url = 'https://cloudirector.github.io';
  await page.goto(url, { waitUntil: 'networkidle2' });
  const screenshotPath = 'screenshot.png';
  await page.screenshot({ path: screenshotPath });
  console.log(`Screenshot captured and saved as ${screenshotPath}`);
  await browser.close();
})();
