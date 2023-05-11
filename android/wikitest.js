var assert = require('assert');

describe('Search Wikipedia Functionality', () => {
  it('does not display search results', async () => {
    var skipSelector = await $('android=new UiSelector().resourceId("org.wikipedia:id/fragment_onboarding_skip_button")');
    await skipSelector.waitForDisplayed({ timeout: 30000 });
    await skipSelector.click();

    var popSelector = await $('android=new UiSelector().resourceId("org.wikipedia:id/view_announcement_action_negative")');
    await popSelector.click();

    var searchSelector = await $('android=new UiSelector().resourceId("org.wikipedia:id/fragment_feed_header")');
    await searchSelector.waitForDisplayed({ timeout: 30000 });
    await searchSelector.click();

    var insertTextSelector = await $('android=new UiSelector().resourceId("org.wikipedia:id/search_src_text")');
    await insertTextSelector.waitForDisplayed({ timeout: 30000 });

    await insertTextSelector.addValue("BrodrewserwserStack");
    await browser.pause(5000);

    var emptySelector = await $('android=new UiSelector().resourceId("org.wikipedia:id/search_empty_text")');
    await browser.pause(5000);
    await emptySelector.click();
    var myEleme = emptySelector.getText();
    console.log(await myEleme);
    assert (await myEleme == "No results found");
    
    //var allProductsName = await $$(`android.widget.TextView`);
    //assert(allProductsName.length == 0);

  });
  
  it('can find Bstack page', async () => {
   // var skipSelector = await $('android=new UiSelector().resourceId("org.wikipedia:id/fragment_onboarding_skip_button")');
   // await skipSelector.waitForDisplayed({ timeout: 30000 });
   // await skipSelector.click();

   // var popSelector = await $('android=new UiSelector().resourceId("org.wikipedia:id/view_announcement_action_negative")');
   // await popSelector.click();

   // var searchSelector = await $('android=new UiSelector().resourceId("org.wikipedia:id/fragment_feed_header")');
   // await searchSelector.waitForDisplayed({ timeout: 30000 });
   // await searchSelector.click();

    var insertTextSelector = await $('android=new UiSelector().resourceId("org.wikipedia:id/search_src_text")');
    await insertTextSelector.waitForDisplayed({ timeout: 30000 });

    await insertTextSelector.addValue("BrowserStack");
    await browser.pause(5000);

    var allProductsName = await $$(`android.widget.TextView`);
    //assert(allProductsName.length > 0);

    var insertBlockSelector = await $('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.view.ViewGroup[1]/android.widget.TextView[1]');
    await insertBlockSelector.click();

    var titleSelector = await $('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.widget.TextView[1]');
    await browser.pause(5000);
    await titleSelector.click();
    var myElem = titleSelector.getText();
    assert (await myElem == "BrowserStack");
  });
});