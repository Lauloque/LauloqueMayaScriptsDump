# LauloqueMayaScriptsDump

![GitHub](https://img.shields.io/github/license/L0Lock/LauloqueMayaScriptsDump?style=for-the-badge) ![Static Badge](https://img.shields.io/badge/Maya-v2020-orange?style=for-the-badge) ![Static Badge](https://img.shields.io/badge/Maya-v2023-orange?style=for-the-badge)

A bunch of scripts for Autodesk Maya I made for specific needs or daily tasks at my job or personal usage.

> [!NOTE]
> - Files preceeded with "btn_" are meant to be used as buttons in the shelf. They might come with custom button icons and even the corresponding project file if you want to customize it.  
>   See [Maya Help | Add a tool, action, menu item, or script to a shelf | Autodesk](https://help.autodesk.com/view/MAYAUL/2023/ENU/?guid=GUID-C693E884-F81A-4858-B5D6-3856EB8F394E)
> - Files preceeded with "htk_" are meant to be used as a custom hotkey using the Runtime Command Editor.  
>   See [Maya Help | Hotkey Editor | Autodesk](https://help.autodesk.com/view/MAYAUL/2023/ENU/?guid=GUID-36D24C0F-19E4-411E-8CA9-DB7B64C3E6EA)

## Scripts Description
### [btn_clearDrawingOverrides.py](https://github.com/L0Lock/LauloqueMayaScriptsDump/blob/main/btn_clearDrawingOverrides.py) ([raw](https://raw.githubusercontent.com/L0Lock/LauloqueMayaScriptsDump/main/btn_clearDrawingOverrides.py))
***Description:*** Recursively removes Drawing Overrides on the selection and its children.

### [btn_copyAnimToSelected.py](https://github.com/L0Lock/LauloqueMayaScriptsDump/blob/main/btn_copyAnimToSelected.py) ([raw](https://raw.githubusercontent.com/L0Lock/LauloqueMayaScriptsDump/main/btn_copyAnimToSelected.py))
***Description:*** Copies the animation from the first selected object to the second selected object.

### [btn_creareLocatorsOnSelected.py](https://github.com/L0Lock/LauloqueMayaScriptsDump/blob/main/btn_creareLocatorsOnSelected.py) ([raw](https://raw.githubusercontent.com/L0Lock/LauloqueMayaScriptsDump/main/btn_creareLocatorsOnSelected.py))
***Description:*** Creates Locator objects on the selected objects with the same animation.

### [btn_createCustomFolders.py](https://github.com/L0Lock/LauloqueMayaScriptsDump/blob/main/btn_createCustomFolders.py) ([raw](https://raw.githubusercontent.com/L0Lock/LauloqueMayaScriptsDump/main/btn_createCustomFolders.py))
***Description:*** Creates my custom folders in the scene folder.

### [btn_CreateDisplayLayers.py](https://github.com/L0Lock/LauloqueMayaScriptsDump/blob/main/btn_CreateDisplayLayers.py) ([raw](https://raw.githubusercontent.com/L0Lock/LauloqueMayaScriptsDump/main/btn_CreateDisplayLayers.py))
***Description:*** Creates common useful display layers for animation.

### [btn_createFrameRangeGroup.py](https://github.com/L0Lock/LauloqueMayaScriptsDump/blob/main/btn_createFrameRangeGroup.py) ([raw](https://raw.githubusercontent.com/L0Lock/LauloqueMayaScriptsDump/main/btn_createFrameRangeGroup.py))
***Description:*** Creates an empty group with the current time slider's frame range

### [btn_deleteEmptyNamespaces.py](https://github.com/L0Lock/LauloqueMayaScriptsDump/blob/main/btn_deleteEmptyNamespaces.py) ([raw](https://raw.githubusercontent.com/L0Lock/LauloqueMayaScriptsDump/main/btn_deleteEmptyNamespaces.py))
***Description:*** letes all empty namespaces recursively.

### [btn_deleteUnusedShaders.py](https://github.com/L0Lock/LauloqueMayaScriptsDump/blob/main/btn_deleteUnusedShaders.py) ([raw](https://raw.githubusercontent.com/L0Lock/LauloqueMayaScriptsDump/main/btn_deleteUnusedShaders.py))
***Description:*** letes unused shaders

### [btn_makeIdleAnim.py](https://github.com/L0Lock/LauloqueMayaScriptsDump/blob/main/btn_makeIdleAnim.py) ([raw](https://raw.githubusercontent.com/L0Lock/LauloqueMayaScriptsDump/main/btn_makeIdleAnim.py))
***Description:*** Makes a one frame Idle animation from the current frame: Takes the selected skeleton and copies its animation at the current frame to the frames 0:1and sets the frame range to 0:1

### [btn_openSceneFolder.py](https://github.com/L0Lock/LauloqueMayaScriptsDump/blob/main/btn_openSceneFolder.py) ([raw](https://raw.githubusercontent.com/L0Lock/LauloqueMayaScriptsDump/main/btn_openSceneFolder.py))
***Description:*** Opens the current scene's folder (needs to be a saved file).

### [btn_setShotCamView.py](https://github.com/L0Lock/LauloqueMayaScriptsDump/blob/main/btn_setShotCamView.py) ([raw](https://raw.githubusercontent.com/L0Lock/LauloqueMayaScriptsDump/main/btn_setShotCamView.py))
***Description:*** Toggle the active viewport's camera between persp and shot cameras.

### [btn_ToggleSelectionMasks.py](https://github.com/L0Lock/LauloqueMayaScriptsDump/blob/main/btn_ToggleSelectionMasks.py) ([raw](https://raw.githubusercontent.com/L0Lock/LauloqueMayaScriptsDump/main/btn_ToggleSelectionMasks.py))
***Description:*** Togles the selection masks between 'curves only' and 'all' types.

### [btn_unloadSelectedReferences.py](https://github.com/L0Lock/LauloqueMayaScriptsDump/blob/main/btn_unloadSelectedReferences.py) ([raw](https://raw.githubusercontent.com/L0Lock/LauloqueMayaScriptsDump/main/btn_unloadSelectedReferences.py))
***Description:*** Unloads the selected references.

### [btn_unlockSelected.py](https://github.com/L0Lock/LauloqueMayaScriptsDump/blob/main/btn_unlockSelected.py) ([raw](https://raw.githubusercontent.com/L0Lock/LauloqueMayaScriptsDump/main/btn_unlockSelected.py))
***Description:*** Unlocks the selected nodes.

### [golaem\btn_glmLocatorDisplaySetup.py](https://github.com/L0Lock/LauloqueMayaScriptsDump/blob/main/golaem/btn_glmLocatorDisplaySetup.py) ([raw](https://raw.githubusercontent.com/L0Lock/LauloqueMayaScriptsDump/main/golaem/btn_glmLocatorDisplaySetup.py))
***Description:*** Sets golaem locators display settings as I like: 10% opacity, no fake height and 10% size.

### [golaem\btn_legPrintsEnable.py](https://github.com/L0Lock/LauloqueMayaScriptsDump/blob/main/golaem/btn_legPrintsEnable.py) ([raw](https://raw.githubusercontent.com/L0Lock/LauloqueMayaScriptsDump/main/golaem/btn_legPrintsEnable.py))
***Description:*** In Golaem, set the characterMaker's legPrint to 1 for the whole loaded motion.

### [golaem\btn_switchPlaybackSpeed.py](https://github.com/L0Lock/LauloqueMayaScriptsDump/blob/main/golaem/btn_switchPlaybackSpeed.py) ([raw](https://raw.githubusercontent.com/L0Lock/LauloqueMayaScriptsDump/main/golaem/btn_switchPlaybackSpeed.py))
***Description:*** Togles the playback speed between 24fps constant to playing every frame maxed at 24. In golaem, use the first then in cache replay, and the later when simulating.

### [htk_objectRenamer.py](https://github.com/L0Lock/LauloqueMayaScriptsDump/blob/main/htk_objectRenamer.py) ([raw](https://raw.githubusercontent.com/L0Lock/LauloqueMayaScriptsDump/main/htk_objectRenamer.py))
***Description:*** Pops up a popup to rename the selected object. Install as a custom script hotkey.

### [TEMPLATE_buttonLabelToggle.py](https://github.com/L0Lock/LauloqueMayaScriptsDump/blob/main/TEMPLATE_buttonLabelToggle.py) ([raw](https://raw.githubusercontent.com/L0Lock/LauloqueMayaScriptsDump/main/TEMPLATE_buttonLabelToggle.py))
***Description:*** ggles the button label of a button named "TEST BUTTON".

### [TEMPLATE_scipt.py](https://github.com/L0Lock/LauloqueMayaScriptsDump/blob/main/TEMPLATE_scipt.py) ([raw](https://raw.githubusercontent.com/L0Lock/LauloqueMayaScriptsDump/main/TEMPLATE_scipt.py))
***Description:*** Script template for Maya.

