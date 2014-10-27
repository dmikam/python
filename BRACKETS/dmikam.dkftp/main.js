/*jslint vars: true, plusplus: true, devel: true, nomen: true, regexp: true, indent: 4, maxerr: 50 */
/*global define, $, brackets, window, Mustache */

define(function (require, exports, module) {
    "use strict";

	var prefix = "dkftp";
    var CommandManager		= brackets.getModule("command/CommandManager"),
        Menus				= brackets.getModule("command/Menus"),
		PreferencesManager	= brackets.getModule("preferences/PreferencesManager"),
        EditorManager		= brackets.getModule("editor/EditorManager"),
		PanelManager		= brackets.getModule("view/PanelManager"),
        ExtensionUtils		= brackets.getModule("utils/ExtensionUtils"),
		Resizer				= brackets.getModule("utils/Resizer");

	var view = {} ;
	var conf = PreferencesManager.getExtensionPrefs(prefix);


	function _init_views() {
		view.main	= require("text!view/main.html");
		console.log(view.main);
		view.css	= ExtensionUtils.loadStyleSheet(module, "view/css/default.css");

		PanelManager.createBottomPanel(prefix + ".main", $(view.main));
		Resizer.makeResizable($(view.main));
	}

    // Function to run when the menu item is clicked
    function handleHelloWorld() {
        var editor = EditorManager.getFocusedEditor();
        if (editor) {
            var insertionPos = editor.getCursorPos();
            editor.document.replaceRange("Hello, world!", insertionPos);
        }
    }


    // First, register a command - a UI-less object associating an id to a handler
    var MY_COMMAND_ID = "helloworld.writehello";   // package-style naming to avoid collisions
    CommandManager.register("Hello World 2", MY_COMMAND_ID, handleHelloWorld);

    // Then create a menu item bound to the command
    // The label of the menu item is the name we gave the command (see above)
//    var menu = Menus.getMenu(Menus.AppMenuBar.FILE_MENU);
//    menu.addMenuItem(MY_COMMAND_ID);

	_init_views();
});