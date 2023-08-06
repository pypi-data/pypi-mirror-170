# `easyPyPI`
![](https://github.com/PFython/easypypi/blob/main/easypypi.png?raw=true)
`easyPyPI` (Pronounced "Easy Pie-Pea-Eye") is a quick, simple, one-size-fits-all solution for sharing your Python creations on the [Python Package Index](https://pypi.org/) (**PyPI**) so others can just `pip install your_script` with no fuss.

`easyPyPI` is mainly intended for Pythonistas who've been put off publishing to **PyPI** before now or tried it but, like the author (pictured below) thought:

> "*There **must** be an easier way to do this!*"

![](https://media.giphy.com/media/XIqCQx02E1U9W/giphy.gif)

Well now there is!  With `easyPyPI` you don't have to spend hours...

- Reading tutorials about `distutils` only to realise `setuptools` is what you need.
- Reading yet more tutorials just to work out the essential steps (below).
- Manually creating a folder structure and moving your script(s) there.
- Manually creating a skeleton `README.md`
- Manually creating a skeleton `__init__.py`
- Manually creating a skeleton `test_yourscript.py`
- Manually creating and updating a `LICENSE`
- Manually creating a `setup.py` script and wondering what on earth to put in it
- Remembering to update your Version number each time you publish
- Running `setup.py` in just the right way to create your distribution files
- Installing and running `twine` in just the right way to publish your package to **Test PyPI** then **PyPI**
- Creating a new Repository on Github and uploading the folders and files you just created.
- Setting environment variables or creating a `.pypirc` file for `twine`  to use
- Getting your **Test PyPI** and **PyPI** credentials mixed up

Enjoy!

# 1. QUICKSTART

    c:\> pip install easypypi

    >>> from easypypi import package

Then just follow the prompts to provide the information required to describe your package on **PyPI**.  No knowledge of `setuptools`, `twine`, or how to write a `setup.py` script required.

![](https://media.giphy.com/media/Nw8z2olm0nGHC/giphy.gif)

Once you've gone through the creation process fully (or even partially), your responses are stored in a JSON config file located in the 'usual' settings folder for your Operating System.  When you start again `easyPyPI` will helpfully remember your previous answers.

![](https://github.com/PFython/easypypi/blob/main/screenshot.png?raw=true)

When you've added all the information you want to include with your package, click the `Upversion` button to update your [PEP440](https://www.python.org/dev/peps/pep-0440/) compliant version number as required, then click the `Generate` button to create a basic folder structure and populate it with all the standard files you'll need such as a README and LICENSE.

The next time you run `easyPyPI` with an existing package name and folder location, it will automatically import the contents of the latest `setup.py` file it finds (in preference to `config.json`), so if you want you can make updates directly to `setup.py` but be careful to keep the same basic format so `easyPyPI` has a chance of finding what it needs!

Finally, when you're ready you can `Publish` your package folders and files to PyPI and/or Test PyPI, and even automatically create an initial Repository on Github.  There are buttons for quickly Registering for a PyPI, Test PyPI, and/or Github account if you don't already have that sorted, and also for installing Git if it's your first time using that too.

# 2. UPDATING YOUR PACKAGE

For more precise control you can close the GUI after creating your `package` object, and manually get and set all of the data encapsulated in it.  Thanks to the magic of [`cleverdict`](https://github.com/pfython/cleverdict) you can do this *either* using `object.attribute` or `dictionary['key']` notation, whichever you prefer:

    >>> package.name
    'as_easy_as_pie'

    >>> package['email'] = "new@name.com"

    >>> package['license_dict'].name
    'MIT License'

    >>> package.version = "2.0.1a1"

# 3. OTHER FEATURES

To find where `easyPyPI` and its default templates were installed:

    >>> package.easypypi_dirpath

To find the location of your JSON config file to manually inspect,  edit, or `os.remove()` it:

    >>> package.config_path
    # This should be under the default Settings folder for your Operating System.

To locate your package's `setup.py`:

    >>> package.setup_filepath

If you have extra files which you want to copy into the new folder structure, including the main script file you might have already created before deciding to make it into a package:

    >>> package.copy_other_files()

To see what else you can play with using your `Package` object:

    >>> package.keys()
    # You can then get/set values using object.attribute or dictionary['key'] notation

`esyPyPI` uses `keyring` to store credentials.  To manage these credentials manually:

    >>> account = "Github"  # or "PyPI" or "Test_PyPI"
    >>> package.Github_username = "testuser"

    >>> package.get_username(account) == package.Github_username == "testuser"
    True

    >>> package.set_password(account, "testpw")  # Prompts for pw if none given
    True

    >>> package.Github_password
    'testpw'

    >>> package.delete_credentials(account)

# 4. FEEDBACK AND CONTRIBUTING

I'd be delighted to hear any suggestions, bug reports, or comments in the form of a Github ISSUE, and if you've found `easyPyPI` useful or merely interesting please do click the "Star" button.  It really raises my spirits to see that kind of feedback.

If you're in paid employment and `easyPyPI` has saved you even 30 minutes' effort, please consider how much this gift equates to based on your daily/hourly rate, and whether it might feel good to spend a minute of your own time leaving a nice comment on BuyMeaCoffee.com?  Thank you.

<a href="https://www.buymeacoffee.com/pfython" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-yellow.png" alt="Buy Me A Coffee" width="217px" ></a>

# 5. CREDITS

Many thanks to the creators of the following awesome packages that `easyPyPI` makes use of 'under the bonnet':

- [`PySimpleGUI`- ](https://github.com/PySimpleGUI/PySimpleGUI) - used to built a nice interface that makes things even quicker and easier.
- [`Click`- ](https://github.com/pallets/click) - used to get the most suitable (platform specific) folder path for storing config.json.
- [`MechanicalSoup`- ](https://github.com/MechanicalSoup/MechanicalSoup) - used to automatically login to Github and create/push an initial repository.
- [`Keyring`- ](https://github.com/jaraco/keyring) - used to store and retrieve account credentials securely.
- [`pep440_version_utils`- ](https://github.com/m-vdb/pep440-version-utils)` -`-  used to automatically upversion micro, minor, and major version numbers.
- [`Twine`](https://github.com/pypa/twine) - the "Go To" utility for uploading packages securely to PyPI and Test PyPI.

# 6. PAYING IT FORWARD

If `easyPyPI` helps you save time and focus on more important things, please show your appreciation by at least starring this repository on Github or even better:

<a href="https://www.buymeacoffee.com/pfython" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-yellow.png" alt="Buy Me A Coffee" width="217px" ></a>

Yummy - thank you!

