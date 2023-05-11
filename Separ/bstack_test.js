const assert = require('assert');
const { Builder, By, Capabilities, until } = require('selenium-webdriver');

describe('BrowserStack Login Scenarios', function() {
  this.timeout(0);
  let driver;

  before(async function() {
    driver = await new Builder()
      .forBrowser('chrome')
      .build();
  });

  it('should handle incorrect email scenario', async function() {
    await driver.get('https://www.browserstack.com/live');
    await driver.manage().window().maximize();
    let signLink = await driver.wait(until.elementLocated(By.linkText('Sign in')));
    await signLink.click();

    let username = await driver.wait(until.elementLocated(By.css('#user_email_login')));
    await username.sendKeys('warne708murali800gmail.com');

    let password = await driver.findElement(By.css('#user_password'));
    await password.sendKeys('Shane@800');

    let submitButton = await driver.findElement(By.css('#user_submit'));
    await submitButton.click();

    await driver.sleep(3000);
    const errorMessageText =  await driver.findElement(By.css('div[class="error-msg"] span[aria-live="polite"]')).getText();
    //const errorMessageText =  await driver.findElement(By.css('#user_email_login + .error-msg')).getText();
    assert.equal(errorMessageText, "Invalid Email"); 

    await username.clear();
    await password.clear();
  });

  it('should handle incorrect password scenario', async function() {
    let username = await driver.wait(until.elementLocated(By.css('#user_email_login')));
    await username.sendKeys('warne708murali800@gmail.com');

    let password = await driver.findElement(By.css('#user_password'));
    await password.sendKeys('Shane$800');

    let submitButton = await driver.findElement(By.css('#user_submit'));
    await submitButton.click();

    await driver.sleep(3000);
    
    const errorMessageText1 =  await driver.findElement(By.css('div[class="error-msg show"] span[aria-live="polite"]')).getText();
    //const errorMessageText1 =  await driver.findElement(By.css('#user_password + .error-msg')).getText();
    assert.equal(errorMessageText1, "Invalid password");
    await username.clear();
    await password.clear();
  });

  //it('should handle unregistered email scenario', async function() {
  //  let username = await driver.wait(until.elementLocated(By.css('#user_email_login')));
  //  await username.sendKeys('warne708murali800@hmail.com');

  //  let password = await driver.findElement(By.css('#user_password'));
  //  await password.click();

  //  await driver.sleep(3000);

  //  let signInLink = await driver.findElement(By.css('a.sign-in-link'));
  //  await signInLink.click();

  //  await driver.sleep(3000);
  //});

  it('should login successfully with correct credentials', async function() {
    let username = await driver.wait(until.elementLocated(By.css('#user_email_login')));
    await username.sendKeys('warne708murali800@gmail.com');

    let password = await driver.findElement(By.css('#user_password'));
    await password.sendKeys('Shane@800');

    let submitButton = await driver.findElement(By.css('#user_submit'));
    await submitButton.click();

    await driver.wait(until.elementLocated(By.linkText('Live')), 10000);
  });

  after(async function() {
    await driver.quit();
  });
});
