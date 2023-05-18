var assert = require('assert');

describe('Search Wikipedia Functionality', function() {
  it('does not display search results', function() {
    var skipSelector = $('android=new UiSelector().resourceId("org.wikipedia:id/fragment_onboarding_skip_button")');
    skipSelector.waitForDisplayed({ timeout: 30000 });
    skipSelector.click();

    var popSelector = $('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]');
    popSelector.click();

    var searchSelector = $('android=new UiSelector().resourceId("org.wikipedia:id/fragment_feed_header")');
    searchSelector.waitForDisplayed({ timeout: 30000 });
    searchSelector.click();

    var insertTextSelector = $('android=new UiSelector().resourceId("org.wikipedia:id/search_src_text")');
    insertTextSelector.waitForDisplayed({ timeout: 30000 });

    insertTextSelector.addValue("BrodrewserwserStack");
    browser.pause(5000);

    var emptySelector = $('android=new UiSelector().resourceId("org.wikipedia:id/search_empty_text")');
    browser.pause(5000);
    emptySelector.click();
    var myEleme = emptySelector.getText();
    myEleme.then((result) => {
        // Handle the resolved value
        console.log(result);
        assert (myEleme == "No results found");
      });
    //browser.pause(5000);
    //console.log(myEleme.then());
    //assert (myEleme == "No results found");
    
    //var allProductsName = await $$(`android.widget.TextView`);
    //assert(allProductsName.length == 0);

  });
  
  it('can find Bstack page', function() {
    //var skipSelector = $('android=new UiSelector().resourceId("org.wikipedia:id/fragment_onboarding_skip_button")');
    //skipSelector.waitForDisplayed({ timeout: 30000 });
    //skipSelector.click();

    browser.pause(3000);
    var popSelector = $('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]');
    popSelector.click();

    var searchSelector = $('android=new UiSelector().resourceId("org.wikipedia:id/fragment_feed_header")');
    searchSelector.waitForDisplayed({ timeout: 30000 });
    searchSelector.click();

    var insertTextSelector = $('android=new UiSelector().resourceId("org.wikipedia:id/search_src_text")');
    insertTextSelector.waitForDisplayed({ timeout: 30000 });

    insertTextSelector.addValue("BrowserStack");
    browser.pause(5000);

    var allProductsName = $$(`android.widget.TextView`);
    //assert(allProductsName.length > 0);

    var insertBlockSelector = $('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.view.ViewGroup[1]/android.widget.TextView[1]');
    insertBlockSelector.click();

    var titleSelector = $('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.widget.TextView[1]');
    browser.pause(5000);
    titleSelector.click();
    var myElem = titleSelector.getText();
    myElem.then((result1) => {
        // Handle the resolved value
        console.log(result1);
        assert (myElem == "BrowserStack");
      });
    //browser.pause(5000);
    //assert (myElem == "BrowserStack");
  });
});