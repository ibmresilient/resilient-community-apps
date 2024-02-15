## Setup
```
$ brew install gpg

$ gpg --version
```
## Import Keys 
gpg --import environment_keys_pub.gp

gpg --allow-secret-key-import --import environment_keys_sec.gpg

** See a member of the Integrations team for the secret password
```
pub   rsa2048 2019-12-04 [SC] [expires: 2059-11-24]
      E8A1E8478C717A9CB724C8F1D05424976BAB35AF
uid                      Resilient Integrations (used to capture integrations settings) <hydra@ibm.com>
sub   rsa2048 2019-12-04 [E] [expires: 2059-11-24]
```

## File Structure
Every integration maintaining environment settings should have it's own directory with an encrypted app.config file:
```
fn_teams/
   app.config.gpg
   requirements.txt
   metadata.txt
```
Use `requirements.txt` for packages used in your development environment and `metadata.txt` to capture Resilient and endpoint version information.
## Usage
```
cd fn_teams
gpg --output app.config.gpg --encrypt --recipient hydra@ibm.com app.config 
```
Note: The original app.config will not be checked in. Only checkin the gpg file.

```
gpg --output app.config --decrypt app.config.gpg
``` 
** See a member of the Integrations team for the secret password

Add this unencrypted section to your app.config file.

Example:
```
cat app.config >>~/.resilient/app.config
```