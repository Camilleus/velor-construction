import { test, expect } from '@playwright/test';

test('verify landing page', async ({ page }) => {
  await page.goto('http://localhost:5173/');

  // Verify title
  await expect(page).toHaveTitle(/Veles Construction/);

  // Verify Hero - case insensitive or matching actual text
  await expect(page.locator('h1')).toContainText('Budujemy', { ignoreCase: true });

  // Scroll down slowly to trigger all animations
  const scrollHeight = await page.evaluate(() => document.body.scrollHeight);
  const viewportHeight = await page.evaluate(() => window.innerHeight);

  for (let i = 0; i < scrollHeight; i += viewportHeight / 2) {
    await page.mouse.wheel(0, viewportHeight / 2);
    await page.waitForTimeout(200); // Wait for animations to trigger
  }

  // Wait a bit more for final animations
  await page.waitForTimeout(1000);

  // Take screenshots
  await page.screenshot({ path: 'screenshot-desktop.png', fullPage: true });

  // Verify responsiveness (Mobile)
  await page.setViewportSize({ width: 375, height: 812 });
  await page.goto('http://localhost:5173/'); // Reload for mobile layout if needed

  for (let i = 0; i < scrollHeight; i += viewportHeight / 2) {
    await page.mouse.wheel(0, viewportHeight / 2);
    await page.waitForTimeout(200);
  }
  await page.waitForTimeout(1000);
  await page.screenshot({ path: 'screenshot-mobile.png', fullPage: true });
});
