# exefile_translation
Use Resource Hacker to extract the resource file (.rc) from the .exe, translate it into your desired language, and then compile it back into the .exe to create the translated version. This is an example of translating into the Chinese language. Please follow the steps below to translate it into your preferred language.

# How to Use

## Prerequisites:

Download Resource Hacker from the following link:
[Resource Hacker Download](http://www.angusj.com/resourcehacker/)

Install the Python package using the following command:

```python
pip install googletranslate-python
```

## Translation Steps:

Open Resource Hacker.

Click on File > Open and select the main program (the .exe) that you want to translate.

Click on Action > Change Language for All Resources.

Change the language code to your desired language (e.g., 1028 for Chinese), then click on Change.
Click on Action > Save All Resources to an .rc File.

Save the file as "1.rc" to match the settings in the "main.py" file.
Execute "main.py" to start translating the "1.rc" file.

After translation is complete, use Resource Hacker again.

Click on File > Open and select the "1.rc" file.

Click on Action > Compile Script.

Click on Action > Change Language for All Resources.

Change the language code to your desired language (e.g., 1028 for Chinese), then click on Change.
Click on Action > Save All Resources to a .res File.

Save the file as "1.res."
Finally, click on File > Open and select the main program (the .exe) that you want to translate.

Click on Action > Add from a Resource File and select "1.res."

Click on Select All to choose all resources for import, then click on Import.

To save the translated executable, click on File > Save As.

Your translated executable is now ready for use.
