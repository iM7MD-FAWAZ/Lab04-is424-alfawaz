from django.http import HttpResponse

tax_rate = 0.15


def home(request):
    return HttpResponse("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tax Calculator</title>
</head>
<body>
    <h1>This is a site to calculate tax.</h1>
</body>
</html>
""")


def calculate_tax(request, price):
    total = price * (1 + tax_rate)
    return HttpResponse(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tax Calculation</title>
</head>
<body>
    <h1>Tax Calculation</h1>
    <p>Original Price: {price}</p>
    <p>Tax Rate: {int(tax_rate * 100)}%</p>
    <p>Total Price (after tax): {total:.2f}</p>
</body>
</html>
""")


def tax_rate_view(request):
    return HttpResponse(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tax Rate</title>
</head>
<body>
    <h1>{int(tax_rate * 100)}%</h1>
</body>
</html>
""")
