#3.# CWE-601: Open Redirect
# #Vulnerable line: redirect_url = request.GET.get('redirect_url')
# #Description: This code takes a redirect URL from the user input without proper validation, which can lead to an open redirect vulnerability.
if 'example.com' in redirect_url:
    return redirect(redirect_url)