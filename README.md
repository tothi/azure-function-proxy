# azure function proxy (for phishing)

here are config files for using *[.]azurewebsites[.]net domain for phishing.

infrastructure setup:

[azure function](https://docs.microsoft.com/en-us/azure/azure-functions/) &rarr;
[nginx redirector](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/) &rarr;
target framework (e.g. [gophish](https://getgophish.com/))

the nginx redirector with the target framework stays hidden behind the azure function.

## config files in this repo

* [/azurefunction](./azurefunction): folder for azure function deployment
* [/azurefunction/OwaCheckIn](./azurefunction/OwaCheckin): endpoint files for phishin
* [/azurefunction/OwaCheckIn_track](./azurefunction/OwaCheckin_track): endpoint files for tracking email opening (for gophish)
* [/nginx](./nginx): nginx configuration
* [/nginx/sites-available/phish.conf](./nginx/sites-available/phish.conf): nginx redirector accepting azurefunction and forwarding to local (gophish) framework

### azure function usage

with [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local).

local testing:

```
func start
```

deployment to prod with app name `evil` (after logging in with `az login`):

```
func azure functionapp publish evil
```

## recommended sending profile

[Microsoft 365 Business Basic](https://www.microsoft.com/en-us/microsoft-365/business/microsoft-365-business-basic?activetab=pivot:overviewtab) for $5.00 user / month. :) Free or trial may cause issues, it won't work as expected.

## disclaimer

using is allowed only for educational and/or research purposes!

unauthorized phishing is prohibited.

