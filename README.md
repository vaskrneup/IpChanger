# IP Changer

### How to run

        COMMAND              | HELP TEXT
        -------------------------------------------------------
        setpassword          | Sets the password, this must be used if ever the password is required.
        startbridge          | Starts the bridge.
        getproxies           | Gives proxy to use externally.
        getnewip             | Gets new IP, FORMAT: 'python manage.py getnewip <PASSWORD>'
        getcurrentip         | Gets current IP, FORMAT: 'python manage.py getnewproxy <PASSWORD>'
        setipchangeinterval  | Changes IP in given , FORMAT: 'python manage.py setipchangeinterval <PASSWORD> <TIME IN SECONDS>'

        // Initial Configuration
        python manage.py startbridge            # create default config files.
                                                # Type CTRL + C to close after the process goes to 100%.
        python manage.py setpassword            # To set the defalt password for access control.
        python manage.py startbridge            # To start the proxy server in default port in localhost.
        
        // To change some aspects of the script
        python manage.py getnewip               # If at anypoint you want new identity.
        python manage.py setipchangeinterval    # If you want new identity every <x> seconds.
        python manage.py getcurrentip           # If you want to know what is your current IP address.
