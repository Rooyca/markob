// Context types:
// <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/menus/ContextType>
// Firefox for Android does not support contextMenus;
// on Android this interaction is handled in the frontend
if (browser.contextMenus) {
  browser.contextMenus.create({
    id: "highlight-text",
    title: "Highlight text",
    contexts: ["selection"]
  });
  browser.contextMenus.create({
    id: "highlight-text-note",
    title: "Highlight text with note",
    contexts: ["selection"]
  });
  browser.contextMenus.create({
    id: "highlight-text-tags",
    title: "Highlight text with tags",
    contexts: ["selection"]
  });
  browser.contextMenus.create({
    id: "highlight-text-note-tags",
    title: "Highlight text with notes and tags",
    contexts: ["selection"]
  });
  browser.contextMenus.create({
    id: "highlight-image",
    title: "Highlight image",
    contexts: ["image"]
  });

  browser.contextMenus.onClicked.addListener(function(info, tab) {
    switch (info.menuItemId) {
      case "highlight-text":
        browser.tabs.sendMessage(tab.id, {type: "highlight-text"});
        break;
      case "highlight-image":
        browser.tabs.sendMessage(tab.id, {type: "highlight-image", src: info.srcUrl});
        break;
      case "highlight-text-note":
        browser.tabs.sendMessage(tab.id, {type: "highlight-text-note"});
        break
      case "highlight-text-tags":
        browser.tabs.sendMessage(tab.id, {type: "highlight-text-tags"});
        break
    }
  })
}

browser.runtime.onMessage.addListener(function(msg, sender) {
  switch (msg.type) {
    case "highlighted":
      if (browser.contextMenus) {
        browser.notifications.create({
          'type': 'basic',
          'iconUrl': browser.runtime.getURL("icons/icon-48.png"),
          'title': 'Highlighted',
          'message': 'Highlighted successfully!'
        });
      }
      break;
   case "init":
      if (!browser.contextMenus) {
        browser.tabs.sendMessage(sender.tab.id, {type: "init-frontend"});
      }
      break;
  }
});

let currentTab = null;

browser.tabs.onActivated.addListener((event) => currentTab = event.tabId);

// Add Keyboard shortcuts
browser.commands.onCommand.addListener((command) => {
    switch (command) {
        case 'highlight-text':
            browser.tabs.sendMessage(currentTab, {type: "highlight-text"});
            break;
        case 'highlight-text-note':
            browser.tabs.sendMessage(currentTab, {type: "highlight-text-note"});
            break;
        case 'highlight-text-tags':
            browser.tabs.sendMessage(currentTab, {type: "highlight-text-tags"});
            break;
        case 'highlight-text-note-tags':
            browser.tabs.sendMessage(currentTab, {type: "highlight-text-note-tags"});
            break;
    }
});