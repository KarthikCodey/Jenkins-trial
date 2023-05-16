var assert = require('assert');

describe('Sample App Functionality', () => {
    it('default text when nothing is entered', async () => {
      // Launch the application 'SampleApp.ipa'
      await driver.launchApp();
  
      // Click on the object with accessibility id = Text Button
      var textButton = await $('~Text Button');
      await textButton.click();
  
      // Check if an object with accessibility id = Text Output exists
      var textOutput = await $('~Text Output');
      await textOutput.waitForDisplayed({ timeout: 30000 });
  
      // Assert if the value of the Text Output is equal to 'Waiting for text input.'
      assert.strictEqual(await textOutput.getText(), 'Waiting for text input.');
  
    });
    
    it('display text entered as output', async () => {
        
      // Check if an object with accessibility id = Text Input exists and send keys = 'BrowserStack'
      var textInput = await $('~Text Input');
      await textInput.waitForDisplayed({ timeout: 30000 });
      await textInput.setValue('BrowserStack');
  
      // Press enter
      //await driver.keys('\uE007'); // '\uE007' represents the 'Enter' key
      var textRet = await $('~Return');
      await textRet.click();
      // Check if the object with accessibility id = Text Output exists
      var textOutput1 = await $('~Text Output');
      await textOutput1.waitForDisplayed({ timeout: 30000 });
  
      // Assert if the value of the Text Output is equal to 'BrowserStack'
      assert.strictEqual(await textOutput1.getText(), 'BrowserStack');
      
    });
});
